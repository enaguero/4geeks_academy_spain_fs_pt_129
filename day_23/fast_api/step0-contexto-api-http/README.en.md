[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧭 Step 0: Virtual Environment + API Context + HTTP (FastAPI)

## 🎯 Goal

Prepare the virtual environment for the FastAPI track and understand the request/response flow.

---

## ⚙️ Setup (one-time)

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

Verify the installation:

```bash
python -m pip show fastapi
python -m pip show uvicorn
```

---

## ▶️ How to run any FastAPI step

General pattern:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/<step>
```

Example:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/step1-primer-servidor
```

Open in the browser:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

---

## 🔄 Base API flow

```text
Client
  ↓ HTTP
FastAPI
  ↓ logic
Memory/DB
  ↓
JSON + status code
```

---

## ✅ Expected outcome

- Virtual environment ready
- FastAPI running per step
- Clear understanding of request/response and status codes
