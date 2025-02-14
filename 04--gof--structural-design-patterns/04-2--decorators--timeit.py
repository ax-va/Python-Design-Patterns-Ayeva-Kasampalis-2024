"""
The *decorator* pattern is used to extend the behavior of an object without using inheritance.
We can add responsibilities to an object dynamically, and in a transparent manner (without affecting other objects).

Note:
The decorator pattern is a built-in feature in Python.
Python decorators can actually do much more than the decorator pattern.
A decorated function in Python cannot be undecorated, but using another decorator wrapper
you can still decide at runtime whether the decorator will be executed or not.

The decorator pattern shines when used for implementing *cross-cutting concerns*
(i.e., all parts of an application that are generic and can be applied to many other parts of it)
such as:
- data validation
- caching
- logging
- monitoring
- debugging
- business rules
- encryption

See also:
- https://docs.python.org/3/reference/compound_stmts.html#function
"""
import functools

# Example: a memoization decorator on an example of an alternative implementation of `math.fsum`

# A naive recursive implementation is very slow
def sum_up_to_v1(num):
	if num == 0:
		return 0
	else:
		return num + sum_up_to_v1(num - 1)


# Using an implementation with memorization is not simple as the naive version
sum_cache = {0: 0}


def sum_up_to_v2(num):
	if num in sum_cache:
		return sum_cache[num]
	res = num + sum_up_to_v2(num - 1)
	# Add the value to the cache
	sum_cache[num] = res
	return res


# The memorization for calculating Fibonacci numbers is not extendable in such a way
fib_cache = {0: 0, 1: 1}


def fibonacci_v2(num):
	if num in fib_cache:
		return fib_cache[num]
	res = fibonacci_v2(num - 1) + fibonacci_v2(num - 2)
	fib_cache[num] = res
	return res


# Keep a function as simple as the naive versions, but achieving # a performance
# similar to the performance of the functions that use memoization.

# decorator
def memoize(func):
	""" Accepts the func function, which needs to be memoized, as an input. """
	cache = {}

	# Make sure that the documentation and the signature
	# of the function that is decorated are preserved.
	@functools.wraps(func)
	def memoizer(*args):
		if args not in cache:
			value = func(*args)
			cache[args] = value
			return value
		return cache[args]

	return memoizer


@memoize
def sum_up_to_v3(num):
	if num == 0:
		return 0
	else:
		return num + sum_up_to_v3(num - 1)


@memoize
def fibonacci_v3(num):
	if num in (0, 1):
		return num
	else:
		return fibonacci_v3(num - 1) + fibonacci_v3(num - 2)


if __name__ == "__main__":
	from timeit import Timer

	# naive and recursive
	t = Timer(
		"sum_up_to_v1(300)",
		"from __main__ import sum_up_to_v1"
	)
	print("Time: ", t.timeit())
	# Time:  23.237666491011623

	# with memorization
	t = Timer(
		"sum_up_to_v2(300)",
		"from __main__ import sum_up_to_v2"
	)
	print("Time: ", t.timeit())
	# Time:  0.0587521240231581

	# with the memorization decorator
	to_execute = [
		(
			sum_up_to_v3,
			Timer(
				"sum_up_to_v3(300)",
				"from __main__ import sum_up_to_v3",
			),
		),
		(
			fibonacci_v3,
			Timer(
				"fibonacci_v3(100)",
				"from __main__ import fibonacci_v3",
			),
		),
	]

	for item in to_execute:
		func = item[0]
		print(f'Function "{func.__name__}": {func.__doc__}')
		t = item[1]
		print(f"Time: {t.timeit()}\n")
	# Function "sum_up_to_v3": None
	# Time: 0.1116248159960378
	#
	# Function "fibonacci_v3": None
	# Time: 0.11177351299556904
