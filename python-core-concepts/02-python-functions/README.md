
# Python Functions: Comprehensive Interview Q&A for Data Scientist Role

## **Basic Functions**

### **1. What is a function in Python?**
- **A**: A function is a reusable block of code that performs a specific task. It is defined using the `def` keyword.

### **2. What is the difference between `return` and `print` in a function?**
- **A**:
  - `return`: Sends the output of the function back to the caller.
  - `print`: Displays the output but does not return it to the caller.

**Example**:
```python
def add(a, b):
    return a + b

result = add(2, 3)  # result = 5
```

### **3. Can a function return multiple values?**
- **A**: Yes, by returning them as a tuple or other iterable.

**Example**:
```python
def calculate(a, b):
    return a + b, a - b
print(calculate(5, 3))  # Output: (8, 2)
```

---

## **Intermediate Functions**

### **1. What are default arguments in Python?**
- **A**: Default arguments are values that a function takes if no value is provided by the caller.

**Example**:
```python
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!
```

### **2. What are `*args` and `**kwargs`?**
- **A**:
  - `*args`: Captures a variable number of positional arguments as a tuple.
  - `**kwargs`: Captures a variable number of keyword arguments as a dictionary.

**Example**:
```python
def display_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

display_info(1, 2, name="Alice", age=25)
# Output:
# Positional: (1, 2)
# Keyword: {'name': 'Alice', 'age': 25}
```

---

## **Advanced Functions**

### **Decorators**

#### **1. What is a decorator in Python?**
- **A**: A decorator is a function that takes another function as input, modifies or extends its behavior, and returns the modified function.

**Example**:
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

### **Recursion**

#### **1. What is recursion in Python?**
- **A**: Recursion is when a function calls itself to solve smaller parts of the same problem.

**Example**:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### **Higher-Order Functions**

#### **1. What is a higher-order function?**
- **A**: A function that accepts another function as an argument or returns a function.

**Example**:
```python
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x ** 2, 5))  # Output: 25
```

---

### **Generators**

#### **1. What is a generator in Python?**
- **A**: A generator is an iterator that generates values lazily using the `yield` keyword.

**Example**:
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(5)))  # Output: [0, 1, 1, 2, 3]
```

---

### **Comprehensive Comparison**

#### **Comparison: Generators vs Lists**
| **Aspect**        | **Generators**                            | **Lists**                        |
|--------------------|-------------------------------------------|----------------------------------|
| Memory Usage       | Low (values generated on demand).         | High (all values stored in memory). |
| Evaluation         | Lazy (values computed when needed).       | Eager (values computed immediately). |
| Use Case           | Ideal for large or infinite data.         | Suitable for small datasets.       |
| Reusability        | Can only be iterated once.                | Can be iterated multiple times.    |

