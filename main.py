import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'students are the power of the future'


def get_db_connection():
    conn = sqlite3.connect('student_project.db')
    conn.row_factory = sqlite3.Row
    return conn


# def get_bird(bird_id):
#     conn = get_db_connection()
#     bird = conn.execute('SELECT * FROM birds WHERE id = ?',
#                         (bird_id,)).fetchone()
#     conn.close()
#     if bird is None:
#         abort(404)
#     return bird


@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    print(students[0]['student_id'])
    conn.close()
    return render_template('index.html', students=students)


# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         name = request.form['name']
#         size = request.form['size']
#         color = request.form['color']
#
#         if not name:
#             flash('Name is required!')
#         elif not size:
#             flash('Size is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO birds (name, size, color) VALUES (?, ?, ?)',
#                          (name, size, color))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#
#     return render_template('create.html')
#
#
# @app.route('/<int:id>/edit/', methods=('GET', 'POST'))
# def edit(id):
#     bird = get_bird(id)
#
#     if request.method == 'POST':
#         name = request.form['name']
#         size = request.form['size']
#         color = request.form['color']
#
#         if not name:
#             flash('Name is required!')
#         elif not size:
#             flash('Size is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('UPDATE birds SET name = ?, size=?, color=? WHERE id=?',
#                          (name, size, color, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#
#     return render_template('edit.html', bird=bird)
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


@app.route('/about/')
def about():
    return render_template('about.html')


## Starts the server and hosts it when we "run" this file on replit
app.run(host='0.0.0.0', port=82)
