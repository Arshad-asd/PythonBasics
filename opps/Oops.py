#========================================================================OOP'S Concept===============================================================================


#<-----------------------------------------------------------------------Attributes-Start---------------------------------------------------------------------------->
'''
Attributes are variables that belong to a class. They can hold data relevant to the objects of the class.

1.Instance Attributes: These are specific to each instance of the class.

2.Class Attributes: These are shared by all instances of the class.
'''

class Person:
    species = 'Homo sapiens'  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

#<-----------------------------------------------------------------------Attributes-End------------------------------------------------------------------------------->

#<-----------------------------------------------------------------------Methods-Start-------------------------------------------------------------------------------->
'''
Methods are functions defined within a class that operate on the class's instances.

1.Instance Methods: These take self as the first parameter and can modify the object's state.

2.Class Methods: These take cls as the first parameter and can modify the class state.

3.Static Methods: These do not take self or cls as the first parameter and cannot modify the object or class state.
'''

class Person:
    species = 'Homo sapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}')

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    @staticmethod
    def is_adult(age):
        return age >= 18
#<-----------------------------------------------------------------------Methods-Start-------------------------------------------------------------------------------->

#<-----------------------------------------------------------------------Constructors and Destructors-Start----------------------------------------------------------->
'''
Constructor (__init__): A special method called when an instance of the class is created.

Destructor (__del__): A special method called when an instance of the class is about to be destroyed.
'''

class Person:
    def __init__(self, name, age): #Constructor
        self.name = name
        self.age = age

    def __del__(self):  #Destructor
        print(f'{self.name} is being deleted')
#<-----------------------------------------------------------------------Constructors and Destructors-End------------------------------------------------------------->

#<-----------------------------------------------------------------------Properties-Start----------------------------------------------------------------------------->
'''
Properties provide a way of customizing access to instance attributes.
Using @property

'''

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

#<-----------------------------------------------------------------------Properties-End----------------------------------------------------------------------------->

#<-----------------------------------------------------------------------Magic Methods (Dunder Methods)-Start-------------------------------------------------------->
'''
These are special methods with double underscores at the beginning and end of their names. They allow customization of behavior for built-in operations.

Example :- __str__ and __repr__: For string representation, __eq__: For equality comparison.

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
#<-----------------------------------------------------------------------Magic Methods (Dunder Methods)-End----------------------------------------------------------->

#<-----------------------------------------------------------------------Accesfires-(access modifiers)-Start---------------------------------------------------------->
'''
In Python, access specifiers (or access modifiers) are used to define the visibility and accessibility of class members (attributes and methods).
Unlike some other programming languages, Python does not have explicit access specifiers like public, protected, and private. 
Instead, it relies on naming conventions and a few language features to suggest how variables and methods should be accessed.

1. Public
Description: Members are accessible from anywhere.
Convention: No leading underscore.

2. Protected
Description: Members are accessible within the class and its subclasses.
Convention: Single leading underscore (_).

3. Private
Description: Members are not accessible outside the class. However, they can be accessed within the class using name mangling.
Convention: Double leading underscores (__).

Use of Access Specifiers:-
* Encapsulation: They help in encapsulating the data within a class and exposing only what is necessary. 
  This is critical for maintaining the integrity and security of the data.
* Control: Provide control over how the class members are accessed and modified.
* Code Maintenance: Makes it easier to change the implementation of a class without affecting its external interface.

'''
class MyBaseClass:
    static_var = 10  # Static variable or class variable

    _protected_var = 10  # Protected variable

    def _protected_method(self):
        print("Protected method")
    
    __private_var = 10  # Private variable

    def __private_method(self):
        print("Private method")

    def access_private(self):
        print(self.__private_var)
        self.__private_method()

class MySubClass(MyBaseClass):
    def access_protected(self):
        print(self._protected_var)
        self._protected_method()

obj = MySubClass()
obj.access_protected()  # Accessing protected variable and method
obj.access_private() # Accessing private variable and method using name mangling

#<-----------------------------------------------------------------------Accesfires-(access modifiers)-End------------------------------------------------------------>

#<----------------------------------------------------------------------Inheritance----------------------------------------------------------------------------------->

'''
Inheritance allows us to define a class that inherits all the attributes and method from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Use of Inheritance:-
* Code Reusability: Allows the reuse of code by inheriting attributes and methods from the parent class.
* Modularity: Encourages a modular approach to programming where classes can be designed and maintained separately.
* Extensibility: New functionalities can be added to existing classes without modifying the original class.
* Polymorphism: Enables the use of polymorphism, where methods can be overridden in the subclass to provide specific implementations.

