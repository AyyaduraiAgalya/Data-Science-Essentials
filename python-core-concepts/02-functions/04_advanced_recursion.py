"""
What Is Recursion?
Recursion occurs when a function calls itself to solve smaller instances of the same problem.
It’s often used for problems that can be broken into smaller sub problems of the same type.

Key Components of a Recursive Function
 > Base Case:
   The condition that stops the recursion to prevent infinite calls.
   Without this, recursion can lead to a stack overflow error.
 > Recursive Case:
   The part where the function calls itself with a smaller problem.
"""
# Recursion Example 1 - Factorial
def factorial(n):
    if n == 0: # Base case
        return 1
    else: # Recursive case
        return n * factorial(n-1)
print(factorial(3))

"""-----------------------------------------------------------------------------------------------------------------"""
"""
Real-World Use Cases in Data Science
 > Parsing Hierarchical Data:
   E.g., Traversing nested JSON files or XML structures.
 > Tree Traversal:
   Used in decision trees, random forests, or hierarchical clustering.
 > Divide-and-Conquer Algorithms:
   QuickSort, MergeSort, etc.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
# Recursion Example 2 - Fibonacci Sequence
# Generating the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10)) # Output is 55 - the 10th fibonacci number
"""-----------------------------------------------------------------------------------------------------------------"""
# Recursion Example 3 - Sum of a list
def sum_of_a_list(data):
    if len(data) == 0:
        return 0
    else:
        return data[0] + sum_of_a_list(data[1:])
print(sum_of_a_list([1,2,3,4]))
"""-----------------------------------------------------------------------------------------------------------------"""
# Recursion Example 4: Parsing Nested Data
# Parsing a nested dictionary to extract all keys.
def extract_keys(data):
    keys =[]
    for key, value in data.items():
        keys.append(key)
        if isinstance(value, dict): # Recursive Case
            keys.extend(extract_keys(value))
    return keys
nested_data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3, "f": 4}},
    "g": 5
}
print(extract_keys(nested_data))
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Q1: What is recursion, and how does it work in Python?
A:
Recursion is when a function calls itself to solve smaller parts of the same problem. It requires:
- A base case to terminate recursion.
- A recursive case to break the problem into smaller subproblems.

Q2: How do you identify a problem that can be solved using recursion?
A:"Recursion is ideal for problems that:
Can be divided into smaller subproblems.
Have a natural base case (e.g., reaching an empty list or hitting a tree leaf). 
Examples include traversing trees, parsing nested data, and implementing divide-and-conquer algorithms.

Q3: What are the pros and cons of recursion?
A:
Pros:
Elegant and concise for hierarchical or divide-and-conquer problems.
Avoids complex manual stack management.
Cons:
May lead to stack overflow for large inputs.
Can be slower than iterative solutions due to repeated function calls.

Q4: How is recursion used in data science workflows?
A:
Recursion is useful in:
Tree traversal: For decision trees or random forests.
Parsing nested data: E.g., JSON or XML parsing.
Dynamic programming: Solving problems like Fibonacci or knapsack by caching results.

Q5: Can you compare recursion to iteration?
A:
Recursion:
Solves problems by breaking them into smaller subproblems.
May lead to stack overflow without a base case.
Iteration:
Uses loops (for or while) to repeat operations.
Generally more memory-efficient.
Example:
```
# Recursive
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
"""
"""-----------------------------------------------------------------------------------------------------------------"""
# Advanced Recursion Example: Memoization
# Use memoization to improve recursive performance by storing intermediate results.
def fibonacci_memo(n, memo={}):
    if n in memo: # check cache
        return memo[n]
    if n <= 1: # base case
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo) # cache result
    return memo[n]
print(fibonacci_memo(50))

"""
Q: How can you optimize recursive functions?
A: Using memoization to store intermediate results, reducing redundant calculations.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Key Takeaways for Recursion
- Always define a base case to terminate recursion.
- Use recursion for problems with hierarchical structure (e.g., trees, nested lists).
- Optimise recursion with memoization or consider iterative solutions when performance is critical.
"""