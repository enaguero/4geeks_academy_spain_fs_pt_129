[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧭 Step 0: Backend + Python Context

## 🎯 Objective

Understand what problem the backend solves and why we start with Python before building APIs with Flask.

---

## 🌐 Frontend vs Backend (Practical View)

### Frontend
What the user sees and interacts with:
- Buttons
- Forms
- Views and styles

### Backend
The logic behind the scenes:
- Validate data
- Save information to a database
- Business rules
- Authentication
- Respond to HTTP requests

Think of it this way:
- Frontend = the storefront of a shop
- Backend = warehouse + internal system

---

## 🔄 Basic Request/Response Flow

```
User clicks "Save"
    ↓
Frontend sends a request (HTTP)
    ↓
Backend validates and processes
    ↓
Backend responds (JSON)
    ↓
Frontend updates the interface
```

This flow is what you'll start mastering today.

---

## 🐍 Why Python here?

- Clean syntax so you can focus on logic
- Large backend ecosystem (Flask, FastAPI, Django)
- Widely used in automation and data
- Friendly learning curve for the first weeks

---

## ⚙️ Minimal environment setup

In the terminal:

```bash
python3 --version
```

You should see something like `Python 3.x.x`.

Create your first script:

```bash
mkdir -p ~/python_intro
cd ~/python_intro
touch app.py
```

Contents of `app.py`:

```python
print("Hola desde Python")
```

Run:

```bash
python3 app.py
```

---

## 🧠 Mini comprehension exercise

Classify each task as frontend or backend:

1. Display a to-do list on screen
2. Save a new task to the database
3. Validate that an email has the correct format on the server
4. Change a button's color on hover

---

## ⚠️ Common mistakes when starting

1. Installing Python but using the wrong command (`python` vs `python3`)
2. Typing code in the terminal without saving it to a file
3. Focusing on memorizing syntax instead of understanding the flow

---

## ✅ Expected outcome for this step

If you finished this step well, you can already explain:
- What the backend does
- How it communicates with the frontend
- Why Python is a good entry point
