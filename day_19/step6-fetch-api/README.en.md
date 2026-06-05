[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 6: Fetch API 🌐

## 🔗 Context: Where Are We?

So far you've learned:
- ✅ **Step 0**: What API, JSON, HTTP and REST are
- ✅ **Steps 1-5**: Async code (Promises, async/await)

Now you'll learn:
- 🎯 **Fetch**: The tool that uses Promises to talk to APIs
- 🎯 **HTTP in practice**: The methods to perform actions (GET, POST, PUT, DELETE)
- 🎯 **JSON in action**: How to convert data to send and receive

**The connection:**
```javascript
// Fetch (tool) + HTTP (method) + JSON (format)
const response = await fetch(url);  // Fetch makes an HTTP request
const data = await response.json(); // Parse JSON to a JavaScript object
```

---

## What Is Fetch?

**Fetch API** is a modern interface for making HTTP requests from JavaScript. It replaces XMLHttpRequest (old).

```javascript
// Basic syntax
fetch(url, opciones)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

---

## 🔗 Why Does Fetch Return a Promise?

### Connection with Previous Steps

Now everything clicks:

**Step 1**: Async operations = things that take time  
**Step 2**: setTimeout = simulates waits  
**Step 3**: Callbacks = "when it finishes, run this"  
**Step 4**: Promises = better way to handle async code  
**Step 5**: Async/Await = cleaner syntax for Promises  
**Step 6**: **Fetch = REAL async operation (requests data from a server)**  

### Why Does Fetch Need to Be Async?

```javascript
// Request data from a server:
fetch('https://api.ejemplo.com/datos')
```

**What happens when you run this?**

1. Your browser sends an HTTP request over the internet
2. The request travels to the server (it might be in another country)
3. The server processes the request
4. The server sends a response back
5. The response travels back across the internet to your browser

**How long does this take?** 100ms, 500ms, 2 seconds... **you don't know**.

It depends on:
- ❌ Your internet speed
- ❌ Distance to the server
- ❌ Server load
- ❌ Data size

### What Would Happen If Fetch Were Synchronous?

```javascript
// IF FETCH WERE SYNCHRONOUS (❌ bad):
console.log('Inicio');
const datos = fetch(url);  // WOULD BLOCK for 2 seconds
console.log('Fin');

// Your page would be FROZEN while it waits
// You couldn't click, scroll, nothing
```

**Unacceptable.** Imagine every time your app requests data, the whole page freezes.

### That's Why Fetch Returns a Promise

```javascript
// FETCH IS ASYNC (✅ good):
console.log('Inicio');

const promesa = fetch(url);  // Returns a Promise immediately

promesa.then(response => {
  console.log('Datos llegaron');  // Runs when they arrive
});

console.log('Fin');  // Doesn't wait, continues immediately

// Output:
// Inicio
// Fin
// (after some time)
// Datos llegaron
```

**Fetch returns a Promise because**:
1. ✅ It doesn't block the browser
2. ✅ You can use `.then()` to handle the response when it arrives
3. ✅ You can use `.catch()` if there's an error
4. ✅ You can use `async/await` for cleaner syntax

### Fetch Uses EVERYTHING You Learned

```javascript
// With Promises (Step 4):
fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));

// With Async/Await (Step 5):
async function obtenerDatos() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}
```

**Fetch is the REAL application of everything you learned:**
- It's **async** (Step 1)
- It could use callbacks but it would be Callback Hell (Step 3)
- It uses **Promises** because they're better (Step 4)
- You can use **Async/Await** for clean code (Step 5)

### Why response.json() Also Returns a Promise

```javascript
const response = await fetch(url);
const data = await response.json();  // Why another await?
```

**Because parsing JSON can also take time:**
- If the data is large (1MB of JSON)
- The browser needs time to process it

That's why `.json()` **also** returns a Promise.

### Visual Summary

```
Your Code
    ↓
fetch(url) → Returns a Promise immediately
    │
    │ (Your code continues, doesn't block)
    │
    ↓ (Meanwhile, over the internet...)
    │
HTTP request travels to the server
    ↓
Server processes
    ↓
Response travels back
    ↓
Promise resolves → .then() runs (or await returns)
```

## HTTP Methods

|| Method | Use |
||--------|-----|
|| **GET** | Get data |
|| **POST** | Create a new resource |
|| **PUT** | Update everything |
|| **PATCH** | Partial update |
|| **DELETE** | Delete |

---

## 📦 JSON in Depth

Before looking at Fetch examples, it's crucial to understand **JSON** because it's the format you'll use to send and receive data.

### What Is JSON?

JSON (JavaScript Object Notation) is a **text format** for exchanging data. It's the "language" spoken by client and server.

### Key Difference: JavaScript Object vs JSON

```javascript
// JavaScript object (in memory, in your code)
const usuario = {
  nombre: "Juan",
  edad: 25
};
console.log(typeof usuario);  // "object"

// JSON (text, to send over the network)
const usuarioJSON = '{"nombre":"Juan","edad":25}';
console.log(typeof usuarioJSON);  // "string"
```

### Conversion: JavaScript ↔ JSON

```javascript
// 1. JavaScript object → JSON (to SEND)
const usuario = { nombre: "Juan", edad: 25 };
const json = JSON.stringify(usuario);
console.log(json);  // '{"nombre":"Juan","edad":25}'

// 2. JSON → JavaScript object (to RECEIVE)
const textoJSON = '{"nombre":"Juan","edad":25}';
const objeto = JSON.parse(textoJSON);
console.log(objeto.nombre);  // "Juan"
```

### In the Context of Fetch

```javascript
// SEND data (POST/PUT)
const nuevoUsuario = { nombre: "Ana", edad: 28 };

fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(nuevoUsuario)  // Convert to JSON string
});

