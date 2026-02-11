# Step 4: Promises - La Solución al Callback Hell 🤝

## 🔗 Contexto: De Callbacks a Promises

### Recordando los Problemas

En los steps anteriores aprendiste:

**Step 1**: Código **asíncrono** = operaciones que tardan (no bloquean)  
**Step 2**: **setTimeout** = primera herramienta asíncrona  
**Step 3**: **Callbacks** = "cuando termines, ejecuta esto"  
**Step 3**: **Callback Hell** = callbacks anidados = código ilegible  

```javascript
// Callback Hell ❌
obtenerUsuario(1, (error, usuario) => {
  if (error) return console.log(error);
  
  obtenerPosts(usuario.id, (error, posts) => {
    if (error) return console.log(error);
    
    obtenerComentarios(posts[0].id, (error, comentarios) => {
      if (error) return console.log(error);
      
      console.log('Listo!');
    });
  });
});
```

**Problemas**:
1. ❌ Pirámide de indentación
2. ❌ Manejo de errores repetitivo
3. ❌ Difícil de leer/mantener

---

## 🎉 La Solución: Promises

En 2015, JavaScript introdujo **Promises** para solucionar estos problemas.

### ¿Qué Cambia?

**Concepto clave**: En lugar de **pasar** un callback a una función, la función **devuelve** una Promise.

```javascript
// ANTES (Callbacks):
funcion(parametros, callback)  // Paso el callback como argumento

// AHORA (Promises):
funcion(parametros)            // Devuelve una Promise
  .then(resultado => ...)      // Encadeno qué hacer con el resultado
```

### El Mismo Ejemplo con Promises

```javascript
// Con Promises ✅
obtenerUsuario(1)
  .then(usuario => obtenerPosts(usuario.id))
  .then(posts => obtenerComentarios(posts[0].id))
  .then(comentarios => {
    console.log('Listo!');
  })
  .catch(error => {
    console.log('Error:', error);  // UN SOLO lugar para errores
  });
```

**Ventajas inmediatas**:
- ✅ Sin pirámide (flujo lineal hacia abajo)
- ✅ Un solo `.catch()` para todos los errores
- ✅ Más legible (como leer un libro)

---

## ¿Qué es una Promise?

Una **Promise** (promesa) es un objeto de JavaScript que representa el resultado **futuro** de una operación asíncrona.

### Analogía: Pedido en un Restaurante

Cuando pides comida:
1. **Haces el pedido** → Te dan un ticket (la Promise)
2. **Esperas** → La comida se está preparando (Promise pendiente)
3. **Resultado**:
   - ✅ Te traen tu comida (Promise resuelta/resolved)
   - ❌ Te dicen "no hay ingredientes" (Promise rechazada/rejected)

### En Código

```javascript
// Crear una Promise
const miPromesa = pedirDatosAlServidor();  // Devuelve Promise

// La Promise está en estado "pending" (esperando)

// Después de 2 segundos...
// - Si todo va bien: Promise "resolved" ✅
// - Si hay error: Promise "rejected" ❌

// Tú decides qué hacer en cada caso:
miPromesa
  .then(datos => console.log('Datos:', datos))      // Si se resuelve
  .catch(error => console.log('Error:', error));   // Si se rechaza
```

### Relación con Asíncrono

**Recuerda**: Operaciones asíncronas tardan tiempo (pedir datos a servidor, leer archivo, etc).

**Problema de callbacks**: Tenías que pasar la función callback como argumento.

**Solución de Promises**: La función devuelve un objeto (Promise) que puedes manipular.

```javascript
// Operación asíncrona con Callback:
pedirDatos(url, function(error, datos) {
  // Manejarlo aquí adentro
});

// Operación asíncrona con Promise:
const promesa = pedirDatos(url);  // Devuelve Promise

// Puedes manipular la promesa:
promesa.then(...);     // Encadenar
promesa.catch(...);    // Manejar errores

// O guardarla para después:
const p1 = pedirDatos(url1);
const p2 = pedirDatos(url2);
Promise.all([p1, p2]).then(...)  // Esperar ambas
```

---

## ¿Qué ES una Promise? (Técnico)

Una **Promise** es un objeto de JavaScript que representa un valor que puede no estar disponible ahora, pero lo estará en el futuro.

Es como un pedido en un restaurante:
- **Haces el pedido** (crear Promise)
- **Esperas** (Promise pendiente)
- **Recibes el resultado** (Promise resuelta) o **te dicen que no hay** (Promise rechazada)

### La Ventaja Principal

Con Promises, el mismo código se vuelve lineal:

```javascript
// Con Promises ✅
obtenerUsuario(1)
  .then(usuario => obtenerPosts(usuario.id))
  .then(posts => obtenerComentarios(posts[0].id))
  .then(comentarios => console.log('Listo!'))
  .catch(error => console.log('Error:', error));
```

**Mucho más legible** 🎉

## Los 3 Estados de una Promise

```javascript
const promise = new Promise((resolve, reject) => {
  // PENDING: La promesa aún no se ha resuelto
  
  setTimeout(() => {
    // RESOLVED: La promesa se completó exitosamente
    resolve('¡Éxito!');
    // O REJECTED: Algo salió mal
    // reject('Error');
  }, 1000);
});
```

