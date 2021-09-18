from urllib.request import urlopen
import time

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

        # Refreshing the cache after a certain time
        self.time_cache_difference = 18000 # 5 hours
        self.last_refreshed = time.time()

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page ... ")
            self._content = urlopen(self.url).read()

        if (time.time() - self.last_refreshed) >= self.time_cache_difference:
            self.last_refresh = time.time()
            self._content = urlopen(self.url).read()
        else:
            return self._content