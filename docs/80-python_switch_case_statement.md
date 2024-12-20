
# Python Switch Case Statement

Python does not have a native `switch` or `case` statement like some other languages, but you can achieve similar functionality using a dictionary, `if-elif-else` constructs, or the `match` statement (available in Python 3.10+).

## Using a Dictionary (Preferred Approach for Simple Cases)

```python
def switch_case_example(option):
    switch = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected"
    }
    return switch.get(option, "Invalid option")  # Default case if option not found

# Example usage
print(switch_case_example(2))  # Output: Option 2 selected
print(switch_case_example(4))  # Output: Invalid option
```

## Using `if-elif-else` (More Flexible for Complex Logic)

```python
def switch_case_example(option):
    if option == 1:
        return "Option 1 selected"
    elif option == 2:
        return "Option 2 selected"
    elif option == 3:
        return "Option 3 selected"
    else:
        return "Invalid option"

# Example usage
print(switch_case_example(2))  # Output: Option 2 selected
print(switch_case_example(4))  # Output: Invalid option
```

## Using `match` (Python 3.10+)

Starting from Python 3.10, you can use the `match` statement for pattern matching, which works similarly to a `switch` statement:

```python
def switch_case_example(option):
    match option:
        case 1:
            return "Option 1 selected"
        case 2:
            return "Option 2 selected"
        case 3:
            return "Option 3 selected"
        case _:
            return "Invalid option"  # Default case

# Example usage
print(switch_case_example(2))  # Output: Option 2 selected
print(switch_case_example(4))  # Output: Invalid option
```

The `match` statement is the closest equivalent to `switch` in modern Python.
