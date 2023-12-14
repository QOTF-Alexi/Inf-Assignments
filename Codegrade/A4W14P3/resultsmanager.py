import os
import sys
import sqlite3

from result import Result
from student import Student
from course import Course


class ResultsManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(
            sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()

    def create_tables(self):
        self.dbc.execute('''CREATE TABLE IF NOT EXISTS courses
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          points INTEGER NOT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS students
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          first_name TEXT NOT NULL,
                          last_name TEXT NOT NULL,
                          date_of_birth DATE NOT NULL,
                          class_code TEXT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS results
                         (student_id INTEGER NOT NULL,
                          course_id INTEGER NOT NULL,
                          mark INTEGER NOT NULL,
                          achieved DATE NOT NULL,
                          PRIMARY KEY(student_id, course_id, mark));''')

        self.conn.commit()

    def get_course(self, course_id):
        self.dbc.execute("SELECT * FROM courses WHERE id=?", (course_id,))
        result = self.dbc.fetchone()
        if result:
            return Course(*result)
        else:
            return None

    def add_course(self, course: Course):
        self.dbc.execute("INSERT INTO courses (name, points) VALUES (?, ?)", (course.name, course.points))
        self.conn.commit()
        course.id = self.dbc.lastrowid
        return course

    def get_student(self, student_id):
        self.dbc.execute("SELECT * FROM students WHERE id=?", (student_id,))
        result = self.dbc.fetchone()
        if result:
            return Student(*result)
        else:
            return None

    def add_student(self, student: Student) -> Student:
        self.dbc.execute("INSERT INTO students (first_name, last_name, date_of_birth, class_code) VALUES (?, ?, ?, ?)",
                         (student.first_name, student.last_name, student.date_of_birth, student.class_code))
        self.conn.commit()
        student.id = self.dbc.lastrowid
        return student

    def add_result(self, result: Result) -> bool:
        self.dbc.execute("SELECT mark FROM results WHERE student_id=? AND course_id=?",
                         (result.student_id, result.course_id))
        previous_mark = self.dbc.fetchone()
        if previous_mark and previous_mark[0] >= result.mark:
            return False
        else:
            self.dbc.execute("INSERT INTO results (student_id, course_id, mark, achieved) VALUES (?, ?, ?, ?)",
                             (result.student_id, result.course_id, result.mark, result.achieved))
            self.conn.commit()
            return True

    def get_results_by_student(self, student_id, only_last=True):
        if only_last:
            self.dbc.execute("SELECT course_id, MAX(mark) FROM results WHERE student_id=? GROUP BY course_id",
                             (student_id,))
        else:
            self.dbc.execute("SELECT * FROM results WHERE student_id=?",
                             (student_id,))
        return self.dbc.fetchall()

    def get_results_by_course(self, course_id, only_last=True):
        if only_last:
            self.dbc.execute("SELECT student_id, MAX(mark) FROM results WHERE course_id=? GROUP BY student_id",
                             (course_id,))
        else:
            self.dbc.execute("SELECT * FROM results WHERE course_id=?",
                             (course_id,))
        return self.dbc.fetchall()

    def close(self):
        self.conn.close()
