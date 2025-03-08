## Concurrency and Asynchronous Patterns

### Thread Pool

In the *Thread Pool* pattern, when one *worker thread* finishes a task, 
it does not terminate but goes back to the pool, 
awaiting another task that it can be used again for.

### Worker Model

In the *Worker Model* pattern, a large task or many tasks are divided into 
smaller, manageable units of work, called *workers*, that can be processed in parallel.
The workers could be threads within a single application, separate processes on the same machine, 
or even different machines in a distributed system.

Three components are involved in this pattern:

- The *workers* that can perform a piece of the task independently of each other;
- The *task queue* where tasks are stored awaiting processing;
- The *dispatcher* / *master* / *boss thread* that assigns tasks to workers based on availability, load, or priority.

### Thread Pool vs. Worker Model

- The Thread Pool pattern emphasizes efficient thread management and reuse, 
while the Worker Model pattern centers on the delegation relationship between a master thread and worker threads.

- In the Thread Pool pattern, tasks are typically placed into a queue and picked up by any available thread. 
In contrast, the Worker Model pattern involves a boss explicitly assigning tasks to specific worker threads.

- The Thread Pool pattern is ideal for scenarios with numerous short-lived tasks requiring efficient thread management. 
The Worker Model pattern suits situations where tasks are dynamic, require specific handling, or involve complex coordination.

### Future and Promise

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

### Observer (in Reactive Programming)