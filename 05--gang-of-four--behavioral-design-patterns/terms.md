# The Gang of Four

## Behavioral Design Patterns

*Behavioral design patterns* deal with object interconnection and algorithms:

- **chains of responsibility**

The *chain of responsibility* pattern is used to handle requests by passing them from the sender (client) to receivers 
(processing elements, handlers) through a chain of handlers. 
Each handler decides either whether it can process the request or whether it should delegate it further along the chain.
The client only interacts with the first processing element in the chain, 
the first one only with the second one, and so forth.
Thus, the client only needs to know how to communicate with the start (head) of the chain.

- **commands**

The *command* pattern is used to encapsulate an operation 
(such as undo, redo, copy, paste, capitalize text, and so forth) as an object.

- **observers**

The *observer* pattern describes a *publish-subscribe relationship* between the *publisher*, 
also known as the *subject* or *observable* (or *event* in event-driven systems), 
and the subscribers, also known as the *observers* (or *listeners* in event-driven systems).
The subject notifies the subscribers of any state changes, typically by calling one of their methods.
The observers can be dynamically attached to or removed from observing the subject at runtime.

- **states**

```unix
$ python -m pip install state_machine
```

- **interpreters**

```unix
$ python –m pip install pyparsing
```

- **strategies**

- **mementos**

- **iterators**

- **templates**

```unix
$ python –m pip install cowpy
```