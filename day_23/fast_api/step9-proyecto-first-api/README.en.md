[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🏁 Step 9: Project - First API with FastAPI

## 🎯 Goal

Build a complete tasks API applying everything you learned during the day.

---

## 🧰 Requirements to run the project

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

## ▶️ How to run this project

1. Implement your project inside this folder (following the suggested structure).
2. Once you have `main.py`, run:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/step9-proyecto-first-api
```

3. Test from:
- `http://127.0.0.1:8000/docs`

---

## ⚠️ Important

This step does not ship a closed final solution.

It includes:
- Functional requirements
- Suggested structure
- Quality criteria

You implement the project.

---

## 📋 Description

You'll build a **Todo API** with FastAPI for a future frontend.

Your API must allow:

- Creating tasks
- Listing tasks
- Fetching details by ID
- Updating a task
- Deleting a task
- Filtering by status (`done=true|false`)

---

## 🔧 Minimum technical requirements

- FastAPI + Uvicorn
- Pydantic models for input/output
- At least 5 CRUD endpoints
- Error handling (`404`, `409`, `422`)
- Correct status codes (`200`, `201`, `204`)
- Documentation available at `/docs`

---

## 🗂️ Suggested structure

```text
first_api_fastapi/
├── main.py
├── schemas.py
├── repository.py
├── service.py
└── README.md
```

---

## ✅ Functional requirements

### 1. Create task
- `POST /tasks`
- Body: `title`, `priority` (1..5), `done` optional
- Response `201`

### 2. List tasks
- `GET /tasks`
- Optional `done` filter
- Response `200`

### 3. View detail
- `GET /tasks/{task_id}`
- If it doesn't exist, `404`

### 4. Update task
- `PUT /tasks/{task_id}`
- Allow changing `title`, `priority`, `done`
- If it doesn't exist, `404`

### 5. Delete task
- `DELETE /tasks/{task_id}`
- Response `204`

---

## 🧠 Suggested business rules

- Do not allow empty titles
- Do not allow duplicate titles (case-insensitive)
- `priority` always between 1 and 5

---

## 🧪 Minimum test plan

1. Create a valid task
2. Create an invalid task (short title)
3. Fetch an existing task
4. Fetch a nonexistent task
5. Update a task
6. Delete a task
7. Confirm it was deleted

---

## ✅ Delivery criteria

- Readable code with clear names
- Consistent endpoints
- Errors handled explicitly
- API demonstrable from `/docs`
- README with instructions to run it
