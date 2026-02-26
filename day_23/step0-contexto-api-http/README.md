# 🧭 Step 0: Ambiente Virtual + Contexto API + HTTP

## 🎯 Objetivo

Preparar un entorno virtual reutilizable para todo el Día 23 y entender cómo se comunica un cliente con una API REST.

---

## 🧪 ¿Qué es un ambiente virtual (`venv`)?

Un entorno virtual es una "caja aislada" de dependencias Python para tu proyecto.

Analogía diaria:
- Es como una cocina separada para una receta.
- Tus ingredientes de esta receta no se mezclan con otros proyectos.

Beneficios:
- Evitas conflictos entre versiones de librerías
- Todos en el equipo usan el mismo setup
- Puedes borrar y recrear el entorno cuando quieras

---

## ⚙️ Setup transversal (hazlo una sola vez)

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

Verifica instalación:

```bash
python -m pip show fastapi
python -m pip show uvicorn
```

Para salir del entorno virtual:

```bash
deactivate
```

> Nota: mientras trabajes en el Día 23, mantén el entorno activo.

---

## ▶️ Cómo ejecutar cualquier ejercicio del Día 23

Patrón general:

```bash
uvicorn main:app --reload --app-dir day_23/<carpeta-del-step>
```

Ejemplo real:

```bash
uvicorn main:app --reload --app-dir day_23/step1-primer-servidor-fastapi
```

Abre en navegador:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

---

## 🌐 ¿Qué es una API?

Una API es un contrato de comunicación entre sistemas.

Analogía diaria:
- Tú (cliente) pides comida
- El camarero (API) recibe el pedido
- La cocina (backend) procesa
- El camarero te devuelve el plato o un error

La API no cocina, pero organiza la comunicación.

---

## 🔄 Flujo Request/Response

```text
Frontend / App móvil
    ↓ (HTTP request)
API FastAPI
    ↓ (lógica)
Base de datos o memoria
    ↓
API responde JSON + status code
```

Ejemplo mental:
- Request: "dame la tarea 5"
- Response 200: `{ "id": 5, "title": "Estudiar" }`
- Response 404: `{ "detail": "Tarea no encontrada" }`

---

## 🧱 Piezas clave que usarás hoy

- `HTTP methods`: `GET`, `POST`, `PUT`, `DELETE`
- `Status codes`: `200`, `201`, `400`, `404`, `500`
- `JSON`: formato de intercambio de datos
- `Endpoint`: una URL específica de tu API (`/tasks`, `/users/3`)

---

## ⚠️ Errores comunes al empezar

1. Instalar librerías fuera del entorno virtual
2. Olvidar activar `.venv` antes de ejecutar `uvicorn`
3. Mezclar conceptos frontend/backend
4. Ignorar códigos HTTP y devolver siempre `200`

---

## ✅ Resultado esperado de este step

Si terminaste bien este step, puedes:

- Explicar qué es y para qué sirve un `venv`
- Configurar FastAPI una sola vez para todos los ejercicios
- Ejecutar cualquier step con el patrón `--app-dir`
- Explicar el flujo básico request/response
