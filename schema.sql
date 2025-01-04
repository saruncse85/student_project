DROP TABLE IF EXISTS students;

CREATE TABLE students (
                          student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          age INTEGER,
                          grade TEXT NOT NULL,
                          email TEXT NOT NULL,
                          phone TEXT NOT NULL
);

DROP TABLE IF EXISTS departments;
create table departments(
    depart_id integer primary key autoincrement,
    depart_name varchar not null
);

DROP TABLE IF EXISTS semesters;
create table semesters(
    semester_id integer primary key autoincrement,
    semester_no varchar not null
);

DROP TABLE IF EXISTS teacher;
create table teacher(
    teacher_id integer primary key autoincrement,
    teacher_name varchar not null,
    depart_id integer not null,
    foreign key (depart_id) references departments(depart_id)
);

DROP TABLE IF EXISTS client;
create table client(
    client_id integer primary key autoincrement,
    client_name varchar not null,
    location varchar not null,
    supervisor_id integer not null,
    phone varchar not null,
    foreign key (supervisor_id) references Supervisor(supervisor_id)
);

DROP TABLE IF EXISTS supervisor;
create table supervisor(
    supervisor_id integer primary key autoincrement,
    supervisor_name varchar not null,
    age integer not null,
    depart_id integer not null,
    foreign key (depart_id) references departments(depart_id)
);

DROP TABLE IF EXISTS student_project_assignment;
create table student_project_assignment(
    spa_id integer primary key autoincrement,
    student_id integer not null,
    client_id integer not null,
    supervisor_id integer not null,
    semester_id integer not null,
    depart_id integer not null,
    status varchar not null,
    start_date date not null,
    end_date date not null,
    foreign key (student_id) references students(student_id),
    foreign key (Client_ID) references client(client_id),
    foreign key (supervisor_id) references supervisor(supervisor_id),
    foreign key (semester_id) references semesters(semester_id),
    foreign key (depart_id) references departments(depart_id)
);

INSERT INTO departments (depart_name) VALUES ('Computer');

INSERT INTO departments (depart_name) VALUES ('Mechanical');

INSERT INTO semesters (semester_no) VALUES ('Fall-2025');

INSERT INTO semesters (semester_no) VALUES ('Spring-2025');

INSERT INTO teacher (teacher_name, depart_id) VALUES ('Teacher 1', '1');

INSERT INTO teacher (teacher_name, depart_id) VALUES ('Teacher 2', '2');

INSERT INTO supervisor (supervisor_name, age, depart_id ) VALUES ('Supervisor 1', '35', '1');

INSERT INTO client (client_name, location, supervisor_id, phone) VALUES ('Abbott', 'Chicago', '1', '203-555-6666');

