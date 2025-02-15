"""
The *Builder* pattern separates the construction of a complex object from its representation,
so that the same construction can be used to create several different representations.

A Factory pattern creates an object in a single step, whereas a Builder
pattern creates an object in multiple steps and almost always uses a *director*.
"""
import time
from enum import Enum

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")
# Delay in seconds
STEP_DELAY = 3


class Pizza:
	def __init__(self, name):
		self.name = name
		self.dough = None
		self.sauce = None
		self.topping = []

	def __str__(self):
		return self.name

	def prepare_dough(self, dough):
		self.dough = dough
		print(f"preparing the {self.dough.name} dough of your {self}...")
		time.sleep(STEP_DELAY)
		print(f"done with the {self.dough.name} dough")


# two builders

class MargaritaBuilder:
	def __init__(self):
		self.pizza = Pizza("margarita")
		self.progress = PizzaProgress.queued
		self.baking_time = 5

	def prepare_dough(self):
		self.progress = PizzaProgress.preparation
		self.pizza.prepare_dough(PizzaDough.thin)

	def add_sauce(self):
		...

	def add_topping(self):
		...

	def bake(self):
		...


class CreamyBaconBuilder:
	def __init__(self):
		self.pizza = Pizza("creamy bacon")
		self.progress = PizzaProgress.queued
		self.baking_time = 7

	def prepare_dough(self):
		self.progress = PizzaProgress.preparation
		self.pizza.prepare_dough(PizzaDough.thick)

	def add_sauce(self):
		...

	def add_topping(self):
		...

	def bake(self):
		...


# The *director* in this example is the waiter.
class Waiter:
	def __init__(self):
		builder = None

	@property
	def steps(self):
		return [
			self.builder.prepare_dough,
			self.builder.add_sauce,
			self.builder.add_topping,
			self.builder.bake,
		]

	@property
	def pizza(self):
		return self.builder.pizza

	def construct_pizza(self, builder):
		self.builder = builder
		[step() for step in self.steps]


def validate_order(builders):
	input_msg = "What pizza would you like, [m]argarita or [c]reamy bacon? "
	try:
		pizza_style = input(input_msg)
		builder = builders[pizza_style]()
	except KeyError:
		error_msg = "Sorry, only margarita (key m) and creamy bacon (key c) are available."
		print(error_msg)
		return False, None
	return True, builder


def main():
	builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
	valid_input = False
	while not valid_input:
		valid_input, builder = validate_order(builders)
	print("-" * 40)
	waiter = Waiter()
	waiter.construct_pizza(builder)
	pizza = waiter.pizza
	print("-" * 40)
	print(f"Enjoy your {pizza}!")


if __name__ == "__main__":
	main()