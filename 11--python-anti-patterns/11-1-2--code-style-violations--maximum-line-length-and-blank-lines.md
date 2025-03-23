# Python Anti-Patterns

## Code Style Violations

### Maximum line length and blank lines

- Limit code line length to a maximum of 79 characters, as recommended in the style guide.

- How to surround top-level function and class definitions and method definitions inside a class:

    ```python
    # not compliant with the style guide
    class MyClass:
        def method1(self):
            pass
        def method2(self):
            pass
    def top_level_function():
        pass
    ```
    
    ```python
    # How many blank lines are compliant with the style guide
    class MyClass:
        # 1
        def method1(self):
            pass
        # 1
        def method2(self):
            pass
    # 1
    # 2
    def top_level_function():
        pass
    ```
