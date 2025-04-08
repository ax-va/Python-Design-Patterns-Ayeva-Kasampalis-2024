"""
State

A *(finite) state machine* is an abstract machine with two key components, that is, states and transitions.
A state is the current (active) status of a system.
A transition is a switch from one state to another that is initiated by an event or condition.
State diagrams represent state machines so that each state is a node, and each transition is an edge between two nodes.
The *State* pattern focuses on implementing a state machine in software engineering.

The *State* design pattern is usually implemented using a parent `State` class
with the common functionality of all the states, and several concrete classes derived from `State`
with the state-specific required functionality.

See also:
- Thomas Jaeger, The State Design Pattern vs State Machine
https://thomasjaeger.wordpress.com/2012/12/13/the-state-design-pattern-vs-state-machine-2/

- state_machine
https://github.com/jtushman/state_machine
https://pypi.org/project/state_machine/
https://snyk.io/advisor/python/state-machine

```unix
$ python -m pip install state_machine
```
"""
from state_machine import acts_as_state_machine, State, Event, after, before, InvalidStateTransition


@acts_as_state_machine
class Process:
    # states
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    # transitions
    wait = Event(
        from_states=(
            created,
            running,
            blocked,
            swapped_out_waiting,
        ),
        to_state=waiting,
    )
    run = Event(
        from_states=waiting,
        to_state=running,
    )
    terminate = Event(
        from_states=running,
        to_state=terminated,
    )
    block = Event(
        from_states=(
            running,
            swapped_out_blocked,
        ),
        to_state=blocked,
    )
    swap_wait = Event(
        from_states=waiting,
        to_state=swapped_out_waiting,
    )
    swap_block = Event(
        from_states=blocked,
        to_state=swapped_out_blocked,
    )

    def __init__(self, name):
        self.name = name

    # The `@before` and `@after` decorators are used to execute actions
    # before or after a transition occurs, respectively.

    @after("wait")
    def wait_info(self):
        print(f"{self.name} entered waiting mode")

    @after("run")
    def run_info(self):
        print(f"{self.name} is running")

    @before("terminate")
    def terminate_info(self):
        print(f"{self.name} is terminating...")

    @after("block")
    def block_info(self):
        print(f"{self.name} is blocked")

    @after("swap_wait")
    def swap_wait_info(self):
        print(f"{self.name} is swapped out and waiting")

    @after("swap_block")
    def swap_block_info(self):
        print(f"{self.name} is swapped out and blocked")


def transition(process: Process, event: Event, event_name: str):
    try:
        event()
    except InvalidStateTransition:
        print(
            f"Transition of {process.name} "
            f"from {process.current_state} "
            f"to {event_name} failed"
        )

def current_state(process: Process):
    print(f"Current state of {process.name}: {process.current_state}")


if __name__ == "__main__":
    # Event names are useful for debugging and
    # providing additional information.
    RUNNING = "running"
    WAITING = "waiting"
    BLOCKED = "blocked"
    TERMINATED = "terminated"

    p1, p2 = Process("process1"), Process("process2")
    [current_state(p) for p in (p1, p2)]
    # Current state of process1: created
    # Current state of process2: created

    transition(p1, p1.wait, WAITING)
    # process1 entered waiting mode
    transition(p2, p2.terminate, TERMINATED)  # illegal transition
    # Transition of process2 from created to terminated failed
    [current_state(p) for p in (p1, p2)]
    # Current state of process1: waiting
    # Current state of process2: created

    transition(p1, p1.run, RUNNING)
    # process1 is running
    transition(p2, p2.wait, WAITING)
    # process2 entered waiting mode
    [current_state(p) for p in (p1, p2)]
    # Current state of process1: running
    # Current state of process2: waiting

    transition(p2, p2.run, RUNNING)
    # process2 is running
    [current_state(p) for p in (p1, p2)]
    # Current state of process1: running
    # Current state of process2: running

    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    # process1 is blocked
    # process2 is blocked
    [current_state(p) for p in (p1, p2)]
    # Current state of process1: blocked
    # Current state of process2: blocked

    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]  # illegal transitions
    # Transition of process1 from blocked to terminated failed
    # Transition of process2 from blocked to terminated failed
    [current_state(p) for p in (p1, p2)]
    # Current state of process1: blocked
    # Current state of process2: blocked
