"""
Script tạo dữ liệu demo cho hệ thống QLVB
Chạy lệnh: python seed_demo.py
"""
import os
import sys
import django
from datetime import timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QLVB.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.utils import timezone
from web.models import (
    UserAccount, VaiTro, DonViBenTrong, DonViBenNgoai,
    VanBanDen, VanBanDi, PhanCong, ChuyenTiep,
    PheDuyet, PhatHanh, LichSuHoatDong, BaoCao, Butphe
)

now = timezone.now()

print("=" * 60)
print("  SEED DU LIEU DEMO - HE THONG QLVB")
print("=" * 60)

# 1. DON VI BEN TRONG
print("\n[1/8] Tao Don vi ben trong (Phong ban)...")
phong_ban_data = [
    {"TenDonVi": "Ban Giam doc",      "DiaChi": "Tang 10, Toa nha HQ", "SoDienThoai": "028.3800.0001", "NguoiLienHe": "Nguyen Van An",   "Email": "ban.giam.doc@company.vn",  "SoThuTu": 1},
    {"TenDonVi": "Phong IT",          "DiaChi": "Tang 5, Toa nha HQ",  "SoDienThoai": "028.3800.0002", "NguoiLienHe": "Tran Minh Duc",   "Email": "phong.it@company.vn",       "SoThuTu": 2},
    {"TenDonVi": "Phong Hanh chinh",  "DiaChi": "Tang 2, Toa nha HQ",  "SoDienThoai": "028.3800.0003", "NguoiLienHe": "Le Thi Huong",    "Email": "hanh.chinh@company.vn",     "SoThuTu": 3},
    {"TenDonVi": "Phong Ke toan",     "DiaChi": "Tang 3, Toa nha HQ",  "SoDienThoai": "028.3800.0004", "NguoiLienHe": "Pham Thi Mai",    "Email": "ke.toan@company.vn",        "SoThuTu": 4},
    {"TenDonVi": "Phong Nhan su",     "DiaChi": "Tang 4, Toa nha HQ",  "SoDienThoai": "028.3800.0005", "NguoiLienHe": "Hoang Van Binh",  "Email": "nhan.su@company.vn",        "SoThuTu": 5},
    {"TenDonVi": "Phong Kinh doanh",  "DiaChi": "Tang 6, Toa nha HQ",  "SoDienThoai": "028.3800.0006", "NguoiLienHe": "Vu Thi Lan",      "Email": "kinh.doanh@company.vn",     "SoThuTu": 6},
    {"TenDonVi": "Phong Phap che",    "DiaChi": "Tang 7, Toa nha HQ",  "SoDienThoai": "028.3800.0007", "NguoiLienHe": "Dang Quoc Hung",  "Email": "phap.che@company.vn",       "SoThuTu": 7},
]
phong_bans = {}
for pb in phong_ban_data:
    obj, created = DonViBenTrong.objects.get_or_create(TenDonVi=pb["TenDonVi"], defaults=pb)
    phong_bans[pb["TenDonVi"]] = obj
    print(f"   {'[NEW]' if created else '[OK]'}: {pb['TenDonVi']}")

