student = {
    "name": "Harshith",
    "age": 20,
    "course": "Data Science",
    "marks": 85
}
for key, value in student.items():
    print(f"{key}: {value}")
student["grade"] = "A"
print("Updated Dictionary:", student)
courses = {"Python", "Data Science", "AI", "Python"}
print("Unique Courses:", courses)
set1 = {"Python", "AI", "ML"}
set2 = {"AI", "Data Science", "ML"}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
