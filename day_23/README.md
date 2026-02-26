# ⚡ Día 23: Tu Primera API con FastAPI

## 🎯 Objetivos de Aprendizaje

Hoy pasas de scripts a servicios web. Al terminar este día deberías poder:

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

### Step 0: Contexto API + HTTP 🧭
**Carpeta**: `step0-contexto-api-http/`

Qué problema resuelve una API y cómo encaja HTTP en el flujo frontend-backend.

### Step 1: Primer Servidor con FastAPI 🚀
**Carpeta**: `step1-primer-servidor-fastapi/`

Instalación mínima, primer endpoint y ejecución con `uvicorn`.

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
- [ ] Puedo crear rutas con `path` y `query params`
- [ ] Puedo implementar CRUD básico en memoria
- [ ] Puedo validar entradas con Pydantic
- [ ] Puedo responder con status codes correctos
- [ ] Puedo probar endpoints desde `/docs` y `curl`
