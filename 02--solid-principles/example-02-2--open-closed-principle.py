"""
Open-closed principle (OCP) =
Software entities, such as classes and modules, should be open
for extension (through inheritance or interfaces to accommodate
new requirements and behaviors) but closed for modification.
"""


# - Anti-example with no OCP
class Rectangle:
    """
    Anti-example:
    Adding more shapes leads to modifying the calculate_area function.
    """
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height


def calculate_area(shape) -> float:
    if isinstance(shape, Rectangle):
        return shape.width * shape.height


# - Example with OCP
import math
from typing import Protocol


class Shape(Protocol):
    def area(self) -> float:
        ...


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height


class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


def calculate_area(shape: Shape) -> float:
    """ Adding a new shape does not lead to modifying the function. """
    return shape.area()


if __name__ == "__main__":
    rect = Rectangle(12, 8)
    rect_area = calculate_area(rect)
    print(f"Rectangle area: {rect_area}")
    # Rectangle area: 96

    circ = Circle(6.5)
    circ_area = calculate_area(circ)
    print(f"Circle area: {circ_area:.2f}")
    # Circle area: 132.73
