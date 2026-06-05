[🇪🇸 Español](README.md) | 🇬🇧 **English**

# ⚡ Day 23: Your First API (Two tracks)

This day is organized into two versions with the same content:

- `day_23/fast_api`
- `day_23/flask_api`

## 🗂️ Expected structure

```text
day_23/
├── fast_api/
│   ├── step0-contexto-api-http/
│   ├── step1-primer-servidor/
│   ├── step2-rutas-y-parametros/
│   ├── step3-crud-en-memoria/
│   ├── step4-modelos-pydantic/
│   ├── step5-status-codes-y-errores/
│   ├── step6-documentacion-y-pruebas/
│   ├── step7-refactor-servicio-simple/
│   ├── step8-mini-retos/
│   └── step9-proyecto-first-api/
└── flask_api/
    ├── step0-contexto-api-http/
    ├── step1-primer-servidor/
    ├── step2-rutas-y-parametros/
    ├── step3-crud-en-memoria/
    ├── step4-modelos-pydantic/
    ├── step5-status-codes-y-errores/
    ├── step6-documentacion-y-pruebas/
    ├── step7-refactor-servicio-simple/
    ├── step8-mini-retos/
    └── step9-proyecto-first-api/
```

## 🚀 One-time setup

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

## ▶️ Running each track

FastAPI:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/<step>
```

Flask:

```bash
flask --app day_23/flask_api/<step>/main.py --debug run
```

## 🧭 Recommendation

Pick one track and follow `step0 -> step9` without skipping.
