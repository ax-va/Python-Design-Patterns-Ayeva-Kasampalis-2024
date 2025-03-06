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

- the *workers* that can perform a piece of the task independently of each other;
- the *task queue* where tasks are stored awaiting processing;
- the *dispatcher* / *master* / *boss thread* that assigns tasks to workers based on availability, load, or priority.

### Thread Pool vs. Worker Model

- The Thread Pool pattern emphasizes efficient thread management and reuse, 
while the Worker Model pattern centers on the delegation relationship between a master thread and worker threads.

- In the Thread Pool pattern, tasks are typically placed into a queue and picked up by any available thread. 
In contrast, the Worker Model pattern involves a boss explicitly assigning tasks to specific worker threads.

- The Thread Pool pattern is ideal for scenarios with numerous short-lived tasks requiring efficient thread management. 
The Worker Model pattern suits situations where tasks are dynamic, require specific handling, or involve complex coordination.

### Future and Promise

### Observer (in Reactive Programming)