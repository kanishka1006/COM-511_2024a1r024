# Program to illustrate iteration over a list and dictionary

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Elements of List:")
for fruit in fruits:
    print(fruit)

student = {
    "Name": "Kanishka",
    "Age": 20,
    "Course": "CSE"
}

print("\nElements of Dictionary:")
for key, value in student.items():
    print(key, ":", value)