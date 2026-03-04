PRAGMA foreign_keys = ON;

INSERT INTO students (name, email, city)
VALUES
    ('Ana', 'ana@example.com', 'Madrid'),
    ('Luis', 'luis@example.com', 'Sevilla'),
    ('Carla', 'carla@example.com', 'Valencia'),
    ('Diego', 'diego@example.com', 'Bilbao'),
    ('Marta', 'marta@example.com', 'Malaga');

INSERT INTO profiles (student_id, github_username, linkedin_url)
VALUES
    (1, 'ana-dev', 'https://www.linkedin.com/in/ana-dev'),
    (2, 'luis-codes', 'https://www.linkedin.com/in/luis-codes'),
    (3, 'carla-data', 'https://www.linkedin.com/in/carla-data'),
    (4, 'diego-api', 'https://www.linkedin.com/in/diego-api'),
    (5, 'marta-sql', 'https://www.linkedin.com/in/marta-sql');

INSERT INTO courses (name, level, is_active)
VALUES
    ('SQL Basico', 'beginner', 1),
    ('Python para APIs', 'intermediate', 1),
    ('Modelado Relacional', 'intermediate', 1);

INSERT INTO lessons (course_id, title, position)
VALUES
    (1, 'SELECT y FROM', 1),
    (1, 'WHERE y ORDER BY', 2),
    (1, 'GROUP BY y HAVING', 3),
    (2, 'Flask primer endpoint', 1),
    (2, 'FastAPI CRUD basico', 2),
    (3, 'Claves PK/FK', 1),
    (3, 'Relaciones 1-1, 1-N, N-N', 2);

INSERT INTO enrollments (student_id, course_id, enrolled_at)
VALUES
    (1, 1, '2026-03-01'),
    (1, 3, '2026-03-02'),
    (2, 1, '2026-03-01'),
    (3, 2, '2026-03-03'),
    (3, 3, '2026-03-03'),
    (4, 1, '2026-03-01'),
    (4, 2, '2026-03-02'),
    (5, 3, '2026-03-04');
