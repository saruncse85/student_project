-- database: student_project.db
select spa.spa_id, std.name, clt.client_name, sp.supervisor_name, sem.semester_no, dp.depart_name,
spa.status, spa.start_date, spa.end_date from student_project_assignment spa 
inner join students std on std.id = spa.student_id
inner join client clt on clt.client_id = spa.client_id
inner join semesters sem on sem.semester_id =  spa.semester_id
inner join supervisor sp on sp.supervisor_id = spa.supervisor_id
inner join departments dp on dp.depart_id = spa.depart_id


