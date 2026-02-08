import requests

def check_open_redirect(url, report):
    """
    OWASP: Unvalidated Redirects
    Detects open redirect vulnerabilities
    """

    payloads = [
        "?next=https://evil.com",
        "?url=https://evil.com",
        "?redirect=https://evil.com",
        "?return=https://evil.com"
    ]

    for payload in payloads:
        test_url = url.rstrip("/") + payload

        try:
            response = requests.get(
                test_url,
                timeout=10,
                allow_redirects=False
            )

            # Redirect response
            if response.status_code in [301, 302, 303, 307, 308]:
                location = response.headers.get("Location", "")

                if "evil.com" in location:
                    report.write(f"[!] Open Redirect Found: {test_url}")
                    return

        except Exception:
            pass
