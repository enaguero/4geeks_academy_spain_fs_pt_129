[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧪 Step 6: Documentation and Testing

## 🎯 Goal

Test your API systematically and understand FastAPI's automatic documentation.

---

## 🧰 Requirements to run this step

- Cross-cutting setup completed in Step 0
- Active virtual environment
- An API running (recommended: Step 5 or Step 7)

---

## 📦 Installation (if you haven't installed dependencies yet)

```bash
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## ▶️ How to run this step

1. Spin up a reference API (example with Step 5):

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/step5-status-codes-y-errores
```

2. Open the documentation:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

3. Use `day_23/fast_api/step6-documentacion-y-pruebas/checks.http` as a guide for requests.

---

## 📘 Automatic documentation

When you launch FastAPI, you get:

- `/docs` -> interactive Swagger UI
- `/redoc` -> alternative, more narrative documentation

This lets you test endpoints without Postman in the early phase.

---

## 🧠 Daily analogy

`/docs` is like an appliance manual with built-in test buttons.
It doesn't just explain — it also lets you interact.

---

## 🔍 What to validate on each endpoint

1. Happy path (`200` / `201`)
2. Invalid data (`422`)
3. Nonexistent resource (`404`)
4. Business conflicts (`409`)

---

## 🛠️ Manual testing strategy

1. Start with `GET` to inspect initial state
2. Create data with `POST`
3. Edit with `PUT`
4. Delete with `DELETE`
5. Repeat `GET` to verify consistency

---

## ✅ Expected outcome of this step

Being able to say: "my API works" with reproducible evidence (concrete requests), not by intuition.
