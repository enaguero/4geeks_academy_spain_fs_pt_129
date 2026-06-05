[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🏁 Step 9: Project - First API with Flask

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
flask --app day_23/flask_api/step9-proyecto-first-api/main.py --debug run
```

---

## ⚠️ Important

This step doesn't include a closed final solution.

It includes:
- Functional requirements
- Suggested structure
- Quality criteria

You implement the project.

---

## 📋 Description

You're going to create a **Todo API** with Flask for a future frontend.

Your API must allow you to:

- Create tasks
- List tasks
- Look up details by ID
- Update a task
- Delete a task
- Filter by status (`done=true|false`)

---

## 🔧 Minimum technical requirements

- Flask
- Pydantic models for input/output
- At least 5 CRUD endpoints
- Error handling (`404`, `409`, `422`)
- Correct status codes (`200`, `201`, `204`)
- README with usage examples

---

## 🗂️ Suggested structure

```text
first_api_flask/
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
- `201` response

### 2. List tasks
- `GET /tasks`
- Optional `done` filter
- `200` response

### 3. View details
- `GET /tasks/{task_id}`
- If it doesn't exist, `404`

### 4. Update task
- `PUT /tasks/{task_id}`
- Allow changing `title`, `priority`, `done`
- If it doesn't exist, `404`

### 5. Delete task
- `DELETE /tasks/{task_id}`
- `204` response

---

## 🧠 Suggested business rules

- Don't allow empty titles
- Don't allow duplicate titles (case-insensitive)
- `priority` always between 1 and 5

---

## 🧪 Minimum test plan

1. Create a valid task
2. Create an invalid task (short title)
3. Look up an existing task
4. Look up a non-existent task
5. Update a task
6. Delete a task
7. Confirm it was deleted

---

## ✅ Delivery criteria

- Readable code with clear names
- Consistent endpoints
- Errors handled explicitly
- API demonstrable with reproducible requests
- README with instructions to run it
