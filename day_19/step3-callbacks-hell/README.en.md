[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 3: Callbacks and "Callback Hell" 🔥

## 🔗 Why This Step?

In Step 2 you learned that setTimeout runs code **after** some time. But what if you need to perform **several operations in sequence**?

Real-world example:
1. Request a user's data from the server (⌛ takes X seconds)
2. With that data, request the user's posts (⌛ takes X more seconds)
3. With the first post, request its comments (⌛ takes X more seconds)

**Each step depends on the previous one.** You can't request posts before you have the user.

This need to **run code in sequence asynchronously** is where callbacks come from... and so does "Callback Hell".

---

## 🔗 Connection: Async + Callbacks

Before looking at what a callback is, you need to understand **why they exist** and **how they relate to async code**.

### The Problem: Async Code Needs to "Notify" When It Finishes

**Remember from Step 1**: Async code = doesn't block, runs "in the future".

**Question**: If an operation takes time (like asking a server for data), how does JavaScript know what to do when it's done?

#### Synchronous Code (easy):
```javascript
// Line by line, in order
const resultado1 = operacion1();     // Waits here until done
const resultado2 = operacion2();     // Then this
const resultado3 = operacion3();     // Then this
console.log('Todo listo');
```

**Simple**: JavaScript waits at each line. When it finishes, it moves on.

#### Async Code (problem):
```javascript
// ❌ THIS DOESN'T WORK
const resultado = pedirDatosAlServidor();  // Takes 2 seconds
console.log(resultado);                    // undefined (hasn't arrived)
```

**Problem**: `pedirDatosAlServidor()` takes 2 seconds, but JavaScript doesn't wait. It moves on immediately and `resultado` doesn't exist yet.

### The Solution: Callbacks

A **callback** is a function you give JavaScript that says: **"When you're done, run this"**.

```javascript
// ✅ WITH A CALLBACK IT WORKS
pedirDatosAlServidor(function(resultado) {
  // This function runs "in the future" when the data arrives
  console.log(resultado);  // Now we have the data
});

console.log('Continúo mientras espero...');

// Output:
// Continúo mientras espero...
// (2 seconds later)
// { datos: [...] }
```

### Flow Visualization

```
Time →

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Synchronous code:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

│ paso1() │ paso2() │ paso3() │ console.log() │
└─────────┴─────────┴─────────┴───────────────┘
   WAIT     WAIT      WAIT       RUNS


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Async code WITH a callback:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

│ pedirDatos(callback) │ console.log() │
└──────────────────────┴───────────────┘
   FIRES (doesn't wait)    RUNS
         ↓
         │ (waiting...)
         ↓
         │ (2 seconds later)
         ↓
   ┌─────────────┐
   │  callback() │  ← Runs when the data arrives
   └─────────────┘
```

---

## What Is a Callback?

A **callback** is a function passed as a parameter to another function so it runs **after** something finishes.

**In other words**: It's how you tell JavaScript "when you finish this async operation, run this function".

```javascript
function hacerAlgo(callback) {
  console.log('Haciendo algo...');
  callback(); // Runs the function we passed in
}

// We pass a function as a callback
hacerAlgo(() => {
  console.log('¡Terminé!');
});

// Output:
// Haciendo algo...
// ¡Terminé!
```

---

## Callbacks in Async Operations

Callbacks are very common in async operations:

### Example with setTimeout

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Callback ejecutado después de 1 segundo');
}, 1000);

console.log('Fin');

// Output:
// Inicio
// Fin
// (waits 1 second)
// Callback ejecutado después de 1 segundo
```

### Example with Events

```javascript
const boton = document.querySelector('button');

// The callback runs when you click
boton.addEventListener('click', () => {
  console.log('¡Botón clickeado!');
});
```

---

## Callbacks for Sequences

What if you need to perform **several operations in sequence**?

### Scenario: Get a user's data

1. Get the user by ID
2. Get their posts
3. Get comments on the first post

```javascript
// Simulate async operations
function obtenerUsuario(id, callback) {
  setTimeout(() => {
    console.log('Usuario obtenido');
    callback({ id: id, nombre: 'Juan' });
  }, 1000);
}

function obtenerPosts(userId, callback) {
  setTimeout(() => {
    console.log('Posts obtenidos');
    callback([{ id: 1, titulo: 'Primer post' }]);
  }, 1000);
}

function obtenerComentarios(postId, callback) {
  setTimeout(() => {
    console.log('Comentarios obtenidos');
    callback(['Comentario 1', 'Comentario 2']);
  }, 1000);
}

