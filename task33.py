#Write a python program to input marks of 10 students. Store only valid marks between 0 and 100 in a list. Skip invalid marks
marks = []

for i in range(10):
    mark = int(input("Enter marks: "))

    if 0 <= mark <= 100:
        marks.append(mark)

print("Valid marks:", marks)