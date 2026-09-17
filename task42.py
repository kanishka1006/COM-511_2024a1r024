#Write a python program to store all month names in  tuple.Input a month nuber and display the corresponding month name.
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

number = int(input("Enter month number (1-12): "))

if 1 <= number <= 12:
    print("Month:", months[number - 1])
else:
    print("Invalid month number")