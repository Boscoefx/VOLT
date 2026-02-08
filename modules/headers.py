import requests
from colorama import Fore

def check_headers(url, report=None):
    try:
        r = requests.get(url, timeout=10)
    except:
        return

    headers = r.headers
    missing = []

    if "Content-Security-Policy" not in headers:
        missing.append("Content-Security-Policy")
    if "X-Frame-Options" not in headers:
        missing.append("X-Frame-Options")
    if "X-Content-Type-Options" not in headers:
        missing.append("X-Content-Type-Options")

    if missing:
        msg = "  [!] Missing security headers: " + ", ".join(missing)
    else:
        msg = "  [+] Security headers OK"

    if report:
        report.write(msg)
    else:
        print(Fore.RED + msg)

