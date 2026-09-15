#Take name, branch, and year. generate  a code name using string concatenation, slicing , and repetition.

student_name = input("Enter your name:")
branch_name = input("Enter your branch:")
year = input("Enter your year:")
code_name = student_name[:3] + "-" + branch_name[:3] + "-" + year[-2:]
print("*" * 30)
print("Student code: ", code_name)
print("*" * 30)