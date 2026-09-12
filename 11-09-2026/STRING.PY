# 1. Join Strings (City Names)

cities = ["Rajkot", "Junagadh", "Ahmedabad", "Surat"]
print(" - ".join(cities))     # Output Is The : Rajkot - Junagadh - Ahmedabad - Surat


# 2. Join Strings (Programming Languages) 

languages = ["Python", "C", "Java", "JavaScript"]
print(" | ".join(languages))   # Output IS The : Python | C | Java | JavaScript 


# 3. Strip 

text = "   Hello World   "
print(text.strip())   # Output Is The : Hello World


#4. Lstrip 

text = "   Hello World"
print(text.lstrip())  # Output Is The : Hello World


# 5. Rstrip 

text = "Hello World   "
print(text.rstrip())     #  Output Is The : Hello World


# 6. Remove Non-Alphabetic Characters 

text = "Python123@# Language!"
result = ""

for ch in text:
    if ch.isalpha() or ch == " ":
        result += ch

print(result)     # Output Is The : Python Language 


# 7. Keep Only Numbers 

text = "Phone: 9876543210"
numbers = ""

for ch in text:
    if ch.isdigit():
        numbers += ch

print(numbers)    # Output Is The : 9876543210


# 8. String Checking 

a = "Python"
b = "12345"
c = "python"
d = "PYTHON"
e = "   "

print(a.isalpha())
print(b.isnumeric())
print(c.islower())
print(d.isupper())
print(e.isspace())    # Output Is The   #True
                                        #True
                                        #True
                                        #True
                                        #True


# 9. Reverse String (Slicing) 

text = "Python"
print(text[::-1])   # Output Is The : nohtyP


# 10. Reverse String (reversed + join) 

text = "Python"
print("".join(reversed(text)))    #  Output Is The : nohtyP



# 11. Reverse String (List + reverse) 

text = "Python"
lst = list(text)
lst.reverse()
print("".join(lst))    #  Output Is The : nohtyP 



# 12. Palindrome (String) 

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")   # Input: madam
                              # Output: Palindrome


# 13. Palindrome Number 

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")   #Input: 121
                                     #Output: Palindrome Number


# 14. Escape Characters     

print("Hello\nWorld")
print("Name:\tdevam")
print("He said, \"Hello\"")
print('It\'s Python')
print("Folder: C:\\Users\\Admin")   #  Output Is The : Hello
                                    # World
                                    # Name:   devam
                                    # He said, "Hello"
                                    # It's Python
                                    # Folder: C:\Users\Admin


# 15. Combined String Task  

text = input("Enter a string: ")

# Remove extra spaces
text = text.strip()

# Keep only alphabets and spaces
clean = ""

for ch in text:
    if ch.isalpha() or ch == " ":
        clean += ch

print("Clean String:", clean)
print("Length:", len(clean))
print("Reverse:", clean[::-1])

if clean.lower() == clean[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")          # Output Is The :  Input:   Madam123!   
                                     # Clean String: Madam
                                     # Length: 5
                                     # Reverse: madaM
                                     # Palindrome


#   ALL OUTPUT IS PYTHON TASK  :---

# Hello World
# Hello World
# Hello World
# Python Language
# 9876543210
# True
# True
# True
# True
# True
# nohtyP
# nohtyP
# nohtyP
# Enter a string: 121
# Palindrome
# Enter a number: 1111122332
# Not Palindrome Number
# Hello
# World
# Name:   devam
# He said, "Hello"
# It's Python
# Folder: C:\Users\Admin
# Enter a string: 212
# Clean String: 
# Length: 0
# Reverse: 
# Palindrome


