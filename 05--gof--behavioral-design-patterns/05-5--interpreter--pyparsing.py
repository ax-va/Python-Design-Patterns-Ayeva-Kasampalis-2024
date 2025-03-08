"""
Interpreter

A *(domain-specific language) DSL* is a computer language of limited expressiveness targeting a particular domain,
such as combat simulation, billing, visualization, configuration, and communication protocols.
*Internal DSLs* are built on top of a host programming language, which is Python in our case.

The *Interpreter* pattern is related only to internal DSLs.
Its goal is to create a simple but useful language using the features provided by the host programming language.
The interpreter pattern assumes that the data already is parsed in some convenient form,
e.g., in an *abstract syntax tree (AST)*.

Example:
Create an internal DSL to control a smart house with sentences of the form:
```
<command> -> <receiver> -> <arguments>
```
e.g.,
```
increase -> boiler temperature -> 3 degrees
```
The grammar of the language to create can be defined using the *Backus-Naur Form (BNF)* notation:
```
event ::= command token receiver token arguments
  command ::= word+
  word ::= a collection of one or more alphanumeric characters
  token ::= ->
  receiver ::= word+
  arguments ::= word+
```

For parsing also included in this example, we need the `pyparsing` package
https://github.com/pyparsing/pyparsing
https://pypi.org/project/pyparsing/
https://snyk.io/advisor/python/pyparsing

```unix
$ python -m pip install pyparsing
```
"""
from pyparsing import Word, alphanums, OneOrMore, Group, Suppress, Optional

# Convert grammar to code
word = Word(alphanums)
command = Group(OneOrMore(word))
token = Suppress("->")
device = Group(OneOrMore(word))
argument = Group(OneOrMore(word))
event = command + token + device + Optional(token + argument)

# Parse sentence
sentence = "increase -> boiler temperature -> 3 degrees"
print(event.parseString(sentence))
# [['increase'], ['boiler', 'temperature'], ['3', 'degrees']]

cmd, dev, args = event.parseString(sentence)
cmd_str = " ".join(cmd)
print(cmd_str)
# increase
dev_str = " ".join(dev)
print(dev_str)
# boiler temperature


class Boiler:
	def __init__(self):
		self.temperature = 83  # in celsius

	def __str__(self):
		return f"boiler temperature: {self.temperature}"

	def increase_temperature(self, amount):
		print(f"increasing the boiler's temperature by {amount} degrees")
		self.temperature += amount

	def decrease_temperature(self, amount):
		print(f"decreasing the boiler's temperature by {amount} degrees")
		self.temperature -= amount


boiler = Boiler()

if "increase" in cmd_str and "boiler" in dev_str:
	boiler.increase_temperature(int(args[0]))
	# increasing the boiler's temperature by 3 degrees

print(boiler)
# boiler temperature: 86
