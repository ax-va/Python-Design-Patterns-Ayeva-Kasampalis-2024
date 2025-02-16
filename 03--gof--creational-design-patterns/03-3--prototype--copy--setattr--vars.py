"""
The *Prototype* pattern helps us create new objects by copying existing ones
with the change of some attributes instead of creating to them from scratch.
This is useful if the object is expensive to create.
"""
import copy
from typing import Any


class Website:
	def __init__(
		self,
		name: str,
		domain: str,
		description: str,
		**kwargs,
	):
		self.name = name
		self.domain = domain
		self.description = description

		for key in kwargs:
			# Use the `setattr(obj, attr, val)` idiom
			setattr(self, key, kwargs[key])

	def __str__(self) -> str:
		summary = [f"- {self.name} (ID: {id(self)})\n"]
		# The `vars` function returns the `__dict__` attribute of an object.
		# The `__dict__` attribute is a dictionary containing both data attributes and methods.
		# Not all objects have a `__dict__` attribute, for example, built-in types such as lists and dictionaries.
		infos = vars(self).items()
		ordered_infos = sorted(infos)
		for attr, val in ordered_infos:
			if attr == "name":
				continue
			summary.append(f"{attr}: {val}\n")
		return "".join(summary)


class Prototype:
	def __init__(self):
		self.registry = {}

	def register(self, identifier: int | str, obj: Any):
		self.registry[identifier] = obj

	def unregister(self, identifier: int | str):
		del self.registry[identifier]

	def clone(self, identifier: int | str, **attrs) -> Any:
		found = self.registry.get(identifier)
		if not found:
			raise ValueError(f"Incorrect object identifier: {identifier}")
		obj = copy.deepcopy(found)
		# Overwrite or set given attributes
		for key in attrs:
			setattr(obj, key, attrs[key])
		return obj


def main():
	# attribute to be copied by `copy.deepcopy`
	keywords = [
		"python",
		"programming",
		"scripts",
		"data",
		"development",
		"automation"
	]

	site1 = Website(
		"Python",
		domain="python.org",
		description="Programming language and ecosystem",
		category="Open Source Software",
		keywords=keywords,
	)

	proto = Prototype()
	proto.register("python-001", site1)

	site2 = proto.clone(
		"python-001",
		name="Python Package Index",
		domain="pypi.org",
		description = "Repository for published packages",
	)

	for site in [site1, site2]:
		print(site)


if __name__ == "__main__":
	main()
"""
- Python (ID: 138659149578848)
category: Open Source Software
description: Programming language and ecosystem
domain: python.org
keywords: ['python', 'programming', 'scripts', 'data', 'development', 'automation']

- Python Package Index (ID: 138659149584560)
category: Open Source Software
description: Repository for published packages
domain: pypi.org
keywords: ['python', 'programming', 'scripts', 'data', 'development', 'automation']
"""