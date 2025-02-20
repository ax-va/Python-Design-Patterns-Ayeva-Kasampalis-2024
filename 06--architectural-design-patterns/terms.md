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

- Docker

- LocalStack (cloud service emulator that runs in a single container on your laptop or in your CI environment) for testing AWS Lambda locally
```unix
$ python -m pip install localstack
```

- awscli-local
```unix
$ python -m pip install awscli-local
```

- awscli
```unix
$ python -m pip install awscli
```

## Event Sourcing

- eventsourcing
```unix
$ python -m pip install eventsourcing
```