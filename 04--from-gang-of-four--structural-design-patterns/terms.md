## Structural Design Patterns

A *structural design pattern* (from the Gang of Four) proposes a way of composing objects to provide new functionality:

- adapters

The *adapter* pattern serves as a flexible solution for harmonizing mismatched interfaces.

- decorators

The *decorator* pattern is used to extend the behavior of an object without using inheritance.

- bridges

While the *adapter* pattern is used *later* to make unrelated classes work together,
the *bridge* pattern is used *up-front* to define an abstraction and its implementation
in a decoupled way so that both can vary independently.

- facades

The *facade* pattern is for providing a simple interface to client code 
that wants to use a complex system but does not need to be aware of the system's complexity.

- flyweights

The *flyweight* pattern is used when an application needs to create 
a large number of computationally expensive objects that share many properties.

- proxies (virtual proxies, protection/protective proxies, remote proxies, smart proxies)

The *proxy* pattern contains:

+ a *virtual proxy*, which uses *lazy initialization* to defer
the creation of a computationally expensive object until the moment it is actually needed;

+ a *protection/protective proxy*, which controls access to a sensitive object;

+ a *remote proxy*, which acts as the local representation of an object that really exists
in a different address space (for example, a network server); an example: an object-relational mapping (ORM) API;

+ a *smart (reference) proxy*, which performs extra actions when an object is accessed;
examples: reference counting and thread-safety checks.