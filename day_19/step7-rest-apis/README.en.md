[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 7: REST APIs 🏭

## 🔗 Recap: What You Already Know

You've learned:
1. ✅ **Step 0**: API, JSON, HTTP and REST concepts
2. ✅ **Steps 1-5**: Promises and Async/Await - Handling async operations
3. ✅ **Step 6**: Fetch - Making HTTP requests and working with JSON

Now we'll dig deeper into:
- 🎯 **REST**: The architecture that ties it all together
- 🎯 **CRUD**: The four fundamental operations
- 🎯 **API design**: How to structure endpoints

---

## 🎯 Now: REST - The Architecture That Ties It Together

**REST** isn't a technology, it's a **set of rules** for designing APIs that use HTTP and JSON.

### The Full Relationship:

```
REST API (architecture)
    ├─> Uses HTTP (protocol)
    │       ├─> GET /usuarios
    │       ├─> POST /usuarios
    │       ├─> PUT /usuarios/1
    │       └─> DELETE /usuarios/1
    │
    ├─> Exchanges JSON (format)
    │       {
    │         "id": 1,
    │         "nombre": "Juan"
    │       }
    │
    └─> Is consumed with Fetch (tool)
            fetch('/usuarios')
```

**In other words:** REST is the design "style", HTTP is the "protocol", JSON is the "language", and Fetch is your "tool".

---

## What Is REST?

**REST** (Representational State Transfer) is an architectural style for designing APIs. It defines conventions for client-server communication.

Example: A book API

```
GET    /api/libros           - Get all books
GET    /api/libros/1         - Get book with ID 1
POST   /api/libros           - Create a new book
PUT    /api/libros/1         - Update book 1
DELETE /api/libros/1         - Delete book 1
```

## REST Principles

1. **Client-Server**: Clear separation between who asks and who answers
2. **Stateless**: Each request is independent
3. **Resources**: Everything is a resource (books, users, posts)
4. **HTTP methods**: GET (retrieve), POST (create), PUT (update), DELETE (delete)
5. **Representation**: Data in JSON, XML, etc.

## Structure of a REST API

### URL = Resource
```
/api/usuarios      - Resource "usuarios"
/api/usuarios/1    - Specific resource "usuario 1"
/api/usuarios/1/posts - Related resource "posts of usuario 1"
```

### HTTP Method = Action
```
GET    /usuarios       → Get the list
GET    /usuarios/1     → Get one
POST   /usuarios       → Create
PUT    /usuarios/1     → Update
DELETE /usuarios/1     → Delete
```

## Example: Tasks CRUD

```javascript
// 1. CREATE
async function crearTarea(titulo) {
  const res = await fetch('/api/tareas', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ titulo, completada: false })
  });
  return res.json();
}

// 2. READ
async function obtenerTareas() {
  const res = await fetch('/api/tareas');
  return res.json();
}

// 3. UPDATE
async function actualizarTarea(id, datos) {
  const res = await fetch(`/api/tareas/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datos)
  });
  return res.json();
}

// 4. DELETE
async function eliminarTarea(id) {
  await fetch(`/api/tareas/${id}`, { method: 'DELETE' });
}
```

## Semantic Status Codes

| Code | Use Case |
|--------|-----------|
| 200 | OK - Successful request |
| 201 | Created - Resource created |
| 400 | Bad Request - Invalid data |
| 401 | Unauthorized - Not authenticated |
| 403 | Forbidden - No permissions |
| 404 | Not Found - Doesn't exist |
| 500 | Server Error - Server error |

## Standard Responses

### Success
```json
{
  "success": true,
  "data": { "id": 1, "titulo": "Mi tarea" },
  "message": "Tarea creada"
}
```

### Error
```json
{
  "success": false,
  "error": "titulo es requerido",
  "code": 400
}
```

## Example: Real API (JSONPlaceholder)

```javascript
// Get posts
const posts = await fetch('https://jsonplaceholder.typicode.com/posts')
  .then(r => r.json());

// Get comments on a post
const comentarios = await fetch('https://jsonplaceholder.typicode.com/comments?postId=1')
  .then(r => r.json());

// Create user (fake)
const nuevoUsuario = await fetch('https://jsonplaceholder.typicode.com/users', {
  method: 'POST',
  body: JSON.stringify({
    name: 'Juan',
    email: 'juan@example.com'
  })
}).then(r => r.json());
```

## Difference: Query String vs Path

```javascript
// Path: /api/tareas/1
GET https://api.example.com/tareas/1

// Query String: /api/tareas?userId=1&completada=true
GET https://api.example.com/tareas?userId=1&completada=true

// Combined
GET https://api.example.com/tareas/1?format=json
```

## Key Points ✨

1. **HTTP methods**: GET, POST, PUT, DELETE
2. **Resources**: Paths like /usuarios, /posts
3. **Status codes**: Use appropriate HTTP codes
4. **Format**: Usually JSON
5. **Stateless**: No dependencies between requests

## Your Exercise 🎯

Study the JSONPlaceholder API:
https://jsonplaceholder.typicode.com/

Build functions to:
1. ✅ GET /posts - Get all posts
2. ✅ GET /posts/1 - Get a specific post
3. ✅ POST /posts - Create a new post
4. ✅ DELETE /posts/1 - Delete a post

---

**💡 Tip**: REST is a pattern, not a protocol. Different APIs implement it in slightly different ways.
