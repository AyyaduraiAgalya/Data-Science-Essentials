"""
What Are Higher-Order Functions?
A function is considered a higher-order function if it:
 - Takes another function as an argument.
 - Returns a function as its result.
This is powerful for writing modular, reusable, and concise code.

Why Are Higher-Order Functions Important?
They allow functional programming patterns.
They are essential for operations like data transformation, filtering, and aggregation in data science workflows.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
# 1. Passing Functions as Arguments
def greet(name):
    return f"Hello {name}!"
def call_function(func, argument): # This is a higher-order function because it accepts another function (greet) as an argument.
    return func(argument)
print(call_function(greet, "Alice"))

"""-----------------------------------------------------------------------------------------------------------------"""
# 2. Key Built-In Higher-Order Functions
# A. map() - Applies a function to each element of an iterable and returns a map object.
# Syntax: map(function, iterable)
numbers = [1,2,3,4,5]
squared = map(lambda x: x**2, numbers)
print(list(squared))

# B. filter() - Filters elements of an iterable based on a condition (function returns True or False).
# Syntax: filter(function, iterable)
numbers =[1,2,3,4,5]
filter_even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(filter_even_numbers))

# C. reduce() - Reduces an iterable to a single value by repeatedly applying a function (cumulative operation).
# Syntax:
# > from functools import reduce
# > reduce(function, iterable, initializer)
from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# D. sorted() with key - Sorts elements of an iterable based on a key function.
# Syntax: sorted(iterable, key=function)

data =[{'name':'Alice', 'age':34}, {'name':'Bob', 'age':27}]
sorted_data = sorted(data, key=lambda item: item['age'])
print(sorted_data)
"""-----------------------------------------------------------------------------------------------------------------"""
# 3. Creating Custom Higher-Order Functions
# Returning Functions - Higher-order functions can return a function as a result.
# Example: Function Factory
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
times_two = multiplier(2)
print(times_two(5))
"""-----------------------------------------------------------------------------------------------------------------"""
# 4. Combining Functions
# Higher-order functions can combine multiple functions.
# Example: Applying Multiple Transformations
def apply_transformations(data, transformations):
    for transformation in transformations:
        data = map(transformation,data)
    return list(data)

data = [1,2,3,4]
transformations = [lambda x: x + 1, lambda x: x ** 2]
print(apply_transformations(data, transformations))
"""-----------------------------------------------------------------------------------------------------------------"""
# 4. Practical Applications in Data Science
# A. Data Preprocessing - Filter and clean a dataset.
data = ["Alice", "Charles", "", None, "Bob"]
clean_data = filter(lambda item: item is not None and item != "", data) # Removing empty values and None values
print(list(clean_data))

# B. Aggregating metrics - Use reduce to calculate cumulative metrics.
sales = [100,200,300]
cumulative_sales = reduce(lambda x, y: x + y, sales)
print(cumulative_sales)

# C. Applying custom functions - Map transformations to columns in a dataset.
columns = ["name", "age", "salary"]
columns_uppercase = map(lambda x: x.upper(), columns)
print(list(columns_uppercase))
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Q1: What is a higher-order function?
A: A higher-order function is a function that either:
    - Accepts another function as an argument.
    - Returns a function as its result.
    
Q2: How is map() different from filter()?
A:
- map() applies a transformation to each element of an iterable.
- filter() selects elements based on a condition.

Q3: How would you use higher-order functions in a data science pipeline?
A:
Higher-order functions like map() can apply transformations to datasets, 
filter() can remove invalid rows, and reduce() can calculate metrics like sums or averages."

Q4: What is the role of key in the sorted() function?
A: The key argument allows you to specify a function that determines how elements are compared during sorting.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
# 6. Practice Exercise
# Task: Write a higher-order function to normalise a list of numbers to a range [0, 1].
def normalise_values(data: list):
    min_value, max_value = min(data), max(data)
    return list(map(lambda x: (x - min_value) / (max_value - min_value), data))
data = [10,20,30,40]
print(normalise_values(data))
"""-----------------------------------------------------------------------------------------------------------------"""
