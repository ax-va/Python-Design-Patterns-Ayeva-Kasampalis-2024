"""
While the **adapter pattern** is used *later* to make unrelated classes work together,
the **bridge pattern** is designed *up-front* to decouple an implementation from its abstraction.

In the bridge pattern, the following special components are defined:
- an abstraction that applies to all the classes;
- a separate interface for the different objects involved.
"""
import os
import urllib.request
from typing import Protocol

# Example:
# building an application where the user is going to manage
# and deliver content # after fetching it from diverse sources,
# which could be the following:
# - a web page (based on its URL),
# - a resource accessed on an FTP server,
# - a file on the local filesystem,
# - a database server.
# ->
# Define an abstraction for the Resource Content and a separate interface
# for the objects that are responsible for fetching the content.

# This class is called the Implementor
class ResourceContentFetcher(Protocol):
	def fetch(self, path: str) -> str:
		...


# Define a class for the interface of the abstraction
class ResourceContent:
	def __init__(self, imp: ResourceContentFetcher):
		# To maintain a reference to the object that represents the Implementor
		# (fulfilling the ResourceContentFetcher interface).
		self._imp = imp

	def get_content(self, path):
		return self._imp.fetch(path)


# implementation class for fetching content from a URL
class URLFetcher:
	def fetch(self, path):
		res = ""
		req = urllib.request.Request(url=path)
		with urllib.request.urlopen(req) as response:
			if response.code == 200:
				res = response.read()
		return res


# implementation class for fetching content from the local filesystem
class LocalFileFetcher:
	def fetch(self, path):
		with open(path) as f:
			res = f.read()
		return res


def main():
	url_fetcher = URLFetcher()
	rc = ResourceContent(url_fetcher)
	res = rc.get_content("http://python.org")
	print(f"Fetched content with {len(res)} characters")

	local_file_fetcher = LocalFileFetcher()
	rc = ResourceContent(local_file_fetcher)
	res = rc.get_content(os.path.abspath(__file__))
	print(f"Fetched content with {len(res)} characters")


if __name__ == "__main__":
	main()
	# Fetched content with 51064 characters
	# Fetched content with 2179 characters
