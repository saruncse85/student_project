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
    student = conn.execute('SELECT * FROM students WHERE student_id = ?',
                        (student_id,)).fetchone()
    conn.close()
    if student is None:
        abort(404)
    return student

@app.route('/internship')
def internship():
    conn = get_db_connection()
    query  = "select spa.spa_id, std.name, clt.client_name, \
                spa.status, spa.start_date, spa.end_date from student_project_assignment spa \
                inner join students std on std.student_id = spa.student_id \
                inner join clients clt on clt.client_id = spa.client_id "
    
    intership_details = conn.execute(query).fetchall()
    conn.close()
    return render_template('internship.html', intership_details = intership_details)


@app.route('/students')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)


@app.route('/create_intern/', methods=('GET', 'POST'))
def create_intern():
    conn = get_db_connection()
    students = conn.execute('SELECT student_id, name FROM students').fetchall();
    clients = conn.execute('SELECT client_id, client_name FROM clients').fetchall();
    
    conn.close()

    if request.method == "POST":
        student_id = request.form['student_dropdown']
        client_id = request.form['client_dropdown']
        status = request.form['status']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        conn = get_db_connection()
        conn.execute('INSERT INTO student_project_assignment (student_id, client_id, status, start_date, end_date) VALUES (?, ?, ?, ?, ?)',
                        (student_id, client_id, status, start_date, end_date))
        conn.commit()
        conn.close()
        return redirect(url_for('internship'))
    
    return render_template('create_intern.html', students=students, clients=clients)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']
        phone = request.form['phone']

        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO students (name, age, grade, email, phone) VALUES (?, ?, ?, ?, ?)',
                         (name, age, grade, email, phone))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    student = get_student(id)
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
            conn.execute('UPDATE students SET name = ?, age=?, grade=?, email=?, phone=? WHERE student_id=?',
                         (name, age, grade, email, phone, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', student=student)

def getInternship(id):
    conn = get_db_connection()
    internship = conn.execute('SELECT * FROM student_project_assignment WHERE spa_id = ?',
                        (id,)).fetchone()
    
    conn.close()
    if internship is None:
        abort(404)
    return internship

@app.route('/<int:id>/editInternship/', methods=('GET','POST'))
def editInternship(id):
    conn = get_db_connection()
    internship = getInternship(id)

    students = conn.execute('SELECT student_id, name FROM students').fetchall();
    clients = conn.execute('SELECT client_id, client_name FROM clients').fetchall();

    if request.method == 'POST':        
        student_id = request.form['student_dropdown']
        client_id = request.form['client_dropdown']
        status = request.form['status']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        conn = get_db_connection()
        conn.execute('UPDATE student_project_assignment SET student_id= ?, client_id= ?, status=?, start_date=?, end_date=? where spa_id =?',
                        (student_id, client_id, status, start_date, end_date,id))
        conn.commit()
        conn.close()
        return redirect(url_for('internship'))

    return render_template('editInternship.html', internship=internship,students=students,clients=clients)

@app.route('/<int:id>/delete/')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE student_id=?;', (id, ))
    rowsAffected = cursor.rowcount
    conn.commit()
    conn.close()
    if rowsAffected == 1:
        flash(f"Student {id} deleted!")
    else:
        flash(f"No student with id {id} to delete...")
    return redirect(url_for('index'))    

@app.route('/<int:id>/deleteInternship/')
def deleteInternship(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM student_project_assignment WHERE spa_id=?;', (id, ))
    rowsAffected = cursor.rowcount
    conn.commit()
    conn.close()
    
    if rowsAffected == 1:
        flash(f"Internship {id} deleted!")
    else:
        flash(f"No Internship with id {id} to delete...")
    return redirect(url_for('internship'))


@app.route('/')
def about():
    return render_template('home.html')


## Starts the server and hosts it when we "run" this file on replit
app.run(host='0.0.0.0', port=82)
