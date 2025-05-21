
# 🤖 Understanding Key Concepts in OpenAI Agent SDK

This README explains important concepts in the OpenAI Agent SDK using simple examples. It covers the `Agent` class, the use of `@dataclass`, system prompts via `instructions`, the `Runner` class, and Python Generics with `TContext`.

---

## 📘 Q1: Why is the `Agent` class defined as a `dataclass`?

Using `@dataclass` simplifies how we define classes that store data (like agent name, tools, etc.). It automatically provides methods like `__init__`, `__repr__`, and more.

### 🧪 Example:
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Kinza", 19)
print(p)  # Output: Person(name='Kinza', age=19)
```

---

## 📘 Q2(a): What are `instructions` in the `Agent` class, and why can they be callable?

- `instructions`: Acts like a **system prompt** – tells the agent how to behave.
- They can be:
  - A **string** (fixed message) – e.g., "Be helpful"
  - A **callable** (function) – generates a prompt based on context

### `__call__`:
The `Agent` class can implement `__call__` so you can use it like a function:
```python
agent("Hello")  # Triggers the agent with input
```
This makes it easy and intuitive to use the agent.

---

## 📘 Q2(b): Why is the user prompt passed to `Runner.run()` and why is it a class method?

- You give your input to `Runner`.
- `Runner` passes it to the `Agent`.
- `Agent` reads its rules (`instructions`) and responds.

### `run` is a class method:
- You can call it like this: `Runner.run("Your question")`
- No need to create an instance of Runner each time.

This keeps it clean and simple to use.

---

## 📘 Q3: What is the purpose of the `Runner` class?

The `Runner` is like a **manager** that handles how the `Agent` works when you give it input.

### 💡 What it does:
- Takes your input (prompt)
- Combines it with the agent’s instructions
- Runs the agent and returns the response

### ✅ Why it’s helpful:
- Organizes how agents are run
- Keeps code simple (just use `run`)
- Separates how the agent thinks from how it's called

---

## 📘 Q4: What are Generics in Python and why use them for `TContext`?

### What are Generics?
Generics allow code to work with **any type** while keeping it type-safe.

It’s like a blueprint that says:
> “This can be any type (string, int, etc.), but stay consistent once chosen.”

Used with `typing` module:
```python
from typing import TypeVar, Generic

T = TypeVar('T')  # A generic type

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content

box_int = Box(123)
box_str = Box("hello")
```

### Why for `TContext`?
- `TContext` is a generic for any context type.
- Makes the agent flexible but still knows what kind of context it's working with.
- Helps catch type errors before running code.

---

## 🏁 Summary

| Concept      | Purpose                                                   |
|--------------|-----------------------------------------------------------|
| `@dataclass` | Quickly creates data-holding classes                      |
| `instructions` | System prompt telling the agent how to behave           |
| `__call__`   | Lets you use agent like a function                        |
| `Runner.run()` | Runs the agent with your input, easily and cleanly      |
| `Generics` (`TContext`) | Make the code reusable and type-safe           |

This setup makes agents **powerful**, **flexible**, and **easy to use**.
