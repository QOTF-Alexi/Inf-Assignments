import os
import sys
import json


def lines(length):
    print("="*length)


def display(addressbook: list):
    for element in addressbook:
        lines(38)
        print("Position:", element["id"])
        print("First name:", element["first_name"])
        print("Last name:", element["last_name"])
        print("Emails: ", end="")
        print(*element["emails"], sep=", ")
        print("Phone numbers: ", end="")
        print(*element["phone_numbers"], sep=", ")
    lines(38)


def list_contacts(addressbook):
    sortedAddressBook = []
    sortingName = input("Sort by firstname or lastname (empty for none)? ")
    if sortingName == "":
        display(addressbook)
    elif sortingName == "firstname" or sortingName == "lastname":
        sortingOrder = input("Sort ASC or DESC? ")
        if sortingOrder == "ASC" or sortingOrder == "":
            if sortingName == "firstname":
                sortedAddressBook = sorted(addressbook, key=lambda d: d['first_name'])
            else:
                sortedAddressBook = sorted(addressbook, key=lambda d: d['last_name'])
            display(sortedAddressBook)
        elif sortingOrder == "DESC":
            if sortingName == "firstname":
                sortedAddressBook = sorted(addressbook, key=lambda d: d['first_name'], reverse=True)
            else:
                sortedAddressBook = sorted(addressbook, key=lambda d: d['last_name'], reverse=True)
            display(sortedAddressBook)
        else:
            print("That is not a valid entry!")
    else:
        print("That is not a valid entry!")
    return sortedAddressBook


def add_contact(addressbook):
    firstName = input("Firstname: ")
    lastName = input("Lastname: ")
    emails = [input("Emails: ")]
    phones = [input("Phonenumbers: ")]
    if len(addressbook) == 0:
        ident = 1
    else:
        ident = (addressbook[-1])["id"] + 1

    addressbook.append({"id": ident,
                        "first_name": firstName,
                        "last_name": lastName,
                        "emails": emails,
                        "phone_numbers": phones
                        })
    print("Contact added to addressbook")


def askToRemove():
    try:
        ident = int(input("Enter the ID number: "))
        return ident
    except ValueError:
        print("That is not a valid entry!")


def remove_contact(addressbook, ident):
    for element in addressbook:
        if element["id"] == ident:
            addressbook.remove(element)
            break
    print("Contact removed successfully.")


def merge_contacts(addressbook):
    for element in addressbook:
        fullname = element["first_name"], element["last_name"]
        ident = element["id"]
        for compareElement in addressbook:
            fullnameComp = compareElement["first_name"], compareElement["last_name"]
            identComp = compareElement["id"]
            if fullname == fullnameComp and ident != identComp:
                merge_emails = compareElement["emails"]
                merge_phones = compareElement["phone_numbers"]
                (element["emails"]) += merge_emails
                (element["phone_numbers"]) += merge_phones
                remove_contact(addressbook, identComp)
                return None


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            addressbook.append(contact)

    return addressbook


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def main(json_file):
    addressbook = read_from_json(json_file)
    running = True
    while running:
        print("[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")
        menuChoice = input("What would you like to do? ")
        if menuChoice == "L":
            display(addressbook)
        elif menuChoice == "A":
            add_contact(addressbook)
            write_to_json(json_file, addressbook)
        elif menuChoice == "R":
            ident = askToRemove()
            remove_contact(addressbook, ident)
            write_to_json(json_file, addressbook)
        elif menuChoice == "M":
            merge_contacts(addressbook)
            write_to_json(json_file, addressbook)
        elif menuChoice == "Q":
            running = False
        else:
            print("That's not a valid entry!")


if __name__ == "__main__":
    main('contacts.json')
