[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🗃️ Day 25: SQL for beginners (from Python fundamentals)

## 📚 Official material (source: main README)

- **READ**: [Mastering Databases: What is SQL Database](https://4geeks.com/syllabus/spain-fs-pt-129/read/what-is-sql-database)
- **PRACTICE**: [Practice SQL](https://4geeks.com/syllabus/spain-fs-pt-129/practice/sql)

---

## 🎯 Goal for the day

Move from thinking about data as Python structures (lists and dictionaries) to thinking about relational data with SQL. The goal isn't to memorize commands, but to understand how to model information so it's consistent, easy to query, and ready to use in APIs with Flask/FastAPI and ORMs like SQLAlchemy.

---

## ✅ Recommended entry profile

This plan is designed for students who already know Python fundamentals: variables, conditionals, functions, and basic collections. If the group understands lists and dictionaries, they already have the mental foundation to start with tables, rows, and columns.

---

## 🛠️ Local SQLite lab (CLI + DBeaver)

Yes, it's totally possible to work through day 25 with a local SQLite database and spin it up with simple commands.

SQLite needs no server or port: the database is a `.db` file you can open with both `sqlite3` and DBeaver.

### Structure added in `day_25`

```text
day_25/
├── Makefile
├── scripts/
│   ├── db_init.sh
│   ├── db_seed.sh
│   ├── db_reset.sh
│   ├── db_drop.sh
│   ├── db_blank.sh
│   ├── db_shell.sh
│   └── db_query.sh
└── sqlite/
    ├── schema.sql
    ├── seed.sql
    └── practice.sql
```

### Recommended commands

From `day_25/`:

```bash
make help      # list available commands
make db-schema # creates sqlite/day25.db with tables only (schema)
make db-seed   # inserts data from sqlite/seed.sql
make db-setup  # recreates sqlite/day25.db with tables + data (schema + seed)
make db-drop   # deletes sqlite/day25.db
make db-demo   # runs queries from sqlite/practice.sql
make db-shell  # opens sqlite3 shell on the database
make db-reset  # runs db-drop + db-setup
make db-blank  # leaves sqlite/day25.db empty (no tables, no data)
make db-init   # alias of db-schema (kept for compatibility)
```

From the repo root:

```bash
make -C day_25 help
make -C day_25 db-schema
make -C day_25 db-seed
make -C day_25 db-setup
make -C day_25 db-demo
```

### 🧠 What is `make` and how does it work?

`make` is an automation tool. Instead of memorizing long commands, you run a short name (a *target*) defined in the `Makefile`.

In this project, each database target calls a script in `scripts/`:

- `make db-schema` runs `./scripts/db_init.sh`
- `make db-seed` runs `./scripts/db_seed.sh`
- `make db-setup` runs `./scripts/db_reset.sh`
- `make db-drop` runs `./scripts/db_drop.sh`

Think of `make` as a menu of standardized actions for the team:

- Prevents errors from copy-pasting manual commands.
- Makes everyone use the same workflow.
- Makes the lab easier to document and teach.

Minimal `Makefile` structure:

```make
target-name:
	command-to-run
```

A real example from this repo:

```make
db-schema:
	./scripts/db_init.sh "$(DB_FILE)"
```

When you run `make db-schema`, `make` finds that block and runs the line with `./scripts/db_init.sh`.

Without `make` (directly with scripts):

```bash
./day_25/scripts/db_init.sh
./day_25/scripts/db_seed.sh
./day_25/scripts/db_query.sh
./day_25/scripts/db_shell.sh
./day_25/scripts/db_reset.sh
./day_25/scripts/db_drop.sh
./day_25/scripts/db_blank.sh
```

### Open the database with DBeaver

1. Create a new connection and choose **SQLite**.
2. In `Database file`, select:
   - `.../4geeks_academy_spain_fs_pt_129/day_25/sqlite/day25.db`
3. Connect and refresh the schema to see the tables (`students`, `profiles`, `courses`, `lessons`, `enrollments`).

---

## 🧭 Incremental learning path

### Block 1: What is SQL and what problem does it solve? (20 min)

A relational database is used to store information persistently and in an organized way. Unlike a Python in-memory list, the data in a relational database survives program restarts, can be queried with clear rules, and lets multiple parts of an application share the same source of truth.

SQL (Structured Query Language) is the standard language for talking to that database. With SQL we request data (`SELECT`), filter it (`WHERE`), sort it (`ORDER BY`), group it (`GROUP BY`), and relate tables (`JOIN`). In other words, SQL is the bridge between the real-world problem and the stored information.

`FROM`

Core concepts:

- **Table**: a collection of records of the same type (e.g., students).
- **Row**: a single record (e.g., a specific student).
- **Column**: a property of the record (e.g., `name`, `email`).

```
SELECT column_one, column_two, ...
FROM table_name
WHERE column_one ~ "Erwin"
```

---

### Block 2: Python -> SQL mental map (25 min)

For someone coming from Python, the most useful comparison is this: a table is like a list of dictionaries. Each row is like a dictionary and each column is like a key in that dictionary. The difference is that SQL has a strict structure (schema) that improves data quality.

Python example:

```python
students = [
    {"id": 1, "name": "Ana", "city": "Madrid"},
    {"id": 2, "name": "Luis", "city": "Sevilla"},
]

madrid = [s for s in students if s["city"] == "Madrid"]
print(madrid)
```

SQL equivalent:

```sql
SELECT id, name, city
FROM students
WHERE city = 'Madrid';
```

Key idea: in Python we filter by iterating through in-memory structures; in SQL we filter directly in the database engine.

---

### Block 3: `PRIMARY KEY` and `FOREIGN KEY` (35 min)

Keys are the heart of a relational model because they prevent ambiguous or disconnected data.

`PRIMARY KEY` (PK): the unique identity of each row. It never repeats and can't be null. Without a PK it's hard to update or delete a record safely, because there's no guaranteed way to identify it.

`FOREIGN KEY` (FK): a column that references the PK of another table. Its purpose is to connect entities and protect referential integrity. If a row points to another that doesn't exist, the database should reject that data.

Example:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE profiles (
    id INTEGER PRIMARY KEY,
    student_id INTEGER UNIQUE NOT NULL,
    github_username TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

Here `students.id` identifies each student and `profiles.student_id` guarantees every profile belongs to a real student.

---

### Block 4: Modeling `1-1`, `1-N`, `N-N` relationships (SQL + Python) (60 min)

#### 1-1 relationship (one-to-one)

Entity A relates to only one entity B, and vice versa. It's used when we want to split data by responsibility or privacy, but without breaking the one-to-one correspondence.

Typical case: `students` and `profiles`.

- SQL: FK in `profiles` + `UNIQUE` to prevent more than one profile per student.
- Python mental model: a student has a single profile object.

```python
students = {1: {"name": "Ana"}, 2: {"name": "Luis"}}
profiles = {
    1: {"student_id": 1, "github_username": "ana-dev"},
    2: {"student_id": 2, "github_username": "luis-codes"},
}
```

#### 1-N relationship (one-to-many)

A row in the main table can have many child rows. This is the most common relationship in real-world applications.

Typical case: a course has many lessons.

```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE lessons (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

```python
courses = {1: {"name": "SQL Basico"}}
lessons = [
    {"id": 1, "title": "SELECT", "course_id": 1},
    {"id": 2, "title": "WHERE", "course_id": 1},
]
```

#### N-N relationship (many-to-many)

When both sides can have multiple relationships, you don't connect them directly with a single FK; you create a junction table.

Typical case: students and courses.

```sql
CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_at TEXT NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

```python
enrollments = {
    (1, 1): {"enrolled_at": "2026-03-01"},
    (2, 1): {"enrolled_at": "2026-03-02"},
}
```

The composite PK prevents duplicating the same enrollment (`student_id`, `course_id`) twice.

---

### Block 5: Querying relationships with SQL (45 min)

Once the tables are modeled, the next step is extracting useful information. `JOIN` lets you "join" tables via PK/FK to get business answers without duplicating data.

```sql
SELECT s.name AS student, c.name AS course
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
ORDER BY student;
```

Aggregations are also combined for analysis:

- `COUNT` to count records.
- `AVG` for averages.
- `GROUP BY` to group by category.
- `HAVING` to filter aggregated results.

Example:

```sql
SELECT c.name, COUNT(*) AS total_students
FROM enrollments e
JOIN courses c ON e.course_id = c.id
GROUP BY c.name
HAVING COUNT(*) > 1;
```

---

### Block 6: Normal forms (1NF, 2NF, 3NF) and their purpose (55 min)

Normalization is a guide for designing tables without unnecessary redundancy and with fewer errors when inserting, updating, or deleting data.

#### 1NF (First Normal Form)

In 1NF every column must contain atomic values (a single value per cell), with no lists or mixed structures inside the same field. The problem it solves is the difficulty of querying and maintaining data when a cell stores multiple values.

Problem example: `students(courses = 'SQL,Python,Flask')`.

Solution: split into a junction table `enrollments`, one row per student-course relationship.

#### 2NF (Second Normal Form)

2NF applies especially when there is a composite primary key. Every non-key column must depend on the entire key, not just part of it. The problem it solves is data duplication and update anomalies.

Problem example in `enrollments(student_id, course_id)`: storing `student_name`. That name depends only on `student_id`, not on the full combination.

Solution: move `student_name` to `students`.

#### 3NF (Third Normal Form)

In 3NF, non-key columns must not depend on other non-key columns (no transitive dependencies). The problem it solves is the propagation of inconsistencies.

Problem example: in `students`, storing `city_id`, `city_name`, `postal_code` in the same table when `city_name` and `postal_code` depend on `city_id`.

Solution: create `cities(id, city_name, postal_code)` and keep `students.city_id` as an FK.

Connection with relationships and keys:

- PK/FK provide the formal structure to separate entities.
- Well-modeled `1-N` and `N-N` help satisfy 1NF and 2NF.
- Splitting out catalogs (`cities`, `countries`, etc.) helps satisfy 3NF.

---

### Block 7: Bridge to Python + SQLAlchemy (20 min)

On day 26, this same design translates to ORM:

- SQL table -> Python class,
- PK -> `id` column,
- FK -> reference column,
- relationship (`1-1`, `1-N`, `N-N`) -> `relationship`.

If the model is normalized, the SQLAlchemy code is clearer and there are fewer bugs from duplicated or inconsistent data.

---

## 🧪 Reinforcement exercises (from easier to harder)

1. Create `students` with a PK and load 5 records.
2. Create `profiles` with an FK to `students` and enforce `1-1` with `UNIQUE`.
3. Create `courses` and `lessons` to model `1-N`.
4. Create `enrollments` with a composite PK (`student_id`, `course_id`) to model `N-N`.
5. Use a `JOIN` to list student and course.
6. Count how many students there are per course (`GROUP BY`).
7. Get courses with more than 1 student (`HAVING`).
8. Convert a design with lists inside a column to 1NF.
9. Fix a junction table with columns that don't depend on the full PK (2NF).
10. Split out transitive dependencies to bring a schema to 3NF.

---

## 🧑‍🏫 Suggested format

- 20% conceptual explanation.
- 30% live coding.
- 50% guided practice.

Useful rule: every new concept should wrap up with a 5-10 minute mini exercise.

---

## ✅ Day 25 closing checklist

- [ ] I can explain in my own words what SQL is and what it's used for.
- [ ] I understand and use `PRIMARY KEY` and `FOREIGN KEY`.
- [ ] I can model `1-1`, `1-N`, and `N-N` relationships.
- [ ] I can query data with `JOIN`, `GROUP BY`, and `HAVING`.
- [ ] I can explain 1NF, 2NF, and 3NF and the problem each one solves.
- [ ] I completed at least 8/10 exercises.

With this checklist done, the group is ready for **Day 26: SQLAlchemy and data modeling**.