// Use them in sequence...
obtenerUsuario(1, (usuario) => {
  console.log('Usuario:', usuario.nombre);
  
  obtenerPosts(usuario.id, (posts) => {
    console.log('Posts:', posts.length);
    
    obtenerComentarios(posts[0].id, (comentarios) => {
      console.log('Comentarios:', comentarios.length);
    });
  });
});
```

**Problem**: It's already starting to look nested and hard to read...

---

## "Callback Hell" (The Pyramid of Doom) 💀

When you have many sequential async operations, your code turns into an **indented pyramid**.

### Real-World Example: Login System

Imagine you're building a login. You need to:

1. Validate the user's email
2. Look up the user in the database
3. Verify the password
4. Generate a session token
5. Save the session
6. Load the profile data
7. Redirect to the dashboard

**Each step takes time and depends on the previous one.** Here's what it looks like with callbacks:

```javascript
validarEmail(email, (errorValidacion, emailValido) => {
  if (errorValidacion) {
    console.log('Error: Email inválido');
    return;
  }
  
  buscarUsuario(emailValido, (errorBusqueda, usuario) => {
    if (errorBusqueda) {
      console.log('Error: Usuario no encontrado');
      return;
    }
    
    verificarPassword(usuario, password, (errorPassword, esValido) => {
      if (errorPassword || !esValido) {
        console.log('Error: Contraseña incorrecta');
        return;
      }
      
      generarToken(usuario.id, (errorToken, token) => {
        if (errorToken) {
          console.log('Error: No se pudo generar token');
          return;
        }
        
        guardarSesion(token, (errorSesion) => {
          if (errorSesion) {
            console.log('Error: No se pudo guardar sesión');
            return;
          }
          
          cargarPerfil(usuario.id, (errorPerfil, perfil) => {
            if (errorPerfil) {
              console.log('Error: No se pudo cargar perfil');
              return;
            }
            
            redirigirDashboard(perfil, (errorRedireccion) => {
              if (errorRedireccion) {
                console.log('Error: No se pudo redirigir');
                return;
              }
              
              console.log('✅ Login exitoso!');
            });
          });
        });
      });
    });
  });
});
```

### See the Problem? 😱

**Count the indentation levels**: 7 levels to the right.

Now imagine:
- ❌ You need to add another step (level 8)
- ❌ You need to change the order of something
- ❌ There's a bug on step 5 and you have to debug it
- ❌ You need to add logs at every step
- ❌ The code is 200 lines long, all nested like this

**It's a nightmare.**

### Why Is This a REAL Problem?

1. **❌ Hard to read**: Your eyes have to follow the pyramid to the right
2. **❌ Hard to maintain**: Adding or removing a step requires touching many lines
3. **❌ Hard to debug**: Where's the error? At which level?
4. **❌ Hard to test**: You can't test "verificarPassword" without running everything before it
5. **❌ Duplicated code**: `if (error) { console.log(...); return; }` is repeated 7 times
6. **❌ You can't reuse**: Each step is locked inside the previous one

### Problem Visualization

```
Normal code (ideal):          Callback Hell (reality):

Step 1                        Step 1
Step 2                          Step 2  
  Step 3                            Step 3
Step 4                                Step 4
Step 5                                    Step 5
Step 6                                        Step 6
Step 7                                            Step 7
                                                      💀
```

---

## Real Example: Callback Hell

Imagine you need to:

1. Authenticate with a server
2. Get the user data
3. Get the user's settings
4. Get notifications
5. Render everything

```javascript
autenticar('usuario', 'password', (error, token) => {
  if (error) {
    console.log('Error de autenticación:', error);
    return;
  }
  
  obtenerUsuario(token, (error, usuario) => {
    if (error) {
      console.log('Error obteniendo usuario:', error);
      return;
    }
    
    obtenerConfiguracion(usuario.id, (error, config) => {
      if (error) {
        console.log('Error obteniendo config:', error);
        return;
      }
      
      obtenerNotificaciones(usuario.id, (error, notificaciones) => {
        if (error) {
          console.log('Error obteniendo notificaciones:', error);
          return;
        }
        
        renderizar(usuario, config, notificaciones, (error) => {
          if (error) {
            console.log('Error renderizando:', error);
            return;
          }
          
          console.log('¡Todo listo!');
        });
      });
    });
  });
});
```

**Result**: Code that's impossible to maintain 😱

---

## Problem Visualization

### Without Callback Hell (Ideal)
```
Step 1
Step 2
Step 3
Step 4
```

### With Callback Hell (Reality)
```
Step 1
  Step 2
    Step 3
      Step 4
        Step 5
          Step 6
            Step 7
              Help!
```

---

## Attempted Solutions: Named Functions

You can try to avoid the pyramid by using named functions:

```javascript
function paso3(resultado3) {
  console.log('Paso 3:', resultado3);
}

function paso2(resultado2) {
  hacerAlgo3(resultado2, paso3);
}

function paso1(resultado1) {
  hacerAlgo2(resultado1, paso2);
}

