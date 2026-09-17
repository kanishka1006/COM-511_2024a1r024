#Write  a python program to input two lists and create a third list containing common elements.
list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

common = []

for element in list1:
    if element in list2:
        common.append(element)

print("Common elements:", common)