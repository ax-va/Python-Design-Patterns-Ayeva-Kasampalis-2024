"""
Factory

In the Factory design pattern, a client creates an object without knowing how (by which class) the object is created.
->
Possible benefits:
- easier tracking an object creation
- decoupling object creation from object usage
- potential to improve the memory usage and performance of application

There are two forms of factories:

- The *factory method* that is, in Python, a function that returns a different object per input parameter
but is considered in Python as over-engineered or unnecessarily complex.

- The *abstract factory* that is a group of factory methods,
where each factory method is responsible for generating a different kind of object.
"""

# Example:
# Create at least two mini-games for children and adults as part of an application.
# Decide which game to use based on the user's age.

# game 1: FrogWorld

class Frog:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact_with(self, obstacle):
		act = obstacle.action()
		msg = f"{self} the Frog encounters {obstacle} and {act}!"
		print(msg)


class Bug:
	def __str__(self):
		return "a bug"

	def action(self):
		return "eats it"


class FrogWorld:
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return "\n\n\t------ Frog World -------"

	def make_character(self):
		return Frog(self.player_name)

	def make_obstacle(self):
		return Bug()


# game 2: WizardWorld

class Wizard:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact_with(self, obstacle):
		act = obstacle.action()
		msg = f"{self} the Wizard battles against {obstacle} and {act}!"
		print(msg)


class Ork:
	def __str__(self):
		return "an evil ork"

	def action(self):
		return "defeats it"


class WizardWorld:
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return "\n\n\t------ Wizard World -------"

	def make_character(self):
		return Wizard(self.player_name)

	def make_obstacle(self):
		return Ork()


class GameEnvironment:
	def __init__(self, factory):
		self.hero = factory.make_character()
		self.obstacle = factory.make_obstacle()

	def play(self):
		self.hero.interact_with(self.obstacle)


def validate_age(name):
	age = None
	age_input = input(f"Welcome {name}. How old are you? ")
	try:
		age = int(age_input)
	except ValueError:
		print(f"Age {age} is invalid, please try again...")
		return False, age
	return True, age


def main():
	name = input("Hello. What's your name? ")
	valid_input = False
	while not valid_input:
		valid_input, age = validate_age(name)
	game = FrogWorld if age < 18 else WizardWorld
	environment = GameEnvironment(game(name))
	environment.play()


if __name__ == "__main__":
	main()








