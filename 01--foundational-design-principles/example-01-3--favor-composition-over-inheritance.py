"""
Favor Composition Over Inheritance (composition = "has-a" relationship)
= Prefer composing objects from simpler parts to inheriting functionalities from a base class.

Advantages:
- Flexibility:          Make code more adaptable changing objects' behavior at runtime
- Reusability:          Promote code reusability by reusing smaller, simpler objects across application's parts
- Ease of maintenance:  Don't affect the overall system when changing components, avoid border effects
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
