"""
Future and Promise

In the asynchronous programming paradigm, a *Future* object is immediately returned
and acts as a placeholder for the actual result available later.
Thus, the program continues executing other tasks rather than waiting for the operation to be completed.
That property is referred to as *non-blocking*.

A *Promise* is the counterpart to a Future.
It represents the producer side of the asynchronous operation,
which will provide a result to its associated Future,
thus, fulfilling or rejecting the Promise.

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
from concurrent.futures import ThreadPoolExecutor, as_completed