[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 4: Promises - The Solution to Callback Hell 🤝

## 🔗 Context: From Callbacks to Promises

### Remembering the Problems

In the previous steps you learned:

**Step 1**: **Async** code = operations that take time (don't block)  
**Step 2**: **setTimeout** = first async tool  
**Step 3**: **Callbacks** = "when you finish, run this"  
**Step 3**: **Callback Hell** = nested callbacks = unreadable code  

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

**Problems**:
1. ❌ Indentation pyramid
2. ❌ Repetitive error handling
3. ❌ Hard to read/maintain

---

## 🎉 The Solution: Promises

In 2015, JavaScript introduced **Promises** to fix these problems.

### What Changes?

**Key concept**: Instead of **passing** a callback to a function, the function **returns** a Promise.

```javascript
// BEFORE (callbacks):
funcion(parametros, callback)  // I pass the callback as an argument

// NOW (Promises):
funcion(parametros)            // Returns a Promise
  .then(resultado => ...)      // Chain what to do with the result
```

### The Same Example with Promises

```javascript
// With Promises ✅
obtenerUsuario(1)
  .then(usuario => obtenerPosts(usuario.id))
  .then(posts => obtenerComentarios(posts[0].id))
  .then(comentarios => {
    console.log('Listo!');
  })
  .catch(error => {
    console.log('Error:', error);  // ONE place to handle errors
  });
```

**Immediate benefits**:
- ✅ No pyramid (linear downward flow)
- ✅ A single `.catch()` for all errors
- ✅ More readable (reads like a book)

---

## What Is a Promise?

A **Promise** is a JavaScript object that represents the **future** result of an async operation.

### Analogy: Ordering at a Restaurant

When you order food:
1. **You place the order** → They give you a ticket (the Promise)
2. **You wait** → The food is being prepared (pending Promise)
3. **Result**:
   - ✅ They bring your food (Promise resolved)
   - ❌ They say "we're out of ingredients" (Promise rejected)

### In Code

```javascript
// Create a Promise
const miPromesa = pedirDatosAlServidor();  // Returns Promise

// The Promise is in "pending" state (waiting)

// After 2 seconds...
// - If all goes well: Promise "resolved" ✅
// - If there's an error: Promise "rejected" ❌

// You decide what to do in each case:
miPromesa
  .then(datos => console.log('Datos:', datos))      // If resolved
  .catch(error => console.log('Error:', error));   // If rejected
```

### Relationship with Async

**Remember**: Async operations take time (asking a server for data, reading a file, etc.).

**Callback problem**: You had to pass the callback function as an argument.

**Promise solution**: The function returns an object (Promise) you can manipulate.

```javascript
// Async operation with a callback:
pedirDatos(url, function(error, datos) {
  // Handle it inside here
});

// Async operation with a Promise:
const promesa = pedirDatos(url);  // Returns a Promise

// You can manipulate the promise:
promesa.then(...);     // Chain
promesa.catch(...);    // Handle errors

// Or save it for later:
const p1 = pedirDatos(url1);
const p2 = pedirDatos(url2);
Promise.all([p1, p2]).then(...)  // Wait for both
```

---

## What IS a Promise? (Technical)

A **Promise** is a JavaScript object that represents a value that may not be available now, but will be in the future.

It's like an order at a restaurant:
- **You place the order** (create the Promise)
- **You wait** (pending Promise)
- **You receive the result** (resolved Promise) or **they tell you they don't have it** (rejected Promise)

### The Main Benefit

With Promises, the same code becomes linear:

```javascript
// With Promises ✅
obtenerUsuario(1)
  .then(usuario => obtenerPosts(usuario.id))
  .then(posts => obtenerComentarios(posts[0].id))
  .then(comentarios => console.log('Listo!'))
  .catch(error => console.log('Error:', error));
```

**Much more readable** 🎉

## The 3 States of a Promise

```javascript
const promise = new Promise((resolve, reject) => {
  // PENDING: The promise hasn't been resolved yet
  
  setTimeout(() => {
    // RESOLVED: The promise completed successfully
    resolve('¡Éxito!');
    // Or REJECTED: Something went wrong
    // reject('Error');
  }, 1000);
});
```

| State | Meaning |
|--------|-------------|
| **Pending** | The promise is still in progress |
| **Resolved** | The promise completed successfully |
| **Rejected** | The promise failed with an error |

## Syntax: then(), catch(), finally()

### then() - When it resolves
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

### catch() - When it fails
```javascript
fetch('https://api.example.com/datos')
  .then(r => r.json())
  .catch(error => {
    console.log('❌ Error:', error);
  });
```

### finally() - Always runs
```javascript
fetch('https://api.example.com/datos')
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(error => console.log(error))
  .finally(() => {
    console.log('Fin de la petición');
  });
```

## Example 1: Basic Promise

```javascript
// Create a promise
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

// Consume the promise
miPromise
  .then(resultado => {
    console.log(resultado); // ✅ '¡Misión cumplida!'
  })
  .catch(error => {
    console.log(error);
  });
```

## Example 2: Promise Chaining

```javascript
function obtenerDatos(userId) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
    .then(response => response.json())
    .then(user => {
      console.log('Usuario:', user.name);
      // Get the user's posts
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

**Flow**:
1. Get the user with ID 1
2. Display the user's name
3. Get the user's posts
4. Display the post count
5. If any step errors, catch it

## Example 3: Promise.all() - Multiple Promises

```javascript
const promise1 = fetch('https://jsonplaceholder.typicode.com/users/1').then(r => r.json());
const promise2 = fetch('https://jsonplaceholder.typicode.com/posts/1').then(r => r.json());
const promise3 = fetch('https://jsonplaceholder.typicode.com/comments/1').then(r => r.json());

// Wait for ALL to resolve
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

## Example 4: Promise.race() - The Fastest

```javascript
const rápida = new Promise(resolve => {
  setTimeout(() => resolve('Rápida'), 100);
});

const lenta = new Promise(resolve => {
  setTimeout(() => resolve('Lenta'), 1000);
});

// Returns the first one to resolve
Promise.race([rápida, lenta])
  .then(resultado => {
    console.log(resultado); // 'Rápida'
  });
```

## Common Mistakes

### Mistake 1: Forgetting return in .then()
```javascript
// ❌ BAD
fetch(url)
  .then(r => r.json())
  .then(data => {
    setData(data);
    // Missing return, the next .then() gets nothing
  })
  .then(resultado => {
    console.log(resultado); // undefined
  });

// ✅ GOOD
fetch(url)
  .then(r => r.json())
  .then(data => {
    setData(data);
    return data; // Return for the next .then()
  })
  .then(resultado => {
    console.log(resultado); // datos
  });
```

### Mistake 2: Not catching errors
```javascript
// ❌ BAD - If it fails, nothing catches it
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data));

// ✅ GOOD
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(error => console.log('Error:', error));
```

## Key Points ✨

1. **Promise = asynchrony**: Code keeps running while waiting
2. **Three states**: Pending, Resolved, Rejected
3. **then()** for success, **catch()** for errors
4. **finally()** always runs
5. **Chaining** to chain operations

## Your Exercise 🎯

Build a function that:

1. ✅ Fetches data from https://jsonplaceholder.typicode.com/users/1
2. ✅ Logs the user's name to the console
3. ✅ Handles errors if something fails
4. ✅ Uses .finally() to print "Petición completada"

**Hint**: Use .then() for r.json(), then another .then() to access the data

---

## Next Steps

Once you understand Promises:

✅ How promises work  
✅ then/catch/finally  
✅ Promise chaining  

You'll be ready for:
- **Step 5**: Async/Await (a cleaner way to use Promises)
- **Step 6**: Fetch API

---

**💡 Tip**: Promises are the foundation of all async code in JavaScript. Master them before moving on.
