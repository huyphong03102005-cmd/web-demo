
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, parse_qs


class OOBReceiver(BaseHTTPRequestHandler):

    def do_GET(self):
        url = urlsplit(self.path)
        params = parse_qs(url.query)

        if (
            url.path != "/callback"
            or params.get("event") != ["OOB_DEMO"]
        ):
            self.send_error(404)
            return

        print(
            "[OOB CALLBACK] Da nhan tin hieu OOB_DEMO",
            flush=True
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = ThreadingHTTPServer(
        ("127.0.0.1", 8765),
        OOBReceiver
    )

    print("[OOB RECEIVER] Dang lang nghe tai:")
    print("http://127.0.0.1:8765", flush=True)

    server.serve_forever()
