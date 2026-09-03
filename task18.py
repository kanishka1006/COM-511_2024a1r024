# Write a Python program to take a 10- digit mobile number and display only the last 4 digits . Replace the first 6 digits with *******
mobile = input("Enter moblile number: ")
masked = "******" + mobile[-4:]
print("Masked mobile number=", masked)