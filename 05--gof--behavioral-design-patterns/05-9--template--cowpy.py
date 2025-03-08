"""
Template

The *Template* pattern focuses on eliminating code repetition
by redefining certain parts of an algorithm without changing its structure.
*Invariant* (common) parts of algorithms are kept in a template method/function, and
*variant* (different) parts are moved in action/hook methods/functions.

Example: Implement a banner generator so that we send some text to a function, and
the function generates a banner containing the text.

See also:
- cowpy
https://github.com/jeffbuttars/cowpy
https://pypi.org/project/cowpy/
https://snyk.io/advisor/python/cowpy

```unix
$ python -m pip install cowpy
```
"""
from cowpy import cow


# template function
def generate_banner(msg, style):
	print("-- start of banner --")
	print(style(msg))
	print("-- end of banner --\n")


# style function 1
def dots_style(msg):
	msg = msg.capitalize()
	ten_dots = "." * 10
	msg = f"{ten_dots}{msg}{ten_dots}"
	return msg


# style function 2
def admire_style(msg):
	msg = msg.upper()
	# Put an exclamation mark between each character of the text
	msg = "!".join(msg)
	return msg

# style function 3
def cow_style(msg):
	msg = cow.milk_random_cow(msg)
	return msg


def main():
	styles = (dots_style, admire_style, cow_style)
	msg = "happy coding"
	[generate_banner(msg, style) for style in styles]


if __name__ == "__main__":
	main()
"""
-- start of banner --
..........Happy coding..........
-- end of banner --

-- start of banner --
H!A!P!P!Y! !C!O!D!I!N!G
-- end of banner --

-- start of banner --
 ______________ 
< happy coding >
 -------------- 
     o
      o
        ,__, |    | 
        (oo)\|    |___
        (__)\|    |   )\_
             |    |_w |  \
             |    |  ||   *

             Cower....
-- end of banner --
"""