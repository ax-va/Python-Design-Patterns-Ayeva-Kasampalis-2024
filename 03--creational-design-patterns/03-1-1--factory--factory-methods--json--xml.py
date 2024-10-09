"""
In the factory design pattern, a client (meaning client code) asks for an object
without knowing where the object is coming from (that is, which class is used to generate it).
->
It is easier to track which objects are created if this is done through a central function,
compared to letting a client create objects using a direct class instantiation.

Factories typically come in two forms:

- the factory method = in Python, a function that returns a different object per input parameter
-> the main critique in Python: over-engineered or unnecessarily complex

- the abstract factory = group of factory methods
"""
import json
import xml.etree.ElementTree as ET
from pathlib import Path


class JSONDataExtractor:
	def __init__(self, filepath: Path):
		self.data = {}
		with open(filepath) as f:
			self.data = json.load(f)

	@property
	def parsed_data(self):
		return self.data


class XMLDataExtractor:
	def __init__(self, filepath: Path):
		self.tree = ET.parse(filepath)

	@property
	def parsed_data(self):
		return self.tree


# Write the factory function
def extract_factory(filepath: Path):
	ext = (filepath.name.split(".")[-1]).lower()
	if ext == "json":
		return JSONDataExtractor(filepath)
	elif ext == "xml":
		return XMLDataExtractor(filepath)
	raise ValueError(f"Cannot extract data from {filepath}.")


# with the factory function -> complexer
def main_v1(case: str):
	dir_path = Path(__file__).parent
	match case:
		case "json":
			path = dir_path / Path("data/movies.json")
			extractor = extract_factory(path)
			data = extractor.parsed_data
			for movie in data:
				print(f"- {movie['title']}")
				director = movie["director"]
				if director:
					print(f"   Director: {director}")
				genre = movie["genre"]
				if genre:
					print(f"   Genre: {genre}")
		case "xml":
			path = dir_path / Path("data/persons.xml")
			extractor = extract_factory(path)
			data = extractor.parsed_data
			# Use XPath
			search_xpath = ".//person[lastName='Liar']"
			items = data.findall(search_xpath)
			for item in items:
				firstname = item.find("firstName").text
				lastname = item.find("lastName").text
				print(f"- {firstname} {lastname}")
				for pn in item.find("phoneNumbers"):
					pn_type = pn.attrib["type"]
					pn_val = pn.text
					phone = f"{pn_type}: {pn_val}"
					print(f"   {phone}")


# without the factory function -> simpler
def main_v2(case: str):
	dir_path = Path(__file__).parent
	match case:
		case "json":
			path = dir_path / Path("data/movies.json")
			# Simple is better than complex
			data = JSONDataExtractor(path).parsed_data
			for movie in data:
				print(f"- {movie['title']}")
				director = movie["director"]
				if director:
					print(f"   Director: {director}")
				genre = movie["genre"]
				if genre:
					print(f"   Genre: {genre}")
		case "xml":
			path = dir_path / Path("data/persons.xml")
			# Simple is better than complex
			data = XMLDataExtractor(path).parsed_data
			# Use XPath
			search_xpath = ".//person[lastName='Liar']"
			items = data.findall(search_xpath)
			for item in items:
				firstname = item.find("firstName").text
				lastname = item.find("lastName").text
				print(f"- {firstname} {lastname}")
				for pn in item.find("phoneNumbers"):
					pn_type = pn.attrib["type"]
					pn_val = pn.text
					phone = f"{pn_type}: {pn_val}"
					print(f"   {phone}")

if __name__ == "__main__":
	print("* JSON case *")
	# * JSON case *
	main_v1(case="json")
	# - After Dark in Central Park
	# - Boarding School Girls' Pajama Parade
	# - Buffalo Bill's Wild West Parade
	# - Caught
	# - Clowns Spinning Hats
	# - Capture of Boer Battery by British
	#    Director: James H. White
	#    Genre: Short documentary
	# - The Enchanted Drawing
	#    Director: J. Stuart Blackton
	# - Family Troubles
	# - Feeding Sea Lions
	print("* XML case *")
	# * XML case *
	main_v1(case="xml")
	# - Jimmy Liar
	#    home: 212 555-1235
	# - Patty Liar
	#    home: 212 555-1235
	#    mobile: 001 452-8819
