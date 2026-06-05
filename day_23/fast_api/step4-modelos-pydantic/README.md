🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# ✅ Step 4: Modelos y Validación con Pydantic

## 🎯 Objetivo

Validar entradas automáticamente para proteger tu API de datos inválidos.

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
uvicorn main:app --reload --app-dir day_23/fast_api/step4-modelos-pydantic
```

Abre:
- `http://127.0.0.1:8000/docs`

---

## 🧩 ¿Qué resuelve Pydantic?

Sin validación, el cliente puede enviar datos rotos.
Con Pydantic, defines reglas claras de entrada/salida.

Analogía diaria:
- Es como un formulario con reglas en recepción.
- Si falta DNI o está mal, no se procesa la solicitud.

---

## 🛠️ Beneficios inmediatos

1. Validación de tipos (`int`, `bool`, `str`)
2. Reglas de negocio simples (`min_length`, `ge`, `le`)
3. Errores HTTP 422 automáticos cuando el body no cumple
4. Documentación Swagger más clara

---

## 📌 Reglas recomendadas para este step

- `title` obligatorio y con longitud mínima
- `priority` entre 1 y 5
- `done` booleano

---

## 🧪 Ejercicios

1. Añade campo `owner_email` con validación de email
2. Crea un modelo de salida que no exponga campos internos
3. Define un modelo para actualización parcial (`PATCH`)
