from django.shortcuts import render
from django.db import connection, DatabaseError
import re
import html

def demo_sql_error_view(request):
    """
    Demo Cơ chế hoạt động của Error-Based SQL Injection
    Dành cho mục đích giáo dục & minh họa cơ chế phòng thủ an toàn.
    """
    search_query = request.GET.get('query', 'CV-DI-52')
    mode = request.GET.get('mode', 'vulnerable')  # 'vulnerable' hoặc 'secure'
    
    context = {
        'search_query': search_query,
        'mode': mode,
        'has_searched': 'query' in request.GET,
        'step1_input': search_query,
        'step2_sql': '',
        'step3_db_status': '',
        'step4_error_message': None,
        'step5_analysis': None,
        'results': [],
        'db_name_display': 'PostgreSQL (Supabase)',
    }

    if context['has_searched']:
        if mode == 'vulnerable':
            # --- BƯỚC 2 (LỖI): NỐI CHUỖI TRỰC TIẾP KHÔNG QUA KIỂM DUYỆT ---
            raw_sql = f'SELECT "VanBanDiID", "SoKyHieu", "TrichYeu", "TrangThai" FROM web_vanbandi WHERE "SoKyHieu" = \'{search_query}\' LIMIT 10'
            context['step2_sql'] = raw_sql
            
            try:
                # --- BƯỚC 3: DBMS THỰC THI TRUY VẤN ---
                with connection.cursor() as cursor:
                    cursor.execute(raw_sql)
                    columns = [col[0] for col in cursor.description] if cursor.description else []
                    rows = cursor.fetchall()
                    context['results'] = [dict(zip(columns, row)) for row in rows]
                
                context['step3_db_status'] = 'Thực thi thành công (Không phát sinh lỗi DBMS).'
                context['step4_error_message'] = None
                context['step5_analysis'] = 'Truy vấn đã được DBMS thực thi bình thường và trả về kết quả hợp lệ.'
                
            except Exception as e:
                # Cần rollback connection khi postgres gặp transaction error
                try:
                    connection.rollback()
                except Exception:
                    pass

                raw_err = str(e).strip()
                context['step3_db_status'] = 'DBMS phát hiện câu lệnh vi phạm cú pháp / kiểu dữ liệu và quăng ngoại lệ (Exception).'
                
                # --- BƯỚC 4: ỨNG DỤNG LÀM LỘ THÔNG BÁO LỖI CHI TIẾT RA BÊN NGOÀI ---
                context['step4_error_message'] = raw_err
                
                # --- BƯỚC 5: PHÂN TÍCH NỘI DUNG LỖI ĐỂ TRÍCH XUẤT THÔNG TIN ---
                analysis = []
                if 'syntax error' in raw_err.lower():
                    analysis.append('🔴 **Lỗi cú pháp (Syntax Error)**: Ký tự đầu vào (như dấu nháy đơn) đã phá vỡ cấu trúc câu truy vấn gốc. Điều này xác nhận ứng dụng đang nối chuỗi trực tiếp và tồn tại lỗ hổng SQL Injection.')
                
                if 'invalid input syntax for type' in raw_err.lower():
                    # Trích xuất dữ liệu rò rỉ trong dấu ngoặc kép của PostgreSQL
                    match = re.search(r'invalid input syntax for type \w+:\s*"([^"]+)"', raw_err, re.IGNORECASE)
                    leaked_data = match.group(1) if match else 'Dữ liệu trích xuất'
                    analysis.append(f'🎯 **Khai thác trích xuất dữ liệu qua Error-Based (Type Cast Failure)**: ')
                    analysis.append(f'- DBMS cố ép kiểu dữ liệu từ câu truy vấn con sang kiểu số nguyên (`int`), nhưng thất bại.')
                    analysis.append(f'- **Dữ liệu nhạy cảm bị rò rỉ ngay trong thông báo lỗi:** `{html.escape(leaked_data)}`')
                    analysis.append('- Kẻ tấn công không cần xem kết quả trên giao diện mà đọc trực tiếp nội dung cơ sở dữ liệu qua chính thông báo lỗi này.')

                if 'relation' in raw_err.lower() or 'column' in raw_err.lower():
                    analysis.append('⚠️ **Rò rỉ cấu trúc cơ sở dữ liệu**: Thông báo lỗi để lộ tên bảng (table) hoặc tên cột (column) trong hệ thống nội bộ.')

                if not analysis:
                    analysis.append('⚠️ **Thông báo lỗi chi tiết bị lộ**: Thông tin chi tiết của DBMS đã bị gửi thẳng về trình duyệt, cung cấp manh mối về hệ quản trị CSDL cho kẻ tấn công.')

                context['step5_analysis'] = '\n\n'.join(analysis)

        else:
            # --- CHẾ ĐỘ AN TOÀN (SECURE MODE): PARAMETERIZED QUERY & GENERIC ERROR ---
            # Bước 2 An toàn: Dùng tham số hóa (%s)
            safe_sql = 'SELECT "VanBanDiID", "SoKyHieu", "TrichYeu", "TrangThai" FROM web_vanbandi WHERE "SoKyHieu" = %s LIMIT 10'
            context['step2_sql'] = f'{safe_sql} -- [Tham số truyền an toàn riêng biệt: {repr(search_query)}]'
            
            try:
                with connection.cursor() as cursor:
                    cursor.execute(safe_sql, [search_query])
                    columns = [col[0] for col in cursor.description] if cursor.description else []
                    rows = cursor.fetchall()
                    context['results'] = [dict(zip(columns, row)) for row in rows]
                
                context['step3_db_status'] = 'Thực thi an toàn qua Parameterized Query (Không thể bị chèn mã độc vào cấu trúc lệnh).'
                context['step4_error_message'] = None
                context['step5_analysis'] = 'An toàn tuyệt đối: Dữ liệu đầu vào được coi như chuỗi văn bản thuần túy (literal), không thể làm thay đổi cú pháp logic của câu lệnh SQL.'
            except Exception as e:
                try:
                    connection.rollback()
                except Exception:
                    pass
                context['step3_db_status'] = 'Có lỗi xảy ra nhưng đã được xử lý phía Server.'
                # Trong chế độ an toàn: Che giấu toàn bộ chi tiết lỗi nội bộ
                context['step4_error_message'] = 'Đã xảy ra lỗi trong quá trình xử lý yêu cầu. Vui lòng thử lại sau hoặc liên hệ quản trị viên. (Mã lỗi nội bộ đã được ghi log an toàn).'
                context['step5_analysis'] = 'Phòng thủ thành công: Không để lộ bất kỳ thông tin chi tiết nào về hệ quản trị CSDL hay cú pháp SQL ra phía người dùng.'

    return render(request, 'demo_sql_error.html', context)

