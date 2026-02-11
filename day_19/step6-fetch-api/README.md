# Step 6: Fetch API 🌐

## 🔗 Contexto: ¿Dónde Estamos?

Hasta ahora has aprendido:
- ✅ **Step 0**: Qué son API, JSON, HTTP y REST
- ✅ **Steps 1-5**: Código asíncrono (Promises, async/await)

Ahora aprenderás:
- 🎯 **Fetch**: La herramienta que usa Promises para comunicarse con APIs
- 🎯 **HTTP en práctica**: Los métodos para realizar acciones (GET, POST, PUT, DELETE)
- 🎯 **JSON en acción**: Cómo convertir datos para enviar y recibir

**La conexión:**
```javascript
// Fetch (herramienta) + HTTP (método) + JSON (formato)
const response = await fetch(url);  // Fetch hace una petición HTTP
const data = await response.json(); // Parse JSON a objeto JavaScript
```

---

## ¿Qué es Fetch?

**Fetch API** es una interfaz moderna para hacer peticiones HTTP desde JavaScript. Reemplaza a XMLHttpRequest (antiguo).

```javascript
// Sintaxis básica
fetch(url, opciones)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

---

## 🔗 ¿Por qué Fetch Devuelve una Promise?

### La Conexión con Steps Anteriores

Ahora todo cobra sentido:

**Step 1**: Operaciones asíncronas = cosas que tardan  
**Step 2**: setTimeout = simula esperas  
**Step 3**: Callbacks = "cuando termine, ejecuta esto"  
**Step 4**: Promises = mejor forma de manejar código asíncrono  
**Step 5**: Async/Await = sintaxis más limpia para Promises  
**Step 6**: **Fetch = operación asíncrona REAL (pide datos a un servidor)**  

### ¿Por qué Fetch Necesita Ser Asíncrono?

```javascript
// Pedir datos a un servidor:
fetch('https://api.ejemplo.com/datos')
```

**¿Qué pasa cuando ejecutas esto?**

1. Tu navegador envía una petición HTTP por internet
2. La petición viaja al servidor (puede estar en otro país)
3. El servidor procesa la petición
4. El servidor envía la respuesta de vuelta
5. La respuesta viaja por internet de regreso a tu navegador

**¿Cuánto tarda esto?** 100ms, 500ms, 2 segundos... **no se sabe**.

Dependiendo de:
- ❌ Velocidad de tu internet
- ❌ Distancia al servidor
- ❌ Carga del servidor
- ❌ Tamaño de los datos

### ¿Qué Pasaría si Fetch Fuera Síncrono?

```javascript
// SI FETCH FUERA SINCRONO (❌ mal):
console.log('Inicio');
const datos = fetch(url);  // BLOQUEARIA aquí 2 segundos
console.log('Fin');

// Tu página estaría CONGELADA mientras espera
// No podrías hacer clic, scrollear, nada
```

**Inaceptable.** Imagina que cada vez que tu app pide datos, toda la página se congela.

### Por Eso Fetch Devuelve una Promise

```javascript
// FETCH ES ASINCRONO (✅ bien):
console.log('Inicio');

const promesa = fetch(url);  // Devuelve Promise inmediatamente

promesa.then(response => {
  console.log('Datos llegaron');  // Se ejecuta cuando lleguen
});

console.log('Fin');  // No espera, continúa inmediatamente

// Salida:
// Inicio
// Fin
// (después de X tiempo)
// Datos llegaron
```

**Fetch devuelve Promise porque**:
1. ✅ No bloquea el navegador
2. ✅ Puedes hacer `.then()` para manejar la respuesta cuando llegue
3. ✅ Puedes hacer `.catch()` si hay error
4. ✅ Puedes usar `async/await` para sintaxis más limpia

### Fetch Usa TODO lo que Aprendiste

```javascript
// Con Promises (Step 4):
fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));

// Con Async/Await (Step 5):
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

**Fetch es la aplicación REAL de todo lo que aprendiste:**
- Es **asíncrono** (Step 1)
- Podría usar callbacks pero sería Callback Hell (Step 3)
- Usa **Promises** porque son mejores (Step 4)
- Puedes usar **Async/Await** para código limpio (Step 5)

### Por Qué response.json() También Devuelve Promise

```javascript
const response = await fetch(url);
const data = await response.json();  // ¿Por qué otro await?
```

**Porque parsear JSON también puede tardar:**
- Si los datos son grandes (1MB de JSON)
- El navegador necesita tiempo para procesarlos

Por eso `.json()` **también** devuelve una Promise.

### Resumen Visual

```
Tu Código
    ↓
fetch(url) → Devuelve Promise inmediatamente
    │
    │ (Tu código continúa, no se bloquea)
    │
    ↓ (Mientras tanto, por internet...)
    │
Petición HTTP viaja al servidor
    ↓
Servidor procesa
    ↓
Respuesta viaja de vuelta
    ↓
Promise se resuelve → .then() se ejecuta (o await retorna)
```

## Métodos HTTP

|| Método | Uso |
||--------|-----|
|| **GET** | Obtener datos |
|| **POST** | Crear nuevo recurso |
|| **PUT** | Actualizar todo |
|| **PATCH** | Actualizar parcial |
|| **DELETE** | Eliminar |

