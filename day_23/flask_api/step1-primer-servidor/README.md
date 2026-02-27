# 🚀 Step 1: Primer Servidor con Flask

## 🎯 Objetivo

Levantar tu primera API con Flask y exponer endpoints básicos.

---

## 🧰 Requisitos para correr este step

- Haber completado el setup transversal del Step 0
- Entorno virtual activo (`source .venv/bin/activate`)
- Dependencias instaladas (`flask`)

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
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({"message": "API viva"})
```

---

## ▶️ Ejecutar servidor

```bash
flask --app day_23/flask_api/step1-primer-servidor/main.py --debug run
```

Abre:
- `http://127.0.0.1:5000/`

---

## 🧠 Analogía diaria

El comando `flask --app ... run` es como encender la persiana del local.
Sin servidor encendido, no hay quién reciba pedidos.

---

## 🧪 Ejercicios cortos

1. Crea endpoint `GET /health` que devuelva `{ "status": "ok" }`
2. Crea endpoint `GET /saludo` que devuelva un mensaje personalizado
3. Añade configuración básica para JSON ordenado: `app.config["JSON_SORT_KEYS"] = False`

---

## ⚠️ Errores comunes

1. Ejecutar `python main.py` sin configurar modo debug
2. No apuntar bien el `--app` al archivo correcto
3. No activar el entorno virtual
