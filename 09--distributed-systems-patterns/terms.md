## Distributed Systems Patterns

### Throttling

The *Throttling* pattern is intended to control the rate of requests 
a user (or a client service) can send to a given service or API in a given amount of time, 
to protect the resources of the service from being overused.

### Retry

When communicating with an external component or service, 
the *Retry* pattern is used to call the service again,
perhaps immediately or after some timeout (such as a few seconds), 
to avoid or minimize the occurrence of transient faults or failures 
that are not related to the application's logic itself.

### Circuit Breaker

In the *Circuit Breaker* pattern, an integration point with an external service
is wrapped in a special (*circuit breaker*) object, which monitors for failures.
Once the failures reach a certain threshold, the circuit breaker transits to
the "open" state, immediately returning an error and preventing further calls 
to the protected function.

## Other Distributed Systems Patterns

### Command and Query Responsibility Segregation (CQRS)

*Command and Query Responsibility Segregation (CQRS)* is a design pattern that separates 
the responsibilities of reading data (queries) and writing data (commands) into distinct models. 
This separation allows for optimized, scalable, and independently evolving read and write operations.

### Two-Phase Commit

*Two-Phase Commit (2PC)* is a protocol used in distributed systems to ensure all participating nodes 
in a transaction either commit or roll back changes in a coordinated manner. 
It involves a *prepare* phase where participants vote on committing, followed by a *commit* phase 
where the *coordinator* finalizes the decision based on the votes.

### Saga

The *Saga* design pattern is used to manage distributed transactions by breaking them into 
a sequence of smaller, independent local transactions, each with its own compensating action in case of failure. 
If any step fails, previously completed steps are rolled back using these compensating actions, 
ensuring data consistency without requiring a global lock.

### Sidecar

The *Sidecar* pattern involves deploying a helper service (the *sidecar*) alongside a main application service 
within the same environment, typically in the same container or pod. 
This sidecar handles auxiliary tasks like logging, monitoring, or proxying, 
allowing the main service to focus solely on its core functionality.

### Service Registry

The *Service Registry* pattern is used in microservice architectures to maintain a dynamic database 
of available service instances and their locations. Services register themselves with the registry, 
and clients or other services query the registry to discover and communicate with available service instances.

### Bulkhead

Inspired by ship design, the *Bulkhead* pattern isolates different parts of a system into 
separate, independent compartments to prevent a failure in one part from cascading to others. 
This improves overall system resilience and ensures 
that critical services remain available even if non-critical services fail.
