# The Gang of Four (GoF)

## Creational Design Pattens

### Factories (Factory Methods, Abstract Factories)

In the *factory* pattern, a client creates an object without knowing how (by which class) the object is created.

There are two forms of factories:

- The *factory method* that is, in Python, a function that returns a different object per input parameter 
but is considered in Python as over-engineered or unnecessarily complex.

- The *abstract factory* that is a group of factory methods,
where each factory method is responsible for generating a different kind of object.

### Builders

The *builder* pattern separates the construction of a complex object from its representation, 
so that the same construction can be used to create several different representations.
A factory pattern creates an object in a single step, whereas a builder
pattern creates an object in multiple steps and almost always uses a *director*.

### Prototypes

The *prototype* pattern helps us create new objects by copying existing ones with the change of some attributes
instead of creating to them from scratch.
This is useful if the object is expensive to create.

### Singletons

The *singleton* pattern restricts a class instance to a single object.
In the Python programmer community, the singleton pattern is actually considered an *anti-pattern*.

### Object Pools

The *object pool* pattern is used to reuse existing objects instead of creating new ones when they are needed.
This is useful when resource initialization is costly or time-consuming.