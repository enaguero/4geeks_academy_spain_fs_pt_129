# 🧱 Step 7: Refactor a Servicio Simple (Flask)

## 🎯 Objetivo

Separar responsabilidades para que el código crezca sin volverse caótico.

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
flask --app day_23/flask_api/step7-refactor-servicio-simple/main.py --debug run
```

---

## 🧠 ¿Qué problema resuelve este refactor?

En proyectos reales, meter todo en `main.py` se vuelve difícil de mantener.

Analogía diaria:
- Cocina profesional: cada persona tiene rol.
- API profesional: rutas, validación, acceso a datos y reglas separadas.

---

## 🗂️ Estructura sugerida

```text
step7-refactor-servicio-simple/
├── main.py        # Endpoints HTTP
├── schemas.py     # Modelos de entrada/salida
├── repository.py  # Acceso a datos (en memoria)
└── service.py     # Reglas de negocio
```

---

## ✅ Beneficios

1. Código más legible
2. Menos duplicación
3. Mejor testabilidad
4. Evolución simple hacia base de datos real

---

## 🧪 Ejercicios

1. Añade endpoint `PATCH /tasks/{id}/done`
2. Impide títulos duplicados en `service.py`
3. Añade query `done=true` filtrando desde servicio
