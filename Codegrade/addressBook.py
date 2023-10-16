import os
import sys
import json


def lines(length):
    print("="*length)


def display(addressbook: list):
    for element in range(len(addressbook)):
        lines(38)
        print("Position:", (addressbook[element])["id"])
        print("First name:", (addressbook[element])["first_name"])
        print("Last name:", (addressbook[element])["last_name"])
        email_1 = ((addressbook[element])["emails"])[0]
        if len((addressbook[element])["emails"]) == 2:
            email_2 = ((addressbook[element])["emails"])[1]
            print("Emails: ", email_1, ", ", email_2, sep="")
        else:
            print("Emails: ", email_1, sep="")

        phone_1 = ((addressbook[element])["phone_numbers"])[0]
        if len((addressbook[element])["phone_numbers"]) == 2:
            phone_2 = ((addressbook[element])["phone_numbers"])[1]
            print("Phone numbers: ", phone_1, ", ", phone_2, sep="")
        else:
            print("Phone numbers: ", phone_1, sep="")
    lines(38)


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''
def list_contacts(addressbook):
    # todo: implement this function
    ...

    return addressbook


def add_contact(addressbook):
    firstName = input("Firstname: ")
    lastName = input("Lastname: ")
    emails = [input("Emails: ")]
    phones = [input("Phonenumbers: ")]
    ident = (addressbook[-1])["id"] + 1

    addressbook.append({"id": ident,
                        "first_name": firstName,
                        "last_name": lastName,
                        "emails": emails,
                        "phone_numbers": phones
                        })
    print("Contact added to addressbook")


'''
remove contact by ID (integer)
'''
def remove_contact(addressbook):
    # todo: implement this function
    ...


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''
def merge_contacts():
    # todo: implement this function
    ...


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
            list_contacts(addressbook)
        elif menuChoice == "A":
            add_contact(addressbook)
            write_to_json(json_file, addressbook)
        elif menuChoice == "R":
            remove_contact(addressbook)
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