Types of Inheritance in Python:-

1.Single Inheritance: A subclass inherits from a single superclass.

2.Multiple Inheritance: A subclass inherits from more than one superclass.

3.Multilevel Inheritance: A subclass inherits from another subclass, creating a chain of inheritance.

4.Hierarchical Inheritance: Multiple subclasses inherit from a single superclass.

5.Hybrid Inheritance: A combination of two or more types of inheritance.
'''
#Single Inheritance
class Parent:
    def method1(self):
        print("This is the parent class.")

class Child(Parent):
    def method2(self):
        print("This is the child class.")

#Multiple Inheritance
class Parent1:
    def method1(self):
        print("This is parent1 class.")

class Parent2:
    def method2(self):
        print("This is parent2 class.")

class Child(Parent1, Parent2):
    def method3(self):
        print("This is the child class.")

#MultiLevel Inheritance
class Grandparent:
    def mehtod1(self):
        print("This is the grandparent class.")

class Parent(Grandparent):
    def method2(self):
        print("This is the parent class.")

class Child(Parent):
    def method3(self):
        print("This is the child class.")

#Hierarchical Inheritance
class Parent:
    def method1(self):
        print("This is the parent class.")

class Child1(Parent):
    def method2(self):
        print("This is the child1 class.")

class Child2(Parent):
    def method3(self):
        print("This is the child2 class.")
#<----------------------------------------------------------------------Inheritance----------------------------------------------------------------------------------->
#<----------------------------------------------------------------------Abstraction--Start--------------------------------------------------------------------------------->
'''
Abstraction in Python is a fundamental concept of object-oriented programming (OOP)that involves hiding the implementation details of a class and exposing only 
the necessary and relevant parts.

Use of Abstraction :-
* Hiding Complexity: Abstraction allows you to hide the complex details of a system and expose only the essential parts, making it easier to understand and use.
* Code Maintenance: By hiding the implementation details, the internal changes can be made without affecting the external code that uses the class.
* Modularity: Abstraction helps in dividing the program into smaller, manageable pieces or modules.
* Security: Abstraction provides a way to secure sensitive data by hiding the implementation details and exposing only the necessary parts.

How to Achieve Abstraction in Python :-
Abstraction in Python is usually achieved through abstract classes and interfaces. An abstract class can be created using the abc module, 
and it can contain one or more abstract methods.An abstract method is a method that is declared, but contains no implementation.

'''
#Using abc module abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
rect = Rectangle(5, 4)
print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 20

circle = Circle(3)
print("Circle Area:", circle.area())  # Output: Circle Area: 28.26

#Simple calss interface concept
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
rect = Rectangle(5, 4)
print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 20

circle = Circle(3)
print("Circle Area:", circle.area())  # Output: Circle Area: 28.26

#Function abstraction
def perform_operation(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        raise ValueError("Unsupported operation")

# Usage
print("Sum:", perform_operation("add", 1, 2, 3))         # Output: Sum: 6
print("Product:", perform_operation("multiply", 2, 3, 4))  # Output: Product: 24


#<----------------------------------------------------------------------Abstraction--End-------------------------------------------------------------------------------->
#<----------------------------------------------------------------------Encapsulation--Start---------------------------------------------------------------------------->

'''
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) 
that operate on the data into a single unit, typically a class.Encapsulation restricts direct access to some of an object's components,
which can prevent the accidental modification of data.

Use of Encapsulation :-
* Data Hiding: By restricting access to the internal state of an object and requiring all interactions to occur through an object's methods, 
  encapsulation helps protect the object's integrity by preventing outside code from directly accessing and modifying internal data.

* Improved Modularity: Encapsulation helps in breaking down a complex system into smaller, 
  more manageable pieces. Each class is a self-contained unit with a clear interface for interacting with it.

* Ease of Maintenance: Changes in one part of the code can be made independently of other parts. Since the internal implementation is hidden, 
  you can modify the internal implementation without affecting the outside code that depends on the class.

