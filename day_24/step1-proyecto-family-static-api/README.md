# 🏁 Step 1: Proyecto - Family Static API (Flask)

## 🎯 Objetivo

Construir una API estática en Flask aplicando OOP para modelar una familia y exponer operaciones básicas por HTTP.

---

## 🧰 Requisitos para correr el proyecto

- Entorno virtual activo
- Dependencias instaladas desde `day_24/requirements.txt`
- Entender la base de OOP del `step0`

---

## 📦 Instalación (si aún no instalaste dependencias)

```bash
source .venv/bin/activate
pip install -r day_24/requirements.txt
```

---

## ▶️ Cómo correr este proyecto

1. Implementa tu proyecto dentro de esta carpeta.
2. Cuando tengas `main.py`, ejecuta:

```bash
flask --app day_24/step1-proyecto-family-static-api/main.py --debug run
```

3. Prueba tu API en:
- `http://127.0.0.1:5000/`

---

## ⚠️ Importante

Este step no trae solución final cerrada.

Incluye:
- Requisitos funcionales
- Estructura sugerida
- Criterios de calidad

Tú implementas el proyecto.

---

## 📋 Descripción

Vas a crear una **Family Static API** con Flask.

La API debe representar una familia en memoria y permitir:

- Consultar todos los miembros
- Consultar un miembro por ID
- Añadir nuevos miembros
- Eliminar miembros existentes

---

## 🗂️ Estructura sugerida

```text
family_static_api/
├── main.py
├── family.py
├── member.py
└── README.md
```

---

## ✅ Requisitos funcionales mínimos

1. `GET /members`
2. `GET /members/<int:member_id>`
3. `POST /members`
4. `DELETE /members/<int:member_id>`

Payload sugerido para crear miembro:

```json
{
  "first_name": "Ana",
  "age": 28,
  "lucky_numbers": [3, 7, 21]
}
```

---

## 🧠 Reglas de negocio sugeridas

- `first_name` obligatorio y no vacío
- `age` mayor o igual a 0
- `lucky_numbers` debe ser lista de enteros
- Si no existe un miembro, responder `404`

---

## 🧪 Plan de pruebas mínimo

1. Listar miembros al iniciar
2. Crear miembro válido
3. Intentar crear miembro inválido
4. Buscar miembro existente
5. Buscar miembro inexistente
6. Eliminar miembro existente
7. Verificar que realmente se eliminó

---

## ✅ Criterios de entrega

- Separación clara entre lógica de dominio y rutas Flask
- Nombres de clases/métodos legibles
- Respuestas JSON consistentes
- Status codes correctos (`200`, `201`, `204`, `404`, `400`)
- API demostrable con requests reproducibles

---

## 🔗 Enlace del proyecto oficial

- [Family Static API with Flask](https://4geeks.com/syllabus/spain-fs-pt-129/project/family-static-api)
