"""
Worker Model

In the *Worker Model* pattern, a large task or many tasks are divided into
smaller, manageable units of work, called *workers*, that can be processed in parallel.
The workers could be threads within a single application, separate processes on the same machine,
or even different machines in a distributed system.

Three components are involved in this pattern:

- The *workers* that can perform a piece of the task independently of each other;
- The *task queue* where tasks are stored awaiting processing;
- The *dispatcher* / *master* / *boss thread* that assigns tasks to workers based on availability, load, or priority.

Thread Pool vs. Worker Model

- The Thread Pool pattern emphasizes efficient thread management and reuse,
while the Worker Model pattern centers on the delegation relationship between a master thread and worker threads.

- In the Thread Pool pattern, tasks are typically placed into a queue and picked up by any available thread.
In contrast, the Worker Model pattern involves a boss explicitly assigning tasks to specific worker threads.

- The Thread Pool pattern is ideal for scenarios with numerous short-lived tasks requiring efficient thread management.
The Worker Model pattern suits situations where tasks are dynamic, require specific handling, or involve complex coordination.
"""
import time
from multiprocessing import Process, Queue


def worker(task_queue):
	while not task_queue.empty():
		task = task_queue.get()
		print(f"Worker {task} is processing...")
		time.sleep(1)
		print(f"Worker {task} completed.")


def main():
	task_queue = Queue()
	# Create 10 tasks and add them to the queue
	for i in range(10):
		task_queue.put(i)

	# Create 5 worker processes
	processes = [Process(target=worker, args=(task_queue,)) for _ in range(5)]

	# Start the worker processes to execute tasks concurrently
	for process in processes:
		process.start()

	# Wait for all worker processes to finish
	for process in processes:
		process.join()

	print("All tasks completed.")


if __name__ == "__main__":
	main()
	# Worker 0 is processing...
	# Worker 1 is processing...
	# Worker 2 is processing...
	# Worker 3 is processing...
	# Worker 4 is processing...
	# Worker 0 completed.
	# Worker 5 is processing...
	# Worker 1 completed.
	# Worker 6 is processing...
	# Worker 2 completed.
	# Worker 3 completed.
	# Worker 7 is processing...
	# Worker 8 is processing...
	# Worker 4 completed.
	# Worker 9 is processing...
	# Worker 5 completed.
	# Worker 6 completed.
	# Worker 7 completed.
	# Worker 8 completed.
	# Worker 9 completed.
	# All tasks completed.
