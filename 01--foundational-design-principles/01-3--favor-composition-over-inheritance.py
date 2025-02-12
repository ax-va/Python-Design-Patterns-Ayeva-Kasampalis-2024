"""
*Favor Composition Over Inheritance* =
Prefer composing objects from simpler parts to inheriting functionalities from a base class.
The *composition* means a "has-a" relationship.
"""

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


if __name__ == "__main__":
    car = Car()
    car.start()
    # Engine started
    # Car started
