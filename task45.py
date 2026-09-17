#Write a python program to check whether a given value is present in a tuple. If present , display its position.
numbers = (10, 20, 30, 40, 50)

value = int(input("Enter a value: "))

if value in numbers:
    print("Value is present at position:", numbers.index(value))
else:
    print("Value is not present in the tuple.")