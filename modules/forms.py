import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore

def scan_forms(url, report=None):
    try:
        r = requests.get(url, timeout=10)
    except:
        return

    soup = BeautifulSoup(r.text, "lxml")
    forms = soup.find_all("form")

    if not forms:
        msg = "  [INFO] No forms found"
        if report:
            report.write(msg)
        else:
            print(Fore.RED + msg)
        return

    msg = f"  [+] Found {len(forms)} form(s)"
    if report:
        report.write(msg)
    else:
        print(Fore.RED + msg)

    for i, form in enumerate(forms, start=1):
        action = form.get("action")
        method = form.get("method", "get").upper()
        full_action = urljoin(url, action) if action else url

        report.write(f"    Form #{i}")
        report.write(f"      Method : {method}")
        report.write(f"      Action : {full_action}")

        inputs = form.find_all(["input", "textarea", "select"])
        for inp in inputs:
            name = inp.get("name")
            if name:
                report.write(f"        Input : {name}")

