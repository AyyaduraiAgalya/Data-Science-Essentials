"""
Definition:
A dictionary is an unordered collection of key-value pairs.

Operations:
Access: Retrieve a value using its key.
Add/Modify: Add new key-value pairs or modify existing ones.
Delete: Remove a key-value pair.
"""

# Creating a dictionary of customer transactions
customer_transactions = {"Alice": 8, "Bob": 7, "Charlie": 6}

# Assessing an element
print("Alice's transactions:", customer_transactions["Alice"])

# Adding a new customer
customer_transactions["Lily"] = 2
print("Customers transactions after adding:", customer_transactions)

# Modifying an existing customer's transactions
customer_transactions["Lily"] = 20
print("Customers transactions after modifying:", customer_transactions)

# Deleting a customer
del customer_transactions["Charlie"]
print("Customers transactions after deleting:", customer_transactions)

# Iterating over dictionary items
for customer, transactions in customer_transactions.items():
    print(f"{customer} made {transactions} transaction(s)")

# Merging two dictionaries
customer_transactions_1 = {"Alice": 8, "Bob": 7, "Charlie": 6}
customer_transactions_2 = {"Dwayne": 8, "Dan": 7, "Jack": 9}
merged_customer_transactions = customer_transactions_1 | customer_transactions_2
print(merged_customer_transactions)

"""
1. What are dictionaries in Python, and how do they differ from lists?
Answer: Dictionaries store data as key-value pairs, while lists store ordered collections of items. Access in dictionaries is via keys, making it faster for lookups.
2. How do you merge two dictionaries in Python?
Answer: 
    In Python 3.9+, use the | operator to merge dictionaries
    In earlier versions, use update() eg. dict1.update(dict2)
"""

"""
LISTS VERSUS DICTIONARIES
Why It Matters in Data Science
Lists:
-Use when you need ordered data or perform iterative computations.
-Avoid searching large lists frequently, as it’s slow (O(n)).

Dictionaries:
-Ideal for fast lookups and storing mappings (e.g., customer IDs to transactions).
-For large datasets, dictionaries outperform lists for accessing or updating elements.

"""