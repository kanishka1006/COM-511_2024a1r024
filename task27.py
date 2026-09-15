#Write a python program to input a number and reverse it using arithmetic operations only.
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse:", rev)