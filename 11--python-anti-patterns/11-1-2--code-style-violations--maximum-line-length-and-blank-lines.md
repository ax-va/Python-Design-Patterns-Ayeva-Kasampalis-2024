# Python Anti-Patterns

## Code Style Violations

### Maximum line length and blank lines

- Limit code line length to a maximum of 79 characters, as recommended in the style guide.

- Separate top-level function and class definitions from the rest of your code with two blank lines.

- Method definitions inside a class should be separated by a single blank line.

```python
# incorrect
class MyClass1:
	def method1(self):
		pass
	def method2(self):
		pass
def top_level_function1():
	pass
```

```python
# correct
class MyClass2:

	def method1(self):
		pass

	def method2(self):
		pass


def top_level_function2():
	pass
```
