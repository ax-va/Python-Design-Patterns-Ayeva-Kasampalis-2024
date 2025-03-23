"""
Don't call protected class' members outside their class
because the developer can change the ones in the class' definition in the future.
Encapsulate them in public methods instead.
"""

class Book:
	def __init__(self, title, author):
		self._title = title
		self._author = author

	def presentation_line(self):
		return f"{self._title} by {self._author}"


if __name__ == "__main__":
	b1 = Book(
		"The Dark Tower II: The Drawing of the Three",
		"Stephen King",
	)

	# bad practice
	print(f"{b1._title} by {b1._author}")
	# The Dark Tower II: The Drawing of the Three by Stephen King

	# recommended
	print(b1.presentation_line())
	# The Dark Tower II: The Drawing of the Three by Stephen King