hacerAlgo1(paso1);
```

**Problem**: Less nested, but still hard to follow the flow of the code.

---

## Error Handling with Callbacks

Error handling is repetitive and error-prone:

```javascript
function obtenerDatos(callback) {
  setTimeout(() => {
    const error = null; // or a real error
    const datos = { nombre: 'Juan' };
    
    if (error) {
      callback(error, null);
    } else {
      callback(null, datos);
    }
  }, 1000);
}

// Use:
obtenerDatos((error, datos) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  
  console.log('Datos:', datos);
  
  // If you need another operation, nest again...
  otraOperacion(datos, (error, resultado) => {
    if (error) {
      console.log('Error:', error);
      return;
    }
    
    // And so on...
  });
});
```

**Problem**: You have to check `if (error)` at every level.

---

## Comparison: Callbacks vs Synchronous Code

### Synchronous Code (easy to read)
```javascript
try {
  const usuario = obtenerUsuario(1);
  const posts = obtenerPosts(usuario.id);
  const comentarios = obtenerComentarios(posts[0].id);
  console.log('Listo!');
} catch (error) {
  console.log('Error:', error);
}
```

### Callbacks (hard to read)
```javascript
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

---

## What's the Solution?

### 🎉 Promises to the Rescue (Preview of Step 4)

The JavaScript community saw this problem, and in 2015 it introduced **Promises** to fix it.

**What changes?** Instead of passing callbacks, functions **return promises** that you can chain.

### Comparison: Before vs After

#### Before (Callbacks - 7 indentation levels):
```javascript
validarEmail(email, (error, emailValido) => {
  if (error) return console.log(error);
  
  buscarUsuario(emailValido, (error, usuario) => {
    if (error) return console.log(error);
    
    verificarPassword(usuario, password, (error, esValido) => {
      if (error) return console.log(error);
      
      generarToken(usuario.id, (error, token) => {
        // ... and on and on and on
      });
    });
  });
});
```

#### After (Promises - linear flow):
```javascript
validarEmail(email)
  .then(emailValido => buscarUsuario(emailValido))
  .then(usuario => verificarPassword(usuario, password))
  .then(esValido => generarToken(usuario.id))
  .then(token => guardarSesion(token))
  .then(() => cargarPerfil(usuario.id))
  .then(perfil => redirigirDashboard(perfil))
  .then(() => {
    console.log('✅ Login exitoso!');
  })
  .catch(error => {
    // ONE single place to handle ALL errors
    console.log('❌ Error:', error.message);
  });
```

### See the Difference? 🤯

**With Promises**:
- ✅ **No pyramid**: Everything flows linearly (downward, not to the right)
- ✅ **A single `.catch()`**: Handles ALL errors in one place
- ✅ **More readable**: You read top to bottom like a book
- ✅ **Easy to modify**: Adding a step = adding one `.then()` line
- ✅ **Reusable**: Each function returns a Promise you can use wherever you want

### The Key Concept

Instead of:
```javascript
funcion(parametros, callback)  // Pass the callback
```

Now:
```javascript
funcion(parametros)           // Returns a Promise
  .then(resultado => ...)     // Do something with the result
```

**In Step 4 you'll learn exactly what a Promise is and how it works.** For now, just understand that **they solve Callback Hell**.

---

## Key Points ✨

1. **Callback**: A function that runs after another operation
2. **Callback Hell**: A pyramid of nested callbacks
3. **Problems**: Hard to read, maintain, debug and test
4. **Solution**: Promises (Step 4) and async/await (Step 5)
5. **Error handling**: Repetitive at every level with callbacks

---

## Your Exercise 🎯

Analyze this code and count how many levels of nesting it has:

```javascript
operacion1((resultado1) => {
  operacion2(resultado1, (resultado2) => {
    operacion3(resultado2, (resultado3) => {
      operacion4(resultado3, (resultado4) => {
        console.log('Final:', resultado4);
      });
    });
  });
});
```

**Answer**: 4 levels of nesting

**Question**: How would you handle errors at each operation? (Spoiler: tedious)

---

## Next Steps

Now that you understand the Callback Hell problem:

✅ What callbacks are  
✅ Why nested callbacks are problematic  
✅ Maintenance and error-handling pain  

You'll be ready for:
- **Step 4**: Promises - The solution to Callback Hell
- **Step 5**: Async/Await - Cleaner syntax on top of Promises

---

**💡 Tip**: Callback Hell was a real problem in old JavaScript. That's why Promises were created. Understanding the problem will help you appreciate the solution.

**🎯 Rule**: If you see more than 2-3 levels of nested callbacks, you probably need Promises or async/await.

**📖 History**: Before 2015 (ES6), everyone had to deal with Callback Hell. Promises changed everything.
