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
