🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🏁 Step 9: Proyecto - First API con Flask

## 🎯 Objetivo

Construir una API completa de tareas aplicando todo lo aprendido en el día.

---

## 🧰 Requisitos para correr el proyecto

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

## ▶️ Cómo correr este proyecto

1. Implementa tu proyecto dentro de esta carpeta (siguiendo la estructura sugerida).
2. Cuando tengas `main.py`, ejecuta:

```bash
flask --app day_23/flask_api/step9-proyecto-first-api/main.py --debug run
```

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

Vas a crear una **Todo API** con Flask para un frontend futuro.

Tu API debe permitir:

- Crear tareas
- Listar tareas
- Consultar detalle por ID
- Actualizar tarea
- Eliminar tarea
- Filtrar por estado (`done=true|false`)

---

## 🔧 Requisitos técnicos mínimos

- Flask
- Modelos Pydantic para entrada/salida
- Al menos 5 endpoints CRUD
- Manejo de errores (`404`, `409`, `422`)
- Status codes correctos (`200`, `201`, `204`)
- README con ejemplos de consumo

---

## 🗂️ Estructura sugerida

```text
first_api_flask/
├── main.py
├── schemas.py
├── repository.py
├── service.py
└── README.md
```

---

## ✅ Requisitos funcionales

### 1. Crear tarea
- `POST /tasks`
- Body: `title`, `priority` (1..5), `done` opcional
- Respuesta `201`

### 2. Listar tareas
- `GET /tasks`
- Filtro opcional `done`
- Respuesta `200`

### 3. Ver detalle
- `GET /tasks/{task_id}`
- Si no existe, `404`

### 4. Actualizar tarea
- `PUT /tasks/{task_id}`
- Permitir cambiar `title`, `priority`, `done`
- Si no existe, `404`

### 5. Eliminar tarea
- `DELETE /tasks/{task_id}`
- Respuesta `204`

---

## 🧠 Reglas de negocio sugeridas

- No permitir títulos vacíos
- No permitir títulos duplicados (case-insensitive)
- `priority` siempre entre 1 y 5

---

## 🧪 Plan de pruebas mínimo

1. Crear tarea válida
2. Crear tarea inválida (title corto)
3. Consultar tarea existente
4. Consultar tarea inexistente
5. Actualizar tarea
6. Eliminar tarea
7. Confirmar que se eliminó

---

## ✅ Criterios de entrega

- Código legible y con nombres claros
- Endpoints consistentes
- Errores manejados de forma explícita
- API demostrable con requests reproducibles
- README con instrucciones para ejecutar
