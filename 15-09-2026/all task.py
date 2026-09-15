
#   Unit 1: Collection Datatypes – List & Tuple



#Task 1: Check Student Name Exists in List 

students = ["Rahul", "Amit", "Komal", "Devam", "Riya"]

name = input("Enter student name: ")

if name in students:
    print("Student found.")
else:
    print("Student not found.")

# Output:
    #  Enter student name: Komal
    # Student found. 
    

# Task 2: Even or Odd Numbers 


numbers = [12, 15, 22, 7, 30]

for num in numbers:
    if num % 2 == 0:
        print(num, "Even")
    else:
        print(num, "Odd") 


        # Output:
        # 12 Even
        # 15 Odd
        # 22 Even
        # 7 Odd
        # 30 Even 



# Task 3: Pass or Fail Using Tuple 


marks = (75, 30, 55, 40, 28)

for m in marks:
    if m >= 35:
        print(m, "Pass")
    else:
        print(m, "Fail")  


        # Output:
        # 75 Pass
        # 30 Fail
        # 55 Pass
        # 40 Pass
        # 28 Fail 


# Task 4: Largest Number Using if 


numbers = [25, 80, 45, 12, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest) 


# Output:
# Largest: 80       


# Task 5: Check List Empty or Not 


items = []

if items:
    print("List is not empty.")
else:
    print("List is empty.") 

    # Output:
    # List is empty.    


   

 #  Unit 2: Mutability – List & Tuple 

 # Task 6: Change Element if Index Valid 


fruits = ["Apple", "Banana", "Mango"]

index = 1

if index < len(fruits):
    fruits[index] = "Orange"

print(fruits)  

# Output:
# ['Apple', 'Orange', 'Mango']  


# Task 7: Check Value Before Accessing Tuple 

marks = (70, 80, 90, 65)

value = 80

if value in marks:
    print("Value exists.")
else:
    print("Value not found.")  


# Output:
# Value exists. 


# Task 8: List vs Tuple Modification 

mylist = [1,2,3]
mylist[0]=10
print(mylist)

mytuple=(1,2,3)

try:
    mytuple[0]=10
except TypeError:
    print("Tuple cannot be modified.") 


# Output:
# [10, 2, 3]    


# Task 9: Check List or Tuple 

data=[1,2,3]

if isinstance(data,list):
    print("It is a List.")
elif isinstance(data,tuple):
    print("It is a Tuple.")
else:
    print("Unknown Collection.") 


# Output:
# It is a List. 




#   Unit 3: List Comprehension 

# Task 10: Even Numbers 1–20 

even=[x for x in range(1,21) if x%2==0]
print(even) 

# Output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  


# Task 11: Odd Numbers 1–20 

odd=[x for x in range(1,21) if x%2!=0]
print(odd) 

# Output:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# Task 12: Numbers Divisible by 3 

nums=[x for x in range(1,51) if x%3==0]
print(nums) 

# Output:
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48] 


# Task 13: Marks Greater Than 40 

marks=[25,40,60,80,35,90]

passed=[m for m in marks if m>=40]

print(passed) 


# Output:
# [40, 60, 80, 90]  


# Task 14: Numbers Between 10 and 50 

numbers=[5,12,25,55,40,9]

result=[x for x in numbers if x>10 and x<50]

print(result) 


# Output:
# [12, 25, 40]  


#Task 15: Names Longer Than 5 Letters 

names=["Komal","Devam","Krishna","Amit","Priyanka"]

result=[n for n in names if len(n)>5]

print(result)

# Output:
# ['Krishna', 'Priyanka']   


# 
    