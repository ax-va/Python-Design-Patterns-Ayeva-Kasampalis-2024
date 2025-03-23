"""
Look Before You Leap (LBYL) vs. Easier to Ask for Forgiveness than Permission (EAFP)

Usually, LBYL leads to more cluttered code,
while EAFP makes use of Python's handling of exceptions
and tends to be cleaner.
"""
import os

filename = "file.txt"

# LBYL
if os.path.exists(filename):
	with open(filename) as f:
		print(f.read())
else:
	print("No file there.")


# EAFP is recommended instead
try:
	with open(filename) as f:
		print(f.read())
except FileNotFoundError:
	print("No file there.")
