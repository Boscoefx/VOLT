import os
from concurrent.futures import ThreadPoolExecutor
from core.crawler import Crawler
from modules.report import Report

from modules.forms import scan_forms
from modules.xss import scan_xss
from modules.sqli import scan_sqli
from modules.headers import check_headers
from modules.http_methods import check_http_methods
from modules.dir_listing import check_directory_listing
from modules.open_redirect import check_open_redirect
from modules.csrf import scan_csrf
from modules.idor import check_idor

from config import MAX_THREADS


class Scanner:
    def __init__(self, target, crawl_limit=None):
        self.target = target
        self.crawl_limit = crawl_limit

    def run_tests(self, url, report):
        scan_forms(url, report)
        scan_xss(url, report)
        scan_sqli(url, report)
        check_headers(url, report)
        check_http_methods(url, report)
        check_directory_listing(url, report)
        check_open_redirect(url, report)
        scan_csrf(url, report)
        check_idor(url, report)

    def run(self):
        report = Report()

        crawler = Crawler(self.target, max_urls=self.crawl_limit)
        urls = crawler.crawl()

        report.write(f"[INFO] Total URLs: {len(urls)}")

        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            for url in urls:
                executor.submit(self.run_tests, url, report)

        report.close()

        # -------- OPEN HTML REPORT AUTOMATICALLY --------
        try:
            import webbrowser
            html_path = os.path.abspath("reports/report.html")
            webbrowser.open(f"file://{html_path}")
            print("\n[INFO] HTML report opened in browser")
        except Exception as e:
            print("[ERROR] Could not open HTML report:", e)

