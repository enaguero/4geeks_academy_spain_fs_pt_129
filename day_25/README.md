# 🗃️ Día 25: SQL para principiantes (desde fundamentos de Python)

## 📚 Material oficial (fuente: README principal)

- **READ**: [Mastering Databases: What is SQL Database](https://4geeks.com/syllabus/spain-fs-pt-129/read/what-is-sql-database)
- **PRACTICE**: [Practice SQL](https://4geeks.com/syllabus/spain-fs-pt-129/practice/sql)

---

## 🎯 Objetivo del día

Pasar de pensar datos en estructuras Python (listas y diccionarios) a pensar en datos relacionales con SQL. La meta no es memorizar comandos, sino entender cómo modelar información para que sea consistente, fácil de consultar y lista para usarse en APIs con Flask/FastAPI y ORM como SQLAlchemy.

---

## ✅ Perfil de entrada recomendado

Este plan está diseñado para estudiantes que ya manejan fundamentos de Python: variables, condicionales, funciones y colecciones básicas. Si el grupo entiende listas y diccionarios, ya tiene la base mental necesaria para empezar con tablas, filas y columnas.

---

## 🧭 Ruta incremental de aprendizaje

### Bloque 1: ¿Qué es SQL y qué problema resuelve? (20 min)

Una base de datos relacional sirve para guardar información de forma persistente y ordenada. A diferencia de una lista en memoria de Python, los datos de una base relacional sobreviven al reinicio del programa, se pueden consultar con reglas claras y permiten que varias partes de una aplicación compartan la misma fuente de verdad.

SQL (Structured Query Language) es el lenguaje estándar para hablar con esa base de datos. Con SQL pedimos datos (`SELECT`), filtramos (`WHERE`), ordenamos (`ORDER BY`), agrupamos (`GROUP BY`) y relacionamos tablas (`JOIN`). Es decir, SQL es el puente entre el problema real y la información almacenada.

Conceptos base:

- **Tabla**: colección de registros del mismo tipo (por ejemplo, estudiantes).
- **Fila**: un registro individual (por ejemplo, un estudiante concreto).
- **Columna**: una propiedad del registro (por ejemplo, `name`, `email`).

---

### Bloque 2: Mapa mental Python -> SQL (25 min)

Para alguien que viene de Python, la comparación más útil es esta: una tabla se parece a una lista de diccionarios. Cada fila es como un diccionario y cada columna es como una clave de ese diccionario. La diferencia es que en SQL existe una estructura estricta (esquema) que mejora la calidad del dato.

Ejemplo en Python:

```python
students = [
    {"id": 1, "name": "Ana", "city": "Madrid"},
    {"id": 2, "name": "Luis", "city": "Sevilla"},
]

madrid = [s for s in students if s["city"] == "Madrid"]
print(madrid)
```

Equivalente en SQL:

```sql
SELECT id, name, city
FROM students
WHERE city = 'Madrid';
```

Idea clave: con Python filtramos recorriendo estructuras en memoria; con SQL filtramos directamente en el motor de base de datos.

---

### Bloque 3: `PRIMARY KEY` y `FOREIGN KEY` (35 min)

Las claves son el corazón de un modelo relacional porque evitan datos ambiguos o desconectados.

`PRIMARY KEY` (PK): es la identidad única de cada fila. No se repite y no puede ser nula. Sin PK es difícil actualizar o borrar un registro con seguridad, porque no hay una forma garantizada de identificarlo.

`FOREIGN KEY` (FK): es una columna que referencia la PK de otra tabla. Su función es conectar entidades y proteger la integridad referencial. Si una fila apunta a otra que no existe, la base debería rechazar ese dato.

Ejemplo:

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

Aquí `students.id` identifica cada estudiante y `profiles.student_id` garantiza que todo perfil pertenece a un estudiante real.

---

### Bloque 4: Modelar relaciones `1-1`, `1-N`, `N-N` (SQL + Python) (60 min)

#### Relación 1-1 (uno a uno)

Una entidad A se relaciona con solo una entidad B, y viceversa. Se usa cuando queremos separar datos por responsabilidad o privacidad, pero sin romper la correspondencia uno a uno.

Caso típico: `students` y `profiles`.

- SQL: FK en `profiles` + `UNIQUE` para impedir más de un perfil por estudiante.
- Python mental model: un estudiante tiene un único objeto de perfil.

```python
students = {1: {"name": "Ana"}, 2: {"name": "Luis"}}
profiles = {
    1: {"student_id": 1, "github_username": "ana-dev"},
    2: {"student_id": 2, "github_username": "luis-codes"},
}
```

#### Relación 1-N (uno a muchos)

Una fila de la tabla principal puede tener muchas filas hijas. Es la relación más común en aplicaciones reales.

Caso típico: un curso tiene muchas lecciones.

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

#### Relación N-N (muchos a muchos)

Cuando ambos lados pueden tener múltiples relaciones, no se conecta directo con una sola FK; se crea una tabla puente.

Caso típico: estudiantes y cursos.

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

La PK compuesta evita duplicar la misma inscripción (`student_id`, `course_id`) dos veces.

---

### Bloque 5: Consultar relaciones con SQL (45 min)

Una vez modeladas las tablas, el siguiente paso es extraer información útil. `JOIN` permite “unir” tablas a través de PK/FK para obtener respuestas de negocio sin duplicar datos.

```sql
SELECT s.name AS student, c.name AS course
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
ORDER BY student;
```

También se combinan agregaciones para análisis:

- `COUNT` para contar registros.
- `AVG` para promedios.
- `GROUP BY` para agrupar por categoría.
- `HAVING` para filtrar resultados agregados.

Ejemplo:

```sql
SELECT c.name, COUNT(*) AS total_students
FROM enrollments e
JOIN courses c ON e.course_id = c.id
GROUP BY c.name
HAVING COUNT(*) > 1;
```

---

### Bloque 6: Formas normales (1FN, 2FN, 3FN) y su propósito (55 min)

La normalización es una guía para diseñar tablas sin redundancia innecesaria y con menos errores al insertar, actualizar o eliminar datos.

#### 1FN (Primera Forma Normal)

En 1FN cada columna debe contener valores atómicos (un solo valor por celda), sin listas ni estructuras mezcladas dentro del mismo campo. El problema que resuelve es la dificultad para consultar y mantener datos cuando una celda guarda múltiples valores.

Ejemplo de problema: `students(courses = 'SQL,Python,Flask')`.

Solución: separar en tabla puente `enrollments`, una fila por relación estudiante-curso.

#### 2FN (Segunda Forma Normal)

La 2FN aplica especialmente cuando hay clave primaria compuesta. Toda columna no clave debe depender de toda la clave, no solo de una parte. El problema que resuelve es la duplicación de datos y las anomalías de actualización.

Ejemplo de problema en `enrollments(student_id, course_id)`: guardar `student_name`. Ese nombre depende solo de `student_id`, no de la combinación completa.

Solución: mover `student_name` a `students`.

#### 3FN (Tercera Forma Normal)

En 3FN las columnas no clave no deben depender de otras columnas no clave (sin dependencias transitivas). El problema que resuelve es la propagación de inconsistencias.

Ejemplo de problema: en `students` guardar `city_id`, `city_name`, `postal_code` en la misma tabla si `city_name` y `postal_code` dependen de `city_id`.

Solución: crear `cities(id, city_name, postal_code)` y dejar `students.city_id` como FK.

Conexión con relaciones y claves:

- PK/FK dan la estructura formal para separar entidades.
- `1-N` y `N-N` bien modeladas ayudan a cumplir 1FN y 2FN.
- separar catálogos (`cities`, `countries`, etc.) ayuda a cumplir 3FN.

---

### Bloque 7: Puente a Python + SQLAlchemy (20 min)

En el día 26, este mismo diseño se traduce a ORM:

- tabla SQL -> clase Python,
- PK -> columna `id`,
- FK -> columna de referencia,
- relación (`1-1`, `1-N`, `N-N`) -> `relationship`.

Si el modelo está normalizado, el código en SQLAlchemy es más claro y hay menos bugs por datos duplicados o inconsistentes.

---

## 🧪 Ejercicios de refuerzo (de menor a mayor dificultad)

1. Crear `students` con PK y cargar 5 registros.
2. Crear `profiles` con FK a `students` y forzar `1-1` con `UNIQUE`.
3. Crear `courses` y `lessons` para modelar `1-N`.
4. Crear `enrollments` con PK compuesta (`student_id`, `course_id`) para modelar `N-N`.
5. Hacer un `JOIN` para listar estudiante y curso.
6. Contar cuántos estudiantes hay por curso (`GROUP BY`).
7. Obtener cursos con más de 1 estudiante (`HAVING`).
8. Convertir un diseño con listas dentro de una columna a 1FN.
9. Corregir una tabla puente con columnas que no dependen de toda la PK (2FN).
10. Separar dependencias transitivas para llevar un esquema a 3FN.

---

## 🧑‍🏫 Dinámica sugerida

- 20% explicación conceptual.
- 30% live coding.
- 50% práctica guiada.

Regla útil: cada concepto nuevo debe cerrar con un mini ejercicio de 5-10 minutos.

---

## ✅ Checklist de cierre del día 25

- [ ] Explico con mis palabras qué es SQL y para qué se usa.
- [ ] Entiendo y uso `PRIMARY KEY` y `FOREIGN KEY`.
- [ ] Puedo modelar relaciones `1-1`, `1-N` y `N-N`.
- [ ] Puedo consultar datos con `JOIN`, `GROUP BY` y `HAVING`.
- [ ] Puedo explicar 1FN, 2FN y 3FN y el problema que resuelve cada una.
- [ ] Completé al menos 8/10 ejercicios.

Con este checklist completo, el grupo llega preparado para **Día 26: SQLAlchemy y modelado de datos**.
