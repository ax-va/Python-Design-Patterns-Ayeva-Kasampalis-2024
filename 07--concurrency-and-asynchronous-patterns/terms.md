## Concurrency and Asynchronous Patterns

### Thread Pool

*Worker threads* are used to offload processing tasks from the main thread.
In the *Thread Pool* pattern, when one worker thread finishes a task, 
it does not terminate but goes back to the pool, 
awaiting another task that it can be used again for.

### Worker Model

In the *Worker Model* pattern, a large task or many tasks are divided into 
smaller, manageable units of work, called *workers*, that can be processed in parallel.
The workers could be threads within a single application, separate processes on the same machine, 
or even different machines in a distributed system.

Three components are involved in this pattern:

- the *workers* that can perform a piece of the task independently of each other;
- the *task queue* where tasks are stored awaiting processing;
- the *dispatcher* that assigns tasks to workers based on availability, load, or priority.

### Future and Promise

### Observer (in Reactive Programming)