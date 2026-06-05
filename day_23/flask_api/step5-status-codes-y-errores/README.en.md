[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🚨 Step 5: Status Codes and Error Handling (Flask)

## 🎯 Goal

Respond in a semantic, professional way using the correct HTTP codes.

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
flask --app day_23/flask_api/step5-status-codes-y-errores/main.py --debug run
```

---

## 🧠 Why does it matter?

An API shouldn't just "work"; it should also communicate well.

Everyday analogy:
- If the bank tells you "ok" for everything, you don't know if your transaction went through.
- Status codes are that traffic light: green, yellow, red.

---

## 📌 Quick code guide

- `200 OK`: successful read or update
- `201 Created`: resource created
- `204 No Content`: deleted with no body
- `400 Bad Request`: malformed data
- `404 Not Found`: resource does not exist
- `422 Unprocessable Entity`: body validation failed

---

## 🧩 Recommended error pattern

```json
{
  "detail": "Clear message for the client"
}
```

---

## 🧪 Exercises

1. Return `409 Conflict` when trying to create a duplicate resource
2. Use a real `204` on delete (no body)
3. Standardize error messages across the entire API