| Estado | Significado |
|--------|-------------|
| **Pending** | La promesa aún está en proceso |
| **Resolved** | La promesa se completó con éxito |
| **Rejected** | La promesa falló con un error |

## Sintaxis: then(), catch(), finally()

### then() - Cuando se resuelve
```javascript
fetch('https://api.example.com/datos')
  .then(response => {
    console.log('✅ Respuesta recibida');
    return response.json();
  })
  .then(data => {
    console.log('Datos:', data);
  });
```

### catch() - Cuando falla
```javascript
fetch('https://api.example.com/datos')
  .then(r => r.json())
  .catch(error => {
    console.log('❌ Error:', error);
  });
```

### finally() - Siempre se ejecuta
```javascript
fetch('https://api.example.com/datos')
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(error => console.log(error))
  .finally(() => {
    console.log('Fin de la petición');
  });
```

## Ejemplo 1: Promise Básica

```javascript
// Crear una promise
const miPromise = new Promise((resolve, reject) => {
  const exito = true;
  
  setTimeout(() => {
    if (exito) {
      resolve('¡Misión cumplida!');
    } else {
      reject('Algo salió mal');
    }
  }, 2000);
});

// Consumir la promise
miPromise
  .then(resultado => {
    console.log(resultado); // ✅ '¡Misión cumplida!'
  })
  .catch(error => {
    console.log(error);
  });
```

## Ejemplo 2: Promise Chaining

```javascript
function obtenerDatos(userId) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
    .then(response => response.json())
    .then(user => {
      console.log('Usuario:', user.name);
      // Obtener posts del usuario
      return fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
    })
    .then(response => response.json())
    .then(posts => {
      console.log('Posts:', posts.length);
      return posts;
    })
    .catch(error => {
      console.log('Error:', error);
    });
}

obtenerDatos(1);
```

**Flujo**:
1. Obtener usuario con ID 1
2. Mostrar nombre del usuario
3. Obtener posts del usuario
4. Mostrar cantidad de posts
5. Si hay error en cualquier paso, atraparlo

## Ejemplo 3: Promise.all() - Múltiples Promises

```javascript
const promise1 = fetch('https://jsonplaceholder.typicode.com/users/1').then(r => r.json());
const promise2 = fetch('https://jsonplaceholder.typicode.com/posts/1').then(r => r.json());
const promise3 = fetch('https://jsonplaceholder.typicode.com/comments/1').then(r => r.json());

// Esperar a que TODAS se resuelvan
Promise.all([promise1, promise2, promise3])
  .then(([usuario, post, comentario]) => {
    console.log('Usuario:', usuario.name);
    console.log('Post:', post.title);
    console.log('Comentario:', comentario.body);
  })
  .catch(error => {
    console.log('Al menos una falló:', error);
  });
```

## Ejemplo 4: Promise.race() - La Más Rápida

```javascript
const rápida = new Promise(resolve => {
  setTimeout(() => resolve('Rápida'), 100);
});

const lenta = new Promise(resolve => {
  setTimeout(() => resolve('Lenta'), 1000);
});

// Devuelve la primera que se resuelva
Promise.race([rápida, lenta])
  .then(resultado => {
    console.log(resultado); // 'Rápida'
  });
```

## Errores Comunes

### Error 1: Olvidar return en .then()
```javascript
// ❌ MALO
fetch(url)
  .then(r => r.json())
  .then(data => {
    setData(data);
    // Falta return, el siguiente .then() no recibe nada
  })
  .then(resultado => {
    console.log(resultado); // undefined
  });

// ✅ BIEN
fetch(url)
  .then(r => r.json())
  .then(data => {
    setData(data);
    return data; // Retorna para el siguiente .then()
  })
  .then(resultado => {
    console.log(resultado); // datos
  });
```

### Error 2: No capturar errores
```javascript
// ❌ MALO - Si falla, nada lo atrapa
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data));

// ✅ BIEN
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(error => console.log('Error:', error));
```

## Puntos Clave ✨

1. **Promise es asincronía**: El código continúa mientras espera
2. **Tres estados**: Pending, Resolved, Rejected
3. **then()** para éxito, **catch()** para errores
4. **finally()** se ejecuta siempre
5. **Chaining** para encadenar operaciones

## Tu Ejercicio 🎯

Crea una función que:

1. ✅ Obtenga datos de https://jsonplaceholder.typicode.com/users/1
2. ✅ Muestre el nombre del usuario en consola
3. ✅ Maneje errores si algo falla
4. ✅ Use .finally() para imprimir "Petición completada"

**Pista**: Usa .then() para r.json(), luego otro .then() para acceder a los datos

---

## Próximos Pasos

Una vez entiendas Promises:

✅ Cómo funcionan las promesas  
✅ then/catch/finally  
✅ Promise chaining  

Estarás listo para:
- **Step 5**: Async/Await (forma más limpia de usar Promises)
- **Step 6**: Fetch API

---

**💡 Consejo**: Las Promises son la base de todo código asincrónico en JavaScript. Domínalas bien antes de continuar.
