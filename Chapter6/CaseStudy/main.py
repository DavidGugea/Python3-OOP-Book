from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys

LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")


class LinkCollector:
    def __init__(self, url):
        self.url = url  # http://localhost/Coding/pyserver/index.html
        self.main_start_url = self.url[0:self.url.rindex("/")]  # http://localhost/Coding/pyserver

        self.collected_links = set()
        self.visited_links = set()

    def collect_links(self, path):
        if path:
            full_url = self.url + path
        else:
            full_url = self.url

        self.visited_links.add(full_url)
        page = str(urlopen(full_url).read())

        links = LINK_REGEX.findall(page)
        links = {self.normalize_url(link) for link in links}
        self.collected_links = links.union(self.collected_links)
        unvisited_links = links.difference(self.visited_links)

        for link in unvisited_links:
            if link.startswith(self.main_start_url + "/index.html"):
                self.collect_links(urlparse(link).path)

    def normalize_url(self, link):
        if link.startswith("http"):
            return link
        elif link.startswith("/"):
            return "{0}/{1}".format(self.main_start_url, link[1:])
        else:
            return "{0}/{1}".format(self.main_start_url, link)


if __name__ == '__main__':
    collector = LinkCollector(sys.argv[1])
    collector.collect_links(None)

    for link in collector.collected_links:
        print(link)
