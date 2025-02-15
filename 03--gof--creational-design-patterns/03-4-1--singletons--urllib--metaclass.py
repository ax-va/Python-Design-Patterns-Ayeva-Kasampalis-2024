"""
The Singleton pattern restricts a class instance to a single object.
->
Coordinates actions for the system such as in
- controlling concurrent access to a shared resource
(for example, the class managing the connection to a database),
- a service or resource that can be accessed
from different parts of the application or by different users and do its work
(for example, the class at the core of a logging system or utility).

Notation:
In the Python programmer community, the Singleton pattern is actually considered as *anti-pattern*.
In Python, developers often prefer a simpler alternative to singleton: using a *module-level global object*.
See the `03-4-2--alternative-to-singleton` directory where it is used.

See also:
- The Global Object Pattern
https://python-patterns.guide/python/module-globals
"""
import urllib.request


# Example:
# Ensure that only one instance of the `URLFetcher` class exist to keep track of all fetched URLs.
# To make it a singleton, the *metaclass* technique will be used.


class SingletonType(type):
	""" Provides a metaclass for a singleton. """
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			obj = super(SingletonType, cls).__call__(*args, **kwargs)
			cls._instances[cls] = obj
		return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
	def __init__(self):
		self.urls = []

	def fetch(self, url):
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req) as response:
			if response.code == 200:
				page_content = response.read()
				with open("data/content.html", "a") as f:
					f.write(str(page_content) + "\n")
				self.urls.append(url)


def main():
	my_urls = [
		"http://python.org",
		"https://www.djangoproject.com/",
	]

	print(URLFetcher() is URLFetcher())

	fetcher = URLFetcher()
	for url in my_urls:
		fetcher.fetch(url)

	print(f"Fetched URLs: {fetcher.urls}")


if __name__ == "__main__":
	main()
	# True
	# Fetched URLs: ['http://python.org', 'https://www.djangoproject.com/']
