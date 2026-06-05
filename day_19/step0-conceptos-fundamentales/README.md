🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# Step 0: Conceptos Fundamentales 🌐

## 🎯 ¿Por qué empezar aquí?

Antes de aprender a hacer peticiones HTTP con Fetch, necesitas entender **qué es una API**, **qué es JSON**, **cómo funciona HTTP** y **qué es REST**. 

Este paso te dará el mapa mental completo para que todo lo demás tenga sentido.

---

## 🌐 La Gran Imagen: Cómo Todo se Conecta

Imagina que quieres pedir comida a domicilio:

1. **API** = El menú del restaurante (interfaz para pedir)
2. **REST** = Las reglas del restaurante (cómo estructurar tu pedido)
3. **HTTP** = El método de comunicación (teléfono, app, etc)
   - GET = "¿Qué hay en el menú?"
   - POST = "Quiero hacer un pedido"
   - PUT = "Cambiar mi pedido completo"
   - DELETE = "Cancelar mi pedido"
4. **JSON** = El lenguaje estructurado en que hablas
5. **Fetch** = Tu teléfono/app (la herramienta para comunicarte)

### En el Mundo del Desarrollo Web:

```
Tu React App (Cliente)  
    ↓
Fetch API (herramienta)
    ↓
HTTP Request (GET/POST/PUT/DELETE)
    ↓
REST API (Servidor)
    ↓
Procesa petición
    ↓
HTTP Response (JSON)
    ↓
Tu React App recibe datos
    ↓
Muestra en la UI
```

---

## 📡 ¿Qué es una API?

**API** = Application Programming Interface (Interfaz de Programación de Aplicaciones)

### Definición Simple

Una API es un **contrato** o **acuerdo** que permite que dos aplicaciones se comuniquen entre sí.

### Analogía: El Camarero

Imagina un restaurante:

- **Tú (Cliente)**: Quieres comida
- **Cocina (Servidor)**: Prepara la comida
- **Camarero (API)**: Lleva tu pedido a la cocina y te trae la comida

**El camarero es la API** - no necesitas saber cómo funciona la cocina, solo haces tu pedido y recibes la comida.

### En la Programación

```javascript
// Tú (tu código JavaScript)
fetch('https://api.ejemplo.com/usuarios')

// API (el camarero)
// - Recibe tu petición
// - Habla con el servidor
// - Te devuelve los datos

// Resultado
// { "usuarios": [...] }
```

### Tipos de APIs

- **APIs Web** (las que veremos): Comunicación por internet usando HTTP
- **APIs de Librerías**: Como `array.map()` en JavaScript
- **APIs del Sistema**: Como acceder a la cámara del móvil

**Nosotros nos enfocamos en APIs Web (REST APIs).**

---

## 📦 ¿Qué es JSON?

**JSON** = JavaScript Object Notation (Notación de Objetos JavaScript)

### Definición Simple

JSON es un **formato de texto** para intercambiar datos entre sistemas. Es el "idioma común" que hablan las aplicaciones web.

### ¿Por qué JSON?

- ✅ **Legible**: Los humanos pueden leerlo fácilmente
- ✅ **Universal**: Funciona en todos los lenguajes de programación
- ✅ **Ligero**: Ocupa poco espacio
- ✅ **Estructurado**: Tiene reglas claras

### Sintaxis JSON

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

### Reglas de JSON

1. ✅ Las claves **siempre** van entre comillas dobles: `"nombre"`
2. ✅ Los strings van entre comillas dobles: `"Juan"`
3. ✅ Los números no llevan comillas: `25`
4. ✅ Los booleanos: `true` o `false`
5. ✅ Arrays: `["item1", "item2"]`
6. ✅ Objetos anidados: `{"clave": {"subclave": "valor"}}`
7. ❌ **No se permiten**: funciones, comentarios, undefined

### JSON vs Objeto JavaScript

```javascript
// Objeto JavaScript (en código)
const usuario = {
  nombre: "Juan",    // Sin comillas en las claves
  edad: 25,
  saludar: function() { return "Hola"; }  // Puede tener funciones
};

// JSON (texto)
const usuarioJSON = `{
  "nombre": "Juan",  
  "edad": 25
}`;  // No puede tener funciones
```

### Conversión: JavaScript ↔ JSON

```javascript
// Objeto JavaScript → JSON (string)
const usuario = { nombre: "Juan", edad: 25 };
const json = JSON.stringify(usuario);
console.log(json);  // '{"nombre":"Juan","edad":25}'
console.log(typeof json);  // "string"

// JSON (string) → Objeto JavaScript
const jsonTexto = '{"nombre":"Juan","edad":25}';
const objeto = JSON.parse(jsonTexto);
console.log(objeto.nombre);  // "Juan"
console.log(typeof objeto);  // "object"
```

### Ejemplo Real: API Response

