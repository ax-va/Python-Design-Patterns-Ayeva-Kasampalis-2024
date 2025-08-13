"""
Future and Promise

The *Future and Promise* pattern allows applications to remain responsive and efficient
by not blocking the main thread with long-running tasks.

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

- The next one is the *resolution* step. If the operation is successful, the Promise is fulfilled with the result.
If the operation fails, the Promise is rejected with an error.
The fulfillment or rejection of the Promise resolves the Future.
"""
import asyncio


# Define coroutine
async def division_of_ten(x):
    # Simulate some IO-bound operation
    await asyncio.sleep(1)  # also a coroutine
    return 10 / x


async def main_v1():
    inputs = (1, 2, 0, 5, 10)
    coroutines = [division_of_ten(x) for x in inputs]
    # Keep the input order and don't throw, but return exceptions
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    for x, result in zip(inputs, results):
        if isinstance(result, Exception):
            print(f"Promise rejected: {x} -> {result}")

        else:
            print(f"Promise fulfilled: {x} -> {result}")


async def worker(x):
    try:
        # Results appear as soon as each task finishes
        result = await division_of_ten(x)
        print(f"Promise fulfilled: {x} -> {result}")

    except Exception as e:
        print(f"Promise rejected: {x} -> {e}")


async def main_v2():
    inputs = (1, 2, 0, 5, 10)
    async with asyncio.TaskGroup() as tg:
        for x in inputs:
            tg.create_task(worker(x))


if __name__ == "__main__":
    # Run event loop
    asyncio.run(main_v1())
    # Promise fulfilled: 1 -> 10.0
    # Promise fulfilled: 2 -> 5.0
    # Promise rejected: 0 -> division by zero
    # Promise fulfilled: 5 -> 2.0
    # Promise fulfilled: 10 -> 1.0
    asyncio.run(main_v2())
    # Promise fulfilled: 1 -> 10.0
    # Promise fulfilled: 2 -> 5.0
    # Promise rejected: 0 -> division by zero
    # Promise fulfilled: 5 -> 2.0
    # Promise fulfilled: 10 -> 1.0
