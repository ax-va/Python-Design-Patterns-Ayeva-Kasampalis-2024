"""
The *Command* pattern is used to encapsulate an operation
(e.g. undo, redo, copy, paste, capitalize text, and so forth) as an object.

Example:
The *Command* pattern to implement the following basic file utilities:
- creating a file and, optionally, adding text to it,
- reading the contents of a file,
- renaming a file.
"""
import logging
import os

# Configure logging to show INFO messages
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class CreateFile:
	def __init__(self, filepath, content=""):
		"""
		Args:
			filepath: path of file to create
			content: text content to write to file
		"""
		self.filepath = filepath
		self.content = content

	def execute(self):
		logging.info(f"[creating file '{self.filepath}']")
		with open(self.filepath, "w", encoding="utf-8") as f:
			f.write(self.content)

	def undo(self):
		logging.info(f"[deleting file '{self.filepath}']")
		os.remove(self.filepath)


class ReadFile:
	def __init__(self, filepath):
		"""
		Args:
			filepath: path of file to read
		"""
		self.filepath = filepath

	def execute(self):
		logging.info(f"[reading file '{self.filepath}']")
		with open(self.filepath, "r", encoding="utf-8") as f:
			print(f.read(), end="")


class RenameFile:
	def __init__(self, src, dest):
		"""
		Args:
			src: source
			dest: destination file path
		"""
		self.src = src
		self.dest = dest

	def execute(self):
		logging.info(f"[renaming '{self.src}' to '{self.dest}']")
		os.rename(self.src, self.dest)

	def undo(self):
		logging.info(f"[renaming '{self.dest}' back to '{self.src}']")
		os.rename(self.dest, self.src)


if __name__ == "__main__":
	fname, new_fname = "file1", "file2"

	commands = [
		CreateFile(fname, "hello world\n"),
		ReadFile(fname),
		RenameFile(fname, new_fname),
		ReadFile(new_fname),
	]

	for command in commands:
		command.execute()

	answer = input("Reverse the executed commands? [y/n] ")
	if answer not in "yY":
		print(f"The result is {new_fname}")
		exit()

	for reversed_command in reversed(commands):
		# Not all commands support `undo`
		try:
			reversed_command.undo()
		except AttributeError as e:
			logging.error(f"[{e}]")

# INFO: [creating file 'file1']
# INFO: [reading file 'file1']
# INFO: [renaming 'file1' to 'file2']
# INFO: [reading file 'file2']

# hello world
# hello world
# Reverse the executed commands? [y/n]
# y

# ERROR: ['ReadFile' object has no attribute 'undo']
# INFO: [renaming 'file2' back to 'file1']
# ERROR: ['ReadFile' object has no attribute 'undo']
# INFO: [deleting file `file1`]
