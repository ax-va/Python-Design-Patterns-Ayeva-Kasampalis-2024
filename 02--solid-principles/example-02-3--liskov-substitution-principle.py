"""
Liskov substitution principle (LSP) =
If a program uses objects of a superclass, then the substitution of them
with objects of a subclass should not change the correctness and expected behavior of the program.
"""


# - Anti-example non-holding LSP
class Bird:
    def fly(self):
        print("I can fly")


class Penguin(Bird):
    def fly(self):
        raise Exception("I cannot fly")


def make_bird_fly(bird):
    # different behavior for instances of Bird and Penguin
    bird.fly()


# - Example holding LSP
class Bird:
    def move(self):
        print("I'm moving")


class FlyingBird(Bird):
    def move(self):
        print("I'm flying")


class FlightlessBird(Bird):
    def move(self):
        print("I'm walking")


def make_bird_move(bird):
    bird.move()


if __name__ == "__main__":
    some_bird = Bird()
    eagle = FlyingBird()
    penguin = FlightlessBird()

    make_bird_move(some_bird)
    # I'm moving
    make_bird_move(eagle)
    # I'm flying
    make_bird_move(penguin)
    # I'm walking