# 2. DON VI BEN NGOAI
print("\n[2/8] Tao Don vi ben ngoai...")
don_vi_ngoai_data = [
    {"TenDonVi": "Bo Tai chinh",               "DiaChi": "28 Tran Hung Dao, Ha Noi",        "SoDienThoai": "024.2220.8088", "NguoiLienHe": "Nguyen Quang Minh", "Email": "vanphong@mof.gov.vn",    "SoThuTu": 1},
    {"TenDonVi": "Bo Ke hoach Dau tu",          "DiaChi": "6B Hoang Dieu, Ba Dinh, Ha Noi",  "SoDienThoai": "024.3843.4201", "NguoiLienHe": "Tran Thi Hoa",      "Email": "banbientap@mpi.gov.vn",  "SoThuTu": 2},
    {"TenDonVi": "So Thong tin Truyen thong",   "DiaChi": "59 Ly Tu Trong, Q.1, TP.HCM",    "SoDienThoai": "028.3825.0555", "NguoiLienHe": "Le Van Khoa",        "Email": "stttt@tphcm.gov.vn",     "SoThuTu": 3},
    {"TenDonVi": "Ngan hang Vietcombank",       "DiaChi": "198 Tran Quang Khai, Ha Noi",     "SoDienThoai": "024.3934.3137", "NguoiLienHe": "Pham Thi Nhung",    "Email": "info@vietcombank.com.vn","SoThuTu": 4},
    {"TenDonVi": "Cong ty CP Phan mem FPT",     "DiaChi": "17 Duy Tan, Cau Giay, Ha Noi",   "SoDienThoai": "024.7300.7300", "NguoiLienHe": "Hoang Minh Chau",   "Email": "contact@fsoft.com.vn",   "SoThuTu": 5},
    {"TenDonVi": "Cong ty TNHH Deloitte VN",   "DiaChi": "12A Floor, Vincom Center, Q.1",   "SoDienThoai": "028.3910.0751", "NguoiLienHe": "Vu Thanh Long",     "Email": "info@deloitte.com.vn",   "SoThuTu": 6},
    {"TenDonVi": "Tong cuc Thue",               "DiaChi": "123 Lo Duc, Hai Ba Trung, Ha Noi","SoDienThoai": "024.3972.5617", "NguoiLienHe": "Nguyen Thi Bich",   "Email": "gdt@gdt.gov.vn",         "SoThuTu": 7},
    {"TenDonVi": "Tap doan Vingroup",           "DiaChi": "7 Ba Huyen Thanh Quan, Q.3",      "SoDienThoai": "1800 8168",     "NguoiLienHe": "Dang Trung Kien",   "Email": "ir@vingroup.net",         "SoThuTu": 8},
]
don_vi_ngoais = {}
for dv in don_vi_ngoai_data:
    obj, created = DonViBenNgoai.objects.get_or_create(TenDonVi=dv["TenDonVi"], defaults=dv)
    don_vi_ngoais[dv["TenDonVi"]] = obj
    print(f"   {'[NEW]' if created else '[OK]'}: {dv['TenDonVi']}")

# 3. VAI TRO
print("\n[3/8] Tao Vai tro...")
vai_tro_data = [
    ("Tong giam doc",     "Ban Giam doc"),
    ("Truong phong IT",   "Phong IT"),
    ("Truong phong HC",   "Phong Hanh chinh"),
    ("Truong phong KT",   "Phong Ke toan"),
    ("Truong phong NS",   "Phong Nhan su"),
    ("Truong phong KD",   "Phong Kinh doanh"),
    ("Truong phong PC",   "Phong Phap che"),
    ("Nhan vien IT",      "Phong IT"),
    ("Nhan vien HC",      "Phong Hanh chinh"),
    ("Nhan vien KT",      "Phong Ke toan"),
    ("Nhan vien NS",      "Phong Nhan su"),
    ("Nhan vien KD",      "Phong Kinh doanh"),
    ("Nhan vien PC",      "Phong Phap che"),
]
vai_tros = {}
for chuc_vu, ten_phong in vai_tro_data:
    pb = phong_bans.get(ten_phong)
    obj, created = VaiTro.objects.get_or_create(ChucVu=chuc_vu, defaults={"PhongBan": pb})
    vai_tros[chuc_vu] = obj
    print(f"   {'[NEW]' if created else '[OK]'}: {chuc_vu}")

