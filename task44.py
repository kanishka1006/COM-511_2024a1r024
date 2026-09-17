#Write a python program to store repeated values in  a tuple and count how many times a given value appears.
numbers = (10, 20, 10, 30, 10, 40, 20)

value = int(input("Enter a value: "))

count = numbers.count(value)

print("The value appears", count, "times.")