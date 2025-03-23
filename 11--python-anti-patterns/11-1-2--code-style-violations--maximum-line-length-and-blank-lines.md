# Python Anti-Patterns

## Code Style Violations

### Maximum line length and blank lines

- Limit code line length to a maximum of 79 characters, as recommended in the style guide.

- Surround top-level function and class definitions with two blank lines.

- Surround method definitions inside a class should with a single blank line.

```python
# not compliant with the style guide
class MyClass1:
	def method1(self):
		pass
	def method2(self):
		pass
def top_level_function1():
	pass
```

```python
# compliant with the style guide
class MyClass2:

	def method1(self):
		pass

	def method2(self):
		pass


def top_level_function2():
	pass
```