```javascript
// La API devuelve esto (JSON string):
`{
  "success": true,
  "data": {
    "id": 1,
    "titulo": "Aprender React",
    "completada": false
  }
}`

// Lo parseamos a objeto JavaScript:
const respuesta = JSON.parse(apiResponse);
console.log(respuesta.data.titulo);  // "Aprender React"
```

---

## 🌍 ¿Qué es HTTP?

**HTTP** = HyperText Transfer Protocol (Protocolo de Transferencia de Hipertexto)

### Definición Simple

HTTP es el **protocolo** (conjunto de reglas) que usan las computadoras para comunicarse en internet.

### Analogía: Enviar Cartas

- **HTTP Request** = Carta que envías al servidor
- **HTTP Response** = Carta de respuesta del servidor
- **HTTP Methods** = Tipo de carta (consulta, pedido, cancelación)

### Anatomía de una Petición HTTP

```
GET /api/usuarios/1 HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Authorization: Bearer token123

{
  "campo": "valor"
}
```

**Componentes:**
1. **Método**: GET, POST, PUT, DELETE
2. **URL**: `/api/usuarios/1`
3. **Headers**: Metadatos (Content-Type, Authorization)
4. **Body**: Datos a enviar (solo POST/PUT/PATCH)

---

## 🔧 Métodos HTTP (Los Verbos)

Los métodos HTTP son **acciones** que puedes realizar sobre los recursos.

### GET - Obtener Datos

```javascript
// Leer todos los usuarios
GET /api/usuarios

// Leer un usuario específico
GET /api/usuarios/1
```

**Características:**
- ✅ Solo lectura (no modifica datos)
- ✅ Sin body
- ✅ Idempotente (llamar 10 veces = mismo resultado)
- ✅ Se puede cachear

---

### POST - Crear Nuevo Recurso

```javascript
// Crear nuevo usuario
POST /api/usuarios
Body: {
  "nombre": "Juan",
  "email": "juan@example.com"
}
```

**Características:**
- ✅ Crea algo nuevo
- ✅ Con body (datos a crear)
- ❌ NO idempotente (llamar 10 veces = 10 usuarios)
- ✅ Devuelve el recurso creado

---

### PUT - Actualizar Completo

```javascript
// Reemplazar usuario 1 completamente
PUT /api/usuarios/1
Body: {
  "nombre": "Juan López",
  "email": "juan@example.com",
  "edad": 30
}
```

**Características:**
- ✅ Reemplaza **todo** el recurso
- ✅ Con body (datos completos)
- ✅ Idempotente
- ⚠️ Si omites un campo, se borra

---

### PATCH - Actualizar Parcial

```javascript
// Actualizar solo el nombre
PATCH /api/usuarios/1
Body: {
  "nombre": "Juan López"
}
```

**Características:**
- ✅ Actualiza **solo** lo que envías
- ✅ Con body (solo campos a cambiar)
- ✅ Más común que PUT en APIs modernas

---

### DELETE - Eliminar

```javascript
// Eliminar usuario 1
DELETE /api/usuarios/1
```

**Características:**
- ✅ Elimina el recurso
- ✅ Sin body (usualmente)
- ✅ Idempotente
- ✅ Devuelve confirmación

---

## 🏛️ ¿Qué es REST?

**REST** = Representational State Transfer

### Definición Simple

REST es un **estilo arquitectónico** (conjunto de reglas de diseño) para crear APIs web. No es una tecnología, es una forma de organizar tu API.

### Principios REST

1. **Cliente-Servidor**: Separación clara
2. **Stateless**: Cada petición es independiente (no guarda sesión)
3. **Recursos**: Todo es un recurso con URL única
4. **Métodos HTTP**: Usar GET, POST, PUT, DELETE correctamente
5. **Representación**: Usualmente JSON

### API RESTful = API que sigue las reglas REST

```javascript
// REST API de Libros

GET    /api/libros           → Obtener todos los libros
GET    /api/libros/1         → Obtener libro con ID 1
POST   /api/libros           → Crear nuevo libro
PUT    /api/libros/1         → Actualizar libro 1
DELETE /api/libros/1         → Eliminar libro 1

// Recursos relacionados
GET    /api/libros/1/reviews → Reviews del libro 1
```

### ¿Por qué REST?

- ✅ **Estandarizado**: Todos siguen las mismas reglas
- ✅ **Predecible**: Si conoces una REST API, conoces otras
- ✅ **Escalable**: Fácil de crecer
- ✅ **Cacheable**: Se puede optimizar

---

## 🔗 Juntando Todo: La Conexión Completa

### Flujo Completo de una Petición

