# 🛣️ Step 2: Rutas y Parámetros

## 🎯 Objetivo

Aprender a recibir datos desde la URL con `path params` y `query params`.

---

## 🧰 Requisitos para correr este step

- Setup transversal completado en Step 0
- Entorno virtual activo
- Dependencias instaladas desde `day_23/requirements.txt`

---

## 📦 Instalación (si aún no instalaste dependencias)

```bash
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## ▶️ Cómo correr este step

```bash
uvicorn main:app --reload --app-dir day_23/step2-rutas-y-parametros
```

Abre:
- `http://127.0.0.1:8000/docs`

---

## 🧭 Path params vs Query params

### Path params
Van dentro de la ruta y suelen identificar un recurso único.

Ejemplo: `/users/15`

### Query params
Van al final de la URL y suelen filtrar o paginar.

Ejemplo: `/users?limit=10&active=true`

---

## 🧠 Analogía diaria

- Path param: número de puerta de una casa (`/casas/12`)
- Query param: preferencias del pedido (`?sin_cebolla=true`)

---

## 🧪 Ejemplos

- `GET /products/4` -> detalle del producto 4
- `GET /products?limit=5` -> primeros 5 productos
- `GET /search?q=python` -> búsqueda por texto

---

## ✅ Buenas prácticas rápidas

1. Usa nombres claros (`product_id`, no `x`)
2. Tipa parámetros (`int`, `bool`, `str`)
3. Define defaults razonables en query params

---

## ⚠️ Errores comunes

1. Confundir query con path para IDs
2. No tipar parámetros y recibir tipos incorrectos
3. Crear rutas ambiguas que colisionan
