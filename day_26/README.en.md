[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🌌 Day 26: SQLAlchemy + Relational Modeling (Instagram and StarWars)

## 📚 Official material identified in the main `README.md`

These are the exact Day 26 links and what each one covers:

- **READ**: [Everything you need to know about SQLAlchemy](https://4geeks.com/syllabus/spain-fs-pt-129/read/everything-you-need-to-start-using-sqlalchemy)
  - Conceptual foundation: ORM, models, relationships, and queries.
- **PROJECT**: [Building Instagram.com Database Model](https://4geeks.com/syllabus/spain-fs-pt-129/project/instagram-data-modeling)
  - Designing entities and relationships of a social network.
- **PROJECT**: [Data Modeling a StarWars Blog](https://4geeks.com/syllabus/spain-fs-pt-129/project/data-modeling-starwars)
  - Modeling a domain with multiple relationships and rules.

---

## 🎯 Day Objectives

By the end of this day you should be able to:

- Explain what SQLAlchemy is and the role `Flask-SQLAlchemy` plays.
- Create models with primary and foreign keys.
- Implement `1-1`, `1-N`, and `N-N` relationships.
- Understand what migrations are and run their full cycle.
- Write `INSERT`, `UPDATE`, `SELECT`, and `DELETE` queries.
- Solve queries with both simple and complex `JOIN`s.

---

## 🗂️ Day Structure

```text
day_26/
├── README.md
├── requirements.txt
├── __init__.py
├── example_app.py
├── example_models.py
├── example_queries.py
├── JOINs-guia-visual.md          # 📊 Visual JOIN guide with diagrams
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

## 🚀 Recommended Setup

From the repo root:

```bash
source .venv/bin/activate
pip install -r day_26/requirements.txt
```

Migration commands using this day's example:

```bash
flask --app day_26/example_app.py db init
flask --app day_26/example_app.py db migrate -m "initial schema day 26"
flask --app day_26/example_app.py db upgrade
```

Run the example queries:

```bash
python -m day_26.example_queries
```

---

## 🧭 Suggested study order

1. `step0-orm-flask-sqlalchemy`
2. `step1-relaciones-modelos`
3. `step2-migraciones-flask-migrate`
4. `step3-crud-y-joins`
5. `JOINs-guia-visual.md` — Visual reference to go deeper into JOINs
6. `step4-proyectos-modelado`

---

## ✅ End-of-Day Checklist

- [ ] I can explain the difference between SQL and ORM.
- [ ] I can explain why the actual ORM is SQLAlchemy.
- [ ] I can model at least one `1-1`, `1-N`, and `N-N` relationship.
- [ ] I can run `db migrate` and `db upgrade` without breaking the schema.
- [ ] I understand what CRUD is and how it relates to REST APIs and SQL.
- [ ] I can build `JOIN` queries for business cases.
- [ ] I know the difference between INNER JOIN and LEFT JOIN.
- [ ] I have made real progress modeling Instagram or StarWars.
