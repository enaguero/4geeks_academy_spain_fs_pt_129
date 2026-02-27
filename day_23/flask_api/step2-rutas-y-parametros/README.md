# 🛣️ Step 2: Rutas y Parámetros (Flask)

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
flask --app day_23/flask_api/step2-rutas-y-parametros/main.py --debug run
```

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
2. Convierte tipos manualmente en Flask (`int`, `bool`)
3. Define defaults razonables en query params

---

## ⚠️ Errores comunes

1. Confundir query con path para IDs
2. No validar tipos en query params
3. Crear rutas ambiguas que colisionan
