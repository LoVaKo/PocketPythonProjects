entries = {}

def add():
    name = input("Enter name: ")
    email = input("Enter email: ")
   
    if email in entries:
        print("Email already exists. Not added to addressbook.")
        return
   
    entries[email] = name
    print(f"Added to addressbook: {name}, {email}")
    

def list_entries():
    if len(entries) == 0:
        print("Your addressbook is empty.")
        return

    for email, name in entries.items():
        print(f"{name} | {email}")


while True:
    user_input = input("""
    ====ADDRESS BOOK====
    1. List all entries
    2. Add new entry
    3. Close
    ====================\n""")

    match user_input:
        case "1": list_entries()
        case "2": add()
        case "3": 
            print("Closing address book.")
            break
        case _:
            print("Invalid input. Please pick 1, 2, or 3")


