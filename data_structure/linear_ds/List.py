
# <-----------------------------------------------------------------Find_maximum_number-Start------------------------------------------------------------------------------------->
#Using for loop
def find_max(array):
   max_item = array[0]
   for item in array:
       if item > max_item:
           max_item = item
   return max_item

array = [1,5,9,2,3,6,7,3,8]
print(find_max(array))

#Using max() inbuilt method
result = max(array)
print(result)

#Using sorted() inbuilt methods and Slice
result = sorted(array)
print(result[-1])

# <-----------------------------------------------------------------Find_maximum_number-End------------------------------------------------------------------------------------->

# <-----------------------------------------------------------------Reomve Duplicate--Start--------------------------------------------------------------------------->

#Remove duplicate elments without using extra memory or variable
def duplicate_remove(lists):
    index = 0
    while index < len(lists):
        current_element = lists[index]
        if current_element in lists[index + 1:]:
            lists.remove(current_element)
        else:
            index += 1
    return lists
my_list = [1, 2, 2, 3, 4, 4, 5,9,2,4,8,5,10,6,5,99,66,7,8,]
print(duplicate_remove(my_list))
# <-----------------------------------------------------------------Reomve Duplicate-End------------------------------------------------------------------------------->
# <-----------------------------------------------------------------Return indices of the two numbers such that they add up to target.-Start----------------------------->
def twoSum(nums, target):
    seen = {}
    for i , num in enumerate(nums):
        diff = target-num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i
    return []
# <-----------------------------------------------------------------Return indices of the two numbers such that they add up to target.-End---------------------------->

#<------------------------------------------------------------------Find missing elements in an array--Start----------------------------------------------------------->
arr = [1, 8, 9, 5, 6, 7, 10]
arr.sort()
n = arr[-1]

#Method 1
print(arr)
result = []
for i in range(len(arr)):
    temp = arr[-1]-arr[i]
    if temp not in arr and temp !=0:
            result.append(temp)
         
print(result)

#Method 2
for i in range(len(arr)-1):
    curr = arr[i]
    next = arr[i+1]
    if next-curr >1:
        for missing in range(curr+1,next):
            result.append(missing)
print(result)
#<------------------------------------------------------------------Find missing elements in an array--End----------------------------------------------------------->

#<------------------------------------------------------------------Find prime numbers in given arra--Start---------------------------------------------------------->
def isprime(num):
    if num < 2:
        return False
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

arr = [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 12, 14, 15]

print("Prime numbers in the list arr are:")
for num in arr:
    if isprime(num):
        print(num, end=" ")
#<------------------------------------------------------------------Find prime numbers in given arra--End------------------------------------------------------------->

#<------------------------------------------------------------------Find sum numbers in given arra using recursion--Start--------------------------------------------->
def sum_of_arr(nums):
    if not nums:
        return 0
    return nums[0]+sum_of_arr(nums[1:])
numbers = [1, 2, 3, 4, 5]
print(sum_of_arr(numbers))

def sums(n,sum=0):
   if n <0:
      return sum
   sum += n
   return sums(n-1,sum)
#<------------------------------------------------------------------Find sum numbers in given arra using recursion--End---------------------------------------------------------->


# <-----------------------------------------------------------------Is Leap year or not--Start----------------------------------------------------------------------->
def isLeapyear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 !=0:
            return False
        else:
            return True
    else:
       return False


def find_leap_years(years):
    leap_years = []
    for year in years:
        if isLeapyear(year):
            leap_years.append(year)
    return leap_years

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,2024]
leap_years = find_leap_years(years)
print(leap_years)
# <-----------------------------------------------------------------Is Leap year or not--End----------------------------------------------------------------------->

#<------------------------------------------------------------------Find Is palindrom--Start------------------------------------------------------------------------->

def is_palindrome(string):
    reverse = string[::-1]
    return string == reverse
print(is_palindrome('malayala'))

def is_palindrome1(string):
    string = string.lower()
    start = 0
    end = len(string)-1
    while start < end:
        if string[start] != string[end]:
            return False
        start +=1
        end -=1
    return True

print(is_palindrome1('malayalam'))
#<------------------------------------------------------------------Find Is palindrom--End------------------------------------------------------------------------->

#<------------------------------------------------------------------Move negative to right and posative to left--Start-------------------------------------------------->

def move_negatives_to_right(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left] < 0 and nums[right] >=0:
           nums[left],nums[right] = nums[right],nums[left]
           left +=1
           right -=1
        elif nums[left] >= 0:
            left += 1
        elif nums[right] < 0:
            right -= 1

numbers = [3, -2, 4, -1, 2, -5, 6, -7]
move_negatives_to_right(numbers)
print(numbers)

#<------------------------------------------------------------------Move negative to right and posative to left--Start-------------------------------------------------->
def containsNearbyDuplicate(nums, k):
    # Create a dictionary to store the index of each element
    num_index = {}
    
    # Traverse the array
    for i, num in enumerate(nums):
        # If the current element is already in the dictionary and its index is within k distance
        if num in num_index and i - num_index[num] <= k:
            return True
        # Update the index of the current element
        num_index[num] = i
    
    # If no duplicates are found within k distance
    return False

# Example usage:
nums = [1, 2, 3, 1, 2, 3]
k = 2
print(containsNearbyDuplicate(nums, k))  # Output: False

nums = [1, 2, 3, 1, 4, 5]
k = 3
print(containsNearbyDuplicate(nums, k))  # Output: True

#<------------------------------------------------------------------Validate Parentheses--Start----------------------------------------------------------------------->

def validate_parentheses(expression):
    stack = []
    opening_brackets = '({['
    closing_brackets = ')}]'
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack

# Test the function 
print(validate_parentheses("()"))              # Output: True
print(validate_parentheses("()[]{}"))          # Output: True
print(validate_parentheses("(]"))              # Output: False
print(validate_parentheses("([)]"))            # Output: False
print(validate_parentheses("{[]}"))            # Output: True

#<------------------------------------------------------------------Validate Parentheses--End----------------------------------------------------------------------->

#<------------------------------------------------------------------FindSeconLargestElement--Start--------------------------------------------------------------------->

def find_secon_largest(array):
    if len(array) < 2:
        return None
    first = second = float('-inf')
    for num in array:
        if num > first:
            second = first
            first = num
        elif num > second and num!=first:
            second = num
    return second if second != float('-inf') else None

print(find_secon_largest(array))
#<------------------------------------------------------------------FindSeconLargestElement--End----------------------------------------------------------------------->

#<------------------------------------------------------------------Reverse_Till_Middle-Start-------------------------------------------------------------------------->
def reverse_till_middle(lst):
    n = len(lst)
    mid = n // 2
    for i in range(mid):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
    return lst

# Test the function
print(reverse_till_middle([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
print(reverse_till_middle([1, 2, 3, 4, 5, 6]))# Output: [6, 5, 4, 3, 2, 1]
print(reverse_till_middle([1, 2, 3]))         # Output: [3, 2, 1]
#<-----------------------------------------------------------------Reverse_Till_Middle-Start--------------------------------------------------------------------------->