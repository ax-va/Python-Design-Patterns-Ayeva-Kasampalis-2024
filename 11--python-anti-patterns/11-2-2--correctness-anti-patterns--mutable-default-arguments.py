"""
Use a default value of `None` and set it to
a mutable data structure within the function if needed.
"""


# This bad practice leads to unexpected behavior:
# `mylist` will be not reset to an empty list after the first call
# with the default parameter, keeping its previous value.
def manipulate_v1(mylist=[]):
	mylist.append("test")
	return mylist


# better
def manipulate_v2(mylist=None):
	if mylist is None:
		mylist = []

	mylist.append("test")
	return mylist


if __name__ == "__main__":
	print(manipulate_v1())
	# ['test']
	print(manipulate_v1())
	# ['test', 'test']
	print(manipulate_v1())
	# ['test', 'test', 'test']

	print(manipulate_v2())
	# ['test']
	print(manipulate_v2())
	# ['test']
