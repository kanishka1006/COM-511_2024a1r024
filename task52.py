'''Write a python program that allows a librarian to add several books to a library. for each book, ask the user to enter its title and the number of copies . Store each book and its available copy count in dictonary.
After the books have been added, sisplay a menu that lets the user issue a book, return a book, display all books, or exit the program

Apply these conditions:
- Book titles should eb compared without distinguishing uppercase and lowercase letters.
- A Book can be issued only if it exists in the library and at least one copy is available.
- Issuing a book edcreases its available copy count by one.
- A book can be returned only if it exists in the library and at least one copy has already been issued.
- Returning a book increases its available copy count by one.
- Display an appropriate message for an unavailable book, an invalid choice, or an invalid number of copies.
'''

library = {}

# 1. Add books to the library
num_books = int(input("How many different books do you want to add? "))

for i in range(num_books):
    title = input(f"\nEnter title for book {i + 1}: ").strip()
    copies = int(input(f"Enter number of copies for '{title}': "))

    key = title.lower()  # Convert to lowercase for case-insensitive matching
    library[key] = {
        "title": title,  # Store original name for display
        "available": copies,
        "total": copies,
    }

# 2. Main Menu
while True:
    print("\n--- MENU ---")
    print("1. Display all books")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        print("\n--- Library Collection ---")
        if not library:
            print("Library is empty.")
        else:
            for book in library.values():
                print(
                    f"Title: {book['title']} | Available: {book['available']} / Total: {book['total']}"
                )

    elif choice == "2":
        search = input("\nEnter book title to issue: ").strip().lower()

        if search not in library:
            print("Error: Book does not exist in the library!")
        elif library[search]["available"] == 0:
            print("Error: No copies available right now!")
        else:
            library[search]["available"] -= 1
            print(f"Success! Issued '{library[search]['title']}'.")

    elif choice == "3":
        search = input("\nEnter book title to return: ").strip().lower()

        if search not in library:
            print("Error: This book does not belong to the library!")
        else:
            # Check if any copy was actually issued
            issued_copies = library[search]["total"] - library[search]["available"]
            if issued_copies <= 0:
                print("Error: All copies are already in the library! None were issued.")
            else:
                library[search]["available"] += 1
                print(f"Success! Returned '{library[search]['title']}'.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")