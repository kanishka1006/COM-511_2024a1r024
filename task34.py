#Write a program to input numbers in a list and find the second largest number.
numbers = list(map(int, input("Enter numbers: ").split()))

unique = list(set(numbers))
unique.sort()

print("Second largest number:", unique[-2])