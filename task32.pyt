#Write a python progrsm to input markks of n students in a list. Display highest marks, lowest marks , and number of students who passed.
n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Number of students passed:", passed)