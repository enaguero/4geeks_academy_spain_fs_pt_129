# Step 3: Fetch API 🌐

## ¿Qué es Fetch?

**Fetch API** es una interfaz moderna para hacer peticiones HTTP desde JavaScript. Reemplaza a XMLHttpRequest (antiguo).

```javascript
// Sintaxis básica
fetch(url, opciones)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

## Métodos HTTP

| Método | Uso |
|--------|-----|
| **GET** | Obtener datos |
| **POST** | Crear nuevo recurso |
| **PUT** | Actualizar todo |
| **PATCH** | Actualizar parcial |
| **DELETE** | Eliminar |

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
- **Step 5**: Integrar Fetch en componentes React
- **Step 6**: TodoList completa con API

---

**💡 Consejo**: Siempre revisa `res.ok` antes de usar los datos.
