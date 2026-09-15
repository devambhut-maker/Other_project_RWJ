# Task 18: Find Duplicate Elements 

numbers=[1,2,3,2,4,5,1]

duplicates=[]

for n in numbers:
    if numbers.count(n)>1 and n not in duplicates:
        duplicates.append(n)

print(duplicates) 


# Output:
# [1, 2]    


# Task 19: Separate Positive, Negative, Zero 


numbers=[10,-5,0,25,-12,8]

positive=[]
negative=[]
zero=[]

for n in numbers:
    if n>0:
        positive.append(n)
    elif n<0:
        negative.append(n)
    else:
        zero.append(n)

print("Positive:",positive)
print("Negative:",negative)
print("Zero:",zero) 



# Output:   
# Positive: [10, 25, 8]
# Negative: [-5, -12]   


# Task 20: Largest and Smallest 

numbers=[45,12,78,5,99]

largest=numbers[0]
smallest=numbers[0]

for n in numbers:
    if n>largest:
        largest=n

    if n<smallest:
        smallest=n

print("Largest:",largest)
print("Smallest:",smallest) 


# Output:
# Largest: 99   


# Task 21: Remove Numbers Less Than 10 

numbers=[3,15,8,22,11,5]

result=[]

for n in numbers:
    if n>=10:
        result.append(n)

print(result) 


# Output:
# [15, 22, 11]  


# Task 22: Generate Even, Odd, Divisible by 5 

numbers=[5,10,15,22,31,40,55]

even=[]
odd=[]
div5=[]

for n in numbers:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)

    if n%5==0:
        div5.append(n)

print("Even:",even)
print("Odd:",odd)
print("Divisible by 5:",div5) 


# Output:
# Even: [10, 22, 40]    
# Odd: [5, 15, 31, 55]  


# Task 23: Names Starting with A 


names=["Amit","Rahul","Anjali","Komal","Ajay"]

for name in names:
    if name.startswith("A"):
        print(name) 

# Output:
# Amit  
# Anjali    
# Ajay  
        

# Task 24: Marks 70 or More 

marks=(65,75,90,45,80)

for m in marks:
    if m>=70:
        print(m) 


# Output:
# 75   
# 90
# 80     


# Task 25: Age Classification 

ages=[8,15,25,45,65]

for age in ages:

    if age<13:
        print(age,"Child")

    elif age<=19:
        print(age,"Teenager")

    elif age<=59:
        print(age,"Adult")

    else:
        print(age,"Senior Citizen") 



# Output:
# 8 Child   
# 15 Teenager
# 25 Adult
# 45 Adult
# 65 Senior Citizen         
