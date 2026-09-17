#Take strudent full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number
full_name = input("Enter your full name: ")
roll_number = input("Enter your roll number: ")

name = full_name.split()

first_name = name[0]
last_name = name[-1]

email = first_name[:3] + last_name[:3] + roll_number[-3:] + "@gmail.com"

print("Generated email:", email)