# 4. TAI KHOAN NGUOI DUNG
print("\n[4/8] Tao Tai khoan nguoi dung...")
users_data = [
    ("admin",    "admin123",   "Quan tri vien",    "admin@company.vn",           "0901234560", None,               None,               True,  True,  0),
    ("giamdoc",  "giamdoc123", "Nguyen Van An",    "nguyen.van.an@company.vn",   "0901234561", "Tong giam doc",    "Ban Giam doc",     True,  False, 1),
    ("tp_it",    "tp123",      "Tran Minh Duc",    "tran.minh.duc@company.vn",   "0901234562", "Truong phong IT",  "Phong IT",         False, False, 2),
    ("tp_hc",    "tp123",      "Le Thi Huong",     "le.thi.huong@company.vn",    "0901234563", "Truong phong HC",  "Phong Hanh chinh", False, False, 3),
    ("tp_kt",    "tp123",      "Pham Thi Mai",     "pham.thi.mai@company.vn",    "0901234564", "Truong phong KT",  "Phong Ke toan",    False, False, 4),
    ("tp_ns",    "tp123",      "Hoang Van Binh",   "hoang.van.binh@company.vn",  "0901234565", "Truong phong NS",  "Phong Nhan su",    False, False, 5),
    ("tp_kd",    "tp123",      "Vu Thi Lan",       "vu.thi.lan@company.vn",      "0901234566", "Truong phong KD",  "Phong Kinh doanh", False, False, 6),
    ("tp_pc",    "tp123",      "Dang Quoc Hung",   "dang.quoc.hung@company.vn",  "0901234567", "Truong phong PC",  "Phong Phap che",   False, False, 7),
    ("nv_it_01", "nv123",      "Nguyen Thi Thanh", "nv.it.01@company.vn",        "0901234568", "Nhan vien IT",     "Phong IT",         False, False, 8),
    ("nv_it_02", "nv123",      "Bui Van Tung",     "nv.it.02@company.vn",        "0901234569", "Nhan vien IT",     "Phong IT",         False, False, 9),
    ("nv_hc_01", "nv123",      "Ngo Thi Diem",     "nv.hc.01@company.vn",        "0901234570", "Nhan vien HC",     "Phong Hanh chinh", False, False, 10),
    ("nv_hc_02", "nv123",      "Ly Minh Quan",     "nv.hc.02@company.vn",        "0901234571", "Nhan vien HC",     "Phong Hanh chinh", False, False, 11),
    ("nv_kt_01", "nv123",      "Trinh Thi Ngoc",   "nv.kt.01@company.vn",        "0901234572", "Nhan vien KT",     "Phong Ke toan",    False, False, 12),
    ("nv_ns_01", "nv123",      "Cao Van Phuc",     "nv.ns.01@company.vn",        "0901234573", "Nhan vien NS",     "Phong Nhan su",    False, False, 13),
    ("nv_kd_01", "nv123",      "Dinh Thi Yen",     "nv.kd.01@company.vn",        "0901234574", "Nhan vien KD",     "Phong Kinh doanh", False, False, 14),
    ("nv_pc_01", "nv123",      "To Quang Tuan",    "nv.pc.01@company.vn",        "0901234575", "Nhan vien PC",     "Phong Phap che",   False, False, 15),
]
users = {}
for username, password, ho_ten, email, phone, chuc_vu, phong_ban, is_staff, is_superuser, so_thu_tu in users_data:
    vai_tro = vai_tros.get(chuc_vu) if chuc_vu else None
    phong   = phong_bans.get(phong_ban) if phong_ban else None
    obj = UserAccount.objects.filter(username=username).first()
    if not obj:
        obj = UserAccount(username=username, HoTen=ho_ten, email=email, SoDienThoai=phone,
                          VaiTroID=vai_tro, PhongBan=phong, is_staff=is_staff,
                          is_superuser=is_superuser, TrangThai=True, trang_thai='ACTIVE', SoThuTu=so_thu_tu)
        obj.set_password(password)
        obj.save()
        print(f"   [NEW]: {username} ({ho_ten})")
    else:
        obj.HoTen=ho_ten; obj.email=email; obj.VaiTroID=vai_tro; obj.PhongBan=phong
        obj.is_staff=is_staff; obj.is_superuser=is_superuser; obj.save()
        print(f"   [OK] : {username} ({ho_ten})")
    users[username] = obj

