import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'students are the power of the future'


def get_db_connection():
    conn = sqlite3.connect('student_project.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_student(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?',
                        (student_id,)).fetchone()
    conn.close()
    if student is None:
        abort(404)
    return student


@app.route('/students')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    print(students[0]['id'])
    conn.close()
    return render_template('index.html', students=students)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     size = request.form['size']
    #     color = request.form['color']

    #     if not name:
    #         flash('Name is required!')
    #     elif not size:
    #         flash('Size is required!')
    #     else:
    #         conn = get_db_connection()
    #         conn.execute('INSERT INTO birds (name, size, color) VALUES (?, ?, ?)',
    #                      (name, size, color))
    #         conn.commit()
    #         conn.close()
    #         return redirect(url_for('index'))

    return render_template('create.html')
#
#
@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    # print('inside edit metho')
    student = get_student(id)
    # print(student['name'])
    # print('request method', request.method)
    if request.method == 'POST':        
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']
        phone = request.form['phone']
        
        if not name:
            flash('Name is required!')
        elif not age:
            flash('Age is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE students SET name = ?, age=?, grade=?, email=?, phone=? WHERE id=?',
                         (name, age, grade, email, phone, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', student=student)
#
#
# @app.route('/<int:id>/delete/')
# def delete(id):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM birds WHERE id=?;', (id, ))
#     rowsAffected = cursor.rowcount
#     conn.commit()
#     conn.close()
#     if rowsAffected == 1:
#         flash(f"Bird {id} deleted!")
#     else:
#         flash(f"No bird with id {id} to delete...")
#     return redirect(url_for('index'))


@app.route('/')
def about():
    return render_template('home.html')


## Starts the server and hosts it when we "run" this file on replit
app.run(host='0.0.0.0', port=82)
