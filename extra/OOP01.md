# How to Start OOP in Python

**Dunder (double underscore) methods**, also known as **magic methods** in Python, are built-in functions for OOP related operations. 

## Key Dunder Methods and Their Roles

### 1. `__new__(cls, ...)`
- **Purpose:** Creates a new instance before `__init__` is called.
- **Usage:** Used when subclassing immutable types like tuples or strings.
- **Example:**

```python
class CustomStr(str):
    def __new__(cls, value):
        print("Creating a CustomStr instance")
        return super().__new__(cls, value)
```

---

### 2. `__init__(self, ...)`
- **Purpose:** Initializes an instance after it is created.
- **Usage:** Used to set up instance attributes.
- **Example:**

```python
class MyClass:
    def __init__(self, value):
        self.value = value
```

---

### 3. `__repr__(self)` and `__str__(self)`
- **`__repr__`**: Official string representation (used by `repr(obj)`, debugging).
- **`__str__`**: Informal, user-friendly string representation (used by `print(obj)`).

```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"MyClass({self.value!r})"
    
    def __str__(self):
        return f"MyClass with value {self.value}"
```

---

### 4. `__eq__(self, other)`
- **Purpose:** Defines equality behavior (`==`).
- **Example:**

```python
class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if isinstance(other, MyNumber):
            return self.value == other.value
        return False
```

---

### 5. `__del__(self)`
- **Purpose:** Destructor, called when an object is deleted.

```python
class MyClass:
    def __del__(self):
        print("Instance deleted")
```

---

### 6. `__enter__(self)` and `__exit__(self, exc_type, exc_value, traceback)`
- **Purpose:** Allow an object to be used in a `with` statement (context management).

```python
class MyResource:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyResource() as r:
    print("Inside with block")
```

---

### 7. `__call__(self, ...)`
- **Purpose:** Makes an instance callable like a function.

```python
class CallableClass:
    def __call__(self, x):
        return x * 2

obj = CallableClass()
print(obj(5))  # Outputs: 10
```

---

### 8. `__getattr__(self, name)`, `__setattr__(self, name, value)`
- **Purpose:** Customize attribute access.

```python
class MyClass:
    def __getattr__(self, name):
        print(f"Attribute '{name}' not found!")
        return None
    
    def __setattr__(self, name, value):
        print(f"Setting attribute '{name}' to {value}")
        super().__setattr__(name, value)

obj = MyClass()
obj.some_attr  # Triggers __getattr__
obj.new_attr = 42  # Triggers __setattr__
```

---

## Comprehensive Example

```python
class MyNumber:
    def __new__(cls, value):
        print("Creating a new MyNumber instance")
        return super().__new__(cls)

    def __init__(self, value):
        print("Initializing MyNumber")
        self.value = value

    def __repr__(self):
        return f"MyNumber({self.value!r})"

    def __str__(self):
        return f"MyNumber with value {self.value}"

    def __eq__(self, other):
        return isinstance(other, MyNumber) and self.value == other.value

    def __del__(self):
        print(f"Deleting MyNumber instance with value {self.value}")

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

    def __call__(self, increment):
        self.value += increment
        return self.value

    def __getattr__(self, name):
        print(f"Attribute '{name}' not found!")
        return None

    def __setattr__(self, name, value):
        print(f"Setting attribute '{name}' to {value}")
        super().__setattr__(name, value)

num = MyNumber(10)
print(repr(num))
print(str(num))
num(5)
with MyNumber(20) as num_context:
    print("Inside with block:", num_context)
```

This guide provides a structured understanding of Python's OOP magic methods to help you create powerful, intuitive classes.
