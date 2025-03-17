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
