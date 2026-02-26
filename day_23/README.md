# ⚡ Día 23: Tu Primera API con FastAPI

## 🎯 Objetivos de Aprendizaje

Hoy pasas de scripts a servicios web. Al terminar este día deberías poder:

- Crear y activar un entorno virtual de Python reutilizable para toda la clase
- Entender el flujo completo `cliente -> request HTTP -> API -> response JSON`
- Levantar un servidor FastAPI y exponer endpoints
- Diferenciar y usar `path params`, `query params` y `request body`
- Implementar un CRUD básico (`GET`, `POST`, `PUT`, `DELETE`)
- Validar datos con modelos Pydantic
- Usar códigos HTTP correctos y manejar errores con `HTTPException`
- Probar la API en Swagger (`/docs`) y con `curl`
- Diseñar y arrancar un mini proyecto de API moderna

---

## 🗺️ Mapa Mental del Día

```text
HTTP + JSON
    ↓
Servidor FastAPI
    ↓
Rutas y parámetros
    ↓
CRUD en memoria
    ↓
Validación con Pydantic
    ↓
Errores + status codes
    ↓
Documentación y pruebas
    ↓
Mini proyecto API
```

Piensa en una API como el mostrador de un restaurante:
- El cliente hace un pedido (request)
- La cocina procesa (lógica backend)
- El camarero devuelve resultado (response)

---

## 📚 Estructura del Día

Este día tiene **10 pasos progresivos**.

### Step 0: Ambiente Virtual + Contexto API 🧭
**Carpeta**: `step0-contexto-api-http/`

Configurar un entorno virtual reutilizable para todo el día y entender el flujo HTTP/API.

### Step 1: Primer Servidor con FastAPI 🚀
**Carpeta**: `step1-primer-servidor-fastapi/`

Crear el primer endpoint y ejecutar FastAPI con `uvicorn`.

### Step 2: Rutas y Parámetros 🛣️
**Carpeta**: `step2-rutas-y-parametros/`

`path params`, `query params` y diseño de endpoints claros.

### Step 3: CRUD en Memoria 📦
**Carpeta**: `step3-crud-en-memoria/`

Crear, listar, editar y eliminar recursos en una lista temporal.

### Step 4: Modelos y Validación con Pydantic ✅
**Carpeta**: `step4-modelos-pydantic/`

Validar datos de entrada para evitar errores y datos basura.

### Step 5: Status Codes y Manejo de Errores 🚨
**Carpeta**: `step5-status-codes-y-errores/`

Respuestas HTTP profesionales y errores controlados.

### Step 6: Documentación y Pruebas 🧪
**Carpeta**: `step6-documentacion-y-pruebas/`

Uso de `/docs`, `/redoc` y pruebas con `curl`.

### Step 7: Refactor a Servicio Simple 🧱
**Carpeta**: `step7-refactor-servicio-simple/`

Separar responsabilidades en módulos para escalar mejor.

### Step 8: Mini Retos FastAPI 🧠
**Carpeta**: `step8-mini-retos-fastapi/`

Retos cortos para reforzar diseño y validaciones.

### Step 9: Proyecto - First API con FastAPI 🏁
**Carpeta**: `step9-proyecto-first-api-fastapi/`

Proyecto guiado sin solución cerrada para consolidar todo.

---

## 🧭 Buenas Prácticas de Diseño REST

### 1. Diseña recursos, no acciones
Usa sustantivos en plural y deja la acción al método HTTP.

- Bien: `GET /tasks`, `POST /tasks`, `PUT /tasks/{task_id}`
- Evitar: `GET /getTasks`, `POST /createTask`

### 2. Sé consistente en nombres y estructura

- Mantén un estilo único (`snake_case` o `kebab-case` en paths)
- Usa el mismo patrón en todos los endpoints
- Evita mezclar singular/plural sin motivo

### 3. Usa status codes semánticos

- `200` para lecturas/actualizaciones correctas
- `201` para creación
- `204` para eliminación sin contenido
- `404` cuando un recurso no existe
- `422` cuando falla validación de datos

### 4. Diseña endpoints simples y predecibles

- Filtros, búsqueda y paginación con query params
- IDs en path params
- Evita respuestas con formatos distintos para endpoints similares

### 5. Maneja errores de forma uniforme

- Mensajes claros para cliente (`detail`)
- Misma forma de error en toda la API
- No ocultar errores de validación

