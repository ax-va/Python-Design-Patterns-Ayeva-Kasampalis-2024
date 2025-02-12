# The Gang of Four (GoF)

## Behavioral Design Patterns

*Behavioral design patterns* deal with object interconnection and algorithms.

### Chains of Responsibility

The *chain of responsibility* pattern is used to handle requests by passing them from the sender (client) to receivers 
(processing elements, handlers) through a chain of handlers. 
Each handler decides either whether it can process the request or whether it should delegate it further along the chain.
The client only interacts with the first processing element in the chain, 
the first one with only the second one, and so on.
Thus, the client only needs to know how to communicate with the start (head) of the chain.

### Commands

The *command* pattern is used to encapsulate an operation 
(e.g. undo, redo, copy, paste, capitalize text, and so forth) as an object.

### Observers

The *observer* pattern describes a *publish-subscribe relationship* between the *publisher*, 
also known as the *subject* or *observable* (or *event* in event-driven systems), 
and the subscribers, also known as the *observers* (or *listeners* in event-driven systems).
The subject notifies the subscribers of any state changes, typically by calling one of their methods.
The observers can be dynamically attached to or removed from observing the subject at runtime.

### States

A *(finite) state machine* is an abstract machine with two key components, that is, states and transitions.
A state is the current (active) status of a system.
A transition is a switch from one state to another that is initiated by an event or condition.
State diagrams represent state machines so that each state is a node, and each transition is an edge between two nodes.
The *state* pattern focuses on implementing a state machine in software engineering.

### Interpreters

A *(domain-specific language) DSL* is a computer language of limited expressiveness targeting a particular domain,
such as combat simulation, billing, visualization, configuration, and communication protocols. 
*Internal DSLs* are built on top of a host programming language, which is Python in our case.
The *interpreter* pattern is related only to internal DSLs. 
Its goal is to create a simple but useful language using the features provided by the host programming language.
The interpreter pattern assumes that the data already is parsed in some convenient form, 
e.g., in an *abstract syntax tree (AST)*.

### Strategies

### Mementos

### Iterators

### Templates

```unix
$ python –m pip install cowpy
```
