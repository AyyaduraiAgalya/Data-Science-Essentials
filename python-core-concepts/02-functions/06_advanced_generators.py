"""
Generators are an essential concept for writing efficient, memory-friendly code, especially when working with large datasets.

What Are Generators?
Generators are a type of iterable, like lists or tuples, but instead of storing all values in memory, they generate values on the fly.
They are created using the yield keyword in a function or through generator expressions.

Key Benefits
 > Memory Efficiency:
   Unlike lists, generators don’t store all items in memory. They generate items one at a time, reducing memory usage.
 > Lazy Evaluation:
   Values are computed only when needed.
 > Useful for Large Data:
   Ideal for streaming data or working with large files.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
1. Generator Functions: 
   > A generator function is defined like a normal function but uses the yield keyword to return values one at a time.
"""
# Simple Generator Example
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # Raises StopIteration (no more values) - uncomment to see the response

"""
yield: Temporarily pauses the function, saving its state, and returns a value.
next(): Resumes the function from where it paused.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
2. Generator Expressions:
   > Generator expressions are a concise way to create generators, similar to list comprehensions but with parentheses instead of square brackets.
"""
gen = (x ** 2 for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""-----------------------------------------------------------------------------------------------------------------"""
"""
3. Use Cases for Generators in Data Science
A. Reading Large Files - Efficiently process a large file line by line.
Why Generators?: Instead of loading the entire file into memory, this processes it line by line.
"""
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
for line in read_large_file("python-core-concepts/02-python-functions/lorem_ipsum.txt"):
    print(line)

"""
B. Infinite Sequences - Generate an infinite series of numbers (e.g., Fibonacci).
Why Generators?: Efficiently generate sequences without storing all values.
"""
def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen_object = infinite_fibonacci()
for _ in range(5):
    print(next(gen_object))

"""
C. Streaming Data Processing - Simulate streaming data for preprocessing
"""
def stream_data(data):
    for item in data:
        yield item * 2

data_stream = stream_data([1, 2, 3, 4, 5, 6, 7, 8, 9])
for item in data_stream:
    print(item)
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Comparison: Generators vs Lists

Generators:
    - Memory Usage: Low (values generated on demand).
    - Evaluation: Lazy (values computed when needed).
    - Use Case: Ideal for large or infinite data.
    - Reusability: Can only be iterated once.

Lists:
    - Memory Usage: High (all values stored in memory).
    - Evaluation: Eager (values computed immediately).
    - Use Case: Suitable for small datasets.
    - Reusability: Can be iterated multiple times.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
4. Generator functions in action
A. Cumulative Sum
"""
def cumulative_sum(data: list):
    total = 0
    for item in data:
        total += item
        yield total
cumulative_sum_gen = cumulative_sum([1,2,3,4,5])
print(list(cumulative_sum_gen))

"""
B. Filtering Data - Filter even numbers lazily
"""
def filter_even_numbers(data: list):
    for value in data:
        if value % 2 == 0:
            yield value
gen = filter_even_numbers(range(10))
print(list(gen))
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Q1: What is a generator in Python?
A: A generator is a special type of iterable that generates values lazily, one at a time, 
using the yield keyword or a generator expression. It doesn’t store all values in memory, making it memory-efficient.

Q2: How is a generator different from a list?
A: Generators generate values on the fly, consuming less memory, while lists store all elements in memory.
Example:
```
# List
numbers = [x ** 2 for x in range(1000)]  # Consumes memory
# Generator
numbers_gen = (x ** 2 for x in range(1000))  # Memory-efficient
```
Q3: When would you use a generator in a data science pipeline?
A: Generators are ideal for:
   - Processing large datasets (e.g., streaming millions of rows).
   - Reading large files line by line.
   - Generating sequences like Fibonacci or random numbers.

Q4: Can you iterate over a generator more than once?
A: No, generators are consumed after one iteration. To reuse the data, you’d need to recreate the generator or store the results in a list."

Q5: Write a generator for sliding window averages.
A:
```
def sliding_window_average(data, window_size):
    for i in range(len(data) - window_size + 1):
        yield sum(data[i:i + window_size]) / window_size

data = [1, 2, 3, 4, 5]
print(list(sliding_window_average(data, 3)))  # Output: [2.0, 3.0, 4.0]
```

Summary of Key Points
   > What Are Generators?: Functions that use yield or expressions to generate values lazily.
   > Why Use Them?: Memory-efficient for large datasets or infinite sequences.
   > Key Use Cases:
        - Reading large files.
        - Infinite or dynamic data generation.
        - Streaming transformations.
"""
