#===========================================================String_Wrokouts==Start===========================================================================================
'''
A string in Python is a sequence of characters enclosed in single, double, or triple quotes.
Strings are immutable, meaning that once they are created, their content cannot be changed.

Use of String Data Type :-
1.Text Manipulation:
Strings are widely used for text manipulation, including tasks like searching, slicing, and concatenating text.

2.Data Storage:
Strings are used to store data such as names, addresses, and descriptions in databases and files.

3.Input and Output:
Strings are essential for handling user input and displaying output.

4.File Operations:
Strings are used to read from and write to files.

5.String Formatting:
Formatting strings is crucial for creating well-structured output and reports.

6.Regular Expressions:
Strings are used in conjunction with regular expressions for pattern matching and validation tasks.

Built-in Methods for Strings :-
upper(): Converts all characters to uppercase.
lower(): Converts all characters to lowercase.
strip(): Removes leading and trailing whitespace.
replace(): Replaces a substring with another substring.
find(): Finds the first occurrence of a substring.
split(): Splits the string into a list based on a delimiter.
join(): Joins a list of strings into a single string with a delimiter.

capitalize(): Capitalizes the first character of the string.
casefold(): Converts string to lowercase.
center(width, [fillchar]): Centers the string within a specified width.
count(sub, [start, end]): Counts occurrences of a substring.
encode([encoding, errors]): Encodes the string.
endswith(suffix, [start, end]): Checks if the string ends with the specified suffix.
expandtabs([tabsize]): Expands tabs to spaces.
find(sub, [start, end]): Finds the first occurrence of a substring.
format(*args, **kwargs): Formats the string.
format_map(mapping): Formats the string using a dictionary.
index(sub, [start, end]): Finds the first occurrence of a substring (raises ValueError if not found).
isalnum(): Checks if all characters are alphanumeric.
isalpha(): Checks if all characters are alphabetic.
isascii(): Checks if all characters are ASCII.
isdecimal(): Checks if all characters are decimal.
isdigit(): Checks if all characters are digits.
isidentifier(): Checks if the string is a valid identifier.
islower(): Checks if all characters are lowercase.
isnumeric(): Checks if all characters are numeric.
isprintable(): Checks if all characters are printable.
isspace(): Checks if all characters are whitespace.
istitle(): Checks if the string is in title case.
isupper(): Checks if all characters are uppercase.
ljust(width, [fillchar]): Left-justifies the string within a specified width.
lstrip([chars]): Strips leading characters.
maketrans(x[, y[, z]]): Returns a translation table.
partition(sep): Partitions the string into a tuple.
removeprefix(prefix): Removes the specified prefix.
removesuffix(suffix): Removes the specified suffix.
rfind(sub, [start, end]): Finds the last occurrence of a substring.
rindex(sub, [start, end]): Finds the last occurrence of a substring (raises ValueError if not found).
rjust(width, [fillchar]): Right-justifies the string within a specified width.
rpartition(sep): Partitions the string into a tuple from the right.
rsplit(sep, [maxsplit]): Splits the string from the right.
rstrip([chars]): Strips trailing characters.
splitlines([keepends]): Splits the string at line breaks.

'''

#<----------------------------------------------------------Ways to split a string in different ways-start------------------------------------------------------------->

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

#<----------------------------------------------------------Ways to split a string in different ways-End------------------------------------------------------------->

#<----------------------------------------------------------Each_word_first_letter_to_capital-start------------------------------------------------------------------>
s = 'helo world digital india'
lists = s.split()
res = ''
for i in range(len(lists)):
    if ord(lists[i][0])>=97 and ord(lists[i][0])<=122:
        res += chr(ord(lists[i][0])-32)
    res += lists[i][1:]
    res += " "
    
print(res)
#<----------------------------------------------------------Each_word_first_letter_to_capital-End-------------------------------------------------------------------->
#<----------------------------------------------------------Reverse_word-start--------------------------------------------------------------------------------------->

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
#<----------------------------------------------------------Reverse_word-End--------------------------------------------------------------------------------------->
#<----------------------------------------------------------Word_is_plaindrome_or_not-start------------------------------------------------------------------------->

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
#<----------------------------------------------------------Word_is_plaindrome_or_not-End------------------------------------------------------------------------->

#<----------------------------------------------------------concatenate_words-start------------------------------------------------------------------------------->

# join two string using + operator
string1 = "hello"
string2 = "wrold"
def join_string(string1,string2):
    result = string1 + " " + string2
    return result

# join two string using join method
def join_strings(string1,string2):
    result = " ".join([string1,string2])
    return result

#<----------------------------------------------------------concatenate_words-End-------------------------------------------------------------------------------->

#<----------------------------------------------------------white_spaces_remove_given_string-start------------------------------------------------------------------------------->

string_with_spaces = "Hello   World\t\nPython"
result = ''.join(char for char in string_with_spaces if not char.isspace())
print('reomve space :',result)

#<----------------------------------------------------------white_spaces_remove_given_string-End------------------------------------------------------------------------------->

#<----------------------------------------------------------Convert_string_to_int-start------------------------------------------------------------------------------->

#  function to convert string to int with a fallback (when it’s not numbers) of 0
def string_to_int(s:str,fall_back=0)->int:
    try:
        return int(s)
    except ValueError:
        return fall_back

print(string_to_int('123'))
#<----------------------------------------------------------Convert_string_to_int-End------------------------------------------------------------------------------->
#<----------------------------------------------------------longest_word_in_a_string-Start------------------------------------------------------------------------------->

def logest_word(s:str)->str:
    words = s.split()
    max_word = words[0]
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word

s = 'welcome to the programming world of python'
print(logest_word(s))

#<----------------------------------------------------------longest_word_in_a_string-End------------------------------------------------------------------------------->

#<----------------------------------------------------------Write_code_to_Check_if_two_strings_are_Anagram_or_not-Start---------------------------------------------->

def isAnagram(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        string1 = sorted(string1)
        string2 = sorted(string2)
    return True if string1 == string2 else False

print(isAnagram('helow','woleh'))
#<----------------------------------------------------------Write_code_to_Check_if_two_strings_are_Anagram_or_not-End------------------------------------------------>

#<----------------------------------------------------------find_second_most_frequent_character-Start---------------------------------------------------------------->

'''

1.Using count in a loop: Each call to count scans the entire string, leading to O(n) time for each call, and if called in a loop, it results in (n^2) complexity.

2.Using a dictionary: Counting frequencies in a single pass and then processing the dictionary results in  O(n) complexity.

'''
def findSecondFC(word):  #Using counting for count() method
    largest = word[0]
    second_largest = ''
    for char in word:
        if word.count(char) > word.count(largest):
            second_largest = largest
            largest = char
    return second_largest

word = 'aabbbccccddddd'
print(findSecondFC(word))


def findSecondFC(word):  #Using Dictionary for counting
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] = 1
    largest = None
    second_largest = None
    for char,count in frequency.items():
        if largest is None or count > frequency[largest]:
            second_largest = largest
            largest = char
        elif second_largest is None or count > frequency(second_largest):
            second_largest = char
    return second_largest



#<----------------------------------------------------------find_second_most_frequent_character-End------------------------------------------------------------------>

