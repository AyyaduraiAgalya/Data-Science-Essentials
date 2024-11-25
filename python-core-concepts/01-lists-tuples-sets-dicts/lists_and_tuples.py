"""
Differences:
Lists are mutable (elements can be added, removed, or changed).
Tuples are immutable (once created, their content cannot be changed).
"""

# List Example
shopping_list = ["apple", "banana", "blueberries"]
shopping_list.append("dates") # Adding an item
print(f"Appended list: {shopping_list}")
shopping_list[1] = "oranges" # Modifying an item
print(f"Modified list: {shopping_list}")
shopping_list.remove("dates")
print(f"Modified list after removing: {shopping_list}")

# Tuple Example
coordinates = (10.5, 20.3)
#coordinates[0] = 10.75 #Uncommenting this line will throw a TypeError: 'tuple' object does not support item assignment
print(f"Coordinates: {coordinates}")

# Using tuples as keys in a dictionary
location_map = {(10.5, 20.3): "Work", (10.3, 20.5): "Home"}
print(f"Location Map: {location_map}")

# Filtering data dynamically
data = [10, 20, 30, 40, 50]
filter_data = [x for x in data if x > 25]
print(f"Filtered data: {filter_data}")

# Modifying all data in the list
data = [10, 20, 30, 40, 50]
modified_data = [x/2 for x in data if x>25]
print(f"Modified data: {modified_data}")

"""
1. What are the key differences between lists and tuples in Python?
Answer: Lists are mutable, meaning their contents can be modified, whereas tuples are immutable, meaning their contents cannot be changed once created.
2. When would you use a tuple over a list?
Answer: Use tuples when you need a fixed collection of elements, such as coordinates or dictionary keys.
3. When would you use a list instead of a tuple in a data science pipeline?
Answer:
Use lists when:
    Data will change during the pipeline (e.g., adding, removing, or modifying values).
    You need dynamic collections for iterative computations (e.g., storing intermediate results).
Use tuples when:
    Data must remain constant, like coordinates or feature names for a model.
4. Why are tuples immutable, and how is this useful in certain data scenarios?
Answer:
Tuples are immutable to ensure:
    Data integrity: Prevent accidental changes (e.g., geographic coordinates, model parameters).
    Performance: Tuples are faster than lists for lookups and iteration.
    Use Case: Tuples can be used as keys in dictionaries, as they are hashable:
```
    data_map = {(10, 20): "Location A", (30, 40): "Location B"}
    print(data_map[(10, 20)])  # Output: Location A
```
"""

