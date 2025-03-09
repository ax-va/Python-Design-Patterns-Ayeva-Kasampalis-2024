"""
Future and Promise

In the asynchronous programming paradigm, a *Future* object is immediately returned
and acts as a placeholder for the actual result available later.
Thus, the program continues executing other tasks rather than waiting for the operation to be completed.
That property is referred to as *non-blocking*.

A *Promise* is the counterpart to a Future.
It represents the producer side of the asynchronous operation,
which will provide a result to its associated Future.
Eventually, the Promise will be fulfilled or rejected.

Three steps of its mechanism:

- The *initiation* step involves starting an asynchronous operation using a function where,
instead of waiting for the operation to complete, the function immediately returns a Future object.
Internally, the asynchronous function creates a Promise object.

- During the *execution* step, the operation proceeds independently of the main program flow.
This allows the program to remain responsive and continue with other tasks.

- The nex one is the *resolution* step. If the operation is successful, the Promise is fulfilled with the result.
If the operation fails, the Promise is rejected with an error.
The fulfillment or rejection of the Promise resolves the Future.
"""
import asyncio


# Define coroutine
async def division_of_ten(x):
	# Simulate some IO-bound operation
	await asyncio.sleep(1)  # also a coroutine
	return 10 / x


async def main():
	futures = [
		asyncio.ensure_future(division_of_ten(i))
		for i in (1, 2, 0, 5, 10)
	]
	# Use coroutine to wait for the Futures to complete and gather the results
	results = await asyncio.gather(*futures, return_exceptions=True)
	for result in results:
		if isinstance(result, Exception):
			print(f"Promise rejected: {result}")
		else:
			print(f"Promise fulfilled: {result}")


if __name__ == "__main__":
	# Run `asyncio`'s event loop
	asyncio.run(main())
	# Promise fulfilled: 10.0
	# Promise fulfilled: 5.0
	# Promise rejected: division by zero
	# Promise fulfilled: 2.0
	# Promise fulfilled: 1.0
