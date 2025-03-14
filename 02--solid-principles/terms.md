## SOLID

SOLID is a set of five design principles proposed by Robert C. Martin.

### Single Responsibility Principle (SRP)

Each class should have one job or responsibility, 
and that job should be encapsulated within that class.

### Open-Closed Principle (OCP)

Software entities, such as classes and modules, should be open 
for extension (through inheritance or interfaces to accommodate 
new requirements and behaviors) but closed for modification.

### Liskov Substitution Principle (LSP)

If a program uses objects of a superclass, then the substitution of them with objects
of a subclass should not change the correctness and expected behavior of the program.

### Interface Segregation Principle (ISP)

A class should not be forced to implement interfaces it does not use.
In the context of Python, this implies that a class shouldn't be forced 
to inherit and implement methods that are irrelevant to its purpose.

### Dependency Inversion Principle (DIP)

High-level modules should not depend directly on low-level modules.
Instead, both should depend on abstractions or interfaces.

The DIP is closely linked to the *loose coupling* principle by promoting a design
where components interact through interfaces rather than concrete implementations.