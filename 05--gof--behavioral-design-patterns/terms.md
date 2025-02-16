# The Gang of Four (GoF)

## Behavioral Design Patterns

*Behavioral design patterns* deal with object interconnection and algorithms.

### Chain of Responsibility

The *Chain of Responsibility* pattern is used to handle requests by passing them from the sender (client) to receivers 
(processing elements, handlers) through a chain of handlers. 
Each handler decides either whether it can process the request or whether it should delegate it further along the chain.
The client only interacts with the first processing element in the chain, 
the first one with only the second one, and so on.
Thus, the client only needs to know how to communicate with the start (head) of the chain.

### Command

The *Command* pattern is used to encapsulate an operation 
(e.g. undo, redo, copy, paste, capitalize text, and so forth) as an object.

### Observer

The *Observer* pattern describes a *publish-subscribe relationship* between the *publisher*, 
also known as the *subject* or *observable* (or *event* in event-driven systems), 
and the subscribers, also known as the *observers* (or *listeners* in event-driven systems).
The subject notifies the subscribers of any state changes, typically by calling one of their methods.
The observers can be dynamically attached to or removed from observing the subject at runtime.

### State

A *(finite) state machine* is an abstract machine with two key components, that is, states and transitions.
A state is the current (active) status of a system.
A transition is a switch from one state to another that is initiated by an event or condition.
State diagrams represent state machines so that each state is a node, and each transition is an edge between two nodes.
The *State* pattern focuses on implementing a state machine in software engineering.

### Interpreter

A *(domain-specific language) DSL* is a computer language of limited expressiveness targeting a particular domain,
such as combat simulation, billing, visualization, configuration, and communication protocols. 
*Internal DSLs* are built on top of a host programming language, which is Python in our case.

The *Interpreter* pattern is related only to internal DSLs. 
Its goal is to create a simple but useful language using the features provided by the host programming language.
The interpreter pattern assumes that the data already is parsed in some convenient form, 
e.g., in an *abstract syntax tree (AST)*.

### Strategy

The *Strategy* pattern promotes using multiple algorithms to solve a problem. 
It makes it possible to switch algorithms at runtime transparently that is,
the client code is unaware of the change.
Normally, the strategy should not be picked by the user.

### Memento

The *Memento* pattern is used to take a snapshot of the internal state of an object, 
so that the object can be restored with it when needed. 
In this design pattern, the following definitions are used:
- The *memento* is a simple object that contains basic state storage and retrieval capabilities.
- The *originator* is an object that gets and sets values of memento instances.
- The *caretaker* is an object that can store and retrieve all previously created memento instances.

### Iterator

The *Iterator* pattern is a design pattern, in which an *iterator* is used to traverse a container and 
access the container's elements. 
The iterator pattern decouples algorithms from containers. 
In some cases, algorithms are necessarily container-specific and thus cannot be decoupled.
Iterator in Python is simply an object that can be iterated upon 
that is, an object that will return data, one element at a time.

### Template

The *Template* pattern focuses on eliminating code repetition 
by redefining certain parts of an algorithm without changing its structure.
*Invariant* (common) parts of algorithms are kept in a template method/function, and 
*variant* (different) parts are moved in action/hook methods/functions.

## Other Patterns 

Behavioral design patterns that are not commonly used by Python developers:

### Mediator

In the *Mediator* pattern, objects don't communicate directly with each other; 
instead, they communicate through a *mediator* object 
that acts as a central hub for coordinating communication between the objects.

In Python, you can use event-driven programming with a library such as `asyncio` 
instead of communication between objects through a mediator object.

### Visitor

For complex use cases, the *Visitor* pattern provides a solution 
for separating algorithms from the objects on which they operate.

In Python, using functions as first-class citizens, decorators, or context managers 
can provide ways to encapsulate algorithms and operations without the need for explicit visitor objects.