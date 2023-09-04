

'''--------------------------------------------------------------------------------------------'''
# 1. Write a Python program to calculate the length of a string.

# Methods 1:

# Using the built-in function len. The built-in function len returns the number of items in a container. 

string = "hello world"
print(len(string))

# Methods 2:

# Using for loop and in operator. A string can be iterated over, directly in a for loop.
# Maintaining a count of the number of iterations will result in the length of the string.

def find_len(string):
    counter = 0
    for i in string:
        counter +=1
    return counter
print(find_len("hello_world"))

# Methods 3:

#Using while loop and Slicing. We slice a string making it shorter by 1 at each iteration will eventually result in an empty string.
#  This is when while loop stops.Maintaining a count of the number of iterations will result in the length of the string. 

def find_len(string):
    counter = 0
    while string[counter:]:
        counter +=1
    return counter
print(find_len("python_world"))

# Methods 4:

# Using string methods join and count. The join method of strings takes in an iterable and returns a string which is the concatenation of the strings in the iterable.
#  The separator between the elements is the original string on which the method is called.
#  Using join and counting the joined string in the original string will also result in the length of the string. 

def find_len(string):
    if not string:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(string)).count(some_random_str) + 1
print(find_len("hi_all"))

# Methods 5:

# Using reduce method.
#  Reduce method is used to iterate over the string and return a result of collection element provided to the reduce function.
#  We will iterate over the string character by character and count 1 to result each time. 

import functools
def find_len(string):
    return functools.reduce(lambda x,y: x+1, string, 0)
print(find_len("welcome_all_this_word"))

# Methods 6:

#Using sum() and list comprehension function.
#  We use list comprehension for iterating over the string and sum function to sum total characters in string 

def find_len(string):
    return sum( 1 for i in string )
print(find_len("django"))

# Methods 7:

# Using enumerate function

string ="abc"
c =0
for i,cha in enumerate(string):
    c +=1
print(c)

'''--------------------------------------------------------------------------------------------'''
