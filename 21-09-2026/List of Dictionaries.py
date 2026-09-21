# Student Records

students = [
    {"id":101, "name":"Alice", "score":85},
    {"id":102, "name":"Bob", "score":78},
    {"id":103, "name":"Charlie", "score":92}
]

# 1. Print student names
print("1. Student Names")
for s in students:
    print(s["name"])

# 2. Average score
total = 0
for s in students:
    total = total + s["score"]

avg = total / len(students)
print("\n2. Average Score =", avg)

# 3. Add new student
students.append({"id":104, "name":"David", "score":81})

print("\n3. New Student Added")

# 4. Update Bob's score to 88
for s in students:
    if s["id"] == 102:
        s["score"] = 88

print("4. Bob's Score Updated")

# 5. Delete Charlie
for s in students:
    if s["name"] == "Charlie":
        students.remove(s)
        break

print("5. Charlie Deleted")

# 6. Students scoring more than 80
print("\n6. Students with Score > 80")
for s in students:
    if s["score"] > 80:
        print(s["name"], "-", s["score"])

# 7. Sort by score (Descending)
students.sort(key=lambda x: x["score"], reverse=True)

print("\n7. Sorted by Score")
for s in students:
    print(s["name"], "-", s["score"])

# 8. Highest score student
top = students[0]

print("\n8. Highest Scorer")
print(top["name"], "-", top["score"])

# 9. Student Report with Grade
print("\n9. Student Report")

for s in students:

    if s["score"] >= 90:
        grade = "A"

    elif s["score"] >= 80:
        grade = "B"

    else:
        grade = "C"

    print("Name:", s["name"], "| Score:", s["score"], "| Grade:", grade)

# 10. Count Grades
a = 0
b = 0
c = 0

for s in students:

    if s["score"] >= 90:
        a += 1

    elif s["score"] >= 80:
        b += 1

    else:
        c += 1

print("\n10. Grade Count")
print("Grade A =", a)
print("Grade B =", b)
print("Grade C =", c)