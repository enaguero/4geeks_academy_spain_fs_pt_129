[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧱 Step 7: Refactor to a Simple Service

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
uvicorn main:app --reload --app-dir day_23/fast_api/step7-refactor-servicio-simple
```

Open:
- `http://127.0.0.1:8000/docs`

---

## 🧠 What problem does this refactor solve?

In real projects, putting everything in `main.py` becomes hard to maintain.

Daily analogy:
- Professional kitchen: each person has a role.
- Professional API: routes, validation, data access and business rules are separated.

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
4. Smooth evolution toward a real database

---

## 🧪 Exercises

1. Add a `PATCH /tasks/{id}/done` endpoint
2. Prevent duplicate titles in `service.py`
3. Add a `done=true` query filter from the service layer
