#Write a python program to input a list of numbers and create a new list containing only unique elements.
numbers = list(map(int, input("Enter numbers: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)