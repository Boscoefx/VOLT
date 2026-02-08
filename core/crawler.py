from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from core.http_client import get
from config import TIMEOUT


class Crawler:
    def __init__(self, start_url, max_urls=None):
        self.start_url = start_url
        self.domain = urlparse(start_url).netloc
        self.visited = set()
        self.max_urls = max_urls

    def is_valid_url(self, url):
        parsed = urlparse(url)

        # Stay inside same domain
        if parsed.netloc != self.domain:
            return False

        # Skip unwanted file types
        if url.lower().endswith((
            ".png", ".jpg", ".jpeg", ".gif",
            ".css", ".js", ".pdf", ".zip",
            ".rar", ".exe", ".svg"
        )):
            return False

        return True

    def normalize(self, url):
        # Remove fragments and trailing slash
        url = url.split("#")[0]
        return url.rstrip("/")

    def crawl(self):
        queue = [self.start_url]

        print(f"[CRAWLER] Starting crawl (limit={self.max_urls or 'FULL'})")

        while queue:
            if self.max_urls and len(self.visited) >= self.max_urls:
                break

            url = queue.pop(0)
            url = self.normalize(url)

            if url in self.visited:
                continue

            self.visited.add(url)
            print(f"[CRAWLER] ({len(self.visited)}) {url}")

            try:
                r = get(url)
            except Exception:
                continue

            soup = BeautifulSoup(r.text, "lxml")

            for a in soup.find_all("a", href=True):
                full_url = urljoin(url, a["href"])
                full_url = self.normalize(full_url)

                if self.is_valid_url(full_url):
                    if full_url not in self.visited and full_url not in queue:
                        queue.append(full_url)

        print(f"[CRAWLER] Finished. Total URLs: {len(self.visited)}")
        return list(self.visited)

