[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧱 Step 7: Refactor to a Simple Service (Flask)

## 🎯 Goal

Separate responsibilities so the code can grow without becoming chaotic.

---

## 🧰 Requirements to run this step

- Cross-cutting setup completed in Step 0
- Active virtual environment
- Dependencies installed from `day_23/requirements.txt`

---

## 📦 Installation (if you haven't installed dependencies yet)

```bash
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## ▶️ How to run this step

```bash
flask --app day_23/flask_api/step7-refactor-servicio-simple/main.py --debug run
```

---

## 🧠 What problem does this refactor solve?

In real projects, putting everything in `main.py` quickly becomes hard to maintain.

Everyday analogy:
- A professional kitchen: each person has a role.
- A professional API: routes, validation, data access, and rules are separated.

---

## 🗂️ Suggested structure

```text
step7-refactor-servicio-simple/
├── main.py        # HTTP endpoints
├── schemas.py     # Input/output models
├── repository.py  # Data access (in memory)
└── service.py     # Business rules
```

---

## ✅ Benefits

1. More readable code
2. Less duplication
3. Better testability
4. Simple evolution toward a real database

---

## 🧪 Exercises

1. Add a `PATCH /tasks/{id}/done` endpoint
2. Prevent duplicate titles in `service.py`
3. Add a `done=true` query, filtered from the service
