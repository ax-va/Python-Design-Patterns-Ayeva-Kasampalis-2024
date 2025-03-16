"""
Lazy Loading

The *Lazy Loading* pattern is used to defer the initialization or loading of resources
until they are actually needed.
"""
import time
from datetime import timedelta
from functools import lru_cache

# Example: calculating factorial (the `math` module has a better implementation)

def recursive_factorial(n):
	""" Calculate factorial (expensive for large n). """
	if n == 1:
		return 1
	else:
		return n * recursive_factorial(n - 1)


@lru_cache(maxsize=128)
def cached_factorial(n):
	return recursive_factorial(n)


def main():
	n = 100

	# without caching
	start_time = time.time()
	result = recursive_factorial(n)
	stop_time = time.time()
	duration = stop_time - start_time
	print(f"recursive_factorial({n}) = {result}, calculated in {duration}")

	# with caching

	start_time = time.time()
	result = cached_factorial(n)
	stop_time = time.time()
	duration = stop_time - start_time
	print(f"cached_factorial({n}) = {result}, calculated in {duration} for the first time")

	start_time = time.time()
	result = cached_factorial(n)
	stop_time = time.time()
	duration = stop_time - start_time
	print(f"cached_factorial({n}) = {result}, calculated in {duration} for the second time")


if __name__ == "__main__":
	main()
	# recursive_factorial(100) = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, calculated in 1.33514404296875e-05
	# cached_factorial(100) = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, calculated in 1.0013580322265625e-05 for the first time
	# cached_factorial(100) = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, calculated in 1.6689300537109375e-06 for the second time
