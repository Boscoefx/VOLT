import re
from core.http_client import get
from modules.severity import SEVERITY

def check_idor(url, report):
    pattern = r"(id|uid|user_id|account_id)=([0-9]+)"
    match = re.search(pattern, url)

    if not match:
        return

    param, value = match.groups()
    new = int(value) + 1

    test_url = url.replace(f"{param}={value}", f"{param}={new}")

    try:
        r1 = get(url)
        r2 = get(test_url)

        if abs(len(r1.text) - len(r2.text)) > 100:
            report.write(
                f"{SEVERITY['IDOR']} Possible IDOR vulnerability: {url}"
            )
    except:
        pass

