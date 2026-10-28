import os
from urllib.request import urlopen
from django.conf import settings


def register_oob_function(db_connection):
    """
    Dang ky ham demo_oob() vao SQLite
    de mo phong SQL Injection Out-of-Band.
    """

    # Chi cho phep trong moi truong demo
    if not settings.DEBUG:
        return

    if os.getenv("OOB_DEMO_ENABLED") != "1":
        return

    # Chi su dung voi SQLite
    if db_connection.vendor != "sqlite":
        return

    db_connection.ensure_connection()

    # Ham duoc goi tu cau truy van SQL
    def demo_oob():

        callback_url = (
            "http://127.0.0.1:8765/"
            "callback?event=OOB_DEMO"
        )

        try:
            with urlopen(callback_url, timeout=2) as response:
                response.read()

            print("[OOB LAB] HTTP callback thanh cong")

        except Exception as e:
            print(f"[OOB LAB] Callback loi: {e}")

        return "PING"

    # Dang ky ham Python vao SQLite
    db_connection.connection.create_function(
        "demo_oob",
        0,
        demo_oob
    )