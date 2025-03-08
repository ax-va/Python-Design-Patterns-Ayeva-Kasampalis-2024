"""
Object Pool

The *Object Pool* pattern is used to reuse existing objects instead of creating new ones when they are needed.
This is useful when resource initialization is costly or time-consuming.
"""
# Example: a car rental application


class Car:
	def __init__(self, make: str, model: str):
		self.make = make
		self.model = model
		self.in_use = False


class CarPool:
	def __init__(self):
		self._available = []
		self._in_use = []

	def acquire_car(self) -> Car:
		if len(self._available) == 0:
			new_car = Car("BMW", "M3")
			self._available.append(new_car)
		car = self._available.pop()
		self._in_use.append(car)
		car.in_use = True
		return car

	def release_car(self, car: Car) -> None:
		car.in_use = False
		self._in_use.remove(car)
		self._available.append(car)


if __name__ == "__main__":
	pool = CarPool()
	car_name = "Car 1"

	print(f"Acquire {car_name}")
	# Acquire Car 1
	car1 = pool.acquire_car()
	print(f"{car_name} in use: {car1.in_use}")
	# Car 1 in use: True

	print(f"Now release {car_name}")
	# Now release Car 1
	pool.release_car(car1)
	print(f"{car_name} in use: {car1.in_use}")
	# Car 1 in use: False
