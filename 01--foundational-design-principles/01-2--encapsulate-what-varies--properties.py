"""
*Encapsulate what varies* =
Isolate the parts of your code that are most likely to change and encapsulate them.

- Advantages:
  - Ease of maintenance:      Reduce the risk of introducing bugs when only modifying the encapsulated parts
  - Enhanced flexibility:     Provide a more adaptable architecture when changing encapsulated components
  - Improved readability:     Code becomes more organized and easier to understand


- Polymorphism and properties:

  - *Polymorphism* allows instances of different classes to be treated as instances of a common superclass.
  - When using *properties*, *getters* allow reading the values of attributes and *setters* enable modifying them.
"""


class Circle:
    def __init__(self, radius: int):
        self._radius: int = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: int):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value


if __name__ == "__main__":
    circle = Circle(5)
    print(f"Initial radius: {circle.radius}")
    # Initial radius: 5

    circle.radius = 10
    print(f"Modified radius: {circle.radius}")
    # Modified radius: 10
