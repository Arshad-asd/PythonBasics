

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

                                  # Ways to split a string in different ways

# 01 : Python code to split string in substring manner
# Methods 1:  Using Iteration 

def split_string(string):
    split_string = string.split('_')
    result = []
    for i in range(len(split_string)):
        temp = split_string[:i+1]
        temp = "_".join(temp)
        result.append(temp)
    return result
print(split_string("hello_digital_world"))

'''--------------------------------------------------------------------------------------------'''
# letters A-Z is 65-90, and the range for lowercase letters a-z is 97-122.
s = 'helo world digital india'
lists = s.split()
res = ''
for i in range(len(lists)):
    if ord(lists[i][0])>=97 and ord(lists[i][0])<=122:
        res += chr(ord(lists[i][0])-32)
    res += lists[i][1:]
    res += " "
    
print(res)
'''--------------------------------------------------------------------------------------------'''
                                                          #Reverse string

s= 'kerala'

#Method 1: Using slice
reverse = s[::-1]

#Method 2: Using loop
i = len(s)-1
reverse = ''
while i >=0:
   reverse += s[i]
   i -=1
print(reverse)

#Method 3: using Recursion
def reverse_string(string):
    if len(string) <= 1:
        return string
    return reverse_string(string[1:])+string[0]
string = 'arshad'
print(string)
print(reverse_string(string))
'''--------------------------------------------------------------------------------------------'''
#Find is plaindrome or not
#Method 1: Using slice
s = 'malayalam'
def is_pailndrome(s:str):
    return True if s == s[::-1] else False

#Method 2 : Using Loop
def is_pailndrome(s:str):
    res = ''
    for i in range(len(s)-1,0,-1):
        res += s[i]
    res += s[-1]
    return True if res == s else False

#Method 3 : Using Recursive
def is_pailndrome(s:str):
    if len(s) <=1:
        return True
    if s[0] == s[-1]:
        return is_pailndrome(s[1:-1])
    else:
        return False

#Remove Palidromic words
s = 'malayalam hello radar world not level'
def is_pailndrome(s:str):
    new = s.split(' ')
    for i in range(len(new)-1,-1,-1):
        if new[i] == new[i][::-1]:
            new.remove(new[i])
    return ' '.join(new)
