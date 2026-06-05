[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧠 Step 8: FastAPI Mini Challenges

## 🎯 Goal

Consolidate routing, validation and HTTP design through small, realistic problems.

---

## 🧰 Requirements to run the challenges

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

## ▶️ How to run your solutions for this step

1. Create your `main.py` inside this folder (`day_23/fast_api/step8-mini-retos/`).
2. Run:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/step8-mini-retos
```

3. Test endpoints from:
- `http://127.0.0.1:8000/docs`

---

## ✅ Challenge 1: Inventory API

### Statement
Create endpoints to manage products:

- `GET /products`
- `POST /products`
- `PUT /products/{id}`
- `DELETE /products/{id}`

Minimum fields: `name`, `price`, `stock`.

Rules:
- `price > 0`
- `stock >= 0`

---

## ✅ Challenge 2: Query Filters

### Statement
In `GET /products`, add filters:

- `?min_price=`
- `?max_price=`
- `?in_stock=true|false`

Goal: practice query params and combined conditions.

---

## ✅ Challenge 3: Appointment Booking

### Statement
Medical appointments API with `doctor`, `patient`, `date`, `status`.

Rules:
- Do not allow double-booking the same doctor and date
- Allowed `status` values: `pending`, `confirmed`, `cancelled`

---

## ✅ Challenge 4: Simple Pagination

### Statement
Implement pagination in listings:

- `GET /products?offset=0&limit=10`

Return:
- `items`
- `total`
- `offset`
- `limit`

---

## 🔍 Quality checklist

- [ ] Input validation with Pydantic is in place
- [ ] Semantic status codes are used
- [ ] Errors have clear messages
- [ ] Endpoints have consistent names
- [ ] You tested happy paths and error cases