# 5. VAN BAN DEN
print("\n[5/8] Tao Van ban den...")
vb_den_list = [
    ("BTC-2025/001",   now-timedelta(days=30), now-timedelta(days=28), "Cong van",  "V/v huong dan quyet toan ngan sach nha nuoc nam 2025",               "Bo Tai chinh",             "Phong Ke toan",    "HOAN_THANH", "tp_kt",    now-timedelta(days=10)),
    ("BKHDT-2025/002", now-timedelta(days=25), now-timedelta(days=23), "Thong tu",  "Thong tu huong dan dang ky kinh doanh dien tu",                      "Bo Ke hoach Dau tu",       "Phong Phap che",   "DANG_XU_LY","tp_pc",    None),
    ("STTTT-2025/003", now-timedelta(days=20), now-timedelta(days=18), "Quyet dinh","Quyet dinh ve chuyen doi so ha tang CNTT giai doan 2025-2030",         "So Thong tin Truyen thong","Phong IT",         "DANG_XU_LY","tp_it",    None),
    ("VCB-2025/004",   now-timedelta(days=15), now-timedelta(days=14), "Cong van",  "V/v thay doi dieu khoan hop dong tin dung doanh nghiep",              "Ngan hang Vietcombank",    "Phong Ke toan",    "MOI",       "nv_kt_01", None),
    ("FPT-2025/005",   now-timedelta(days=12), now-timedelta(days=11), "Hop dong",  "Hop dong cung cap dich vu phan mem quan ly nhan su 2025",             "Cong ty CP Phan mem FPT",  "Phong IT",         "DANG_XU_LY","nv_it_01", None),
    ("DLT-2025/006",   now-timedelta(days=10), now-timedelta(days=9),  "Bien ban",  "Bien ban kiem toan bao cao tai chinh quy III nam 2025",               "Cong ty TNHH Deloitte VN", "Phong Ke toan",    "DANG_XU_LY","tp_kt",    None),
    ("GDT-2025/007",   now-timedelta(days=7),  now-timedelta(days=6),  "Thong bao", "Thong bao ve viec khai thue TNDN quy III/2025",                       "Tong cuc Thue",            "Phong Ke toan",    "MOI",       "nv_kt_01", None),
    ("VGR-2025/008",   now-timedelta(days=5),  now-timedelta(days=4),  "To trinh",  "To trinh ve de xuat hop tac chien luoc nam 2026",                     "Tap doan Vingroup",        "Phong Kinh doanh", "MOI",       "tp_kd",    None),
    ("BTC-2025/009",   now-timedelta(days=3),  now-timedelta(days=2),  "Nghi dinh", "Nghi dinh sua doi quy dinh ve quan ly chi phi dau tu xay dung",       "Bo Tai chinh",             "Phong Phap che",   "MOI",       "nv_pc_01", None),
    ("BKHDT-2025/010", now-timedelta(days=1),  now,                    "Cong van",  "V/v bao cao tinh hinh thuc hien von dau tu nam 2025",                 "Bo Ke hoach Dau tu",       "Phong Hanh chinh", "MOI",       "nv_hc_01", None),
    ("STTTT-2025/011", now-timedelta(days=35), now-timedelta(days=33), "Ke hoach",  "Ke hoach ung dung CNTT trong co quan nha nuoc 2025",                  "So Thong tin Truyen thong","Phong IT",         "HOAN_THANH","tp_it",    now-timedelta(days=20)),
    ("VCB-2025/012",   now-timedelta(days=40), now-timedelta(days=38), "Thong bao", "Thong bao dieu chinh lai suat vay doanh nghiep",                      "Ngan hang Vietcombank",    "Phong Ke toan",    "HOAN_THANH","nv_kt_01", now-timedelta(days=30)),
]
van_ban_dens = {}
for row in vb_den_list:
    sku, ngh, nnhan, loai, trich, dv_ngoai, dv_trong, tt, uid, ngay_ht = row
    if VanBanDen.objects.filter(SoKyHieu=sku).exists():
        van_ban_dens[sku] = VanBanDen.objects.get(SoKyHieu=sku)
        print(f"   [OK]: {sku}")
        continue
    obj = VanBanDen.objects.create(
        SoKyHieu=sku, NgayBanHanh=ngh, NgayNhan=nnhan, LoaiVanBan=loai, TrichYeu=trich,
        DonViNgoaiID=don_vi_ngoais.get(dv_ngoai), DonViTrongID=phong_bans.get(dv_trong),
        TrangThai=tt, UserID=users.get(uid), NgayHoanThanh=ngay_ht)
    van_ban_dens[sku] = obj
    print(f"   [NEW]: {sku} - {trich[:55]}...")

