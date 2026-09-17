#Write a python program to take an email address and print the domain name.
email = input("Enter your email: ")

domain = email.split("@")[1]

print("Domain name:", domain)