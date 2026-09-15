#Write a python program to a decimal number and convert it into binary without using the built-in function.
n = int(input("Enter a decimal number: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print("Binary:", binary)