# 6. VAN BAN DI
print("\n[6/8] Tao Van ban di...")
vb_di_list = [
    ("CTY-2025/VBD-001", now-timedelta(days=25), "Cong van",  "V/v bao cao tinh hinh SXKD quy III/2025",                    "Bo Ke hoach Dau tu",       "Phong Kinh doanh", "tp_kd",  "nv_kd_01","DA_PHAT_HANH", now-timedelta(days=25), now-timedelta(days=23), now-timedelta(days=22)),
    ("CTY-2025/VBD-002", now-timedelta(days=18), "To trinh",  "To trinh xin phe duyet ke hoach mua sam thiet bi CNTT 2026", None,                       "Ban Giam doc",     "tp_it",  "nv_it_01","DA_PHE_DUYET",  now-timedelta(days=18), now-timedelta(days=15), None),
    ("CTY-2025/VBD-003", now-timedelta(days=15), "Hop dong",  "Hop dong cung ung dich vu thue van phong nam 2026",           "Tap doan Vingroup",        "Phong Hanh chinh", "tp_hc",  "nv_hc_01","CHO_PHE_DUYET", now-timedelta(days=3),  None,                   None),
    ("CTY-2025/VBD-004", now+timedelta(days=5),  "Thong bao", "Thong bao lich nghi le Quoc khanh 2/9 toan the CBNV",        None,                       "Phong Nhan su",    "tp_ns",  "nv_ns_01","DU_THAO",       None,                   None,                   None),
    ("CTY-2025/VBD-005", now-timedelta(days=10), "Bao cao",   "Bao cao ket qua kiem toan noi bo 6 thang dau nam 2025",       "Bo Tai chinh",             "Phong Ke toan",    "tp_kt",  "nv_kt_01","DA_PHAT_HANH",  now-timedelta(days=10), now-timedelta(days=8),  now-timedelta(days=7)),
    ("CTY-2025/VBD-006", now-timedelta(days=5),  "Quyet dinh","Quyet dinh bo nhiem Truong nhom Phat trien phan mem",         None,                       "Phong IT",         "giamdoc","tp_it",   "DA_PHAT_HANH",  now-timedelta(days=5),  now-timedelta(days=4),  now-timedelta(days=3)),
    ("CTY-2025/VBD-007", now+timedelta(days=3),  "Cong van",  "V/v phoi hop trien khai ke hoach chuyen doi so Q4/2025",      "So Thong tin Truyen thong","Phong IT",         "tp_it",  "nv_it_02","DU_THAO",       None,                   None,                   None),
    ("CTY-2025/VBD-008", now-timedelta(days=2),  "Ke hoach",  "Ke hoach tuyen dung nhan su quy IV nam 2025",                 None,                       "Phong Nhan su",    "tp_ns",  "nv_ns_01","CHO_PHE_DUYET", now-timedelta(days=1),  None,                   None),
    ("CTY-2025/VBD-009", now-timedelta(days=45), "Hop dong",  "Hop dong dich vu kiem toan doc lap nam tai chinh 2025",       "Cong ty TNHH Deloitte VN", "Phong Ke toan",    "giamdoc","tp_kt",   "DA_PHAT_HANH",  now-timedelta(days=45), now-timedelta(days=43), now-timedelta(days=42)),
    ("CTY-2025/VBD-010", now-timedelta(days=8),  "To trinh",  "To trinh xin phe duyet ngan sach marketing Q4/2025",          None,                       "Phong Kinh doanh", "tp_kd",  "nv_kd_01","CAN_SUA_DOI",   now-timedelta(days=8),  None,                   None),
]
van_ban_dis = {}
for row in vb_di_list:
    sku, ngh, loai, trich, dv_ngoai, dv_trong, ng_gui, uid, tt, ngay_gpd, ngay_pd, ngay_ph = row
    if VanBanDi.objects.filter(SoKyHieu=sku).exists():
        van_ban_dis[sku] = VanBanDi.objects.get(SoKyHieu=sku)
        print(f"   [OK]: {sku}")
        continue
    obj = VanBanDi.objects.create(
        SoKyHieu=sku, NgayBanHanh=ngh, LoaiVanBan=loai, TrichYeu=trich,
        DonViNgoaiID=don_vi_ngoais.get(dv_ngoai) if dv_ngoai else None,
        DonViTrongID=phong_bans.get(dv_trong) if dv_trong else None,
        NguoiGui=users.get(ng_gui), UserID=users.get(uid), TrangThai=tt,
        NgayGuiPheDuyet=ngay_gpd, NgayPheDuyet=ngay_pd, NgayPhatHanh=ngay_ph)
    van_ban_dis[sku] = obj
    print(f"   [NEW]: {sku} - {trich[:55]}...")

