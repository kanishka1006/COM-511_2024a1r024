# Take an email address and print username , domain, and reversed domain.
email = input("Enter email address: ")
at_position = email.find("@")

username = email[:at_position]
domain = email[at_position + 1:]
reversed_domain = domain[::-1]

print("Username:" , username)
print("Domain:" , domain)   
print("Reversed Domain:" , reversed_domain)