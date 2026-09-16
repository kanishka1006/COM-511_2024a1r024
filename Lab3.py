# Program to perform operations on a string

string = "Welcome to Python World"

# Count the number of alphabets
count = 0

for ch in string:
    if ch.isalpha():
        count += 1

print("Number of alphabets:", count)

# Extract characters from a given range
print("Characters from index 0 to 10:", string[0:10])

# Check if the string is alphanumeric
print("Is the string alphanumeric?", string.isalnum())