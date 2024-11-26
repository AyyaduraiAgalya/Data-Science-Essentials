"""
Functions are reusable blocks of code designed to perform specific tasks. They allow modularity, reusability, and easier debugging.
"""

# Syntax of a function
def function_name(parameters):
    # Function Body
    value = parameters
    return value

# Function to call the square of a number
def square_number(num):
    return num ** 2
print(square_number(4))

"""
Q: Why are functions important in Python?
A: Functions improve modularity and reusability by enabling the separation of code into logical, manageable parts. 
For example, instead of rewriting code for common tasks like data cleaning, you can use functions.
"""

"""-----------------------------------------------------------------------------------------------------------------"""

# Parameters and return value
# Function to calculate the total price with tax
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total
print(calculate_total(100, 0.05))

"""
Q: What is the difference between print and return in a function?
A: Return sends a value back to the caller and ends the function’s execution.
   Print only outputs a value to the console and doesn’t affect the flow of the program.
"""

"""-----------------------------------------------------------------------------------------------------------------"""

"""
Default Arguments
Default arguments allow you to define a parameter’s default value if no argument is passed during the function call.
"""

# Function with default tax_rate
def calculate_total(price, tax_rate=0.05):
    total = price + (price * tax_rate)
    return total
print(f"With default tax_rate: {calculate_total(100)}")
print(f"With a tax rate given: {calculate_total(100, 0.01)}")

"""
Q: When would you use default arguments in a function?
A: Use default arguments for parameters that usually take the same value, such as a default tax rate 
or a default threshold in machine learning pipelines.
"""

"""-----------------------------------------------------------------------------------------------------------------"""

"""
Keyword Arguments
With keyword arguments, you can specify parameter names during the function call.
"""

# Keyword arguments example
def introduce(name, age):
    return f"My name is {name}, I am {age} years old"
print(introduce(age=34, name="Alice"))

"""
Q: What is the benefit of keyword arguments?
A: Keyword arguments enhance code readability by clearly specifying which parameter is being passed.
"""

"""-----------------------------------------------------------------------------------------------------------------"""

"""
Variable-Length Arguments (*args and **kwargs)
- *args collects additional positional arguments.
- **kwargs collects additional keyword arguments.
"""

# Using *args for flexible number of inputs
def add_numbers(*args):
    return sum(args)
print(add_numbers(1,2,3,4,5))

# Using **kwargs for named parameters
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(age=34, name="Alice", gender="Female")

"""
Q: When would you use *args and **kwargs?
A: Use *args for functions that accept an unknown number of positional arguments (e.g., summing numbers). 
Use **kwargs for functions that need flexibility with named arguments (e.g., displaying metadata about a dataset).
"""

"""-----------------------------------------------------------------------------------------------------------------"""

# Real World use case for functions

# Creating a reusable function for data cleaning
def clean_data(data):
    data = [item.lower() for item in data]  # Converting to lowercase
    data = list(set(data))  # Removing duplicates
    return data
raw_data = ["ALICE", "bob", "ChaRLie", "BOB"]
print(clean_data(raw_data))

"""-----------------------------------------------------------------------------------------------------------------"""

# Defining functions inside another function
def outer_function(x):
    def inner_function(y):
        return y ** 2
    return inner_function(x) + 1
print(outer_function(3))

"""-----------------------------------------------------------------------------------------------------------------"""

"""
Q: What happens if a function doesn’t have a return statement?
A: If no return statement is used, the function implicitly returns None.
"""

def greet():
    print("Hello World!")
result = greet()
print(result)

"""-----------------------------------------------------------------------------------------------------------------"""

"""
Q: What are the benefits of modular code using functions?
A:
Reusability: Functions can be reused across projects or workflows.
Readability: Code is easier to understand and maintain.
Debugging: Functions isolate logic, making debugging easier.
"""