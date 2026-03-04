-- Listado simple de estudiantes.
SELECT id, name, city
FROM students
ORDER BY id;

-- JOIN: estudiante y curso.
SELECT s.name AS student, c.name AS course
FROM enrollments e
JOIN students s ON s.id = e.student_id
JOIN courses c ON c.id = e.course_id
ORDER BY student, course;

-- GROUP BY + HAVING: cursos con mas de un estudiante.
SELECT c.name, COUNT(*) AS total_students
FROM enrollments e
JOIN courses c ON c.id = e.course_id
GROUP BY c.name
HAVING COUNT(*) > 1
ORDER BY total_students DESC, c.name;

-- Relacion 1-1: estudiante y su perfil.
SELECT s.name, p.github_username
FROM students s
JOIN profiles p ON p.student_id = s.id
ORDER BY s.id;
