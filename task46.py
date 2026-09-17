#Write a python program to store one student data as a tuple: name, roll number, and marks. Display grade based on marks.


student = ("Kanishka", 101, 85)

name = student[0]
roll_number = student[1]
marks = student[2]

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Name:", name)
print("Roll Number:", roll_number)
print("Marks:", marks)
print("Grade:", grade)