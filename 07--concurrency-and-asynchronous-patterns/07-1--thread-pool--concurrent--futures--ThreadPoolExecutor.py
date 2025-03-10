"""
Thread Pool

In the *Thread Pool* pattern, when one *worker thread* finishes a task,
it does not terminate but goes back to the pool,
awaiting another task that it can be used again for.

While the Thread Pool pattern focuses on reusing a fixed number of threads to execute tasks,
the Worker Model pattern is more about the dynamic distribution of tasks across potentially scalable
and flexible worker entities.
"""
import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
	""" This function simulates a task. """
	print(f"Executing task {i} ...")
	time.sleep(1)
	print(f"Task {i} completed.")


with ThreadPoolExecutor(max_workers=5) as executor:
	# Submit 10 tasks to the thread pool
	for j in range(10):
		executor.submit(task, j)
	# The tasks are executed concurrently
	# using the threads available in the thread pool.
	# Once a worker thread completes a task,
	# it picks up another from the queue.

# Executing task 0 ...
# Executing task 1 ...
# Executing task 2 ...
# Executing task 3 ...
# Executing task 4 ...
# Task 0 completed.Task 2 completed.
# Executing task 5 ...
# Task 3 completed.
# Executing task 6 ...
# Task 1 completed.
# Executing task 7 ...
# Task 4 completed.
# Executing task 8 ...
#
# Executing task 9 ...
# Task 5 completed.
# Task 6 completed.
# Task 7 completed.
# Task 8 completed.
# Task 9 completed.
