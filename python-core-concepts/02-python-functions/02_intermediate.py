"""
Intermediate-level Python functions - focusing on the following concepts:
 > Default and keyword arguments
 > Variable-length arguments (*args and **kwargs)
 > Lambda functions
 > Scope and closures
 > Function Annotations
 > Partial Functions
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
1. Default and Keyword Arguments - What Are They?
Default Arguments: Allow you to define a default value for a parameter if no argument is provided during the function call.
Keyword Arguments: Specify arguments by their parameter names to improve readability.
"""

# Default Arguments
def calculate_discounted_price(price, discount = 0.1):
    return price - (price * discount)
print(calculate_discounted_price(100)) # Uses defualt parameter value
print(calculate_discounted_price(100, discount =0.2)) # Uses the argument provided for the discount parameter

# Keyword Arguments
def display_info(name, age, profession):
    return f"{name} is a {age} year old {profession}."
print(display_info(name="Alice", profession="Data Scientist", age="34"))

"""
Q: Why use default arguments in a function?
A: Default arguments improve flexibility by allowing the caller to skip less commonly modified parameters. 
For example, in a data preprocessing function, you might set a default threshold for outlier removal.

Q: What are the benefits of keyword arguments?
A: Keyword arguments enhance readability and reduce errors by explicitly naming parameters during the function call.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
2. Variable-Length Arguments (*args and **kwargs) - What Are They?
*args: Allows a function to accept a variable number of positional arguments.
**kwargs: Allows a function to accept a variable number of keyword arguments.
"""

# Variable number of positional arguments
def sum_of_numbers(*args):
    return sum(args)
print(sum_of_numbers(1,2,3,4,5))

"""
Q: When would you use *args in a function?
A: Use *args when the number of arguments isn’t known in advance. 
For instance, when calculating the mean of an unknown number of values in a dataset:
```
def calculate_mean(*args):
    return sum(args) / len(args)
```
"""

# Variable number of keyword arguments
def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
create_profile(name="Alice", age=34, profession="Data Scientist")

"""
Q: How do **kwargs enhance flexibility in function design?
A: **kwargs allow passing of arbitrary metadata. 
For example, when creating a machine learning model, you could pass parameters like learning_rate or max_depth dynamically:
```
def train_model(**kwargs):
    for param, value in kwargs.items():
        print(f"{param}: {value}")
train_model(learning_rate=0.01, max_depth=5)
```
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
3. Lambda Functions - What Are They?
Lambda functions are anonymous functions defined with the lambda keyword. They are useful for simple operations.
"""
# Sorting a list of dictionaries
data = [{"name":"Alice", "age":34}, {"name":"Bob", "age":25}, {"name":"Charlie", "age":30}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

# Data filtering
transactions = [100,200,300,450]

high_value = list(filter(lambda x: x > 200, transactions))
print(high_value)

"""
Q: What are lambda functions, and when would you use them?
A: Lambda functions are concise, single-expression functions used when defining a full function is unnecessary. 
For example, when sorting or filtering data during preprocessing.

Q: What are the limitations of lambda functions?
A: They are limited to single expressions and lack readability for complex logic.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
4. Scope and Closures - What Are They?
Scope: Refers to the visibility of variables in a program.
Closures: Functions that remember variables from their enclosing scope even after that scope has ended.
"""

# Scope Example
def outer():
    x = 2 # Local variable
    def inner():
        return x * 2 # Access variable from outer scope
    return inner()
print(outer())

# Closures Example
def multiplier(factor):
    def multiply(num):
        return num * factor
    return multiply
times_two = multiplier(2)
print(times_two(5))

"""
Q: What is the difference between local and global scope in Python?
A:
Local scope: Variables defined inside a function.
Global scope: Variables accessible throughout the program.
```
global_var = 10
def access_global():
    return global_var  # Accessible inside the function
```

Q: What are closures, and how are they useful?
A: Closures allow functions to remember the state of their enclosing scope. 
This is useful in scenarios like creating dynamic functions for feature scaling:
```
def scaler(factor):
    def scale(value):
        return value * factor
    return scale

scale_by_2 = scaler(2)
print(scale_by_2(5))  # Output: 10
```
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
5. Function Annotations
Function annotations allow you to provide metadata about a function’s parameters and return value.
While not enforced by Python, they can improve code readability, especially in collaborative environments.
"""
def add_num(x:int, y:int) -> int:
    return x + y
"""
Q: What are function annotations, and why are they useful?
A: Annotations are metadata for function parameters and return types, 
helping improve readability and assisting with type checking in tools like mypy.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
6. Partial Functions (functools.partial)
Partial functions let you create a version of a function with some arguments pre-filled.
Useful when reusing functions in different contexts.
"""
from functools import partial
def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)
print(square(5))

"""
Q: When would you use functools.partial in a data science pipeline?
A: To pre-configure functions for common tasks, such as scaling data by a specific factor or applying specific preprocessing steps.
"""