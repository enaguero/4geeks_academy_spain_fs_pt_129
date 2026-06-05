🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🧭 Step 0: Ambiente Virtual + Contexto API + HTTP (Flask)

## 🎯 Objetivo

Preparar el entorno virtual para el track de Flask y entender el flujo request/response.

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
python -m pip show flask
```

---

## ▶️ Cómo ejecutar cualquier step de Flask

Patrón general:

```bash
flask --app day_23/flask_api/<step>/main.py --debug run
```

Ejemplo:

```bash
flask --app day_23/flask_api/step1-primer-servidor/main.py --debug run
```

Abre en navegador:
- `http://127.0.0.1:5000/`

---

## 🔄 Flujo base API

```text
Cliente
  ↓ HTTP
Flask
  ↓ lógica
Memoria/DB
  ↓
JSON + status code
```

---

## ✅ Resultado esperado

- Entorno virtual listo
- Flask ejecutando por step
- Claridad en request/response y status codes