# 7. PHAN CONG & CHUYEN TIEP
print("\n[7/8] Tao Phan cong & Chuyen tiep...")
pc_den = [
    ("BTC-2025/001",   "nv_kt_01", now-timedelta(days=27), now-timedelta(days=17), "Binh thuong","Hoan thanh",  "Xu ly quyet toan ngan sach"),
    ("BKHDT-2025/002", "nv_pc_01", now-timedelta(days=22), now-timedelta(days=8),  "Cao",        "Dang xu ly",  "Nghien cuu va soan phuc dap"),
    ("STTTT-2025/003", "nv_it_01", now-timedelta(days=17), now-timedelta(days=5),  "Cao",        "Dang xu ly",  "Lap ke hoach trien khai"),
    ("STTTT-2025/003", "nv_it_02", now-timedelta(days=17), now-timedelta(days=5),  "Cao",        "Dang xu ly",  "Ho tro ky thuat"),
    ("FPT-2025/005",   "nv_it_01", now-timedelta(days=10), now+timedelta(days=5),  "Cao",        "Dang xu ly",  "Ra soat hop dong phan mem"),
    ("DLT-2025/006",   "nv_kt_01", now-timedelta(days=8),  now+timedelta(days=2),  "Cao",        "Dang xu ly",  "Chuan bi tai lieu doi soat"),
    ("VCB-2025/012",   "nv_kt_01", now-timedelta(days=37), now-timedelta(days=27), "Binh thuong","Hoan thanh",  "Xu ly thong bao lai suat"),
    ("STTTT-2025/011", "nv_it_02", now-timedelta(days=32), now-timedelta(days=22), "Binh thuong","Hoan thanh",  "Nghien cuu ke hoach CNTT"),
]
for sku, uid, ngay_pc, han_xl, muc_do, tt, ghi_chu in pc_den:
    vbd = van_ban_dens.get(sku); user = users.get(uid)
    if vbd and user:
        obj, created = PhanCong.objects.get_or_create(
            VanBanDenID=vbd, UserID=user,
            defaults={"NgayPhanCong": ngay_pc, "HanXuLy": han_xl, "MucDoUuTien": muc_do, "TrangThaiXuLy": tt, "GhiChu": ghi_chu})
        print(f"   {'[NEW]' if created else '[OK]'} PC Den: [{sku}] -> {uid}")

pc_di = [
    ("CTY-2025/VBD-001","nv_kd_01", now-timedelta(days=26), now-timedelta(days=20),"Cao",        "Hoan thanh",  "Soan bao cao kinh doanh"),
    ("CTY-2025/VBD-002","nv_it_01", now-timedelta(days=17), now-timedelta(days=12),"Cao",        "Hoan thanh",  "Soan to trinh mua thiet bi"),
    ("CTY-2025/VBD-003","nv_hc_01", now-timedelta(days=14), now+timedelta(days=3), "Binh thuong","Dang xu ly",  "Soan hop dong thue van phong"),
    ("CTY-2025/VBD-005","nv_kt_01", now-timedelta(days=9),  now-timedelta(days=6), "Cao",        "Hoan thanh",  "Soan bao cao kiem toan"),
    ("CTY-2025/VBD-007","nv_it_02", now-timedelta(days=1),  now+timedelta(days=7), "Binh thuong","Dang xu ly",  "Soan cong van phoi hop CNTT"),
    ("CTY-2025/VBD-008","nv_ns_01", now-timedelta(days=2),  now+timedelta(days=5), "Binh thuong","Dang xu ly",  "Soan ke hoach tuyen dung"),
    ("CTY-2025/VBD-010","nv_kd_01", now-timedelta(days=7),  now+timedelta(days=3), "Cao",        "Dang xu ly",  "Dieu chinh ngan sach marketing"),
]
for sku, uid, ngay_pc, han_xl, muc_do, tt, ghi_chu in pc_di:
    vbd = van_ban_dis.get(sku); user = users.get(uid)
    if vbd and user:
        obj, created = PhanCong.objects.get_or_create(
            VanBanDiID=vbd, UserID=user,
            defaults={"NgayPhanCong": ngay_pc, "HanXuLy": han_xl, "MucDoUuTien": muc_do, "TrangThaiXuLy": tt, "GhiChu": ghi_chu})
        print(f"   {'[NEW]' if created else '[OK]'} PC Di:  [{sku}] -> {uid}")

