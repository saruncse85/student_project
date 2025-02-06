DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
);

DROP TABLE IF EXISTS clients;
create table clients(
    client_id integer primary key autoincrement,
    client_name varchar not null,
    location varchar not null,
    phone varchar not null
);

DROP TABLE IF EXISTS student_project_assignment;
create table student_project_assignment(
    spa_id integer primary key autoincrement,
    student_id integer not null,
    client_id integer not null,
    status varchar not null,
    start_date date not null,
    end_date date not null,
    foreign key (student_id) references students(student_id),
    foreign key (client_id) references clients(client_id)
);

INSERT INTO clients (client_name, location, phone) VALUES ('Abbott', 'Chicago', '203-555-6666');