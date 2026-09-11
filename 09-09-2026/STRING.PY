# 1. Student Name

student_name = "Rahul"
print(student_name)


# 2.Multiline String

course_name = """Python Programming
Semester 1"""
print(course_name)


#3. Index 2 Character

text = "DataScience"
print(text[2])    # OUTPUT IS THE ( t ) 


# 4. Last Two Characters

text = "DataScience"
print(text[-2:])  # OUTPUT IS THE ( ce )


# 5. Index 1 to 5

text = "DataScience"
print(text[1:6]) # OUTPUT IS THE ( ataSc )


# 6. Reverse String

text = "DataScience"
print(text[::-1])  # OUTPUT IS THE  ( ecneicSataD )


# 7. Complete Name 

first = "Amit"
surname = "Patel"
complete_name = first + " " + surname
print(complete_name)  # OUTPUT IS THE ( Amit Patel )


# 8. Product & Amount (f-string) 

product = "Mobile"
amount = 25000
print(f"Product: {product}, Amount: {amount}")    # OUTPUT IS THE  ( Product: Mobile, Amount: 25000  )


# 9. Amount with 2 Decimal Places 

product = "Keyboard"
amount = 799.567
print(f"Product: {product}, Amount: {amount:.2f}")   # OUTPUT IS THE ( Product: Keyboard, Amount: 799.57 )


# 10. Addition in f-string 

x = 15
y = 25
print(f"Addition = {x + y}") # OUTPUT IS THE (Addition = 40)


# 11. Employee Details (format()) 

employee = "Rakesh"
department = "IT"
salary = 30000

print("Employee: {}, Department: {}, Salary: {}".format(employee, department, salary)) # OUTPUT IS THE (Employee: Rakesh, Department: IT, Salary: 30000 )


# 12. Positional Arguments 

name = "Priya"
designation = "Manager"
print("Name: {0}, Designation: {1}".format(name, designation)) # OUTPUT IS THE (Name: Priya, Designation: Manager )


# 13. Named Arguments 

name = "Asha"
city = "Rajkot"
course = "Python"
print("Name: {name}, City: {city}, Course: {course}".format(name=name, city=city, course=course)) # OUTPUT IS THE ( Name: Asha, City: Rajkot, Course: Python )


# 14. Apple iPhone 

brand = "Apple"
model = "iPhone"
print(f"Brand: {brand}, Model: {model}")  # OUTPUT IS THE ( Brand: Apple, Model: iPhone )


# 15. Marks with 2 Decimal Places 

student = "Neha"
marks = 85.4567
print(f"{student} scored {marks:.2f}") # OUTPUT IS THE ( Brand: Apple, Model: iPhone )


# 16. Sum, Difference, Multiplication

a = 50
b = 30

print(f"Sum = {a+b}")
print(f"Difference = {a-b}")
print(f"Multiplication = {a*b}")  
# OUTPUT IS THE (  Sum = 80
            #    Difference = 20
             #    Multiplication = 1500


# 17. Kiran lives in Rajkot 

name = "Kiran"
city = "Rajkot"
print("{} lives in {}.".format(name, city)) # OUTPUT IS THE (Kiran lives in Rajkot.)


# 18. Total Price 

item = "Laptop"
price = 45000
quantity = 2
print(f"Total Price = {price * quantity}") # OUTPUT IS THE (Total Price = 90000)


# 19. Named Arguments Sentence 

first_name = "Ravi"
last_name = "Mehta"
course = "Python"
print("{first} {last} is studying {course}.".format(first=first_name, last=last_name, course=course)) # OUTPUT IS THE (Ravi Mehta is studying Python.)


# 20. Student Information Program 


student_name = "Devam"
course = "Python"
city = "Rajkot"
marks = 88.456

print(f"""
Student Information
-------------------
Name  : {student_name}
Course: {course}
City  : {city}
Marks : {marks:.2f}
""")    

 # OUTPUT IS THE (## Student Information

                         # Name  : Devam
                         # Course: Python
                         # City  : Rajkot
                         # Marks : 88.46 )

#  ALL OUTPUT 


#Rahul
# Python Programming
# Semester 1
# t
# ce
# ataSc
# ecneicSataD
# Amit Patel
# Product: Mobile, Amount: 25000
# Product: Keyboard, Amount: 799.57
# Addition = 40
# Employee: Rakesh, Department: IT, Salary: 30000
# Name: Priya, Designation: Manager
# Name: Asha, City: Rajkot, Course: Python
# Brand: Apple, Model: iPhone
# Neha scored 85.46
# Sum = 80
# Difference = 20
# Multiplication = 1500
# Kiran lives in Rajkot.
# Total Price = 90000
# Ravi Mehta is studying Python.

# Student Information
# -------------------
# Name  : Devam
# Course: Python
# City  : Rajkot
# Marks : 88.46