ct_data = [
    ("STTTT-2025/003","nv_it_01", now-timedelta(days=16), now-timedelta(days=16), now-timedelta(days=6), "Cao"),
    ("FPT-2025/005",  "tp_it",    now-timedelta(days=9),  now-timedelta(days=9),  now+timedelta(days=7), "Cao"),
    ("DLT-2025/006",  "tp_kt",    now-timedelta(days=7),  now-timedelta(days=7),  now+timedelta(days=3), "Cao"),
]
for sku, uid, ngay_ct, ngay_bd, ngay_hh, muc_do in ct_data:
    vbd = van_ban_dens.get(sku); user = users.get(uid)
    if vbd and user:
        obj, created = ChuyenTiep.objects.get_or_create(
            VanBanDenID=vbd, UserID=user,
            defaults={"NgayChuyenTiep": ngay_ct, "NgayBatDau": ngay_bd, "NgayHetHan": ngay_hh, "MucDoUuTien": muc_do})
        print(f"   {'[NEW]' if created else '[OK]'} CT Den: [{sku}] -> {uid}")

# 8. PHE DUYET, PHAT HANH & LICH SU
print("\n[8/8] Tao Phe duyet, Phat hanh & Lich su...")
pd_data = [
    ("CTY-2025/VBD-001","giamdoc", now-timedelta(days=23), True, "Da kiem tra va phe duyet bao cao kinh doanh Q3."),
    ("CTY-2025/VBD-002","giamdoc", now-timedelta(days=15), True, "Phe duyet ke hoach mua sam thiet bi CNTT 2026."),
    ("CTY-2025/VBD-005","giamdoc", now-timedelta(days=8),  True, "Phe duyet bao cao kiem toan 6 thang dau nam."),
    ("CTY-2025/VBD-006","giamdoc", now-timedelta(days=4),  True, "Phe duyet quyet dinh bo nhiem nhan su."),
    ("CTY-2025/VBD-009","giamdoc", now-timedelta(days=43), True, "Phe duyet hop dong kiem toan Deloitte."),
]
for sku, uid, ngay_pd, tt_duyet, ghi_chu in pd_data:
    vbd = van_ban_dis.get(sku); user = users.get(uid)
    if vbd and user:
        obj, created = PheDuyet.objects.get_or_create(
            VanBanDiID=vbd, UserID=user,
            defaults={"NgayPheDuyet": ngay_pd, "TrangThaiDuyet": tt_duyet, "GhiChu": ghi_chu})
        print(f"   {'[NEW]' if created else '[OK]'} Phe duyet: [{sku}]")

ph_data = [
    ("CTY-2025/VBD-001","tp_hc", "Phat hanh cong van bao cao kinh doanh Q3",     "DA_PHAT_HANH", now-timedelta(days=22)),
    ("CTY-2025/VBD-005","tp_hc", "Phat hanh bao cao kiem toan 6 thang dau nam",  "DA_PHAT_HANH", now-timedelta(days=7)),
    ("CTY-2025/VBD-006","tp_hc", "Phat hanh quyet dinh bo nhiem nhan su IT",     "DA_PHAT_HANH", now-timedelta(days=3)),
    ("CTY-2025/VBD-009","tp_hc", "Phat hanh hop dong kiem toan Deloitte",        "DA_PHAT_HANH", now-timedelta(days=42)),
]
for sku, uid, tieu_de, tt, ngay_ph in ph_data:
    vbd = van_ban_dis.get(sku); user = users.get(uid)
    if vbd and user:
        obj, created = PhatHanh.objects.get_or_create(
            VanBanDiID=vbd, UserID=user,
            defaults={"TieuDe": tieu_de, "TrangThai": tt, "NgayPhatHanh": ngay_ph})
        print(f"   {'[NEW]' if created else '[OK]'} Phat hanh: [{sku}]")

