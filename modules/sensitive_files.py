import requests

def check_sensitive_files(url, report):
    """
    OWASP: Sensitive Data Exposure
    Checks for exposed sensitive files
    """

    sensitive_files = [
        ".env",
        "config.php",
        "backup.zip",
        "db.sql",
        ".git/config",
        "wp-config.php"
    ]

    for file in sensitive_files:
        test_url = url.rstrip("/") + "/" + file

        try:
            response = requests.get(test_url, timeout=10)

            if response.status_code == 200:
                report.write(f"[!] Sensitive File Exposed: {test_url}")

        except Exception:
            pass
