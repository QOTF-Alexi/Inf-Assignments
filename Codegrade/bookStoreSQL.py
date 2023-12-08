import os
import sys
import json
import sqlite3
from datetime import datetime, timedelta


# Function to read books from a JSON file
def read_from_json(filename) -> list:
    bookList = list()
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        for book in json_data:
            bookList.append(book)
    return bookList


# Function to synchronize JSON with the database
def sync_with_database(books_json, con):
    cursor = con.cursor()
    for book in books_json:
        cursor.execute("INSERT INTO books (isbn, title, author, pages, year, status) VALUES (?, ?, ?, ?, ?, ?)",
                       (book['isbn'], book['title'], book['author'], book['pages'], book['year'], 'AVAILABLE'))
    con.commit()


# Function to borrow a book
def borrow_book(book_id, con):
    cursor = con.cursor()
    duration = int(input("Enter duration in days: "))
    current_date = datetime.now()
    return_date = current_date + timedelta(days=duration)

    cursor.execute("SELECT status FROM books WHERE id = ? OR isbn = ?", (book_id, book_id))
    book = cursor.fetchone()
    if book and book[0] == 'AVAILABLE':
        cursor.execute("UPDATE books SET status = ?, return_date = ? WHERE id = ? OR isbn = ?",
                       ('BORROWED', return_date.strftime('%Y-%m-%d'), book_id, book_id))
        con.commit()
        print(f"Book can be borrowed until {return_date.strftime('%d-%m-%Y')}")
    else:
        print("Book is currently borrowed or does not exist.")


# Function to return a book
def return_book(book_id, con):
    cursor = con.cursor()
    current_date = datetime.now()

    cursor.execute("SELECT return_date FROM books WHERE id = ? OR isbn = ?", (book_id, book_id))
    book = cursor.fetchone()
    if book:
        return_date = datetime.strptime(book[0], '%Y-%m-%d')
        if current_date > return_date:
            days_late = (current_date - return_date).days
            fine = days_late * 0.50
            print(f"Fine to pay: €{fine:.2f}")
        else:
            print("No fine to pay.")
        cursor.execute("UPDATE books SET status = ?, return_date = NULL WHERE id = ? OR isbn = ?",
                       ('AVAILABLE', book_id, book_id))
        con.commit()
    else:
        print("Book does not exist.")


# Function to search a book
def search_book(search_term, con):
    cursor = con.cursor()
    cursor.execute(f'''SELECT * FROM books
                   WHERE title = "{search_term}" OR isbn = "{search_term}" OR author = "{search_term}"''')
    for book in cursor.fetchall():
        book.split(sep=", ")
        print("{'id': ", book[0], ", 'isbn': ", book[1], ", 'title': ", book[2], ", 'author': ", book[3],
              ", 'pages': ", book[4], ", 'year': ", book[5], ", 'status': ", book[6], ", 'return_date': ",
              book[6], "}", sep="")


# Initial setup and main menu
def main():
    # SQL database setup
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );'''
    )

    # Load the JSON data and synchronize with the database
    books_json = read_from_json('books.json')
    sync_with_database(books_json, con)

    # Menu structure
    running = True
    while running:
        print("[B] Borrow book\n[R] Return book\n[S] Search book\n[Q] Quit program")
        choice = input("Please choose an option: ").upper()
        if choice == 'B':
            book_id = input("Enter a book ID or ISBN: ")
            borrow_book(book_id, con)
        elif choice == 'R':
            book_id = input("Enter a book ID or ISBN: ")
            return_book(book_id, con)
        elif choice == 'S':
            search_term = input("Enter a search term: ")
            search_book(search_term, con)
        elif choice == 'Q':
            running = False
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