ls_data = [
    (users["nv_kt_01"], "VanBanDen", 1, "Them",     "Nhap van ban den BTC-2025/001",               None,            "DANG_XU_LY"),
    (users["tp_kt"],    "VanBanDen", 1, "Phan cong","Phan cong xu ly cho nv_kt_01",                "DANG_XU_LY",    "DANG_XU_LY"),
    (users["nv_kt_01"], "VanBanDen", 1, "Cap nhat", "Hoan thanh xu ly van ban BTC-2025/001",       "DANG_XU_LY",    "HOAN_THANH"),
    (users["nv_it_01"], "VanBanDen", 3, "Them",     "Nhap van ban den STTTT-2025/003",             None,            "DANG_XU_LY"),
    (users["tp_it"],    "VanBanDen", 3, "Phan cong","Phan cong cho nv_it_01 va nv_it_02",          "DANG_XU_LY",    "DANG_XU_LY"),
    (users["nv_kd_01"], "VanBanDi",  1, "Them",     "Soan van ban di CTY-2025/VBD-001",            None,            "DU_THAO"),
    (users["tp_kd"],    "VanBanDi",  1, "Cap nhat", "Gui phe duyet van ban VBD-001",               "DU_THAO",       "CHO_PHE_DUYET"),
    (users["giamdoc"],  "VanBanDi",  1, "Phe duyet","Phe duyet bao cao kinh doanh Q3",             "CHO_PHE_DUYET", "DA_PHE_DUYET"),
    (users["tp_hc"],    "VanBanDi",  1, "Phat hanh","Phat hanh van ban di VBD-001",                "DA_PHE_DUYET",  "DA_PHAT_HANH"),
]
cnt = 0
for user, loai, doi_tuong_id, hanh_dong, noi_dung, tt_cu, tt_moi in ls_data:
    LichSuHoatDong.objects.create(UserID=user, LoaiDoiTuong=loai, DoiTuongID=doi_tuong_id,
                                   HanhDong=hanh_dong, NoiDungThayDoi=noi_dung, TrangThaiCu=tt_cu, TrangThaiMoi=tt_moi)
    cnt += 1
print(f"   [NEW]: {cnt} ban ghi lich su hoat dong")

print("\n" + "=" * 60)
print("  HOAN THANH! Thong ke du lieu:")
print("=" * 60)
print(f"  Don vi ben trong  : {DonViBenTrong.objects.count():>3}")
print(f"  Don vi ben ngoai  : {DonViBenNgoai.objects.count():>3}")
print(f"  Vai tro           : {VaiTro.objects.count():>3}")
print(f"  Nguoi dung        : {UserAccount.objects.count():>3}")
print(f"  Van ban den       : {VanBanDen.objects.count():>3}")
print(f"  Van ban di        : {VanBanDi.objects.count():>3}")
print(f"  Phan cong         : {PhanCong.objects.count():>3}")
print(f"  Chuyen tiep       : {ChuyenTiep.objects.count():>3}")
print(f"  Phe duyet         : {PheDuyet.objects.count():>3}")
print(f"  Phat hanh         : {PhatHanh.objects.count():>3}")
print(f"  Lich su hoat dong : {LichSuHoatDong.objects.count():>3}")
print("=" * 60)
print("\n  TAI KHOAN DEMO:")
accounts = [
    ("admin",    "admin123",   "Quan tri he thong"),
    ("giamdoc",  "giamdoc123", "Tong giam doc - Ban Giam doc"),
    ("tp_it",    "tp123",      "Truong phong IT"),
    ("tp_hc",    "tp123",      "Truong phong Hanh chinh"),
    ("tp_kt",    "tp123",      "Truong phong Ke toan"),
    ("tp_ns",    "tp123",      "Truong phong Nhan su"),
    ("tp_kd",    "tp123",      "Truong phong Kinh doanh"),
    ("tp_pc",    "tp123",      "Truong phong Phap che"),
    ("nv_it_01", "nv123",      "Nhan vien IT 01"),
    ("nv_it_02", "nv123",      "Nhan vien IT 02"),
    ("nv_hc_01", "nv123",      "Nhan vien Hanh chinh 01"),
    ("nv_kt_01", "nv123",      "Nhan vien Ke toan 01"),
    ("nv_ns_01", "nv123",      "Nhan vien Nhan su 01"),
    ("nv_kd_01", "nv123",      "Nhan vien Kinh doanh 01"),
    ("nv_pc_01", "nv123",      "Nhan vien Phap che 01"),
]
for u, p, role in accounts:
    print(f"  {u:<15} | {p:<12} | {role}")
print("=" * 60)
print("\n  SEED HOAN TAT!\n")
