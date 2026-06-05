[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 5: Async/Await ⏳

## 🔗 Context: Why Async/Await If We Already Have Promises?

### The Evolution of Async Code

You've seen the evolution:

**Step 3**: Callbacks → Callback Hell (indentation pyramid)  
**Step 4**: Promises → Solve Callback Hell (linear flow with `.then()`)  
**Step 5**: Async/Await → Why do we need **another** improvement?  

### The Problem with Promises

Promises are **much better** than callbacks, but they still have issues:

```javascript
// With Promises - still feels "different"
function procesarDatos() {
  return obtenerUsuario(1)
    .then(usuario => {
      console.log('Usuario:', usuario.name);
      return obtenerPosts(usuario.id);
    })
    .then(posts => {
      console.log('Posts:', posts.length);
      return obtenerComentarios(posts[0].id);
    })
    .then(comentarios => {
      console.log('Comentarios:', comentarios.length);
      return comentarios;
    })
    .catch(error => {
      console.log('Error:', error);
    });
}
```

**Problems**:
1. ❌ Still looks "async" - lots of `.then()`
2. ❌ Hard to debug (weird breakpoints)
3. ❌ Doesn't look like "normal" code
4. ❌ Sharing variables between `.then()` calls is awkward

### The Question

What if we could write async code that **looks** like synchronous code?

```javascript
// Imagine SYNCHRONOUS code (if it were possible):
const usuario = obtenerUsuario(1);           // Wait
const posts = obtenerPosts(usuario.id);      // Wait
const comentarios = obtenerComentarios(posts[0].id);  // Wait
console.log('Todo listo');
```

**This code is impossible** — it would block the browser while waiting.

But... what if we could **simulate** this syntax without blocking?

---

## 🎉 The Solution: Async/Await (ES2017)

In 2017, JavaScript introduced **Async/Await**: a way to write async code that **looks** synchronous.

### What Is Async/Await?

**Async/Await** is "syntactic sugar" on top of Promises. It doesn't replace Promises, it makes them **easier to use**.

```javascript
// BEFORE (Promises with .then())
function procesarDatos() {
  return obtenerUsuario(1)
    .then(usuario => obtenerPosts(usuario.id))
    .then(posts => obtenerComentarios(posts[0].id))
    .catch(error => console.log(error));
}

// NOW (Async/Await)
async function procesarDatos() {
  try {
    const usuario = await obtenerUsuario(1);
    const posts = await obtenerPosts(usuario.id);
    const comentarios = await obtenerComentarios(posts[0].id);
    return comentarios;
  } catch (error) {
    console.log(error);
  }
}
```

### See the Difference?

**With Async/Await**:
- ✅ Reads **top to bottom** like normal code
- ✅ Looks **synchronous** (but it's still async)
- ✅ Easy-to-use variables (const usuario, const posts)
- ✅ try/catch works like in normal code
- ✅ Easier to debug

### Key Concept

**Async/Await is NOT a new technology** — it's a nicer way to write Promises.

```javascript
// These two are EXACTLY the same:

// Option 1: Promises
fetch(url).then(r => r.json()).then(data => console.log(data));

// Option 2: Async/Await
const res = await fetch(url);
const data = await res.json();
console.log(data);
```

**Under the hood, Async/Await uses Promises.** It's just nicer syntax.

---

## What Is Async/Await? (Technical Details)

**Async/Await** is a cleaner, more readable way to work with Promises. Instead of `.then()` and `.catch()`, you use syntax that looks like sync code.

```javascript
// ❌ With Promises (complex)
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(err => console.log(err));

// ✅ With Async/Await (readable)
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

## Syntax

### async function
An `async` function always returns a Promise:

```javascript
// Async function
async function saludar() {
  return 'Hola'; // Automatically becomes a Promise
}

// Equivalent to:
function saludar() {
  return Promise.resolve('Hola');
}

// Both are used the same way:
saludar().then(resultado => console.log(resultado)); // 'Hola'
```

### await keyword
`await` **pauses** the function until the Promise resolves:

```javascript
async function obtenerUsuario() {
  console.log('Obteniendo...');
  const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
  console.log('Recibido!');
  return res;
}

// When you call it:
obtenerUsuario(); // 'Obteniendo...' prints immediately
                  // 'Recibido!' prints after the request
```

## Example 1: Basic

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

**Flow**:
1. Pauses on `fetch` until the response arrives
2. Pauses on `response.json()` until the JSON is parsed
3. Prints name and email
4. If there's an error, catches it
5. finally always runs

## Example 2: Multiple awaits

```javascript
async function obtenerDatosCompletos() {
  try {
    // Wait for the user
    const userRes = await fetch('https://jsonplaceholder.typicode.com/users/1');
    const user = await userRes.json();

    // Wait for the user's posts
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

## Example 3: Await in Parallel

```javascript
async function obtenerTodo() {
  try {
    // ❌ BAD - Wait for one, then the other (slow)
    const usuario = await fetch('...').then(r => r.json());
    const posts = await fetch('...').then(r => r.json());

    // ✅ GOOD - Both in parallel (fast)
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

## Example 4: With React

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

  if (cargando) return <p>Loading...</p>;
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

## Comparison: then() vs Async/Await

```javascript
// WITH THEN()
function obtenerConThen() {
  return fetch(url)
    .then(r => r.json())
    .then(data => {
      console.log(data);
      return data;
    })
    .catch(err => console.log(err));
}

// WITH ASYNC/AWAIT
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

Both work the same, but async/await is more readable.

## Common Mistakes

### Mistake 1: Forgetting async on the function
```javascript
// ❌ BAD - Error: await outside async
function obtenerDatos() {
  const data = await fetch(url); // SyntaxError
}

// ✅ GOOD
async function obtenerDatos() {
  const data = await fetch(url);
}
```

### Mistake 2: Not handling errors
```javascript
// ❌ BAD - If it fails, the error isn't caught
async function obtenerDatos() {
  const data = await fetch(url); // If it fails, uncaught error
}

// ✅ GOOD
async function obtenerDatos() {
  try {
    const data = await fetch(url);
  } catch (error) {
    console.log('Error:', error);
  }
}
```

### Mistake 3: Mixing callbacks with async/await
```javascript
// ❌ BAD - Confusing code
async function obtenerDatos() {
  fetch(url)
    .then(r => r.json())
    .then(data => {
      await procesarDatos(data); // Confusing mix
    });
}

// ✅ GOOD - Consistent
async function obtenerDatos() {
  const res = await fetch(url);
  const data = await res.json();
  await procesarDatos(data);
}
```

## Key Points ✨

1. **async** makes a function return a Promise
2. **await** pauses execution until it resolves
3. **try/catch** to handle errors
4. **More readable** than .then().catch()
5. **Works** with any Promise, not just fetch

## Your Exercise 🎯

Convert this Promises code to async/await:

```javascript
// With Promises:
function obtenerDatos() {
  return fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(r => r.json())
    .then(user => {
      console.log(user.name);
      return user;
    })
    .catch(err => console.log(err));
}

// ❓ TODO: Convert it to async/await
```

---

## Next Steps

Once you've mastered async/await:

✅ async/await  
✅ try/catch  
✅ Integration with React  

You'll be ready for:
- **Step 6**: Complete Fetch API
- **Step 7**: REST APIs
- **Step 8**: Fetch in React components

---

**💡 Tip**: Async/Await is more readable and used in professional code. Prefer it over .then().
