# Task 16: Student Result System 


marks=[78,65,82,45,55]

total=sum(marks)
percentage=total/5

print("Total:",total)
print("Percentage:",percentage)

for m in marks:
    if m>=35:
        print(m,"Pass")
    else:
        print(m,"Fail")

if percentage>=75:
    print("Distinction")
elif percentage>=60:
    print("First Class")
elif percentage>=50:
    print("Second Class")
elif percentage>=40:
    print("Pass")
else:
    print("Fail") 




#Output:
# Total: 325
# Percentage: 65.0
# 78 Pass
# 65 Pass
# 82 Pass
# 45 Pass
# 55 Pass
# First Class 



# Task 17: Shopping Cart 


products=["Laptop","Mouse","Keyboard"]
prices=[50000,800,1200]

item=input("Enter product: ")

if item in products:
    index=products.index(item)
    price=prices[index]

    if price>1000:
        price=price-(price*10/100)

    print("Final Price:",price)
else:
    print("Product not available.") 



    #Output:
    # Enter product: Laptop
    # Final Price: 45000.0  


# 