---

## 📦 JSON en Profundidad

Antes de ver ejemplos de Fetch, es crucial entender **JSON** porque es el formato que usarás para enviar y recibir datos.

### ¿Qué es JSON?

JSON (JavaScript Object Notation) es un **formato de texto** para intercambiar datos. Es el "idioma" que hablan el cliente y el servidor.

### Diferencia Clave: Objeto JavaScript vs JSON

```javascript
// Objeto JavaScript (en memoria, en tu código)
const usuario = {
  nombre: "Juan",
  edad: 25
};
console.log(typeof usuario);  // "object"

// JSON (texto, para enviar por la red)
const usuarioJSON = '{"nombre":"Juan","edad":25}';
console.log(typeof usuarioJSON);  // "string"
```

### Conversión: JavaScript ↔ JSON

```javascript
// 1. Objeto JavaScript → JSON (para ENVIAR)
const usuario = { nombre: "Juan", edad: 25 };
const json = JSON.stringify(usuario);
console.log(json);  // '{"nombre":"Juan","edad":25}'

// 2. JSON → Objeto JavaScript (para RECIBIR)
const textoJSON = '{"nombre":"Juan","edad":25}';
const objeto = JSON.parse(textoJSON);
console.log(objeto.nombre);  // "Juan"
```

### En el Contexto de Fetch

```javascript
// ENVIAR datos (POST/PUT)
const nuevoUsuario = { nombre: "Ana", edad: 28 };

fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(nuevoUsuario)  // Convierte a JSON string
});

// RECIBIR datos (GET)
const response = await fetch(url);
const datos = await response.json();  // Convierte JSON string a objeto
console.log(datos.nombre);
```

### ¿Por qué esta conversión?

✅ **HTTP solo puede transmitir texto** (no objetos JavaScript directamente)  
✅ **JSON.stringify()** convierte objeto → texto (para enviar)  
✅ **response.json()** convierte texto → objeto (para usar)  

---

## Ejemplo 1: GET (Obtener)

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

## Ejemplo 2: POST (Crear)

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

## Ejemplo 3: PUT (Actualizar)

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

## Ejemplo 4: DELETE (Eliminar)

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

El objeto `response` tiene propiedades útiles:

```javascript
const res = await fetch(url);

// Propiedades
console.log(res.status);      // Código HTTP (200, 404, etc)
console.log(res.ok);          // true si status 200-299
console.log(res.statusText);  // "OK", "Not Found", etc
console.log(res.headers);     // Headers de la respuesta

// Métodos para leer el cuerpo
res.json()      // Parse como JSON
res.text()      // Parse como texto
res.blob()      // Parse como archivo
res.arrayBuffer() // Parse como buffer
```

## Status Codes Comunes

| Código | Significado |
|--------|------------|
| 200 | OK - Éxito |
| 201 | Created - Recurso creado |
| 400 | Bad Request - Petición inválida |
| 401 | Unauthorized - No autorizado |
| 404 | Not Found - No encontrado |
| 500 | Server Error - Error del servidor |

## Ejemplo 5: Headers y Autenticación

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

## Ejemplo 6: Manejo Completo de Errores

```javascript
async function obtenerConValidacion() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
    
    // Validar HTTP
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    
    const datos = await res.json();
    
    // Validar datos
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

## Errores Comunes

### Error 1: Confundir status con error
```javascript
// ❌ MALO - fetch no rechaza con status 404
fetch(url).catch(...); // El catch no se ejecuta con 404

// ✅ BIEN - Verificar res.ok
const res = await fetch(url);
if (!res.ok) {
  throw new Error('Error HTTP: ' + res.status);
}
```

### Error 2: Olvidar JSON.stringify
```javascript
// ❌ MALO - Envía [object Object]
fetch(url, {
  body: { name: 'Juan' }
});

// ✅ BIEN
fetch(url, {
  body: JSON.stringify({ name: 'Juan' })
});
```

### Error 3: No parsear el body
```javascript
// ❌ MALO
const datos = await fetch(url);
console.log(datos.title); // undefined

// ✅ BIEN
const res = await fetch(url);
const datos = await res.json();
console.log(datos.title);
```

## Puntos Clave ✨

1. **GET**: Sin body, obtener datos
2. **POST/PUT/PATCH/DELETE**: Incluir method y body
3. **JSON.stringify()**: Para convertir objeto a JSON
4. **response.json()**: Para parsear respuesta
5. **res.ok**: Siempre verificar que la petición fue exitosa

## Tu Ejercicio 🎯

Crea funciones para:
1. ✅ GET - Obtener usuario con ID 1
2. ✅ POST - Crear nuevo post
3. ✅ DELETE - Eliminar post con ID 1

Usa JSONPlaceholder: https://jsonplaceholder.typicode.com/

---

## Próximos Pasos

Una vez domines Fetch:

✅ GET, POST, PUT, DELETE  
✅ Headers y autenticación  
✅ Manejo de errores  

Estarás listo para:
- **Step 7**: REST APIs - Conceptos fundamentales
- **Step 8**: Integrar Fetch en componentes React
- **Step 9**: TodoList completa con API

---

**💡 Consejo**: Siempre revisa `res.ok` antes de usar los datos.