// RECEIVE data (GET)
const response = await fetch(url);
const datos = await response.json();  // Convert JSON string to object
console.log(datos.nombre);
```

### Why This Conversion?

✅ **HTTP can only transmit text** (not JavaScript objects directly)  
✅ **JSON.stringify()** converts object → text (to send)  
✅ **response.json()** converts text → object (to use)  

---

## Example 1: GET (Retrieve)

```javascript
async function obtenerUsuario() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
    const datos = await res.json();
    console.log(datos);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

## Example 2: POST (Create)

```javascript
async function crearPost() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: 'Mi primer post',
        body: 'Contenido del post',
        userId: 1
      })
    });
    const datos = await res.json();
    console.log('Creado:', datos);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

## Example 3: PUT (Update)

```javascript
async function actualizarPost() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        id: 1,
        title: 'Actualizado',
        body: 'Nuevo contenido',
        userId: 1
      })
    });
    const datos = await res.json();
    console.log('Actualizado:', datos);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

## Example 4: DELETE (Delete)

```javascript
async function eliminarPost() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'DELETE'
    });
    console.log('Eliminado:', res.status);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

## Response Object

The `response` object has useful properties:

```javascript
const res = await fetch(url);

// Properties
console.log(res.status);      // HTTP code (200, 404, etc.)
console.log(res.ok);          // true if status 200-299
console.log(res.statusText);  // "OK", "Not Found", etc.
console.log(res.headers);     // Response headers

// Methods to read the body
res.json()      // Parse as JSON
res.text()      // Parse as text
res.blob()      // Parse as file
res.arrayBuffer() // Parse as buffer
```

## Common Status Codes

| Code | Meaning |
|--------|------------|
| 200 | OK - Success |
| 201 | Created - Resource created |
| 400 | Bad Request - Invalid request |
| 401 | Unauthorized - Not authenticated |
| 404 | Not Found - Not found |
| 500 | Server Error - Server error |

## Example 5: Headers and Authentication

```javascript
async function obtenerConAutenticacion() {
  try {
    const token = 'mi-token-secreto';
    const res = await fetch('https://api.example.com/datos', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });
    const datos = await res.json();
    console.log(datos);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

## Example 6: Full Error Handling

```javascript
async function obtenerConValidacion() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
    
    // Validate HTTP
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    
    const datos = await res.json();
    
    // Validate data
    if (!datos.id) {
      throw new Error('Datos inválidos');
    }
    
    return datos;
  } catch (error) {
    console.log('Error completo:', error.message);
    throw error;
  }
}
```

## Common Mistakes

### Mistake 1: Confusing status with error
```javascript
// ❌ BAD - fetch doesn't reject on status 404
fetch(url).catch(...); // The catch doesn't fire with 404

// ✅ GOOD - Check res.ok
const res = await fetch(url);
if (!res.ok) {
  throw new Error('Error HTTP: ' + res.status);
}
```

### Mistake 2: Forgetting JSON.stringify
```javascript
// ❌ BAD - Sends [object Object]
fetch(url, {
  body: { name: 'Juan' }
});

// ✅ GOOD
fetch(url, {
  body: JSON.stringify({ name: 'Juan' })
});
```

### Mistake 3: Not parsing the body
```javascript
// ❌ BAD
const datos = await fetch(url);
console.log(datos.title); // undefined

// ✅ GOOD
const res = await fetch(url);
const datos = await res.json();
console.log(datos.title);
```

## Key Points ✨

1. **GET**: No body, retrieves data
2. **POST/PUT/PATCH/DELETE**: Include method and body
3. **JSON.stringify()**: To convert an object to JSON
4. **response.json()**: To parse the response
5. **res.ok**: Always check that the request was successful

## Your Exercise 🎯

Build functions to:
1. ✅ GET - Fetch user with ID 1
2. ✅ POST - Create a new post
3. ✅ DELETE - Delete post with ID 1

Use JSONPlaceholder: https://jsonplaceholder.typicode.com/

---

## Next Steps

Once you've mastered Fetch:

✅ GET, POST, PUT, DELETE  
✅ Headers and authentication  
✅ Error handling  

You'll be ready for:
- **Step 7**: REST APIs - Fundamental concepts
- **Step 8**: Integrate Fetch into React components
- **Step 9**: Full TodoList with API

---

**💡 Tip**: Always check `res.ok` before using the data.
