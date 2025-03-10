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

While the Thread Pool pattern focuses on reusing a fixed number of threads to execute tasks, 
the Worker Model pattern is more about the dynamic distribution of tasks across potentially scalable 
and flexible worker entities.

Three components are involved in this pattern:

- The *workers* that can perform a piece of the task independently of each other;
- The *task queue* where tasks are stored awaiting processing;
- The *dispatcher* / *master* / *boss thread* that assigns tasks to workers based on availability, load, or priority.

### Future and Promise

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

### Observer in Reactive Programming

To put it simply, the concept of *reactive programming* is 
to react to many events (streams of events) while keeping the code clean,
This concept, added to the traditional Observer pattern, 
creates the *Observer* pattern *in reactive programming*.

## Other Patterns

### Actor Model

The *Actor Model* defines some rules for how actor instances should behave. 
An actor can make local decisions, create more actors, send more messages, 
and determine how to respond to the next message received.

### Coroutines

*Coroutines* are general control structures 
where flow control is cooperatively passed between two different routines without returning.

### Message Passing

Software entities communicate and coordinate their actions by passing messages to each other.

### Backpressure

*Backpressure* is a mechanism to manage the flow of data through software systems and prevent overwhelming components. 
It allows systems to gracefully handle overload by signaling the producer to slow down until the consumer can catch up.
