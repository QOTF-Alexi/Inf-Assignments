books = []
foundEntries = []


def addBook():
    bookDetails = input("Book details: ")
    bookDetailsList = bookDetails.split(sep=", ")
    bookDetailsDict = {'title': bookDetailsList[0], 'author': bookDetailsList[1],
                       'publisher': bookDetailsList[2], 'pub_date': bookDetailsList[3]}
    if len(bookDetailsList) == 4:
        if bookDetailsDict not in books:
            books.append(bookDetailsDict)
            print("Book has been added")
        else:
            print("Entry already exists!")
    else:
        print("That is not a valid entry!")


def search_book(books, term):
    poppedEntries = books
    bookCount = 0
    # find term in dicts in list
    for element in poppedEntries:
        if term in element.values():
            poppedEntries.remove(element)
            foundEntries.append(element)
            bookCount += 1

    if bookCount == 1:
        print("Found a book for:", term)
        return True
    elif len(foundEntries) == 0:
        print("Found no books for", term)
        return False
    else:
        print(f"Found {bookCount} books for: {term}")
        return True


def mainMenu():
    running = True
    while running:
        print("[A] Add book")
        print("[S] Search book")
        print("[E] Exit (and print)")
        menuChoice = input()
        if menuChoice == "A":
            addBook()
        elif menuChoice == "S":
            term = input("Search term: ")
            search_book(books, term)
        elif menuChoice == "E":
            print(*foundEntries, sep="\n")
            running = False
        else:
            print("That's not a valid entry!")


if __name__ == "__main__":
    mainMenu()