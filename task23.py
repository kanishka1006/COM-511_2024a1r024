#Take a password and checck length, presence of @, and whether first and last characters are different.
password = input("Enter password: ")

if len(password) >= 8 and "@" in password and password[0] != password[-1]:
    print("Password is valid")
else:
    print("Password is invalid")