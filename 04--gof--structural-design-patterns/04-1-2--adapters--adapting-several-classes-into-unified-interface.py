"""
The adapter pattern is a structural design pattern to make two incompatible interfaces compatible.
For example, to adapt an old system component to a new system component or vice versa.

- Consider adapting several classes into a unified interface.
"""

# The `organize_performance` method is the main action that `Club` can perform
class Club:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"the club {self.name}"

	def organize_event(self):
		return "hires an artist to perform some evenings in the club"


# In `Musician`, the main action is performed by the `play` method
class Musician:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"the musician {self.name}"

	def play(self):
		return "plays music"


# In `Dancer`, the main action is performed by the `dance` method
class Dancer:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"the dancer {self.name}"

	def dance(self):
		return "does a dance performance"


# A generic `Adapter` class adapts a number of objects
# with different interfaces into one unified interface.
# `adapted_methods` is a dictionary containing key-value pairs matching
# the method the client calls and the method that should be called.
class Adapter:
	def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self.obj)


# The client code can continue using the `organize_performance` method
# on all objects without the need to be aware of any interface differences.
def main():
	objects = [
		Club("Jazz Cafe"),
		Musician("Roy Ayers"),
		Dancer("Shane Sparks"),
	]

	for obj in objects:
		if hasattr(obj, "play"):
			adapted_methods = dict(organize_event=obj.play)
			obj = Adapter(obj, adapted_methods)
		if hasattr(obj, "dance"):
			adapted_methods = dict(organize_event=obj.dance)
			obj = Adapter(obj, adapted_methods)

		# The `Musician` and `Dancer` classes are compatible with the interface expected by
		# the client code without changing the source code of these external classes.
		print(f"{obj} {obj.organize_event()}")


if __name__ == "__main__":
	main()
	# the club Jazz Cafe hires an artist to perform some evenings in the club
	# the musician Roy Ayers plays music
	# the dancer Shane Sparks does a dance performance
