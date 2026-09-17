#Write a python program to take a student name and roll number, then generate a username using the first 3 letters of the name and last 2 digits of the roll number.
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

username = name[:3] + roll_number[-2:]

print("Username:", username)