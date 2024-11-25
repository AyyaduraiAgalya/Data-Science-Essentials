"""
Definition:
Sets are unordered collections of unique elements.
Operations:
Union (|): Combine all unique elements from two sets.
Intersection (&): Find common elements between sets.
Difference (-): Find elements in one set but not the other.
Subset Check (<=): Check if one set is a subset of another.
"""
# Create two sets of products
set_a = {"apple", "banana", "cherry", "cherry"} # even if "cherry" is duplicated the set returns only one "cherry"
set_b = {"dog", "cat", "elephant", "cherry"}
print(f"Set a is: {set_a}")
print(f"Set b is: {set_b}")

# Union - Combine all unique elements from two sets.
set_union = set_a | set_b
print(f"Set union: {set_union}")

# Intersection - Find common elements between sets.
set_intersection = set_a & set_b
print(f"Set intersection: {set_intersection}")

# Difference - Find elements in one set but not the other.
set_difference = set_a - set_b
print(f"Set difference: {set_difference}")

# Subset check - Check if one set is a subset of another.
set_c = {"apple", "cherry"}
subset_check = set_c <= set_a
print(f"Subset Check is: {subset_check}")
subset_check = set_c <= set_b
print(f"Subset Check is: {subset_check}")

# Removing duplicates from a list using a set
product_list = ["apple", "banana", "cherry", "banana"]
unique_products = set(product_list)
print(f"Unique products: {unique_products}")


"""
1. What are sets in Python, and how do they differ from lists?
Answer: Sets are unordered collections of unique elements, whereas lists can have duplicates and maintain order.
2. How would you remove duplicates from a list using a set?
Answer: Convert the list to a set:
``` product_list = ["apple", "banana", "apple", "date"]
    unique_products = set(product_list)
    print(unique_products)
```
3. What are sets in Python, and how do they differ from lists?
Answer: Sets are unordered collections of unique elements, while lists allow duplicates and maintain order.
Use Case:
Deduplicating data:
```
    data = [1, 2, 2, 3, 3, 3]
    unique_data = set(data)
    print(unique_data)  # Output: {1, 2, 3}
```
4. How would you remove duplicates from a list using a set?
Answer: Convert the list to a set, then back to a list (if ordering doesn’t matter):
```
    data = [1, 2, 2, 3]
    unique_data = list(set(data))
    print(unique_data)  # Output: [1, 2, 3]
```

5.How would you remove duplicates from a list while maintaining order?
```
    data = [1, 2, 2, 3]
    deduplicated = []
    for item in data:
        if item not in deduplicated:
            deduplicated.append(item)
    print(deduplicated)  # Output: [1, 2, 3]
```
"""