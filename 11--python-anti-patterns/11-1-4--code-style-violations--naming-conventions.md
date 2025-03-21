# Python Anti-Patterns

## Code Style Violations

### Naming Conventions

```python
# not good practice
def calculateSum(a, b):
    return a + b


class my_class:
    pass


maxValue = 100
```

```python
# the best practice
def calculate_sum(a, b):
    return a + b


class MyClass:
    pass


MAX_VALUE = 100
```
