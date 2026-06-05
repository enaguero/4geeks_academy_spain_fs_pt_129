[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🚀 Step 1: First Server with FastAPI

## 🎯 Goal

Spin up your first modern API with FastAPI and expose basic endpoints.

---

## 🧰 Requirements to run this step

- Completed the cross-cutting setup from Step 0
- Active virtual environment (`source .venv/bin/activate`)
- Installed dependencies (`fastapi`, `uvicorn`)

---

## 📦 Installation (only if you haven't done Step 0 yet)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## 🧩 First `main.py` file

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API viva"}
```

---

## ▶️ Run the server

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/step1-primer-servidor
```

- `main`: file name
- `app`: FastAPI object
- `--reload`: restarts on save

Open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

---

## 🧠 Daily analogy

`uvicorn` is like raising the shutter at a storefront.
Without the server running, there's no one to take orders.

---

## 🧪 Short exercises

1. Create a `GET /health` endpoint that returns `{ "status": "ok" }`
2. Create a `GET /saludo` endpoint that returns a personalized message
3. Change the API title with `FastAPI(title="...")`

---

## ⚠️ Common mistakes

1. Running `python main.py` expecting it to serve HTTP
2. Misspelling `main:app` in the `uvicorn` command
3. Not activating the virtual environment
