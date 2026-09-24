# Q.1
# Write a recursive function to calculate the factorial of a given number.
# Ensure the program handles edge cases (e.g., negative inputs).

def factorial(num):
    if num==0 or num==1:
        return 1
    if num<0:
        return "Not Possible for nagative value"
    return num*factorial(num-1)
print(factorial(5))


# Q.2
# Implement a recursive function to calculate the nth Fibonacci number.
# Test the function with various inputs.

def fibo(num):
  if num <= 0:
    return 0

  if num == 1:
    return 1

  return fibo(num - 1) + fibo(num - 2)

num = int(input("Enter fibonacci number:"))
print(fibo(num))


# Q.3
# Develop a program using recursion to reverse a string.

def str(text):
  if len(text)<=1:
     return text
  return text[-1] + str(text[:-1])

text = input("Enter String:")
print(str(text))

# Q.4
# Write a recursive function to find the sum of all digits of a given number until a single-digit number remains
def sum(n):
    if n < 10:
        return n
    return (n % 10) + sum(n // 10)
number = 2345
print(sum(number)) 

# Q.5
# Create a recursive function to print all prime numbers between two given numbers.



# Q.6
# Create a lambda function to calculate the square of a number.Use it inside a map() function to generate a list of squares from a given list of numbers.

square = lambda x : x * x
num = int(input("Enter a number:"))
print(square(num))
 
# Q.7
# Write a program to filter out odd numbers from a list using a lambda function and the filter() method.

numbers = [10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50]
even_num = list(filter(lambda x : x % 2 == 0 , numbers))
print(even_num)

# Q.8
# Write a lambda function that accepts three numbers and returns the largest of the three.

largest = lambda a , b , c : max(a , b , c)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

print(largest(a , b, c))