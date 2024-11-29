"""
Core Basic OOP Concepts to Cover
 > Classes and Objects
 > Instance Variables and Methods
 > The __init__ Constructor
 > The self Keyword
 > Basic Real-World Applications
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Concept 1: Classes and Objects
Definition
 - A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that objects of the class will have.
 - An object is an instance of a class that contains the data and behaviors defined by the class.
Why It Matters in Data Science
 - Reusability: Classes allow you to encapsulate preprocessing steps or feature engineering tasks, making your code modular and reusable.
 - Modularity: ML models or pipelines can be represented as objects, encapsulating all relevant methods (train, predict, evaluate).

"""
# Example - Creating a Feature Engineering Class
class FeatureScaler:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def scale(self, value):
        return (value - self.mean) / self.std
scaler = FeatureScaler(mean=10, std=2)
scaled_value = scaler.scale(14)
print(scaled_value)
print(scaler.mean) # No encapsulation - to understand go through the next concept

"""
What is the difference between a class and an object?
Answer:
A class is a blueprint or template for creating objects.
An object is an instance of a class that contains the actual data and behaviors.

How would you use classes in a data science project?
Answer:
I use classes to create reusable modules for tasks like feature engineering, model training, and evaluation. 
For example, a class can encapsulate methods to scale data, handle missing values, or extract features from text."

How do __init__ and self work in Python classes?
Answer:
__init__ is the constructor method called when an object is created.
self represents the instance of the class, allowing you to access its attributes and methods.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Concept 2: Encapsulation
Definition
 - Encapsulation refers to restricting access to some attributes and methods of a class to protect its integrity.
 - In Python, we use single underscores (_) or double underscores (__) to indicate that an attribute is private.

Why It Matters in Data Science
 - Protects data integrity: Ensures that sensitive or intermediate data within a pipeline (e.g., raw data) cannot be accidentally modified.
 - Makes code easier to debug and maintain by controlling how data is accessed or updated.
"""
"""
A. Banking Application (Account Balance Management)
Scenario: A bank wants to ensure that a user cannot directly modify their account balance.
Encapsulation: The __balance attribute is private, and methods like deposit() and withdraw() control how the balance is updated.
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"You deposited {amount}")
        else:
            print("Not a valid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"You withdrew {amount}")
        else:
            print("Invalid amount entered or You don't have enough money")

    def get_balance(self):
        return self.__balance # Getter method

account = BankAccount(1000)
account.deposit(20)
print(account.get_balance())
account.withdraw(100)
print(account.get_balance())
# Direct access attempt will fail
# print(account.__balance)  # AttributeError

"""
B. Machine Learning Pipeline (Hyperparameter Management)
Scenario: You want to ensure that hyperparameters are initialised properly and not accidentally modified during training.
Encapsulation: Use private attributes for hyperparameters and provide getter and setter methods.
"""
class MLModel:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.__learning_rate = learning_rate
        self.__epochs = epochs
    def get_hyperparameters(self):
        return {"learning_rate": self.__learning_rate, "epochs": self.__epochs}

    def set_hyperparameters(self, learning_rate):
        if 0 < learning_rate <= 1:
            self.__learning_rate = learning_rate
            print(f"Learning rate")
        else:
            print("Invalid")

model = MLModel()
print(model.get_hyperparameters())
model.set_hyperparameters(learning_rate=0.05)
print(model.get_hyperparameters())
model.set_hyperparameters(learning_rate=0) # Output - Invalid
print(model.get_hyperparameters())

"""
C. Data Processing Pipeline (Handling Missing Data)
Scenario: A data processing class should handle missing values without exposing the raw data structure to external code.
Encapsulation: Data cleaning logic is encapsulated, allowing consistent preprocessing across the pipeline.
"""
class DataCleaner:
    def __init__(self, data):
        self.__data = data

    def missing_values(self, value):
        self.__data = [x if x is not None else value for x in self.__data]

    def get_cleaned_data(self):
        return self.__data

data = [1, 0, None, 3, None, 5]
cleaner = DataCleaner(data)
cleaner.missing_values(-1)
print(cleaner.get_cleaned_data())

"""
D. Web Applications (User Authentication)
Scenario: A web application stores user passwords and needs to ensure they are securely hashed and cannot be retrieved directly.
Encapsulation: Store the hashed password as a private attribute and expose authentication methods instead.
"""
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash_password(password)

    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, password):
        return self.__hash_password(password) == self.__password

user = User("John", "PASSWORD")
print(user.authenticate("<PASSWORD>")) # FALSE
print(user.authenticate("PASSWORD")) # TRUE

"""
E. Single underscore - Indicating "Protected" Attributes or Methods
What It Means:
A single underscore indicates that an attribute or method is protected.
It should be used only within the class or its subclasses and not accessed directly by external code.
"""
class BaseClass:
    def __init__(self):
        self._protected_attribute = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

base = BaseClass()
print(base._protected_attribute)
print(base._protected_method())

"""
What is encapsulation, and why is it important?
Answer:
Encapsulation is the practice of restricting access to class attributes and methods, 
ensuring better control over how data is modified and accessed.

