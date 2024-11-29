"""
Intermediate OOP Concepts covers:

 > Polymorphism
 > Abstraction
 > Method Overloading (Pythonic approach using *args and **kwargs)
 > Property Decorators
"""

"""
1. Polymorphism
Definition
 - Polymorphism allows objects of different classes to be treated as objects of a common superclass.
 - A single interface can perform different implementations based on the object.
Example
 - Different types of ML models (LogisticRegression, RandomForest) share a common interface (fit, predict).
"""
"""
A. Creating a Model interface and implement it for LinearRegressionModel and DecisionTreeModel.
"""
class Model:
    def fit(self, data):
        raise NotImplementedError("Subclasses must import this method")

    def predict(self, data):
        raise NotImplementedError("Subclasses must import this method")

class LinearRegressionModel(Model):
    def fit(self, data):
        print(f"Fitting Linear Regression on {data}")

    def predict(self,data):
        return [x*2 for x in data]

class DecisionTreeModel(Model):
    def fit(self,data):
        print(f"Fitting Decision Tree on {data}")

    def predict(self, data):
        return [x ** 2 for x in data]

models = [LinearRegressionModel(), DecisionTreeModel()]
for model in models:
    model.fit([1,2,3])
    print(model.predict([1,2,3]))

"""
Real-World Relevance for Data Scientists
Unified Interfaces:
Enables the creation of reusable pipelines where any model can be swapped without changing the pipeline structure.

ETL Pipelines:
Different data sources (CSV, API) can share the same interface while implementing extraction differently.
"""
"""
Q: What is polymorphism in Python?
Answer: Polymorphism allows a single interface (e.g., a method name) to have different implementations 
depending on the object or class. It supports flexible and reusable code.

Q: How is polymorphism useful in data science workflows?
Answer: Polymorphism allows multiple models (e.g., LinearRegression, RandomForest) to implement the 
same interface (e.g., fit, predict). This simplifies model selection and integration into pipelines.

Q: How would you implement polymorphism in Python?
Answer: By creating a base class with abstract methods and implementing those methods in subclasses. 
Example: Model base class with fit and predict methods.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
2. Abstraction: 
Definition
 - Abstraction hides the implementation details of a class and exposes only the essential interface.
 - Achieved using abstract classes (via abc module).
"""
"""
Example: Abstract Base Class for ETL Pipelines
Scenario: Creating a standardised ETL pipeline for handling different data sources.
1. Abstract Base Class (ETLBase): Defines the extract, transform, and load methods that every data source must implement.
2. Subclasses: Implement the abstract methods for specific data sources like CSVETL and APIETL.
"""
from abc import ABC, abstractmethod
class ETLBase(ABC):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass

class CSVETL(ETLBase):
    def extract(self):
        print(f"Extracting data from {self.source}")
        return [1,2,3] # mock data from csv
    def transform(self, data):
        print(f"Transforming data: scaling by 2")
        return [x * 2 for x in data]

    def load(self, data):
        print(f"loading transformed data: {data}")

class APIETL(ETLBase):
    def extract(self):
        print(f"Extracting data from API endpoint: {self.source}")
        return [4, 5, 6]  # Simulated data from API

    def transform(self, data):
        print("Transforming data: Adding 10")
        return [x + 10 for x in data]

    def load(self, data):
        print(f"Loading transformed data: {data}")

print("CSV Pipeline:")
csv_pipeline = CSVETL("data.csv")
data = csv_pipeline.extract()
print(data)
transformed_data = csv_pipeline.transform(data)
csv_pipeline.load(transformed_data)

print("API Pipeline:")
api_pipeline = APIETL("https://api.example.com/data")
data = api_pipeline.extract()
print(data)
transformed_data = api_pipeline.transform(data)
api_pipeline.load(transformed_data)

"""
Real-World Relevance for Data Scientists
Standardised Workflows:
 - Abstract base classes enforce a consistent interface for ETL or ML pipelines.
 - Makes the code modular and extensible.
Error Prevention:
 - Ensures all subclasses implement essential methods like extract, transform, and load.

Q:What is abstraction in Python?
Answer: Abstraction hides implementation details and provides a blueprint using abstract classes or methods.

Q:How does abstraction help in real-world data science?
Answer: It standardises workflows, ensuring all pipeline components (e.g., Preprocessor, ETL) implement required methods consistently.

Q:How do you implement abstraction in Python?
Answer: Using the abc module to define abstract base classes with @abstractmethod decorators.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
3. Method Overloading
Definition - In Python, method overloading isn’t supported directly but can be simulated using:
 - Default arguments.
 - Variable-length arguments (*args, **kwargs).
"""
"""
Example: Creating a function that preprocesses data differently based on the number of arguments.
"""
class dataPreprocessor:
    def process(self, *args):
        if len(args) == 1:
            print(f"Processing single dataset: {args[0]}")
        elif len(args) > 1:
            print(f"Processing multiple datasets: {args}")
        else:
            print(f"No dataset provided")

processor = dataPreprocessor()
processor.process([1,2,3])
processor.process([1,2,3], [4,5,6])
processor.process()

"""
Real-World Relevance for Data Scientists
Flexible Functionality:
 - Allows methods to handle diverse inputs (e.g., single dataset vs. multiple datasets).
 - Reduces redundant code for methods with similar logic.
"""
"""
Q: Does Python support method overloading?
Answer: Python doesn’t support method overloading directly. It can be implemented using default or 
variable-length arguments (*args, **kwargs).

Q: How is method overloading useful in data science?
Answer: It allows flexibility in handling different data structures or configurations, such as preprocessing single 
or multiple datasets.
"""
"""-----------------------------------------------------------------------------------------------------------------"""
"""
4. Property Decorators
Definition
 - @property is used to create read-only attributes or computed properties in Python.
 - @property can replace getter methods.
"""
"""
Example: Computing the mean of data dynamically using a property.
"""
class DataStats:
    def __init__(self, data):
        self.data = data

    @property
    def mean(self):
        return sum(self.data) / len(self.data)

stats = DataStats([1,2,3,5,6])
print(stats.mean)

"""
Real-World Relevance for Data Scientists
 - Dynamic Statistics:
   Use properties for computed values like mean, median, or standard deviation.
 - Encapsulation:
   Hides the calculation logic behind simple attribute access.


Q: What is the @property decorator?
Answer: It’s used to create computed attributes in a class, allowing method-like behaviour with attribute-style access.

Q: How is @property useful in data science?
Answer: It simplifies access to computed metrics like mean, variance, or model accuracy.
"""
"""-----------------------------------------------------------------------------------------------------------------"""