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
from concurrent.futures import ThreadPoolExecutor, as_completed


def division_of_ten(x):
    return 10 / x


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(division_of_ten, i)
            for i in (1, 2, 0, 5, 10)
        ]
        # Iterate over completed Future objects and retrieve their results
        for future in as_completed(futures):
            try:
                print(f"Promise fulfilled: {future.result()}")
            
            except Exception as e:
                print(f"Promise rejected: {e}")


if __name__ == "__main__":
    main()
    # Promise fulfilled: 5.0
    # Promise rejected: division by zero
    # Promise fulfilled: 10.0
    # Promise fulfilled: 2.0
    # Promise fulfilled: 1.0
