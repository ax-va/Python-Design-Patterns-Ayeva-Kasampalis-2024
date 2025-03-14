"""
In the *Memoization* pattern, the results of expensive function calls are cached
to avoid repetitive and costly computations, significantly reducing execution time.
This pattern is used if a function is called with the same inputs more than once.
"""
from functools import lru_cache

# Example: calculate Fibonacci numbers

# without memorization
def fibonacci_func1(n):
	if n < 2:
		return n
	return fibonacci_func1(n - 1) + fibonacci_func1(n - 2)


# with memorization
@lru_cache(maxsize=None)
def fibonacci_func2(n):
	return fibonacci_func1(n)


def main():
	import time
	from datetime import timedelta

	n = 30

	# without memorization
	start_time = time.time()
	result = fibonacci_func1(n)
	stop_time = time.time()
	duration = timedelta(stop_time - start_time)
	print(f"fibonacci_func1({n}) = {result}, calculated in {duration} for the first time")

	# without memorization
	start_time = time.time()
	result = fibonacci_func1(n)
	stop_time = time.time()
	duration = timedelta(stop_time - start_time)
	print(f"fibonacci_func1({n}) = {result}, calculated in {duration} for the second time")

	# with memorization
	start_time = time.time()
	result = fibonacci_func2(n)
	stop_time = time.time()
	duration = timedelta(stop_time - start_time)
	print(f"fibonacci_func2({n}) = {result}, calculated in {duration} for the first time")

	# with memorization
	start_time = time.time()
	result = fibonacci_func2(n)
	stop_time = time.time()
	duration = timedelta(stop_time - start_time)
	print(f"fibonacci_func2({n}) = {result}, calculated in {duration} for the second time")


if __name__ == "__main__":
	main()
	# fibonacci_func1(30) = 832040, calculated in 2:19:09.561310 for the first time
	# fibonacci_func1(30) = 832040, calculated in 2:20:37.149811 for the second time
	# fibonacci_func2(30) = 832040, calculated in 2:20:34.142303 for the first time
	# fibonacci_func2(30) = 832040, calculated in 0:00:00.617981 for the second time
