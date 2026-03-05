# 🌌 Día 26: SQLAlchemy + Modelado Relacional (Instagram y StarWars)

## 📚 Material oficial identificado en el `README.md` principal

Estos son los links exactos del Día 26 y qué cubre cada uno:

- **READ**: [Everything you need to know about SQLAlchemy](https://4geeks.com/syllabus/spain-fs-pt-129/read/everything-you-need-to-start-using-sqlalchemy)
  - Base conceptual: ORM, modelos, relaciones y queries.
- **PROJECT**: [Building Instagram.com Database Model](https://4geeks.com/syllabus/spain-fs-pt-129/project/instagram-data-modeling)
  - Diseño de entidades y relaciones de una red social.
- **PROJECT**: [Data Modeling a StarWars Blog](https://4geeks.com/syllabus/spain-fs-pt-129/project/data-modeling-starwars)
  - Modelado de un dominio con múltiples relaciones y reglas.

---

## 🎯 Objetivos del día

Al terminar este día deberías poder:

- Explicar qué es SQLAlchemy y qué papel cumple `Flask-SQLAlchemy`.
- Crear modelos con claves primarias y foráneas.
- Implementar relaciones `1-1`, `1-N` y `N-N`.
- Entender qué son las migraciones y ejecutar su ciclo completo.
- Escribir consultas `INSERT`, `UPDATE`, `SELECT`, `DELETE`.
- Resolver consultas con `JOIN` simples y complejas.

---

## 🗂️ Estructura del día

```text
day_26/
├── README.md
├── requirements.txt
├── __init__.py
├── example_app.py
├── example_models.py
├── example_queries.py
├── step0-orm-flask-sqlalchemy/
│   └── README.md
├── step1-relaciones-modelos/
│   └── README.md
├── step2-migraciones-flask-migrate/
│   └── README.md
├── step3-crud-y-joins/
│   └── README.md
└── step4-proyectos-modelado/
    └── README.md
```

---

## 🚀 Setup recomendado

Desde la raíz del repo:

```bash
source .venv/bin/activate
pip install -r day_26/requirements.txt
```

Comandos de migración usando el ejemplo de este día:

```bash
flask --app day_26/example_app.py db init
flask --app day_26/example_app.py db migrate -m "initial schema day 26"
flask --app day_26/example_app.py db upgrade
```

Ejecutar consultas de ejemplo:

```bash
python -m day_26.example_queries
```

---

## 🧭 Orden sugerido de estudio

1. `step0-orm-flask-sqlalchemy`
2. `step1-relaciones-modelos`
3. `step2-migraciones-flask-migrate`
4. `step3-crud-y-joins`
5. `step4-proyectos-modelado`

---

## ✅ Checklist de cierre del día

- [ ] Sé explicar la diferencia entre SQL y ORM.
- [ ] Sé explicar por qué el ORM real es SQLAlchemy.
- [ ] Puedo modelar al menos una relación `1-1`, `1-N` y `N-N`.
- [ ] Puedo ejecutar `db migrate` y `db upgrade` sin romper el esquema.
- [ ] Puedo construir queries con `JOIN` para casos de negocio.
- [ ] Tengo avance real en el modelado de Instagram o StarWars.
