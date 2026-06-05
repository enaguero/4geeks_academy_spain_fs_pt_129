[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🛣️ Step 2: Routes and Parameters (Flask)

## 🎯 Goal

Learn how to receive data from the URL using `path params` and `query params`.

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
flask --app day_23/flask_api/step2-rutas-y-parametros/main.py --debug run
```

---

## 🧭 Path params vs Query params

### Path params
They live inside the route and usually identify a single resource.

Example: `/users/15`

### Query params
They go at the end of the URL and usually filter or paginate.

Example: `/users?limit=10&active=true`

---

## 🧠 Everyday analogy

- Path param: the house number on a street (`/casas/12`)
- Query param: the preferences for the order (`?sin_cebolla=true`)

---

## 🧪 Examples

- `GET /products/4` -> details of product 4
- `GET /products?limit=5` -> first 5 products
- `GET /search?q=python` -> text search

---

## ✅ Quick best practices

1. Use clear names (`product_id`, not `x`)
2. Convert types manually in Flask (`int`, `bool`)
3. Define reasonable defaults for query params

---

## ⚠️ Common mistakes

1. Confusing query with path for IDs
2. Not validating types in query params
3. Creating ambiguous routes that collide
