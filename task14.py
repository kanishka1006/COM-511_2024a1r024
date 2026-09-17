#write a pyhton program to take a student's full name and display:
#Total number of characters
#First character
#Last character
#Name in uppercase form
name = input("Enter student's full name: ")

print("Total number of characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("Name in uppercase:", name.upper())