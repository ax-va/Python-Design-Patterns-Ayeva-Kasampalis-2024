"""
Concatenating strings using `+` or `+=` in a loop creates
a new string object each time, which is inefficient for large loop repetitions.
Use `join` instead that is more efficient
when concatenating strings from a sequence or iterable.
"""
import time
from datetime import timedelta

my_list = list(str(i) for i in range(1000))

start_time = time.time()
# ----------------------------------------
# not recommended
result = ""
for item in my_list:
    result += f", {item}"
# ----------------------------------------
stop_time = time.time()
duration = timedelta(stop_time - start_time)
print(f"Duration: {duration}")
# Duration: 0:00:17.509460

start_time = time.time()
# ----------------------------------------
# much better
result = ", ".join(my_list)
# ----------------------------------------
stop_time = time.time()
duration = timedelta(stop_time - start_time)
print(f"Duration: {duration}")
# Duration: 0:00:00.926971
