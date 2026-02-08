import requests

def check_directory_listing(url, report):
    """
    OWASP: Security Misconfiguration
    Check for Directory Listing vulnerability
    """

    directories = [
        "/uploads/",
        "/images/",
        "/files/",
        "/backup/"
    ]

    for directory in directories:
        test_url = url.rstrip("/") + directory

        try:
            response = requests.get(test_url, timeout=10)

            # Common text shown when directory listing is enabled
            if "Index of /" in response.text:
                report.write(f"[!] Directory Listing Enabled: {test_url}")
                return

        except Exception:
            # Ignore errors and continue scanning
            pass

