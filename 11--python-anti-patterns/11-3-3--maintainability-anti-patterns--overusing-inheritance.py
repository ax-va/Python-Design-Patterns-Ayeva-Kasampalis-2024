"""
Don't create a deep inheritance hierarchy.
Create smaller, more focused classes
and combine them to achieve the desired behavior.
"""


# not recommended
class GrandParent:
	pass

class Parent(GrandParent):
	pass

class Child(Parent):
	pass


# Favor composition over inheritance
class Member:
	def __init__(self, parent=None):
		self.parent = parent
