"""
Lazy Loading

The *Lazy Loading* pattern is used to defer the initialization or loading of resources
until they are actually needed.
"""

# Example: Initialize a class attribute only when it's accessed for the first time

class LazyLoadedData:
	def __init__(self):
		# Expensive data hasn't been loaded yet
		self._data = None

	@property
	def data(self):
		if self._data is None:
			self._data = self.load_data()

		return self._data

	def load_data(self):
		print("Simulating loading expensive data...")
		return sum(i * i for i in range(100000))


def main():
	obj = LazyLoadedData()
	print("Object created, expensive attribute not loaded yet.")
	print("Accessing expensive attribute:")
	print(obj.data)
	print("Accessing expensive attribute again, no reloading occurs:")
	print(obj.data)


if __name__ == "__main__":
	main()
	# Object created, expensive attribute not loaded yet.
	# Accessing expensive attribute:
	# Simulating loading expensive data...
	# 333328333350000
	# Accessing expensive attribute again, no reloading occurs:
	# 333328333350000
