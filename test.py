import requests

from cashier import cache, Cashier
from time import time

TEST_DB_FILENAME = "testing.db"
c = Cashier(file_name=TEST_DB_FILENAME)
c.clear()

data = requests.get("https://news.ycombinator.com")
if data.status_code == 200:
    page = data.content
else:
    page = ""
    print("Failed to scrape test urls")
    exit()

urls = []


def getURL(page):
    start_link = page.find(b"a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find(b'"', start_link)
    end_quote = page.find(b'"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote


part_page = page
while True:
    url, n = getURL(page)
    page = page[n:]
    if url:
        urls.append(url)
    else:
        break

final_urls = []
for url in urls:
    if b"http" in url and url not in final_urls:
        final_urls.append(url)


def add(a):
    try:
        return requests.get(a)
    except:
        print("Scraping failed for %s" % a)
        return


start_time = time()
for i in final_urls:
    add(i)
end_time = time()
no_cache_run = end_time - start_time


@cache(TEST_DB_FILENAME, 60, 100, True)
def add(a):
    try:
        return requests.get(a)
    except:
        print("Scraping failed for %s" % a)
        return


start_time = time()
for i in final_urls:
    add(i)
end_time = time()
first_run = end_time - start_time

start_time = time()
for i in final_urls:
    add(i)
end_time = time()
cache_run = end_time - start_time
print("No Cache Run: %f seconds\nFirst Caching Run: %f seconds\nCached Run: %f seconds (%d x faster)" % (
    no_cache_run, first_run, cache_run, int(no_cache_run / cache_run)))

c.clear()
