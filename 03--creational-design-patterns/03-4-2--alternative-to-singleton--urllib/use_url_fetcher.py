import url_fetcher


for url in [
    "http://python.org",
    "https://www.djangoproject.com/",
]:
    url_fetcher.fetcher.fetch(url)

print(f"Fetched URLs: {url_fetcher.fetcher.urls}")
# Fetched URLs: ['http://python.org', 'https://www.djangoproject.com/']