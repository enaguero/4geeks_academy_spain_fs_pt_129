[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧪 Step 6: Documentation and Testing (Flask)

## 🎯 Goal

Test your API systematically and maintain minimal documentation for the endpoints.

---

## 🧰 Requirements to run this step

- Cross-cutting setup completed in Step 0
- Active virtual environment
- A running API (recommended: Flask Step 5 or Step 7)

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
flask --app day_23/flask_api/step5-status-codes-y-errores/main.py --debug run
```

2. Use `day_23/flask_api/step6-documentacion-y-pruebas/checks.http` as a request guide.

---

## 📘 Recommended documentation in Flask

Flask doesn't generate `/docs` automatically by default.
For this step, document manually:

- List of endpoints
- JSON body examples
- Expected status codes
- Possible errors (`404`, `409`, `422`)

You can do it in a project `README.md` or use OpenAPI extensions if you want to go further.

---

## 🧠 Everyday analogy

`checks.http` is like an operational checklist:
you always run the same checks to validate quality.

---

## 🔍 What to validate on each endpoint

1. Happy path (`200` / `201`)
2. Invalid data (`422`)
3. Non-existent resource (`404`)
4. Business conflicts (`409`)

---

## 🛠️ Manual testing strategy

1. Start with `GET` to inspect the initial state
2. Create data with `POST`
3. Edit with `PUT`
4. Delete with `DELETE`
5. Repeat `GET` to verify consistency

---

## ✅ Expected outcome of this step

Being able to say: "my API works" with reproducible evidence (concrete requests), not by intuition.
