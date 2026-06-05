[🇪🇸 Español](README.md) | 🇬🇧 **English**

# ✅ Step 4: Models and Validation with Pydantic

## 🎯 Goal

Automatically validate inputs to protect your API from invalid data.

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
uvicorn main:app --reload --app-dir day_23/fast_api/step4-modelos-pydantic
```

Open:
- `http://127.0.0.1:8000/docs`

---

## 🧩 What does Pydantic solve?

Without validation, the client can send broken data.
With Pydantic, you define clear input/output rules.

Daily analogy:
- It's like a form with rules at the front desk.
- If the ID is missing or wrong, the request is not processed.

---

## 🛠️ Immediate benefits

1. Type validation (`int`, `bool`, `str`)
2. Simple business rules (`min_length`, `ge`, `le`)
3. Automatic HTTP 422 errors when the body doesn't comply
4. Clearer Swagger documentation

---

## 📌 Recommended rules for this step

- `title` required and with minimum length
- `priority` between 1 and 5
- `done` boolean

---

## 🧪 Exercises

1. Add an `owner_email` field with email validation
2. Create an output model that does not expose internal fields
3. Define a model for partial update (`PATCH`)
