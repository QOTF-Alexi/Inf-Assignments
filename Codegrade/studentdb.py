import os
import sys
import sqlite3


def addStudent(con, fName, lName, city, dob, schoolClass=""):
    curs = con.cursor()
    curs.execute('SELECT * FROM students')
    students = curs.fetchall()
    studentNumber = len(students) + 1
    curs.execute(f'''INSERT INTO students VALUES("{studentNumber}", "{fName}",
                 "{lName}", "{city}", "{dob}", "{schoolClass}")''')
    con.commit()
    return studentNumber


def assignToClass(studentNumber, schoolClass, con):
    curs = con.cursor()
    curs.execute(f'SELECT * FROM students WHERE studentnumber = {studentNumber}')
    student = curs.fetchone()
    if student is None:
        print("Could not find student with number:", studentNumber)
    else:
        curs.execute(f'''UPDATE students
                     SET class = "{schoolClass}"
                     WHERE studentnumber = {studentNumber}''')
        con.commit()
        pass


def listAll(con):
    curs = con.cursor()
    curs.execute('''SELECT * FROM students
                 ORDER BY class DESC''')
    students = curs.fetchall()
    print(*students)


def listClass(schoolClass, con):
    curs = con.cursor()
    curs.execute(f'SELECT * FROM students WHERE class = "{schoolClass}"')
    students = curs.fetchall()
    print(*students)


def searchStudent(searchterm, con):
    curs = con.cursor()
    curs.execute(f'''SELECT * FROM students
                 WHERE first_name = "{searchterm}" or last_name = "{searchterm}" or city = "{searchterm}"''')
    student = curs.fetchone()
    print(student)


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL
        );'''
    )
    running = True
    while running:
        print("[A] Add new student")
        print("[C] Assign student to class")
        print("[D] List all students")
        print("[L] List all students in class")
        print("[S] Search student")
        print("[Q] Quit program")
        choice = input("What would you like to do? ").upper()
        if choice == "A":
            fName = input("Enter first name: ")
            lName = input("Enter last name: ")
            city = input("Enter city: ")
            dob = input("Enter date of birth (DD-MM-YYYY): ")
            schoolClass = input("Enter a class (empty for none): ")
            addiator = addStudent(con, fName, lName, city, dob, schoolClass)
            print("Student number:", addiator)
        elif choice == "C":
            studNum = input("Enter student number: ")
            schoolClass = input("Enter a class: ")
            assignToClass(studNum, schoolClass, con)
        elif choice == "D":
            listAll(con)
        elif choice == "L":
            schoolClass = input("Enter a class: ")
            listClass(schoolClass, con)
        elif choice == "S":
            criterium = input("Enter a search term: ")
            searchStudent(criterium, con)
        elif choice == "Q":
            running = False
        else:
            print("Invalid entry!")


if __name__ == "__main__":
    main()