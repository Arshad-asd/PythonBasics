

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
'''--------------------------------------------------------------------------------------------'''
