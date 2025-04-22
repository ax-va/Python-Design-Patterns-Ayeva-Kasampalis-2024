"""
Avoid global variables for sharing data.
Otherwise, you get bugs if different parts of the application
unexpectedly modify global state.
"""

# not recommended
counter = 0  # global variable


def increment():
    global counter
    counter += 1


def reset():
    global counter
    counter = 0

"""
Explanation:
In Python, the need to declare a variable as `global` within a function arises 
when you intend to modify a variable defined in the global scope. 
This is because, by default, assigning a value to a variable inside a function creates 
a new local variable within that function's scope. 
To modify the global variable, you must explicitly declare it as `global` within the function.
"""

# better
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


if __name__ == "__main__":


    def foo():
        for _ in range(5):
            print(f"Counter value: {counter.value}")
            # some operations
            counter.increment()


    counter = Counter()
    foo()
    # Counter value: 0
    # Counter value: 1
    # Counter value: 2
    # Counter value: 3
    # Counter value: 4
    counter.reset()
    print(f"Counter value: {counter.value}")
    # Counter value: 0

"""
Explanation:
In contrast, when working with class instances, 
you can access and modify their attributes without using the `global` keyword, 
provided the instance itself is accessible within the function's scope. 
This is because you're not reassigning the variable that holds the instance. 
Instead, you're modifying the attributes of the object it references.
"""
