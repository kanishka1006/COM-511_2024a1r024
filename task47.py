#Write a python program to store multiple student records as a list of tuples. Each tuple should contain name, rollnumber , and marks . Display students who scored above 75.
students = [
    ("Kanishka", 101, 85),
    ("Rahul", 102, 68),
    ("Ananya", 103, 92),
    ("Aman", 104, 74)
]

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print(student)