from bs4 import BeautifulSoup
from core.http_client import get
from modules.severity import SEVERITY

def scan_csrf(url, report):
    try:
        r = get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        for form in soup.find_all("form"):
            inputs = form.find_all("input", {"type": "hidden"})

            token = False
            for i in inputs:
                name = i.get("name", "").lower()
                if any(x in name for x in ["csrf", "token", "xsrf"]):
                    token = True

            if not token:
                report.write(
                    f"{SEVERITY['CSRF']} Form without CSRF protection at {url}"
                )
    except:
        pass

