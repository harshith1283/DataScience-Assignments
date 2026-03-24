with open("student_data.txt", "w") as file:
    file.write("Ravi,Data Science,80\n")
    file.write("Anjali,Python,70\n")
    file.write("Kiran,AI,90\n")
    file.write("Sneha,ML,65\n")
    file.write("Rahul,Data Science,85\n")
print("Students with marks above 75:")
with open("student_data.txt", "r") as file:
    for line in file:
        name, course, marks = line.strip().split(",")
        if int(marks) > 75:
            print(f"{name} - {course} - {marks}")
