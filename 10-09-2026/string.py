print("========== PYTHON STRING TASKS ==========\n")



# 1. String Formatting

print("1. String Formatting")
name = "Rahul"
subject = "Python"
experience = 3
print("Teacher %s teaches %s and has %d years experience." % (name, subject, experience))



# 2. Float Formatting

print("\n2. Float Formatting")
movie = "Avatar"
rating = 8.567
print("Movie %s has rating %.2f." % (movie, rating))



# 3. Case Conversion

print("\n3. Case Conversion")
text = "summer vacation is fun"
print("Upper      :", text.upper())
print("Lower      :", text.lower())
print("Title      :", text.title())
print("Capitalize :", text.capitalize())
print("Swapcase   :", text.swapcase())



# 4. String Searching

print("\n4. String Searching")
text = "I am learning Java and Python."
print("Position of Java:", text.find("Java"))



# 5. Membership

print("\n5. Membership")
food = "I like pizza and burger."
print("Is pizza present?", "pizza" in food)



# 6. String Index

print("\n6. String Index")
animal = "Elephant"
print("First character :", animal[0])
print("Third character :", animal[2])
print("Last character  :", animal[-1])
print("Second last     :", animal[-2])



# 7. Startswith & Endswith

print("\n7. Startswith & Endswith")
movie = "The Avengers!"
print("Starts with 'The' :", movie.startswith("The"))
print("Ends with '!'     :", movie.endswith("!"))



# 8. String Replacement

print("\n8. String Replacement")
cricket = "India is playing cricket."
print(cricket.replace("India", "Team India"))



# 9. Replace Only First Occurrence

print("\n9. Replace First Occurrence")
car_text = "I have a car. My car is red."
print(car_text.replace("car", "bike", 1))



# 10. String Counting

print("\n10. String Counting")
travel = "I am traveling to Gujarat."
print("Count of 'a':", travel.count("a"))



# 11. Split Comma

print("\n11. Split Comma")
brands = "Apple,Samsung,OnePlus,Redmi"
print(brands.split(","))



# 12. Split Words

print("\n12. Split Words")
education = "Education is very important"
print(education.split())



# 13. Multiline String

print("\n13. Multiline String")
cities = "Junagadh\nRajkot\nAhmedabad\nSurat"
print(cities.split("\n"))



# 14. For Loop with Multiline String

print("\n14. For Loop")
animals = "Dog\nCat\nLion\nTiger\nElephant"
animal_list = animals.split("\n")
for i in animal_list:
    print(i)



# 15. Combined Task


print("\n15. Combined Task")
product = "Laptop"
quantity = 2
price = 50000
customer = "Rahul"

order = "Customer %s ordered %d %s at price %d." % (customer, quantity, product, price)

print(order)
print("Upper Product :", product.upper())
print("Lower Customer:", customer.lower())
print("Find Laptop   :", order.find("Laptop"))
print("Replace       :", order.replace("Laptop", "Computer"))
print("Count 'a'     :", order.count("a"))
print("Split         :", order.split())

print("\n========== END ==========")