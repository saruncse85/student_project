import sqlite3

connection = sqlite3.connect('student_project.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO students (name, age, grade, email, phone) VALUES (?, ?, ?, ? ,?)",
            ('John Doe', '15', 12, 'johndoe@gmail.com', '222-111-5555'))

cur.execute("INSERT INTO students (name, age, grade,email, phone) VALUES (?, ?, ?, ? ,?)",
            ('John Smith', '15', 12,  'johnsmith@gmail.com', '123-111-5678'))

cur.execute("INSERT INTO students (name, age, grade,email, phone) VALUES (?, ?, ?, ? ,?)",
            ('Mark Cuban', '15', 12, 'markcuban@gmail.com', '765-333-0000'))

connection.commit()
connection.close()
