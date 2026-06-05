[🇪🇸 Español](README.md) | 🇬🇧 **English**

# ✅ Step 4: Models and Validation with Pydantic (Flask)

## 🎯 Goal

Validate inputs automatically to protect your API from invalid data.

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
flask --app day_23/flask_api/step4-modelos-pydantic/main.py --debug run
```

---

## 🧩 What does Pydantic solve in Flask?

Without validation, the client can send broken data.
With Pydantic, you define clear input/output rules even when the framework is Flask.

Everyday analogy:
- It's like a form with rules at the front desk.
- If the ID is missing or wrong, the request isn't processed.

---

## 🛠️ Immediate benefits

1. Type validation (`int`, `bool`, `str`)
2. Simple business rules (`min_length`, `ge`, `le`)
3. `422` responses when the body doesn't comply
4. More consistent data contracts

---

## 📌 Recommended rules for this step

- `title` required and with a minimum length
- `priority` between 1 and 5
- `done` boolean

---

## 🧪 Exercises

1. Add an `owner_email` field with email validation
2. Create an output model that doesn't expose internal fields
3. Define a model for partial updates (`PATCH`)
