🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 📦 Step 3: CRUD en Memoria (Flask)

## 🎯 Objetivo

Implementar un CRUD completo sin base de datos, usando una lista en memoria.

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
flask --app day_23/flask_api/step3-crud-en-memoria/main.py --debug run
```

---

## 🧠 ¿Por qué en memoria primero?

Porque te permite practicar el flujo de API sin complejidad extra.

Analogía diaria:
- Es una pizarra del aula.
- Funciona para practicar.
- Al cerrar la clase, se borra todo.

---

## 🛠️ Endpoints CRUD básicos

- `GET /tasks` -> listar
- `GET /tasks/{task_id}` -> detalle
- `POST /tasks` -> crear
- `PUT /tasks/{task_id}` -> actualizar
- `DELETE /tasks/{task_id}` -> eliminar

---

## ✅ Conceptos que consolidar

1. Buscar recurso por ID
2. Responder `404` cuando no existe
3. Devolver `201` al crear
4. Mantener IDs consistentes

---

## ⚠️ Limitación esperada

Si reinicias el servidor, se pierde todo. Es normal en este step.
El objetivo es entender API design, no persistencia todavía.

---

## 🧪 Ejercicios

1. Añade filtro `done=true/false` en `GET /tasks`
2. Ordena tareas por ID descendente con query param `sort=desc`
3. Evita crear tareas duplicadas por título
