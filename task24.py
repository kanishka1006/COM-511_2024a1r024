#WA pyhton program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.
n = int(input("Enter a number: "))

while n > 9:
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    n = s

print(n)