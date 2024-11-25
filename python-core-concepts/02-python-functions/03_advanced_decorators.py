"""
What Are Decorators?
A decorator is a function that takes another function as input, modifies or extends its behavior, and returns the modified function.
It’s a wrapper around an existing function.

Why Use Decorators?
- Re-usability: Add functionality (e.g., logging, timing, validation) without modifying the original function.
- Cleaner Code: Avoid repetitive code by abstracting common patterns.

Common Use Cases in Data Science:
- Logging function calls during model training.
- Measuring the execution time of preprocessing steps.
- Validating input data before computation.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
# Create and Use a Decorator
# Basic Structure
def decorator_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

# Using the Decorator - can apply a decorator using the @decorator_name syntax above the function definition
@decorator_name
def function_to_decorate():
    pass
"""-----------------------------------------------------------------------------------------------------------------"""

"""
1. Logging Decorator
A simple decorator to log the input arguments and output of a function.
"""
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args}, kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(x,y):
    return x + y
print(add(3,5))

"""
2. Timing Decorator
A decorator to measure the execution time of a function.
"""
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result = func(*args, **kwargs)
        end_time=time.time()
        print(f"{func.__name__} executed in {end_time-start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Finished"
print(slow_function())

"""
3. Validating Input Data
A decorator to check that all inputs are positive numbers.
"""
def validate_positive(func):
    def wrapper(*args, **kwargs):
        if any(arg<0 for arg in args if isinstance(arg,(int, float))):
            raise ValueError("All inputs must be positive")
        return func(*args, **kwargs)
    return wrapper
@validate_positive
def multiply(x, y):
    return x * y
print (multiply(5, 10))
# print(multiply(5, 10)) # Uncomment this line to check the ValueError message

"""-----------------------------------------------------------------------------------------------------------------"""
"""
Decorators in a Data Science Context
1. Logging Preprocessing Steps
"""
import time
def log_preprocessing(func):
    def wrapper(*args, **kwargs):
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{start_time}: Calling {func.__name__} with args {args} & kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_preprocessing
def clean_data(data):
    return [item.strip() for item in data]

data = ["Alice ", " Bob", " Charlie "] # Added Whitespaces before or after double quotes to strip/clean
cleaned_data = clean_data(data)
print(cleaned_data)

"""
2. Timing Model Training
"""
@timing_decorator
def train_model():
    time.sleep(1) # Simulating training
    return "Model Trained"
train_model()

"""
3. Validating input shapes
"""
def validate_shapes(func):
    def wrapper(data, expected_shape):
        if len(data) != expected_shape[0]:
            raise ValueError("Data shapes does not match expected shape")
        return func(data, expected_shape)
    return wrapper
@validate_shapes
def process_data(data, expected_shape):
    print("Processing data of shape ", expected_shape)
    return True
process_data([1,2,3], (3,)) # Shape matches
#process_data([1,2], (3,)) # Shape doesnt match - uncomment to check the output in console

"""-----------------------------------------------------------------------------------------------------------------"""
"""
Q: What is a decorator in Python?
A: "A decorator is a function that modifies or extends the behavior of another function without changing its code. 
It’s often used for tasks like logging, timing, or validation."

Q: How are decorators useful in a data science pipeline?
A: "Decorators can:
Log data preprocessing steps for traceability.
Measure execution time for performance optimization.
Validate input shapes or types for robust pipelines."

Q: What are the advantages of using decorators over modifying functions directly?
A:
Re-usability: The same decorator can be applied to multiple functions.
Clean Code: Avoids cluttering function definitions with repetitive logic.
Separation of Concerns: Keeps core logic separate from auxiliary tasks like logging or validation.

Q: How would you implement multiple decorators on a single function?
A: Multiple decorators can be stacked:
```
@decorator1
@decorator2
def my_function():
    pass
```
"""