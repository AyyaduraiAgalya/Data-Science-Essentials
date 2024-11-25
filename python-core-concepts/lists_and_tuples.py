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

"""
Interview Questions
What are the key differences between lists and tuples in Python?
Answer: Lists are mutable, meaning their contents can be modified, whereas tuples are immutable, meaning their contents cannot be changed once created.
When would you use a tuple over a list?
Answer: Use tuples when you need a fixed collection of elements, such as coordinates or dictionary keys.
"""