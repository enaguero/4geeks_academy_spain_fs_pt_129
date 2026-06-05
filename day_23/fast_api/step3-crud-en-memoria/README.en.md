[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 📦 Step 3: In-Memory CRUD

## 🎯 Goal

Implement a full CRUD without a database, using an in-memory list.

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
uvicorn main:app --reload --app-dir day_23/fast_api/step3-crud-en-memoria
```

Open:
- `http://127.0.0.1:8000/docs`

---

## 🧠 Why in-memory first?

Because it lets you practice the API flow without extra complexity.

Daily analogy:
- It's a classroom whiteboard.
- It works for practicing.
- When class ends, everything gets wiped.

---

## 🛠️ Basic CRUD endpoints

- `GET /tasks` -> list
- `GET /tasks/{task_id}` -> detail
- `POST /tasks` -> create
- `PUT /tasks/{task_id}` -> update
- `DELETE /tasks/{task_id}` -> delete

---

## ✅ Concepts to consolidate

1. Find a resource by ID
2. Respond with `404` when it doesn't exist
3. Return `201` on creation
4. Keep IDs consistent

---

## ⚠️ Expected limitation

If you restart the server, everything is lost. That's normal at this step.
The goal is to understand API design, not persistence yet.

---

## 🧪 Exercises

1. Add a `done=true/false` filter to `GET /tasks`
2. Sort tasks by descending ID with the query param `sort=desc`
3. Prevent creating duplicate tasks by title