* Control Over Data: Encapsulation allows you to control how the data is accessed and modified. For example, 
  you can use getter and setter methods to control the access and modification of an object's attributes.

Achieving Encapsulation in Python :-
In Python, encapsulation can be achieved using the following conventions:

1.Public Attributes: Accessible from anywhere (default behavior).
2.Protected Attributes: Indicated by a single underscore (_). These are meant to be accessed only within the class and its subclasses.
3.Private Attributes: Indicated by a double underscore (__). These are meant to be accessed only within the class itself.

'''
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute

    # Getter method for make
    def get_make(self):
        return self.__make

    # Setter method for make
    def set_make(self, make):
        self.__make = make

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        self.__model = model

    # Getter method for year
    def get_year(self):
        return self.__year

    # Setter method for year
    def set_year(self, year):
        self.__year = year

    def display_info(self):
        print(f"Car: {self.__make} {self.__model}, Year: {self.__year}")
#<----------------------------------------------------------------------Encapsulation--End----------------------------------------------------------------------------->
#<----------------------------------------------------------------------Polymorphism--Start---------------------------------------------------------------------------->
'''
Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
It is a Greek term that means "many shapes" or "many forms."Polymorphism provides a way to perform a single action in different forms.

Use of Polymorphism in Python :-
Polymorphism is used to define methods in the child class that have the same name as the methods in the parent class. 
It is mainly used to achieve the functionality of method overriding. Polymorphism allows for the implementation of elegant, reusable code.

Types of Polymorphism in Python :-
1.Compile-time Polymorphism (Method Overloading):
In Python, method overloading is not supported as it is in some other languages like Java. However, you can achieve a similar effect by using default 
parameters or by checking the types of parameters within the method.

2.Run-time Polymorphism (Method Overriding):
Inheritance allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This is known as method overriding.

