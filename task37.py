#Write a python program to rotate a list one psition to the right.
my_list = list(map(int, input("Enter elements of the list: ").split()))

last = my_list.pop()
my_list.insert(0, last)

print("Rotated list:", my_list)