How does Python support encapsulation?
Answer:
Python uses single underscores (_) to indicate attributes as protected (convention) 
and double underscores (__) to make attributes private (enforced).

Give an example of encapsulation in a data science pipeline.
Answer:
In a feature engineering class, sensitive information like scaling parameters (mean, standard deviation) 
can be encapsulated to prevent accidental modification.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
Concept 3: Inheritance
Definition
 - Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class).

Why It Matters in Data Science
 - Reusability: Common preprocessing steps can be defined in a parent class, and specific steps can be implemented in child classes.
 - Extensibility: You can extend existing functionality without modifying the base class.
  - Maintainability: Changes in the parent class automatically propagate to child classes, reducing the need for repetitive updates.
"""
# Basic Syntax of inheritance
class Parent:
    def __init__(self, name):
        self.name = name
    def displayName(self):
        print (f"My name is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def displayAge(self):
        print (f"I am {self.age} years old")

child_details = Child("John", 25)
child_details.displayName()
child_details.displayAge()
"""
Key Points:
 - Child inherits attributes (name) and methods (display_name()) from Parent.
 - super().__init__(name) calls the Parent class constructor to initialize name.
 - Child can define its own methods (display_age) and attributes (age).
"""
"""
A. Preprocessing Pipelines
Scenario: You have a generic data preprocessing pipeline, but specific datasets require specialised preprocessing.
"""
class PreProcessor:
    def __init__(self, data):
        self.data = data

    def clean(self):
        self.data = [x for x in self.data if x is not None] # Removes missing values

class TextPreProcessor(PreProcessor):
    def clean(self):
        super().clean() # Calls the parent clean method
        self.data = [x.lower() for x in self.data] # Converts to lowercase

text_data = ["Alice", "BOB", "CHarLIe", None]
preprocessor = TextPreProcessor(text_data)
preprocessor.clean()
print(preprocessor.data)

"""
B. Machine Learning Pipelines
Scenario: You build a base class for machine learning models and extend it for specific algorithms.
"""
class BaseModel:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        return [(x - min(self.data))/(min(self.data) - max(self.data)) for x in self.data] # Min-Max Scaling

    def train(self):
        return NotImplementedError("Subclasses must implement this method")

class LogisticRegressionModel(BaseModel):
    def train(self):
        print("Training Logistic Regression")

class DecisionTreeModel(BaseModel):
    def train(self):
        print("Training Decision Trees")

model = LogisticRegressionModel([10,20, -30, 50, 5, 9.5])
print(model.preprocess())
model.train()

"""
C. ETL Pipelines (Extract, Transform, Load)
Scenario: Extend a base ETL class to process data from different sources.
"""
class ETLBase:
    def __init__(self, source):
        self.source = source

    def extract(self):
        return NotImplementedError("Subclasses must implement this error")

    def transform(self, data):
        return [x*2 for x in data] # Common transformation logic

    def load(self, data):
        print("Loading transformed data ", data)

    def etl_process(self):
        # Complete ETL process: extract -> transform -> load
        raw_data = self.extract()
        transformed_data = self.transform(raw_data)
        self.load(transformed_data)

class CSVETL(ETLBase):
    def extract(self):
        print("Extracting data from CSV: ", self.source)
        return [1,2,3,5] # mock data from csv

class APIETL(ETLBase):
    def extract(self):
        print("Extracting data from API: ", self.source)
        return [4,5,6,7] # mock data from API

csv_etl = CSVETL("data.csv")
csv_etl.etl_process()

api_etl = APIETL("https://api.example.com/data")
api_etl.etl_process()

"""
What is inheritance, and why is it useful?
Answer: Inheritance allows a child class to reuse methods and attributes of a parent class, 
enabling code reuse and extensibility.

How can inheritance be applied to data science projects?
Answer: I use inheritance to create specialised classes for different types of preprocessing. 
For example, a base class might handle data cleaning, while child classes implement specific feature extraction techniques.

What is the difference between super() and overriding a method?
Answer: super() allows a child class to call a method from its parent class, 
while overriding replaces the parent class’s method with a new implementation in the child class.
"""