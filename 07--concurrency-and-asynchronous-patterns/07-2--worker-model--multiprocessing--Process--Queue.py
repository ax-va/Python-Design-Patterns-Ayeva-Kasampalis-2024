"""
Worker Model

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
