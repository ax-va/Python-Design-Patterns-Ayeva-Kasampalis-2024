# Architectural Design Patterns

## Model-View-Controller (MVC)

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

## Microservices

The *Microservice Architecture* pattern, or *Microservices*, is used to build 
an application as a set of loosely coupled, collaborating services.
These services are loosely coupled, independently deployable, and communicate via well-defined APIs.
We usually run those services packed as containers with our application server, 
dependencies and runtime libraries, compiled code, configurations, etc.

## Serverless

The *Serverless* pattern abstracts server management, allowing developers to focus solely on code.
Cloud providers handle the scaling and execution based on event triggers, 
such as HTTP requests, file uploads, or database modifications.
For example, AWS Lambda is Amazon's serverless compute service, which runs code in response to triggers.

## Event Sourcing

- eventsourcing
```unix
$ python -m pip install eventsourcing
```