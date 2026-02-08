import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import argparse
from core.scanner import Scanner
from colorama import Fore, Style
from urllib.parse import urlparse


def validate_url(url):
    p = urlparse(url)
    return p.scheme in ("http", "https") and p.netloc


# ===== BANNER =====
print(Fore.RED + r"""
██╗   ██╗ ██████╗ ██╗     ████████╗
██║   ██║██╔═══██╗██║     ╚══██╔══╝
██║   ██║██║   ██║██║        ██║   
╚██╗ ██╔╝██║   ██║██║        ██║   
 ╚████╔╝ ╚██████╔╝███████╗   ██║   
  ╚═══╝   ╚═════╝ ╚══════╝   ╚═╝   

        VOLT Web Vulnerability Scanner
        Version      : v1.00
        Author       : Bosco
""" + Style.RESET_ALL)


# ===== SHORT PROFESSIONAL DISCLAIMER =====
print(Fore.RED + """
[!] LEGAL DISCLAIMER
------------------------------------------------------------

This tool is intended strictly for EDUCATIONAL and AUTHORIZED
SECURITY TESTING purposes only.

Use this software ONLY on systems and websites you own
or have explicit permission to test.

Unauthorized scanning or testing of any system may be illegal.

By using this tool, you acknowledge that:

- You accept full responsibility for your actions.
- All risks and consequences are solely on the user.
- The author and project are not liable for any damage,
  misuse, or legal issues resulting from its use.
- This software is provided "AS IS" without any warranty.

Use responsibly and ethically.

------------------------------------------------------------
""" + Style.RESET_ALL)


# ===== COMMAND LINE ARGUMENTS =====
parser = argparse.ArgumentParser(
    description="VOLT - Web Vulnerability Scanner v1.00",
    epilog="Example: python volt.py -u http://example.com -l 20"
)

parser.add_argument(
    "-u", "--url",
    help="Target URL to scan",
    required=False
)

parser.add_argument(
    "-l", "--limit",
    help="Limit number of URLs to crawl",
    type=int,
    default=None
)

parser.add_argument(
    "-f", "--fast",
    help="Fast scan mode (limit 10 URLs)",
    action="store_true"
)

parser.add_argument(
    "--version",
    action="version",
    version="VOLT Scanner v1.00"
)

args = parser.parse_args()


# ===== INTERACTIVE OR CLI MODE =====
if not args.url:
    print("\nNo URL provided. Switching to interactive mode...\n")

    target = input("Enter target URL: ").strip()

    if not validate_url(target):
        print("Invalid URL format")
        print("Example: http://testphp.vulnweb.com/search.php?test=abc")
        exit()

    print("\nScan Mode Options:")
    print("1) Full Scan (slow)")
    print("2) Limited Scan (example: 20 URLs)\n")

    choice = input("Enter option (1 or 2): ").strip()

    if choice == "1":
        crawl_limit = None

    elif choice == "2":
        try:
            crawl_limit = int(input("Enter crawl limit (e.g. 20): "))
        except:
            print("Invalid number entered")
            exit()

    else:
        print("Invalid option selected")
        exit()

else:
    target = args.url.strip()

    if not validate_url(target):
        print("Invalid URL format")
        print("Example: http://testphp.vulnweb.com/search.php?test=abc")
        exit()

    crawl_limit = args.limit

    if args.fast:
        crawl_limit = 10


print(f"\n[INFO] Target: {target}")
print(f"[INFO] Crawl Limit: {crawl_limit if crawl_limit else 'FULL'}\n")


scanner = Scanner(target, crawl_limit)
scanner.run()

