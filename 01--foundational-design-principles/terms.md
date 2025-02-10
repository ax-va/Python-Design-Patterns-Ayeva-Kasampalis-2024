# Foundational Design Principles

## Encapsulate what varies

Isolate the parts of your code that are most likely to change and encapsulate them.

  - Advantages:
    - Ease of maintenance:      Reduce the risk of introducing bugs when only modifying the encapsulated parts
    - Enhanced flexibility:     Provide a more adaptable architecture when changing encapsulated components
    - Improved readability:     Code becomes more organized and easier to understand


  - Polymorphism and properties: 

    - *Polymorphism* allows instances of different classes to be treated as instances of a common superclass.
    - When using *properties*, *getters* allow reading the values of attributes and *setters* enable modifying them.


## Favor Composition Over Inheritance 

Prefer composing objects from simpler parts to inheriting functionalities from a base class (*composition* = "has-a" relationship).

## Program to Interfaces, Not Implementations

Code against an interface rather than a concrete class.

  - Benefits:
    - Flexibility:          Easily switch between different implementations without altering the code that uses them
    - Maintainability:      Make the code easier to update or replace components because of no specific implementations
    - Testability:          Simpler to write unit tests, as you can easily mock the interface during testing

  
- In Python, interfaces can be implemented using two primary techniques:

    1. **Abstract base classes (ABCs)** define abstract methods that must be implemented by any concrete (i.e., non-abstract) subclass.
    2. **Protocols** offer a more flexible approach than ABCs, known as *structural duck typing*, 
    where an object is considered valid if it has certain attributes or methods, regardless of its actual inheritance.

## Loose coupling

Decrease the dependencies between different parts of a program so that
components are independent and interact through well-defined interfaces.

  - Benefits:
    - Maintainability:          Easier to update or replace individual components because of fewer dependencies
    - Extensibility:            Can be more easily extended with new features or components
    - Testability:              Easier to test independent components in isolation

  
- There are two primary techniques to reduce the interdependencies between components:
    1. The **dependency injection** pattern allows a component to receive its dependencies from an external source
rather than creating them, making it easier to swap or mock these dependencies.

    2. The **observer** pattern allows an object to publish changes to its state so that other objects
can react accordingly, without being tightly bound to each other.