---

## 🌳 Niveles de Anidación de Recursos

Regla práctica para APIs mantenibles:

- Recomendado: `1` o `2` niveles
- Aceptable en casos puntuales: `3` niveles
- Evitar: más de `3` niveles

Ejemplos:

- Bien: `/users/{user_id}/orders`
- Bien: `/orders/{order_id}/items`
- Aceptable puntual: `/companies/{company_id}/teams/{team_id}/members`
- Evitar: `/a/{a_id}/b/{b_id}/c/{c_id}/d/{d_id}/e/{e_id}`

Cuando la ruta se vuelve muy profunda, suele ser mejor desacoplar:

- Mejor alternativa: `/orders?user_id=10&status=paid`

Así reduces acoplamiento entre recursos y simplificas consumo.

---

## 📚 Cómo Documentar una API REST

Una documentación útil debe incluir, por endpoint:

- Método HTTP + ruta
- Descripción funcional
- Parámetros de path/query
- Body de entrada (ejemplo válido)
- Respuesta esperada (ejemplo)
- Códigos de estado y errores posibles
- Requisitos de autenticación (si aplica)

El estándar más usado es **OpenAPI**.

---

## ⚡ Cómo FastAPI Resuelve la Documentación

FastAPI genera documentación automáticamente desde tu código:

- OpenAPI JSON en `/openapi.json`
- Swagger UI interactivo en `/docs`
- ReDoc en `/redoc`
- Esquemas de request/response generados desde modelos Pydantic

Eso reduce el trabajo manual y evita que código y documentación se desalineen.

También puedes enriquecer documentación con metadatos:

```python
@app.post(
    "/tasks",
    summary="Crear una nueva tarea",
    description="Crea una tarea validando title y priority",
    tags=["Tasks"],
)
def create_task(payload: TaskCreate):
    ...
```

---

## 🧪 Setup Transversal (una sola vez para todo el Día 23)

Este setup aplica a todos los ejercicios del día.  
No necesitas crear un entorno virtual por step.

### Requisitos

- Python 3.10+ (`python3 --version`)
- `pip` disponible

### Instalación única

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

### Patrón para ejecutar cualquier step con API

```bash
uvicorn main:app --reload --app-dir day_23/<carpeta-del-step>
```

Ejemplos:

- `uvicorn main:app --reload --app-dir day_23/step1-primer-servidor-fastapi`
- `uvicorn main:app --reload --app-dir day_23/step5-status-codes-y-errores`

---

## 🚀 Cómo Usar Este Material

### 1. Sigue el orden
Cada step asume el anterior. Evita saltar de Step 1 al Step 5.

### 2. Ejecuta cada ejemplo
Lee, ejecuta, rompe y corrige. No hagas lectura pasiva.

### 3. Valida siempre entradas
Si tu API acepta cualquier cosa, el problema aparece después.

### 4. Practica respuesta semántica
No solo importa que funcione: importa responder bien (`200`, `201`, `404`, etc.).

---

## 🔗 Requisitos Previos

Antes de este día deberías dominar (Día 22):

- Variables, condicionales, listas y funciones en Python
- Ejecución de scripts con `python3`
- Lectura básica de mensajes de error

---

## 📖 Lecturas Oficiales (Syllabus)

Estas lecturas siguen siendo útiles por los conceptos HTTP/REST.
La implementación de esta clase se hace con **FastAPI**.

- [Building RESTful APIs using Flask](https://4geeks.com/syllabus/spain-fs-pt-129/read/building-apis-with-python-flask)
- [Interactive Todo List API with Python and Flask](https://4geeks.com/syllabus/spain-fs-pt-129/project/python-flask-api-tutorial)

## 📘 Referencias Extra (FastAPI)

- [FastAPI - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI - Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [FastAPI - Body and Pydantic Models](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI - Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)

---

## ✅ Checklist de Cierre del Día

Marca esto antes de pasar al Día 24:

- [ ] Puedo levantar FastAPI con `uvicorn`
- [ ] Puedo crear/activar un entorno virtual para trabajar todo el día
- [ ] Puedo crear rutas con `path` y `query params`
- [ ] Puedo implementar CRUD básico en memoria
- [ ] Puedo validar entradas con Pydantic
- [ ] Puedo responder con status codes correctos
- [ ] Puedo probar endpoints desde `/docs` y `curl`
