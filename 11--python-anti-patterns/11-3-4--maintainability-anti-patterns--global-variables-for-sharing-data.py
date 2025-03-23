"""
Avoid global variables for sharing data.
Otherwise, you get bugs if different parts of the application
unexpectedly modify global state.
"""

# not recommended
counter = 0  # global variable


def increment():
	global counter
	counter += 1


def reset():
	global counter
	counter = 0


# better
class Counter:
	def __init__(self):
		self.value = 0

	def increment(self):
		self.value += 1

	def reset(self):
		self.value = 0


if __name__ == "__main__":


	def foo():
		for _ in range(5):
			print(f"Counter value: {counter.value}")
			# some operations
			counter.increment()


	counter = Counter()
	foo()
	# Counter value: 0
	# Counter value: 1
	# Counter value: 2
	# Counter value: 3
	# Counter value: 4
	counter.reset()
	print(f"Counter value: {counter.value}")
	# Counter value: 0
