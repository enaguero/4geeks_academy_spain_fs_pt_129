[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🏁 Step 1: Project - Family Static API (Flask)

## 🎯 Goal

Build a static API in Flask, applying OOP to model a family and expose basic operations over HTTP.

---

## 🧰 Requirements to run the project

- Active virtual environment
- Dependencies installed from `day_24/requirements.txt`
- Understanding of the OOP foundations from `step0`

---

## 📦 Installation (if you haven't installed dependencies yet)

```bash
source .venv/bin/activate
pip install -r day_24/requirements.txt
```

---

## ▶️ How to run this project

1. Implement your project inside this folder.
2. Once you have `main.py`, run:

```bash
flask --app day_24/step1-proyecto-family-static-api/main.py --debug run
```

3. Test your API at:
- `http://127.0.0.1:5000/`

---

## ⚠️ Important

This step does not ship a final closed-form solution.

It includes:
- Functional requirements
- Suggested structure
- Quality criteria

You implement the project.

---

## 📋 Description

You will build a **Family Static API** with Flask.

The API must represent a family in memory and allow you to:

- Query all members
- Query a member by ID
- Add new members
- Delete existing members

---

## 🗂️ Suggested structure

```text
family_static_api/
├── main.py
├── family.py
├── member.py
└── README.md
```

---

## ✅ Minimum functional requirements

1. `GET /members`
2. `GET /members/<int:member_id>`
3. `POST /members`
4. `DELETE /members/<int:member_id>`

Suggested payload for creating a member:

```json
{
  "first_name": "Ana",
  "age": 28,
  "lucky_numbers": [3, 7, 21]
}
```

---

## 🧠 Suggested business rules

- `first_name` is required and non-empty
- `age` greater than or equal to 0
- `lucky_numbers` must be a list of integers
- If a member does not exist, respond with `404`

---

## 🧪 Minimum test plan

1. List members on startup
2. Create a valid member
3. Try to create an invalid member
4. Look up an existing member
5. Look up a non-existent member
6. Delete an existing member
7. Verify it was actually deleted

---

## ✅ Submission criteria

- Clear separation between domain logic and Flask routes
- Readable class/method names
- Consistent JSON responses
- Correct status codes (`200`, `201`, `204`, `404`, `400`)
- API demonstrable with reproducible requests

---

## 🔗 Official project link

- [Family Static API with Flask](https://4geeks.com/syllabus/spain-fs-pt-129/project/family-static-api)
