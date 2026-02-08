import requests

def check_http_methods(url, report):
    """
    Checks for dangerous HTTP methods
    OWASP: Security Misconfiguration
    """

    try:
        # OPTIONS request shows allowed methods
        response = requests.options(url, timeout=10)

        allow = response.headers.get("Allow", "")

        # Dangerous methods
        if "PUT" in allow:
            report.write(f"[!] Dangerous HTTP Method ENABLED (PUT): {url}")

        if "DELETE" in allow:
            report.write(f"[!] Dangerous HTTP Method ENABLED (DELETE): {url}")

    except Exception:
        # Ignore errors and continue scanning
        pass
