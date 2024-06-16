
#========================================================================BuiltIn-Methods==Start===========================================================================

#<-----------------------------------------------------------------------Object Initialization and Destruction-------------------------------------------------------->
class Person:
    def __init__(self, name, age):  # Called when a new instance is created.
        self.name = name
        self.age = age
        print(f'Person {self.name}, {self.age} years old, has been created.')

    def __del__(self):  #Called when an instance is about to be destroyed.
        print(f'Person {self.name}, {self.age} years old, has been deleted.')
    
#<-----------------------------------------------------------------------Object Representation----------------------------------------------------------------------->
    def __str__(self):  #Defines the “informal” string representation of an object (used by str() and print()).
        return f'{self.name}, {self.age} years old'

    def __repr__(self):  #Defines the “official” string representation of an object (used by repr()).
        return f'ExampleClass(name={self.name!r}, age={self.age!r})'
#<-----------------------------------------------------------------------Attribute Access---------------------------------------------------------------------------->
    def __getattr__(self, name):  #Called when an attribute is accessed that doesn't exist.
        print(f'__getattr__ method called for attribute {name}')
        raise AttributeError(f"'Person' object has no attribute '{name}'")

    def __getattribute__(self, name):  #Called for every attribute access.
        print(f'__getattribute__ method called for attribute {name}')
        return super().__getattribute__(name)

    def __setattr__(self, name, value):  #Called when an attribute assignment is attempted.
        print(f'__setattr__ method called for attribute {name}')
        super().__setattr__(name, value)

    def __delattr__(self, name):  # Called when an attribute deletion is attempted
        print(f'__delattr__ method called for attribute {name}')
        super().__delattr__(name)

#<-----------------------------------------------------------------------Item Access--------------------------------------------------------------------------------->
    def __getitem__(self, key):  # Called to retrieve an item using the self[key] syntax
            print(f'__getitem__ method called for key {key}')
            return self.skills.get(key, None)

    def __setitem__(self, key, value):  # Called to set an item using the self[key] = value syntax.
        print(f'__setitem__ method called for key {key} with value {value}')
        self.skills[key] = value

    def __delitem__(self, key):  #Called to delete an item using the del self[key] syntax.
        print(f'__delitem__ method called for key {key}')
        if key in self.skills:
            del self.skills[key]
#<-----------------------------------------------------------------------Iteration----------------------------------------------------------------------------------->
    def __iter__(self):  #Returns the iterator object itself.
        print('__iter__ method called')
        self.iter_skills = iter(self.skills)
        return self.iter_skills

    def __next__(self):  #Returns the next item from the iterator.
        print('__next__ method called')
        return next(self.iter_skills)
#<-----------------------------------------------------------------------Context Management----------------------------------------------------------------------------------->
    def __enter__(self):  # Called when entering a context (used with with statements).
        print('__enter__ method called')
        return self

    def __exit__(self, exc_type, exc_value, traceback): # Makes an instance callable like a function.
        print('__exit__ method called')
        if exc_type:
            print(f'Exiting with exception: {exc_type}')
#<-----------------------------------------------------------------------Callable Objects----------------------------------------------------------------------------------->
    def __call__(self, *args, **kwargs):  # Makes an instance callable like a function.
        print('__call__ method called')
        return f'{self.name} is {self.age} years old'

#========================================================================BuiltIn-Methods=End===========================================================================