```
1. Tu React Component
   ↓
2. Llamas a Fetch API
   fetch('https://api.ejemplo.com/usuarios')
   ↓
3. Fetch crea una HTTP Request
   GET /usuarios HTTP/1.1
   Host: api.ejemplo.com
   ↓
4. Request viaja por internet a la REST API
   ↓
5. REST API procesa (busca en base de datos)
   ↓
6. REST API devuelve HTTP Response con JSON
   HTTP/1.1 200 OK
   Content-Type: application/json
   
   {"usuarios": [...]}
   ↓
7. Fetch recibe la respuesta
   ↓
8. Parseas JSON a objeto JavaScript
   const data = await response.json()
   ↓
9. Actualizas tu UI con los datos
   setUsuarios(data.usuarios)
```

### Código Real del Flujo Completo

```javascript
// En tu componente React
async function obtenerUsuarios() {
  try {
    // 1. Fetch hace HTTP Request (GET)
    const response = await fetch('https://api.ejemplo.com/usuarios');
    
    // 2. Verificar que fue exitoso (status 200-299)
    if (!response.ok) {
      throw new Error('Error HTTP: ' + response.status);
    }
    
    // 3. Parsear JSON a objeto JavaScript
    const data = await response.json();
    
    // 4. Usar los datos
    console.log(data.usuarios);
    setUsuarios(data.usuarios);
    
  } catch (error) {
    console.error('Error:', error);
  }
}
```

---

## 🎯 Resumen: La Jerarquía Completa

```
API (concepto general)
 └─> Contrato entre aplicaciones

REST (arquitectura)
 └─> Conjunto de reglas para diseñar APIs
 
HTTP (protocolo)
 └─> Cómo se comunican (GET, POST, PUT, DELETE)
 
JSON (formato)
 └─> Lenguaje común para intercambiar datos
 
Fetch API (herramienta)
 └─> JavaScript para consumir APIs REST con HTTP y JSON
 
React + Hooks (framework)
 └─> Integra Fetch en tu interfaz de usuario
```

---

## 💡 Ejemplo Completo: De Principio a Fin

### El Servidor (REST API)

```javascript
// Endpoint en el servidor
GET https://api.tareas.com/api/tareas

// Devuelve:
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

### El Cliente (Tu React App)

```javascript
import { useState, useEffect } from 'react';

function ListaTareas() {
  const [tareas, setTareas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Función asíncrona para obtener tareas
    async function cargarTareas() {
      try {
        // 1. HTTP GET Request usando Fetch
        const response = await fetch('https://api.tareas.com/api/tareas');
        
        // 2. Validar respuesta
        if (!response.ok) {
          throw new Error(`Error HTTP: ${response.status}`);
        }
        
        // 3. Parsear JSON a objeto JavaScript
        const resultado = await response.json();
        
        // 4. Actualizar estado de React
        setTareas(resultado.data);
        setLoading(false);
        
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    }

    cargarTareas();
  }, []);

  if (loading) return <p>Cargando tareas...</p>;
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

### ¿Qué Está Pasando?

1. **React** monta el componente
2. **useEffect** se ejecuta (una vez)
3. **Fetch** hace petición **HTTP GET** a la **REST API**
4. **Servidor** procesa y devuelve **JSON**
5. **response.json()** parsea el JSON a objeto JavaScript
6. **setState** actualiza el estado de React
7. **React** re-renderiza mostrando las tareas

---

## 🎓 Conceptos Clave para Recordar

### 1. API
- Contrato entre aplicaciones
- No necesitas saber cómo funciona internamente
- Solo necesitas conocer los endpoints y qué devuelven

### 2. JSON
- Formato de texto para datos
- Usas `JSON.parse()` para leer
- Usas `JSON.stringify()` para enviar

### 3. HTTP
- Protocolo de comunicación
- Métodos: GET (leer), POST (crear), PUT/PATCH (actualizar), DELETE (eliminar)

### 4. REST
- Estilo de diseño para APIs
- Usa HTTP + JSON
- Recursos con URLs claras

### 5. Fetch
- Herramienta JavaScript para hacer peticiones HTTP
- Devuelve Promises
- Se integra con async/await

---

## 🚀 Próximos Pasos

Ahora que entiendes los conceptos fundamentales, estás listo para:

1. **Step 1-5**: Aprender asincronía (setTimeout, Promises, async/await)
2. **Step 6**: Usar Fetch API en la práctica
3. **Step 7**: Profundizar en REST APIs
4. **Step 8-9**: Integrar todo en React

---

## ✅ Checklist de Comprensión

Antes de continuar, asegúrate de entender:

- [ ] ¿Qué es una API y por qué existe?
- [ ] ¿Qué es JSON y cómo se diferencia de un objeto JavaScript?
- [ ] ¿Cuáles son los 4 métodos HTTP principales y para qué sirven?
- [ ] ¿Qué es REST y por qué es útil?
- [ ] ¿Cómo se conectan todos estos conceptos?

---

**💡 Consejo Final**: No intentes memorizar todo. Entiende el panorama general. Con la práctica, estos conceptos se volverán naturales.

**¡Ahora sí estás listo para aprender a consumir APIs! 🚀**
