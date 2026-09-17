##Write a python program to count how many times a particular element appears in  a list.
my_list = list(map(int, input("Enter elements of the list: ").split()))
element = int(input("Enter the element to count: "))

count = 0

for item in my_list:
    if item == element:
        count += 1

print("The element appears", count, "times.")