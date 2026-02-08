from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from core.http_client import get
from modules.severity import SEVERITY

PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>"
]

def scan_xss(url, report):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    if not params:
        return

    report.write("  [XSS] Testing parameters...")

    for payload in PAYLOADS:
        for param in params:
            test = params.copy()
            test[param] = payload

            new_query = urlencode(test, doseq=True)
            test_url = urlunparse(parsed._replace(query=new_query))

            try:
                r = get(test_url)

                if payload in r.text:
                    report.write(
                        f"{SEVERITY['XSS']} Reflected XSS at parameter: {param}"
                    )
                    report.write(f"URL: {test_url}")
                    return
            except:
                pass

