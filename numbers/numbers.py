#<------------------------------------------------------------Write a code to reverse a number---------------------------------------------------------------------->
def reverse_number(number):
    temp = number
    reverse = 0
    while number > 0:
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10
    return (temp,reverse)

print(reverse_number(10))
#<------------------------------------------------------------Write_a_code_to_reverse_a_number---------------------------------------------------------------------->
#<------------------------------------------------------------Write_the_code_to_find_the_Fibonacci_series_upto_the_nth_term.---------------------------------------->
#using loop with three varibles
def fibnoci_series(number):
    n1,n2=0,1
    result = [0,1]
    for i in range(2,number):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        result.append(n3)
    return result

print(fibnoci_series(5))

#using loop without 3 variables
def fib_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

#using generator
def fibnoci_generator(stop):
    current_fib,next_fib = 0,1
    for _ in range(0,stop):
        fib_number = current_fib
        current_fib,next_fib = next_fib,current_fib + next_fib
        yield fib_number

result = list(fibnoci_generator(10))
#<------------------------------------------------------------Write_the_code_to_find_the_Fibonacci_series_upto_the_nth_term.---------------------------------------->

#<------------------------------------------------------------------Find_Factorial_of_a_number--Start-------------------------------------------------------------->

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    # Multiply result by numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result
#<------------------------------------------------------------------Find_Factorial_of_a_number--End---------------------------------------------------------------->

#<------------------------------------------------------------------ Write_code_of_Greatest_Common_Divisor--Start-------------------------------------------------->

def gcdFunction(num1,num2):
    gcd = 0
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1,small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    return gcd

print(gcdFunction(10,15))

#<------------------------------------------------------------------ Write_code_of_Greatest_Common_Divisor--End---------------------------------------------------->

#<------------------------------------------------------------------ Write_code_of_Perfect_number--Start----------------------------------------------------------->

def isPerfectNumber(number):
    sump = 0
    for i in range(1,number):
       if number % i == 0:
           sump = sump + i
    return True if sump == number else False

print(isPerfectNumber(6))

#<------------------------------------------------------------------ Write_code_of_Perfect_number--End----------------------------------------------------------->
