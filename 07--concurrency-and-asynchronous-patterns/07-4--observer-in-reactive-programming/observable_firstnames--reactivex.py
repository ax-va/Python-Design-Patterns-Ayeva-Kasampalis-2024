import reactivex as rx
from pathlib import Path
from reactivex import operators as ops

# Example:
# Build a stream of a list of (fake) people's names text file, and an observable based on it.

# Define an Observable from the text file as the stream of data
def firstnames(path: Path):
	file = path.open()
	# Collect and push stored people firstnames
	return rx.from_iterable(file).pipe(
		ops.flat_map(
			lambda content: rx.from_iterable(
				content.split("\n")
			)
		),
		ops.filter(lambda name: name != ""),
		ops.map(lambda name: name.split()[0]),
		ops.group_by(lambda firstname: firstname),
		ops.flat_map(
			lambda group: group.pipe(
				ops.count(),
				ops.map(lambda count: (group.key, count)),
			)
		),
	)


# Define an Observable that emits data every 5 seconds
def main():
	# source of the data
	filepath = Path(__file__).parent / Path("fake_people.txt")
	# Emit data every 5 seconds and merge results to the output
	rx.interval(5.0).pipe(
		ops.flat_map(lambda i: firstnames(filepath))
	).subscribe(lambda value: print(str(value)))

	# Keep alive until user presses any key
	input("Starting... Press any key and ENTER, to quit\n")


if __name__ == "__main__":
	main()