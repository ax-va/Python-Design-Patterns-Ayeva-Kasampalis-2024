"""
Flyweight

The *Flyweight* pattern is used when an application needs to create
a large number of computationally expensive objects that share many properties.
Thus, we minimize memory usage and improve performance by introducing data sharing between similar objects.

A flyweight is a shared object that contains state-independent, immutable (also known as *intrinsic*) data.
The state-dependent, mutable (also known as *extrinsic*) data should not be part of
flyweight because this is information that cannot be shared, since it differs per object.

Requirements for effectively using the flyweight pattern:

- The application needs to use a large number of objects.

- There are so many objects that it's too expensive to store/render them.
Once the mutable state is removed, many groups of distinct objects can be replaced by relatively few shared objects.

- Object identity is not important for the application.
"""
import random
from enum import Enum

# Example with a car park: no matter how large the car park is, the memory allocation stays the same.

CarType = Enum("CarType", "SUBCOMPACT COMPACT SUV")


class Car:
	pool = dict()

	# `__new__` is called before `__init__()` to convert
	# the `Car` class to a metaclass that supports self-references.
	# `cls` references the `Car` class.
	def __new__(cls, car_type):
		# The type of the car is used to check whether
		# a car of the same type has already been created.
		obj = cls.pool.get(car_type)
		if not obj:
			obj = object.__new__(cls)
			cls.pool[car_type] = obj
			obj.car_type = car_type
		return obj

	def render(self, color, x, y):
		""" Renders a car on the screen. """
		type = self.car_type
		msg = f"Render a {color} {type.name} car at ({x}, {y})"
		print(msg)


def main():
	rnd = random.Random()
	colors = [
		"white",
		"black",
		"silver",
		"gray",
		"red",
		"blue",
		"brown",
		"beige",
		"yellow",
		"green",
	]
	min_point, max_point = 0, 100
	car_counter = 0

	# Although 18 cars are rendered, memory is allocated only for 3
	for _ in range(10):
		c1 = Car(CarType.SUBCOMPACT)
		c1.render(
			random.choice(colors),
			rnd.randint(min_point, max_point),
			rnd.randint(min_point, max_point),
		)
		car_counter += 1

	for _ in range(3):
		c2 = Car(CarType.COMPACT)
		c2.render(
			random.choice(colors),
			rnd.randint(min_point, max_point),
			rnd.randint(min_point, max_point),
		)
		car_counter += 1

	for _ in range(5):
		c3 = Car(CarType.SUV)
		c3.render(
			random.choice(colors),
			rnd.randint(min_point, max_point),
			rnd.randint(min_point, max_point),
		)
		car_counter += 1

	print(f"Cars rendered: {car_counter}")
	print(f"Cars actually allocated in memory: {len(Car.pool)}")

	c4 = Car(CarType.SUBCOMPACT)
	c5 = Car(CarType.SUBCOMPACT)
	c6 = Car(CarType.SUV)

	print(f"{id(c4)} == {id(c5)}? {id(c4) == id(c5)}")
	print(f"{id(c5)} == {id(c6)}? {id(c5) == id(c6)}")


if __name__ == "__main__":
	main()
	# Render a beige SUBCOMPACT car at (28, 59)
	# Render a black SUBCOMPACT car at (59, 16)
	# Render a blue SUBCOMPACT car at (30, 79)
	# Render a black SUBCOMPACT car at (30, 14)
	# Render a yellow SUBCOMPACT car at (58, 49)
	# Render a green SUBCOMPACT car at (6, 99)
	# Render a brown SUBCOMPACT car at (45, 97)
	# Render a blue SUBCOMPACT car at (6, 48)
	# Render a white SUBCOMPACT car at (70, 87)
	# Render a white SUBCOMPACT car at (69, 58)
	# Render a green COMPACT car at (42, 11)
	# Render a white COMPACT car at (100, 61)
	# Render a yellow COMPACT car at (69, 49)
	# Render a green SUV car at (16, 82)
	# Render a blue SUV car at (17, 35)
	# Render a beige SUV car at (91, 15)
	# Render a red SUV car at (7, 49)
	# Render a gray SUV car at (64, 68)
	# Cars rendered: 18
	# Cars actually allocated in memory: 3
	# 134894084245600 == 134894084245600? True
	# 134894084245600 == 134894084321408? False
