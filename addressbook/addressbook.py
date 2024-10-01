"""Simple address book

This program can add, list and remove entries consisting
of names and emailaddresses. The data is stored in a json
file. 

Features:
    - List all entries in the address book
    - Add new entry with name and email validation
    - Remove entry by email 
    - Autosave upon closing the program
""" 

import json
from email_validator import validate_email, EmailNotValidError

def main():
    entries = load_data()
    menu = """
        ====ADDRESS BOOK====
        1. List all entries
        2. Add new entry
        3. Remove entry
        4. Close address book
        ====================\n"""
        
    while True: 
        user_input = input(menu)

        match user_input:
            case "1": list_entries(entries)
            case "2": add(entries)
            case "3": remove(entries)
            case "4":
                print("Saving and closing address book.")
                update_data(entries)
                return
            case _:
                print("Invalid input. Please pick a number from 1 to 4.")


def load_data():
    with open("data.json") as f:
        data = json.load(f)
    return data


def update_data(entries):
    with open("data.json", "w") as f:
        json.dump(entries, f, indent=4)


def add(entries):
    name = input("Enter name: ")
    email = input("Enter email: ")
   
    if email in entries:
        print("Email already exists. Not added to addressbook.")
        return

    try:
        #  set check_deliverability to true to perform a DNS check.
        checked_mail = validate_email(email, check_deliverability=False)
        entries[checked_mail.normalized] = name
        print(f"Added to addressbook: {name}, {email}")
    except EmailNotValidError:
        print("The provided email address is not valid.")


def remove(entries):
    try:
        mail = input("Which email adress would you like to remove?" )
        if mail in entries:
            entries.pop(mail)
            print(f"{mail} has been removed from your addressbook.")
            return

        print(f"{mail} was not found in your addressbook.")
    except ValueError:
        print("Invalid input type.") 
    

def list_entries(entries):
    if len(entries) == 0:
        print("Your addressbook is empty.")
        return

    for email, name in entries.items():
        print(f"{name} | {email}")


if __name__ == "__main__":
    main()
