# 🧭 Step 0: Ambiente Virtual + Contexto API + HTTP (FastAPI)

## 🎯 Objetivo

Preparar el entorno virtual para el track de FastAPI y entender el flujo request/response.

---

## ⚙️ Setup (una sola vez)

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

---

## ▶️ Cómo ejecutar cualquier step de FastAPI

Patrón general:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/<step>
```

Ejemplo:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/step1-primer-servidor
```

Abre en navegador:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

---

## 🔄 Flujo base API

```text
Cliente
  ↓ HTTP
FastAPI
  ↓ lógica
Memoria/DB
  ↓
JSON + status code
```

---

## ✅ Resultado esperado

- Entorno virtual listo
- FastAPI ejecutando por step
- Claridad en request/response y status codes
