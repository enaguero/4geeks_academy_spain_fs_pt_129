# 🧭 Step 0: Contexto API + HTTP

## 🎯 Objetivo

Entender qué es una API, para qué sirve y cómo se mueve la información entre cliente y servidor.

---

## 🌐 ¿Qué es una API?

Una API es un contrato de comunicación entre sistemas.

Analogía diaria:
- Tú (cliente) pides comida
- El camarero (API) recibe el pedido
- La cocina (backend) procesa
- El camarero te devuelve el plato o un error

La API no cocina, pero organiza la comunicación.

---

## 🔄 Flujo Request/Response

```text
Frontend / App móvil
    ↓ (HTTP request)
API FastAPI
    ↓ (lógica)
Base de datos o memoria
    ↓
API responde JSON + status code
```

Ejemplo mental:
- Request: "dame la tarea 5"
- Response 200: `{ "id": 5, "title": "Estudiar" }`
- Response 404: `{ "detail": "Tarea no encontrada" }`

---

## 🧱 Piezas clave que usarás hoy

- `HTTP methods`: `GET`, `POST`, `PUT`, `DELETE`
- `Status codes`: `200`, `201`, `400`, `404`, `500`
- `JSON`: formato de intercambio de datos
- `Endpoint`: una URL específica de tu API (`/tasks`, `/users/3`)

---

## 🧠 Mini ejercicio rápido

Clasifica cada acción:

1. Mostrar lista de productos en pantalla
2. Guardar un nuevo producto
3. Validar que el precio no sea negativo
4. Devolver error si no existe el producto

Pista: 1 es frontend, 2-4 son API/backend.

---

## ⚠️ Errores comunes al empezar APIs

1. Mezclar conceptos de vista (frontend) con lógica backend
2. Ignorar códigos HTTP y devolver siempre `200`
3. No validar entradas desde el cliente

---

## ✅ Resultado esperado de este step

Si lo tienes claro, puedes explicar:

- Qué papel cumple una API
- Cómo viajan los datos con HTTP
- Por qué status codes y JSON son parte del contrato
