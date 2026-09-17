#Write a python program to show that tuple values cannot be changed directly. Convert tuple into list, update it, and convert it back into tuple.
numbers = (10, 20, 30, 40)

print("Original tuple:", numbers)

# Convert tuple into list
numbers_list = list(numbers)

# Update the list
numbers_list[1] = 25

# Convert list back into tuple
numbers = tuple(numbers_list)

print("Updated tuple:", numbers)