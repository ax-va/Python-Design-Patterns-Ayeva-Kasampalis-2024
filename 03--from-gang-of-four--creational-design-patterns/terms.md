## Creational Design Pattens

Creational design pattens (from the Gang of Four):

- factories (factory methods, abstract factories)

In the *factory* design pattern, a client creates an object without knowing how (by which class) the object is created.

- builders

The *builder* pattern separates the construction of a complex object from its representation, 
so that the same construction can be used to create several different representations.
A factory pattern creates an object in a single step, whereas a builder
pattern creates an object in multiple steps and almost always uses a *director*.

- prototypes

Create new objects by copying existing ones with the change of some attributes instead of creating to them from scratch.

- singletons

The *singleton* pattern restricts a class instance to a single object.

- object pools

Reuse existing objects instead of creating new ones when they are needed.