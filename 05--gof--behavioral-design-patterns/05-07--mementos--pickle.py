"""
The *Memento* pattern is used to take a snapshot of the internal state of an object,
so that the object can be restored with it when needed.
In this design pattern, the following definitions are used:
- The *memento* is a simple object that contains basic state storage and retrieval capabilities.
- The *originator* is an object that gets and sets values of memento instances.
- The *caretaker* is an object that can store and retrieve all previously created memento instances.

In this example, we use the pickle module that can transform a complex object into a byte stream, and vice versa:
https://docs.python.org/3/library/pickle.html

Warning:
The pickle module is not secure.
Only unpickle data you trust.
"""
import pickle


class Quote:
	def __init__(self, text, author):
		self.text = text
		self.author = author

	def save_state(self):
		current_state = pickle.dumps(self.__dict__)
		return current_state

	def restore_state(self, memento):
		previous_state = pickle.loads(memento)
		self.__dict__.clear()
		self.__dict__.update(previous_state)

	def __str__(self):
		return f"{self.text}\n- By {self.author}."


if __name__ == "__main__":
	print("** Quote 1 **")
	# ** Quote 1 **
	q1 = Quote(
		"A room without books is like a body without a soul.",
		"Unknown author",
	)
	print(f"\nOriginal version:\n{q1}")
	#
	# Original version:
	# A room without books is like a body without a soul.
	# - By Unknown author.
	q1_mem = q1.save_state()

	# The author's name was found
	q1.author = "Marcus Tullius Cicero"
	print(f"\nThe author was found, and the update was done:\n{q1}")
	#
	# The author was found, and the update was done:
	# A room without books is like a body without a soul.
	# - By Marcus Tullius Cicero.

	# Undo by restoring previous state
	q1.restore_state(q1_mem)
	print(f"\nThe previous version has been restored:\n{q1}")
	#
	# The previous version has been restored:
	# A room without books is like a body without a soul.
	# - By Unknown author.

	print("\n** Quote 2 **")
	#
	# * Quote 2 **
	text = (
		"To be you in a world that is constantly \n"
		"trying to make you be something else is \n"
		"the greatest accomplishment."
	)
	q2 = Quote(
		text,
		"Ralph Waldo Emerson",
	)
	print(f"\nOriginal version:\n{q2}")
	#
	# Original version:
	_ = q2.save_state()
	# To be you in a world that is constantly
	# trying to make you be something else is
	# the greatest accomplishment.
	# - By Ralph Waldo Emerson.

	# Fix the text
	q2.text = (
		"To be yourself in a world that is constantly \n"
		"trying to make you something else is the greatest \n"
		"accomplishment."
	)
	print(f"\nThe text was fixed:\n{q2}")
	#
	# The text was fixed:
	# To be yourself in a world that is constantly
	# trying to make you something else is the greatest
	# accomplishment.
	# - By Ralph Waldo Emerson.
	q2_mem2 = q2.save_state()

	# Fix the text again
	q2.text = (
		"To be yourself when the world is constantly \n"
		"trying to make you something else is the greatest \n"
		"accomplishment."
	)
	print(f"\nThe text was fixed again:\n{q2}")
	#
	# The text was fixed again:
	# To be yourself when the world is constantly
	# trying to make you something else is the greatest
	# accomplishment.
	# - By Ralph Waldo Emerson.

	# Undo by restoring previous state
	q2.restore_state(q2_mem2)
	print(f"\nThe 2nd version, the correct one, has been restored:\n{q2}")
	#
	# The 2nd version, the correct one, has been restored:
	# To be yourself in a world that is constantly
	# trying to make you something else is the greatest
	# accomplishment.
	# - By Ralph Waldo Emerson.
