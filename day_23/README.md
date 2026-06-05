🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# ⚡ Día 23: Tu Primera API (Dos tracks)

Este día está organizado en dos versiones con el mismo contenido:

- `day_23/fast_api`
- `day_23/flask_api`

## 🗂️ Estructura esperada

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

## 🚀 Setup único

Desde la raíz del repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

## ▶️ Ejecución por track

FastAPI:

```bash
uvicorn main:app --reload --app-dir day_23/fast_api/<step>
```

Flask:

```bash
flask --app day_23/flask_api/<step>/main.py --debug run
```

## 🧭 Recomendación

Elige un track y sigue `step0 -> step9` sin saltos.
