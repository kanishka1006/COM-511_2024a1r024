#Write a python program to print a square of stars for n rows and n columns.

n =int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n):
        print("*", end =" ")
    print()