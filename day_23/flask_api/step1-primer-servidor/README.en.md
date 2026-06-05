[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🚀 Step 1: First Server with Flask

## 🎯 Goal

Spin up your first API with Flask and expose basic endpoints.

---

## 🧰 Requirements to run this step

- Completed the cross-cutting setup from Step 0
- Active virtual environment (`source .venv/bin/activate`)
- Dependencies installed (`flask`)

---

## 📦 Installation (only if you haven't done Step 0)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## 🧩 First `main.py` file

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({"message": "API viva"})
```

---

## ▶️ Run the server

```bash
flask --app day_23/flask_api/step1-primer-servidor/main.py --debug run
```

Open:
- `http://127.0.0.1:5000/`

---

## 🧠 Everyday analogy

The `flask --app ... run` command is like raising the shop's shutter.
With no server running, there's no one to take orders.

---

## 🧪 Short exercises

1. Create a `GET /health` endpoint that returns `{ "status": "ok" }`
2. Create a `GET /saludo` endpoint that returns a personalized message
3. Add basic configuration for ordered JSON: `app.config["JSON_SORT_KEYS"] = False`

---

## ⚠️ Common mistakes

1. Running `python main.py` without configuring debug mode
2. Not pointing `--app` to the correct file
3. Not activating the virtual environment
