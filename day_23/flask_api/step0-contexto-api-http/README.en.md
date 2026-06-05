[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧭 Step 0: Virtual Environment + API Context + HTTP (Flask)

## 🎯 Goal

Prepare the virtual environment for the Flask track and understand the request/response flow.

---

## ⚙️ Setup (one time only)

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

Verify the installation:

```bash
python -m pip show flask
```

---

## ▶️ How to run any Flask step

General pattern:

```bash
flask --app day_23/flask_api/<step>/main.py --debug run
```

Example:

```bash
flask --app day_23/flask_api/step1-primer-servidor/main.py --debug run
```

Open in your browser:
- `http://127.0.0.1:5000/`

---

## 🔄 Base API flow

```text
Client
  ↓ HTTP
Flask
  ↓ logic
Memory/DB
  ↓
JSON + status code
```

---

## ✅ Expected outcome

- Virtual environment ready
- Flask running per step
- Clarity on request/response and status codes
