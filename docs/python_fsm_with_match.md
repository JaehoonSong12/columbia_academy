
# Python Switch Case Statement with `match` Syntax

## What is a Finite State Machine (FSM)?

A **Finite State Machine (FSM)** is a computational model used to represent and control the execution flow of a system. It consists of:

1. **States**: The various conditions or situations the system can be in.
2. **Transitions**: Rules that define how the system moves from one state to another based on inputs or events.
3. **Events/Inputs**: Triggers that cause state transitions.

FSMs are commonly used in areas like game development, compilers, network protocols, and user interface design.

## Using `match` for FSM Implementation

The `match` statement in Python 3.10+ is an elegant way to implement FSMs. It allows for pattern matching, which makes state-based decision-making concise and readable.

### Example: Simple FSM for a Traffic Light System

```python
def traffic_light_fsm(state, event):
    """Finite State Machine for a traffic light."""
    match (state, event):
        case ("RED", "TIMER"):
            return "GREEN"
        case ("GREEN", "TIMER"):
            return "YELLOW"
        case ("YELLOW", "TIMER"):
            return "RED"
        case (_, "EMERGENCY"):
            return "RED"  # Emergency forces the light to RED state
        case _:
            return "INVALID"  # Handles unexpected inputs

# Example usage
current_state = "RED"
print(traffic_light_fsm(current_state, "TIMER"))      # Output: GREEN
print(traffic_light_fsm("YELLOW", "TIMER"))          # Output: RED
print(traffic_light_fsm("GREEN", "EMERGENCY"))       # Output: RED
```

### Why Use `match` for FSMs?

- **Readability**: The `match` statement clearly defines state-event combinations and their outcomes.
- **Extensibility**: Adding new states or transitions is straightforward.
- **Error Handling**: The `case _` block can handle invalid or unexpected events, ensuring robustness.

## Benefits of FSM Design

1. **Structured Design**: FSMs simplify complex systems by breaking them into well-defined states and transitions.
2. **Predictability**: The behavior of the system is predictable and easier to debug.
3. **Scalability**: FSMs can be extended as new features or conditions are added.
4. **Reusability**: FSM designs are modular and can often be reused across projects.

The `match` syntax in Python enhances FSM design by providing a clean and expressive way to define and handle states and transitions.
