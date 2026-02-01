# Step 2: Async/Await ⏳

## ¿Qué es Async/Await?

**Async/Await** es una forma más limpia y legible de trabajar con Promises. En lugar de `.then()` y `.catch()`, usas sintaxis que se parece a código sincrónico.

```javascript
// ❌ Con Promises (complejo)
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(err => console.log(err));

// ✅ Con Async/Await (legible)
async function obtenerDatos() {
  try {
    const res = await fetch(url);
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}
```

## Sintaxis

### async function
Una función `async` siempre devuelve una Promise:

```javascript
// Función async
async function saludar() {
  return 'Hola'; // Automáticamente se convierte en Promise
}

// Es equivalente a:
function saludar() {
  return Promise.resolve('Hola');
}

// Ambas se usan igual:
saludar().then(resultado => console.log(resultado)); // 'Hola'
```

### await keyword
`await` **pausa** la función hasta que la Promise se resuelva:

```javascript
async function obtenerUsuario() {
  console.log('Obteniendo...');
  const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
  console.log('Recibido!');
  return res;
}

// Cuando llames:
obtenerUsuario(); // 'Obteniendo...' se imprime inmediatamente
                  // 'Recibido!' se imprime después de la petición
```

## Ejemplo 1: Básico

```javascript
async function obtenerUsuario() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
    const usuario = await response.json();
    console.log('Nombre:', usuario.name);
    console.log('Email:', usuario.email);
  } catch (error) {
    console.log('Error:', error);
  } finally {
    console.log('Finalizado');
  }
}

obtenerUsuario();
```

**Flujo**:
1. Pausa en `fetch` hasta que llegue la respuesta
2. Pausa en `response.json()` hasta que se parse el JSON
3. Imprime nombre y email
4. Si hay error, lo atrapa
5. finally se ejecuta siempre

## Ejemplo 2: Múltiples await

```javascript
async function obtenerDatosCompletos() {
  try {
    // Esperar usuario
    const userRes = await fetch('https://jsonplaceholder.typicode.com/users/1');
    const user = await userRes.json();

    // Esperar posts del usuario
    const postsRes = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=1`);
    const posts = await postsRes.json();

    console.log('Usuario:', user.name);
    console.log('Posts:', posts.length);
  } catch (error) {
    console.log('Error:', error);
  }
}

obtenerDatosCompletos();
```

## Ejemplo 3: Await en Paralelo

```javascript
async function obtenerTodo() {
  try {
    // ❌ MALO - Espera una, luego la otra (lento)
    const usuario = await fetch('...').then(r => r.json());
    const posts = await fetch('...').then(r => r.json());

    // ✅ BIEN - Las dos en paralelo (rápido)
    const [usuario, posts] = await Promise.all([
      fetch('https://jsonplaceholder.typicode.com/users/1').then(r => r.json()),
      fetch('https://jsonplaceholder.typicode.com/posts?userId=1').then(r => r.json())
    ]);

    console.log(usuario, posts);
  } catch (error) {
    console.log('Error:', error);
  }
}

obtenerTodo();
```

## Ejemplo 4: Con React

```javascript
import { useState, useEffect } from 'react';

function MiComponente() {
  const [datos, setDatos] = useState(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function cargarDatos() {
      try {
        const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
        const data = await res.json();
        setDatos(data);
      } catch (err) {
        setError(err);
      } finally {
        setCargando(false);
      }
    }

    cargarDatos();
  }, []);

  if (cargando) return <p>Cargando...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h2>{datos.name}</h2>
      <p>{datos.email}</p>
    </div>
  );
}

export default MiComponente;
```

## Comparación: then() vs Async/Await

```javascript
// CON THEN()
function obtenerConThen() {
  return fetch(url)
    .then(r => r.json())
    .then(data => {
      console.log(data);
      return data;
    })
    .catch(err => console.log(err));
}

// CON ASYNC/AWAIT
async function obtenerConAsync() {
  try {
    const res = await fetch(url);
    const data = await res.json();
    console.log(data);
    return data;
  } catch (err) {
    console.log(err);
  }
}
```

Ambas funcionan igual, pero async/await es más legible.

## Errores Comunes

### Error 1: Olvidar async en la función
```javascript
// ❌ MALO - Error: await fuera de async
function obtenerDatos() {
  const data = await fetch(url); // SyntaxError
}

// ✅ BIEN
async function obtenerDatos() {
  const data = await fetch(url);
}
```

### Error 2: No manejar errores
```javascript
// ❌ MALO - Si falla, el error no se atrapa
async function obtenerDatos() {
  const data = await fetch(url); // Si falla, error no controlado
}

// ✅ BIEN
async function obtenerDatos() {
  try {
    const data = await fetch(url);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

### Error 3: Mezclar callbacks con async/await
```javascript
// ❌ MALO - Código confuso
async function obtenerDatos() {
  fetch(url)
    .then(r => r.json())
    .then(data => {
      await procesarDatos(data); // Mezcla confusa
    });
}

// ✅ BIEN - Consistente
async function obtenerDatos() {
  const res = await fetch(url);
  const data = await res.json();
  await procesarDatos(data);
}
```

## Puntos Clave ✨

1. **async** hace que una función devuelva una Promise
2. **await** pausa la ejecución hasta que se resuelva
3. **try/catch** para manejar errores
4. **Más legible** que .then().catch()
5. **Funciona** con cualquier Promise, no solo fetch

## Tu Ejercicio 🎯

Convierte este código con promises a async/await:

```javascript
// Con Promises:
function obtenerDatos() {
  return fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(r => r.json())
    .then(user => {
      console.log(user.name);
      return user;
    })
    .catch(err => console.log(err));
}

// ❓ TODO: Cónviertelo a async/await
```

---

## Próximos Pasos

Una vez domines async/await:

✅ async/await  
✅ try/catch  
✅ Integración con React  

Estarás listo para:
- **Step 3**: Fetch API completa
- **Step 5**: Fetch en componentes React

---

**💡 Consejo**: Async/Await es más legible y se usa en código profesional. Prefierelo sobre .then().
