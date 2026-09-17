#Write a python program to input numbers in a list and create two seperate lists for even and odd numbers.
numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)