3.Duck Typing:
Python uses a concept called "duck typing," which means that the suitability of an object is determined by the presence of certain methods and properties,
rather than the type of the object itself.This allows for more flexible and dynamic code.
'''
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

#<----------------------------------------------------------------------Polymorphism--Start---------------------------------------------------------------------------->

#<----------------------------------------------------------------------Duck Typing----------------------------------------------------------------------------------->

'''
Python uses a concept called "duck typing," which means that the suitability of an object is determined by the presence of certain methods and properties,
rather than the type of the object itself.This allows for more flexible and dynamic code.
'''
class Bird:
    def fly(self):
        return 'Flap Flap!'

class Airplane:
    def fly(self):
        return 'Zoom Zoom!'

def in_the_sky(flier):
    print(flier.fly())

pigeon = Bird()
boeing = Airplane()
in_the_sky(pigeon)
in_the_sky(boeing)

def print_items(iterable):
    for item in iterable:
        print(item)

# Example usage
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)
my_set = {11, 12, 13, 14, 15}

print_items(my_list)   # Output: 1 2 3 4 5
print_items(my_tuple)  # Output: 6 7 8 9 10
print_items(my_set)    # Output: 11 12 13 14 15
#<----------------------------------------------------------------------Duck Typing----------------------------------------------------------------------------------->

#<----------------------------------------------------------------------MRO-Start------------------------------------------------------------------------------------------>

class A:
    def method(self):
        print("Method of class A")

class B(A):
    pass

class C(A):
    def method(self):
        print("Method of class C")

class D(B, C):
    pass

obj_d = D()
obj_d.method()  # Output: Method of class C
#<----------------------------------------------------------------------MRO-End---------------------------------------------------------------------------------------->

#<----------------------------------------------------------------------custom iterators------------------------------------------------------------------------------>

# creating custom iterators using iter and next method
class MyIter:
    def __init__(self,max_val) -> None:
        self.max_val = max_val
        self.current = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.max_val:
            value = self.current
            self.current +=1
            return value
        else:
            raise StopIteration
my_iter  = MyIter(5)
for item in my_iter:
    print(item)

#<----------------------------------------------------------------------custom iterators------------------------------------------------------------------------------>


#<----------------------------------------------------------------------Gnerator-Start---------------------------------------------------------------------------------->

#generator to generate even numbers
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2
even_gen = even_numbers()
for _ in range(5):
    print(next(even_gen))

#generator to generate prime numbers
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_numbers():
    yield 2  # Start by yielding the first prime number
    num = 3
    while True:
        if is_prime(num):
            yield num
        num += 2  # Move to the next odd number

# Example usage:
prime_gen = prime_numbers()
arr = [next(prime_gen) for _ in range(10)]
print(arr)

#<----------------------------------------------------------------------Gnerator-End---------------------------------------------------------------------------------->

#<----------------------------------------------------------------------Decorator------------------------------------------------------------------------------------->
def check_zero(func):
    def wrapper(num):
        if num == 0:
            print('division not postble by 0')
            return 0
        else:
            return func(num)
    return wrapper
@check_zero
def division(num):
    return num //2
result = division(10)
print(result)
#<----------------------------------------------------------------------Decorator------------------------------------------------------------------------------------->


#<----------------------------------------------------------------Print_The_Truth_Table-Start--------------------------------------------------------------------------->
def sum_and_truth_table(*args):
    # Filter out non-numeric arguments and calculate the sum
    total = sum(arg for arg in args if isinstance(arg, (int, float)))
    
    # Generate truth table
    truth_table = [bool(arg) for arg in args]

    return total, truth_table

total, truth_table = sum_and_truth_table(1, 0, "", "Hello", None)
print("Total:", total)                
print("Truth Table:", truth_table)     

#<----------------------------------------------------------------Print_The_Truth_Table-End--------------------------------------------------------------------------->

#<------------------------------------------------------------------function to generate 6 digit_otp--Start------------------------------------------------------------>
import random
gen_otp = lambda :''.join(random.choices('123456',k=6))
otp = gen_otp()
print(otp)
#<------------------------------------------------------------------function to generate 6 digit_otp--End------------------------------------------------------------>

#<-------------------------------------------------------------------How-Find-Refernce_count--Start-------------------------------------------------------------------->

import sys

a = [1, 2, 3]
ref_count = sys.getrefcount(a)
print(ref_count)

#<-------------------------------------------------------------------How-Find-Refernce_count-End---------------------------------------------------------------------->
#<-------------------------------------------------------------------Shalow_Copy_Deep_Copy--start----------------------------------------------------------------------->

import copy

original_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Creating a shallow copy
'''
Shallow copy: Copies the top-level structure of the original object and inserts references to the nested objects.
In the example above, modifying shallow_copy also modifies original_list because the nested lists inside original_list are referenced in shallow_copy
'''
shallow_copy = copy.copy(original_list1)

shallow_copy[0][0] = 100

print("Original list after shallow copy modification:", original_list1)
print("Shallow copy:", shallow_copy)


original_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Creating a deep copy
'''
Deep copy: Recursively copies the original object and all its nested objects.
In this example, modifying deep_copy does not affect original_list because deepcopy() creates a new independent copy of each nested list.

'''
deep_copy = copy.deepcopy(original_list2)

deep_copy[0][0] = 100

print("Original list after deep copy modification:", original_list2)
print("Deep copy:", deep_copy)

#<-------------------------------------------------------------------Shalow_Copy_Deep_Copy--start----------------------------------------------------------------------->

#<-------------------------------------------------------------------Packing_Unpacking--Start-------------------------------------------------------------------------->
# Packing into a tuple
packed_tuple = 1, 2, 3, 4, 5
print(packed_tuple)  # Output: (1, 2, 3, 4, 5)

# Packing into a list
packed_list = [10, 20, 30, 40, 50]
print(packed_list)  # Output: [10, 20, 30, 40, 50]

# Unpacking a tuple
a, b, c = packed_tuple
print(a, b, c)  # Output: 1 2 3

# Unpacking a list
x, y, z = packed_list
print(x, y, z)  # Output: 10 20 30

# Unpacking with *
first, *middle, last = packed_tuple
print(first)     # Output: 1
print(middle)    # Output: [2, 3, 4]
print(last)      # Output: 5

# Unpacking with *
start, *rest, end = packed_list
print(start)     # Output: 10
print(rest)      # Output: [20, 30, 40]
print(end)       # Output: 50

#<-------------------------------------------------------------------Packing_Unpacking--End-------------------------------------------------------------------------->
