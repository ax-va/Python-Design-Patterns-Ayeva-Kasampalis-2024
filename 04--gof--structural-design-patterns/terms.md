# The Gang of Four (GoF)

## Structural Design Patterns

A *structural design pattern* proposes a way of composing objects to provide new functionality.

### Adapters

The *Adapter* pattern serves as a flexible solution for harmonizing mismatched interfaces.
An example may be adapting an old system component to a new system component or vice versa.

### Decorators

The *Decorator* pattern is used to extend the behavior of an object without using inheritance.
We can add responsibilities to an object dynamically, and in a transparent manner (without affecting other objects).
Python decorators can actually do much more than the decorator pattern.

### Bridges

While the *Adapter* pattern is used *later* to make unrelated classes work together,
the *Bridge* pattern is used *up-front* to define an abstraction and its implementation
in a decoupled way so that both can vary independently.

### Facades

The *Facade* pattern is for providing a simple interface to client code 
that wants to use a complex system but does not need to be aware of the system's complexity.
We can hide the internal complexity of our systems and expose only
what is necessary to the client through a simplified interface.

### Flyweights

The *Flyweight* pattern is used when an application needs to create 
a large number of computationally expensive objects that share many properties.
Thus, we minimize memory usage and improve performance by introducing data sharing between similar objects.
A flyweight is a shared object that contains state-independent, immutable (also known as *intrinsic*) data.
The state-dependent, mutable (also known as *extrinsic*) data should not be part of
flyweight because this is information that cannot be shared, since it differs per object.

### Proxies (Virtual Proxies, Protection/Protective Proxies, Remote Proxies, Smart Proxies)

The *Proxy* pattern contains:

  - a *virtual proxy*, which uses *lazy initialization* to defer the creation of a computationally expensive object until the moment it is actually needed;
  
  - a *protection/protective proxy*, which controls access to a sensitive object;
  
  - a *remote proxy*, which acts as the local representation of an object that really exists in a different address space (for example, a network server); an example: an object-relational mapping (ORM) API;
  
  - a *smart (reference) proxy*, which performs extra actions when an object is accessed; examples: reference counting and thread-safety checks.