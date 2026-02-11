# Step 7: REST APIs 🏭

## 🔗 Recapitulación: Lo Que Ya Sabes

Has aprendido:
1. ✅ **Step 0**: Conceptos de API, JSON, HTTP y REST
2. ✅ **Steps 1-5**: Promises y Async/Await - Manejar operaciones asíncronas
3. ✅ **Step 6**: Fetch - Hacer peticiones HTTP y trabajar con JSON

Ahora profundizaremos en:
- 🎯 **REST**: La arquitectura que une todo
- 🎯 **CRUD**: Las 4 operaciones fundamentales
- 🎯 **Diseño de APIs**: Cómo estructurar endpoints

---

## 🎯 Ahora: REST - La Arquitectura que Une Todo

**REST** no es una tecnología, es un **conjunto de reglas** para diseñar APIs que usan HTTP y JSON.

### La Relación Completa:

```
REST API (arquitectura)
    ├─> Usa HTTP (protocolo)
    │       ├─> GET /usuarios
    │       ├─> POST /usuarios
    │       ├─> PUT /usuarios/1
    │       └─> DELETE /usuarios/1
    │
    ├─> Intercambia JSON (formato)
    │       {
    │         "id": 1,
    │         "nombre": "Juan"
    │       }
    │
    └─> Se consume con Fetch (herramienta)
            fetch('/usuarios')
```

**En otras palabras:** REST es el "estilo" de diseño, HTTP es el "protocolo", JSON es el "idioma", y Fetch es tu "herramienta".

---

## ¿Qué es REST?

**REST** (Representational State Transfer) es un estilo arquitectónico para diseñar APIs. Define convenciones para comunicación entre cliente y servidor.

Ejemplo: Una API de libros

```
GET    /api/libros           - Obtener todos los libros
GET    /api/libros/1         - Obtener libro con ID 1
POST   /api/libros           - Crear nuevo libro
PUT    /api/libros/1         - Actualizar libro 1
DELETE /api/libros/1         - Eliminar libro 1
```

## Principios de REST

1. **Cliente-Servidor**: Separación clara entre quien pide y quien responde
2. **Stateless**: Cada petición es independiente
3. **Recursos**: Todo es un recurso (libros, usuarios, posts)
4. **Métodos HTTP**: GET (obtener), POST (crear), PUT (actualizar), DELETE (eliminar)
5. **Representación**: Datos en JSON, XML, etc.

## Estructura de una API REST

### URL = Recurso
```
/api/usuarios      - Recurso "usuarios"
/api/usuarios/1    - Recurso específico "usuario 1"
/api/usuarios/1/posts - Recurso relacionado "posts del usuario 1"
```

### Método HTTP = Acción
```
GET    /usuarios       → Obtener lista
GET    /usuarios/1     → Obtener uno
POST   /usuarios       → Crear
PUT    /usuarios/1     → Actualizar
DELETE /usuarios/1     → Eliminar
```

## Ejemplo: CRUD de Tareas

```javascript
// 1. CREAR (CREATE)
async function crearTarea(titulo) {
  const res = await fetch('/api/tareas', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ titulo, completada: false })
  });
  return res.json();
}

// 2. LEER (READ)
async function obtenerTareas() {
  const res = await fetch('/api/tareas');
  return res.json();
}

// 3. ACTUALIZAR (UPDATE)
async function actualizarTarea(id, datos) {
  const res = await fetch(`/api/tareas/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datos)
  });
  return res.json();
}

// 4. ELIMINAR (DELETE)
async function eliminarTarea(id) {
  await fetch(`/api/tareas/${id}`, { method: 'DELETE' });
}
```

## Status Codes Semánticos

| Código | Caso de Uso |
|--------|-----------|
| 200 | OK - Petición exitosa |
| 201 | Created - Recurso creado |
| 400 | Bad Request - Datos inválidos |
| 401 | Unauthorized - Sin autenticación |
| 403 | Forbidden - Sin permisos |
| 404 | Not Found - No existe |
| 500 | Server Error - Error del servidor |

## Respuestas Estándar

### Éxito
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

## Ejemplo: API Real (JSONPlaceholder)

```javascript
// Obtener posts
const posts = await fetch('https://jsonplaceholder.typicode.com/posts')
  .then(r => r.json());

// Obtener comentarios de un post
const comentarios = await fetch('https://jsonplaceholder.typicode.com/comments?postId=1')
  .then(r => r.json());

// Crear usuario (fake)
const nuevoUsuario = await fetch('https://jsonplaceholder.typicode.com/users', {
  method: 'POST',
  body: JSON.stringify({
    name: 'Juan',
    email: 'juan@example.com'
  })
}).then(r => r.json());
```

## Diferencia: Query String vs Path

```javascript
// Path: /api/tareas/1
GET https://api.example.com/tareas/1

// Query String: /api/tareas?userId=1&completada=true
GET https://api.example.com/tareas?userId=1&completada=true

// Combinadas
GET https://api.example.com/tareas/1?format=json
```

## Puntos Clave ✨

1. **Métodos HTTP**: GET, POST, PUT, DELETE
2. **Recursos**: Rutas como /usuarios, /posts
3. **Status codes**: Códigos HTTP adecuados
4. **Formato**: Generalmente JSON
5. **Stateless**: Sin dependencias entre peticiones

## Tu Ejercicio 🎯

Estudia la API de JSONPlaceholder:
https://jsonplaceholder.typicode.com/

Crea funciones para:
1. ✅ GET /posts - Obtener todos los posts
2. ✅ GET /posts/1 - Obtener post específico
3. ✅ POST /posts - Crear nuevo post
4. ✅ DELETE /posts/1 - Eliminar post

---

**💡 Consejo**: REST es un patrón, no un protocolo. Diferentes APIs lo implementan de formas ligeramente diferentes.
