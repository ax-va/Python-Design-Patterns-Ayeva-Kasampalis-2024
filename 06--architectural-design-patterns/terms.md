## Architectural Design Patterns

### Model-View-Controller (MVC)

The *Model-View-Controller (MVC)* pattern is an application of the *separation of concern* principle and 
used for *loose coupling* to split a software application into three components:

- The *model* is the core component that contains and manages 
the (business) logic, data, state, and rules of an application.

- The *view* is a visual representation of the model to only displays the data (but not to handle it).
The examples may be a GUI, an output in a terminal, a PDF document, a chart, and so forth. 

- The *controller* is used for all communication between the model and the view. 
The controller allows us to use more than one view without modifying the model.
To achieve decoupling between the model and its representation, every view typically needs its own controller.

When implementing MVC from scratch, be sure that you create smart models, thin controllers, and dumb views.

### Microservices

In the *Microservice Architecture* pattern, or *Microservices*, an application is considered 
as a set of collaborating and independent services, each responsible for a specific business function.
These services are loosely coupled, independently deployable, and communicate via well-defined APIs.
We usually run those services packed as containers with our application server, 
dependencies and runtime libraries, compiled code, configurations, etc.

### Serverless

The *Serverless* pattern shifts the focus from server management to pure business logic 
by leveraging cloud services to execute code snippets in response to events.
Cloud providers handle the scaling and execution based on event triggers, 
such as HTTP requests, file uploads, or database modifications.
For example, AWS Lambda is Amazon's serverless compute service, which runs code in response to triggers.

### Event Sourcing

The *Event Sourcing* pattern helps us in storing all changes to an application state as a sequence of events.
This way, the application state can be reconstructed at any point in time by replaying these events.

The components of the Event Sourcing pattern implementation are as follows:

- **Event**: A representation of a state change. Once an event is created and applied, it cannot be changed.

- **Aggregate**: An object (or group of objects) for tracking that represents a single unit of business logic or data.
Every time something changes (an event), it makes a record of it.

- **Event store**: A collection of all the events that have occurred.

## Other Architectural Design Patterns

### Event-Driven Architecture (EDA)

This pattern emphasizes the production, detection, consumption of, and reaction to events.

### Command Query Responsibility Segregation (CQRS)

This pattern separates the models for reading and writing data.

### Clean Architecture

This pattern proposes a way to organize code such that it encapsulates the business logic 
but keeps it separate from the interfaces through which the application is exposed to users or other systems.
