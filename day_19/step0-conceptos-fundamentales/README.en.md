[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 0: Fundamental Concepts 🌐

## 🎯 Why Start Here?

Before learning how to make HTTP requests with Fetch, you need to understand **what an API is**, **what JSON is**, **how HTTP works** and **what REST is**.

This step will give you the complete mental map so everything else makes sense.

---

## 🌐 The Big Picture: How Everything Connects

Imagine you want to order food for delivery:

1. **API** = The restaurant's menu (interface to order)
2. **REST** = The restaurant's rules (how to structure your order)
3. **HTTP** = The communication method (phone, app, etc.)
   - GET = "What's on the menu?"
   - POST = "I want to place an order"
   - PUT = "Change my entire order"
   - DELETE = "Cancel my order"
4. **JSON** = The structured language you speak
5. **Fetch** = Your phone/app (the tool to communicate)

### In the Web Development World:

```
Your React App (Client)
    ↓
Fetch API (tool)
    ↓
HTTP Request (GET/POST/PUT/DELETE)
    ↓
REST API (Server)
    ↓
Processes request
    ↓
HTTP Response (JSON)
    ↓
Your React App receives data
    ↓
Renders to the UI
```

---

## 📡 What Is an API?

**API** = Application Programming Interface

### Simple Definition

An API is a **contract** or **agreement** that lets two applications talk to each other.

### Analogy: The Waiter

Imagine a restaurant:

- **You (Client)**: You want food
- **Kitchen (Server)**: Prepares the food
- **Waiter (API)**: Takes your order to the kitchen and brings you the food

**The waiter is the API** — you don't need to know how the kitchen works, you just place your order and receive your food.

### In Programming

```javascript
// You (your JavaScript code)
fetch('https://api.ejemplo.com/usuarios')

// API (the waiter)
// - Receives your request
// - Talks to the server
// - Returns the data

// Result
// { "usuarios": [...] }
```

### Types of APIs

- **Web APIs** (the ones we'll see): Communication over the internet using HTTP
- **Library APIs**: Like `array.map()` in JavaScript
- **System APIs**: Like accessing your phone's camera

**We're focusing on Web APIs (REST APIs).**

---

## 📦 What Is JSON?

**JSON** = JavaScript Object Notation

### Simple Definition

JSON is a **text format** for exchanging data between systems. It's the "common language" spoken by web applications.

### Why JSON?

- ✅ **Readable**: Humans can read it easily
- ✅ **Universal**: Works in every programming language
- ✅ **Lightweight**: Takes up little space
- ✅ **Structured**: Has clear rules

### JSON Syntax

```json
{
  "nombre": "Juan",
  "edad": 25,
  "activo": true,
  "hobbies": ["programar", "leer", "correr"],
  "direccion": {
    "ciudad": "Madrid",
    "pais": "España"
  }
}
```

### JSON Rules

1. ✅ Keys **always** use double quotes: `"nombre"`
2. ✅ Strings use double quotes: `"Juan"`
3. ✅ Numbers have no quotes: `25`
4. ✅ Booleans: `true` or `false`
5. ✅ Arrays: `["item1", "item2"]`
6. ✅ Nested objects: `{"clave": {"subclave": "valor"}}`
7. ❌ **Not allowed**: functions, comments, undefined

### JSON vs JavaScript Object

```javascript
// JavaScript object (in code)
const usuario = {
  nombre: "Juan",    // No quotes on keys
  edad: 25,
  saludar: function() { return "Hola"; }  // Can have functions
};

// JSON (text)
const usuarioJSON = `{
  "nombre": "Juan",  
  "edad": 25
}`;  // Cannot have functions
```

### Conversion: JavaScript ↔ JSON

```javascript
// JavaScript object → JSON (string)
const usuario = { nombre: "Juan", edad: 25 };
const json = JSON.stringify(usuario);
console.log(json);  // '{"nombre":"Juan","edad":25}'
console.log(typeof json);  // "string"

// JSON (string) → JavaScript object
const jsonTexto = '{"nombre":"Juan","edad":25}';
const objeto = JSON.parse(jsonTexto);
console.log(objeto.nombre);  // "Juan"
console.log(typeof objeto);  // "object"
```

### Real Example: API Response

```javascript
// The API returns this (JSON string):
`{
  "success": true,
  "data": {
    "id": 1,
    "titulo": "Aprender React",
    "completada": false
  }
}`

// We parse it into a JavaScript object:
const respuesta = JSON.parse(apiResponse);
console.log(respuesta.data.titulo);  // "Aprender React"
```

---

## 🌍 What Is HTTP?

**HTTP** = HyperText Transfer Protocol

### Simple Definition

HTTP is the **protocol** (set of rules) computers use to talk over the internet.

### Analogy: Sending Letters

- **HTTP Request** = The letter you send to the server
- **HTTP Response** = The reply letter from the server
- **HTTP Methods** = The type of letter (inquiry, order, cancellation)

### Anatomy of an HTTP Request

```
GET /api/usuarios/1 HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Authorization: Bearer token123

{
  "campo": "valor"
}
```

**Components:**
1. **Method**: GET, POST, PUT, DELETE
2. **URL**: `/api/usuarios/1`
3. **Headers**: Metadata (Content-Type, Authorization)
4. **Body**: Data to send (only POST/PUT/PATCH)

---

## 🔧 HTTP Methods (The Verbs)

HTTP methods are **actions** you can perform on resources.

### GET - Retrieve Data

```javascript
// Read all users
GET /api/usuarios

// Read a specific user
GET /api/usuarios/1
```

**Characteristics:**
- ✅ Read-only (doesn't modify data)
- ✅ No body
- ✅ Idempotent (calling 10 times = same result)
- ✅ Can be cached

---

### POST - Create a New Resource

```javascript
// Create new user
POST /api/usuarios
Body: {
  "nombre": "Juan",
  "email": "juan@example.com"
}
```

**Characteristics:**
- ✅ Creates something new
- ✅ Has a body (data to create)
- ❌ NOT idempotent (calling 10 times = 10 users)
- ✅ Returns the created resource

---

### PUT - Full Update

```javascript
// Replace user 1 entirely
PUT /api/usuarios/1
Body: {
  "nombre": "Juan López",
  "email": "juan@example.com",
  "edad": 30
}
```

**Characteristics:**
- ✅ Replaces **the entire** resource
- ✅ Has a body (complete data)
- ✅ Idempotent
- ⚠️ If you omit a field, it gets erased

---

### PATCH - Partial Update

```javascript
// Update only the name
PATCH /api/usuarios/1
Body: {
  "nombre": "Juan López"
}
```

**Characteristics:**
- ✅ Updates **only** what you send
- ✅ Has a body (only fields to change)
- ✅ More common than PUT in modern APIs

---

### DELETE - Remove

```javascript
// Delete user 1
DELETE /api/usuarios/1
```

**Characteristics:**
- ✅ Removes the resource
- ✅ No body (usually)
- ✅ Idempotent
- ✅ Returns confirmation

---

## 🏛️ What Is REST?

**REST** = Representational State Transfer

### Simple Definition

REST is an **architectural style** (set of design rules) for building web APIs. It's not a technology, it's a way of organizing your API.

### REST Principles

1. **Client-Server**: Clear separation
2. **Stateless**: Each request is independent (no session is kept)
3. **Resources**: Everything is a resource with a unique URL
4. **HTTP Methods**: Use GET, POST, PUT, DELETE correctly
5. **Representation**: Usually JSON

### RESTful API = An API that follows REST rules

```javascript
// Books REST API

GET    /api/libros           → Get all books
GET    /api/libros/1         → Get the book with ID 1
POST   /api/libros           → Create a new book
PUT    /api/libros/1         → Update book 1
DELETE /api/libros/1         → Delete book 1

// Related resources
GET    /api/libros/1/reviews → Reviews for book 1
```

### Why REST?

- ✅ **Standardized**: Everyone follows the same rules
- ✅ **Predictable**: If you know one REST API, you know others
- ✅ **Scalable**: Easy to grow
- ✅ **Cacheable**: Can be optimized

---

## 🔗 Putting It All Together: The Full Connection

### Full Request Flow

```
1. Your React Component
   ↓
2. You call the Fetch API
   fetch('https://api.ejemplo.com/usuarios')
   ↓
3. Fetch creates an HTTP Request
   GET /usuarios HTTP/1.1
   Host: api.ejemplo.com
   ↓
4. The request travels across the internet to the REST API
   ↓
5. The REST API processes it (queries the database)
   ↓
6. The REST API returns an HTTP Response with JSON
   HTTP/1.1 200 OK
   Content-Type: application/json
   
   {"usuarios": [...]}
   ↓
7. Fetch receives the response
   ↓
8. You parse the JSON into a JavaScript object
   const data = await response.json()
   ↓
9. You update your UI with the data
   setUsuarios(data.usuarios)
```

### Real Code for the Complete Flow

```javascript
// In your React component
async function obtenerUsuarios() {
  try {
    // 1. Fetch makes an HTTP Request (GET)
    const response = await fetch('https://api.ejemplo.com/usuarios');
    
    // 2. Verify it was successful (status 200-299)
    if (!response.ok) {
      throw new Error('HTTP Error: ' + response.status);
    }
    
    // 3. Parse JSON into a JavaScript object
    const data = await response.json();
    
    // 4. Use the data
    console.log(data.usuarios);
    setUsuarios(data.usuarios);
    
  } catch (error) {
    console.error('Error:', error);
  }
}
```

---

## 🎯 Summary: The Complete Hierarchy

```
API (general concept)
 └─> Contract between applications

REST (architecture)
 └─> Set of rules for designing APIs
 
HTTP (protocol)
 └─> How they communicate (GET, POST, PUT, DELETE)
 
JSON (format)
 └─> Common language to exchange data
 
Fetch API (tool)
 └─> JavaScript to consume REST APIs with HTTP and JSON
 
React + Hooks (framework)
 └─> Integrates Fetch into your user interface
```

---

## 💡 Full Example: From Start to Finish

### The Server (REST API)

```javascript
// Endpoint on the server
GET https://api.tareas.com/api/tareas

// Returns:
{
  "success": true,
  "data": [
    {
      "id": 1,
      "titulo": "Aprender React",
      "completada": false
    },
    {
      "id": 2,
      "titulo": "Hacer ejercicio",
      "completada": true
    }
  ]
}
```

### The Client (Your React App)

```javascript
import { useState, useEffect } from 'react';

function ListaTareas() {
  const [tareas, setTareas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Async function to fetch tasks
    async function cargarTareas() {
      try {
        // 1. HTTP GET request using Fetch
        const response = await fetch('https://api.tareas.com/api/tareas');
        
        // 2. Validate response
        if (!response.ok) {
          throw new Error(`HTTP Error: ${response.status}`);
        }
        
        // 3. Parse JSON into a JavaScript object
        const resultado = await response.json();
        
        // 4. Update React state
        setTareas(resultado.data);
        setLoading(false);
        
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    }

    cargarTareas();
  }, []);

  if (loading) return <p>Loading tasks...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {tareas.map(tarea => (
        <li key={tarea.id}>
          {tarea.titulo} - {tarea.completada ? '✅' : '⏳'}
        </li>
      ))}
    </ul>
  );
}
```

### What's Happening?

1. **React** mounts the component
2. **useEffect** runs (once)
3. **Fetch** makes an **HTTP GET** request to the **REST API**
4. The **server** processes it and returns **JSON**
5. **response.json()** parses the JSON into a JavaScript object
6. **setState** updates React state
7. **React** re-renders showing the tasks

---

## 🎓 Key Concepts to Remember

### 1. API
- A contract between applications
- You don't need to know how it works internally
- You only need to know the endpoints and what they return

### 2. JSON
- Text format for data
- Use `JSON.parse()` to read it
- Use `JSON.stringify()` to send it

### 3. HTTP
- Communication protocol
- Methods: GET (read), POST (create), PUT/PATCH (update), DELETE (delete)

### 4. REST
- Design style for APIs
- Uses HTTP + JSON
- Resources with clear URLs

### 5. Fetch
- JavaScript tool to make HTTP requests
- Returns Promises
- Works with async/await

---

## 🚀 Next Steps

Now that you understand the fundamental concepts, you're ready to:

1. **Steps 1-5**: Learn asynchrony (setTimeout, Promises, async/await)
2. **Step 6**: Use the Fetch API in practice
3. **Step 7**: Go deeper into REST APIs
4. **Steps 8-9**: Integrate everything into React

---

## ✅ Comprehension Checklist

Before moving on, make sure you understand:

- [ ] What an API is and why it exists
- [ ] What JSON is and how it differs from a JavaScript object
- [ ] The 4 main HTTP methods and what they're for
- [ ] What REST is and why it's useful
- [ ] How all these concepts connect

---

**💡 Final Tip**: Don't try to memorize everything. Get the big picture. With practice, these concepts will become second nature.

**Now you're ready to learn how to consume APIs! 🚀**
