#Take roll number and exract admission year , program code, and rollnumber digit using slicing.
roll = input("Enter roll number: ")

admission_year = roll[0:2]
program_code = roll[2:5]
roll_number = roll[5:]

print("Admission year:", admission_year)
print("Program code:", program_code)
print("Roll number:", roll_number)