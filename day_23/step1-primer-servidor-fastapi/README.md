# 🚀 Step 1: Primer Servidor con FastAPI

## 🎯 Objetivo

Levantar tu primera API moderna con FastAPI y exponer endpoints básicos.

---

## 🧰 Requisitos para correr este step

- Haber completado el setup transversal del Step 0
- Entorno virtual activo (`source .venv/bin/activate`)
- Dependencias instaladas (`fastapi`, `uvicorn`)

---

## 📦 Instalación (solo si aún no hiciste Step 0)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## 🧩 Primer archivo `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API viva"}
```

---

## ▶️ Ejecutar servidor

```bash
uvicorn main:app --reload --app-dir day_23/step1-primer-servidor-fastapi
```

- `main`: nombre del archivo
- `app`: objeto FastAPI
- `--reload`: reinicia al guardar cambios

Abre:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

---

## 🧠 Analogía diaria

`uvicorn` es como encender la persiana del local.
Sin servidor encendido, no hay quién reciba pedidos.

---

## 🧪 Ejercicios cortos

1. Crea endpoint `GET /health` que devuelva `{ "status": "ok" }`
2. Crea endpoint `GET /saludo` que devuelva un mensaje personalizado
3. Cambia el título de la API con `FastAPI(title="...")`

---

## ⚠️ Errores comunes

1. Ejecutar `python main.py` esperando que sirva HTTP
2. Escribir mal `main:app` en el comando de `uvicorn`
3. No activar el entorno virtual
