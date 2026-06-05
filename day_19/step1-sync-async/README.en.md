[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 1: Synchronous vs Asynchronous 🔄

## What Is Synchronous Code?

**Synchronous code** is code that runs **line by line**, in order, waiting for each operation to finish before moving on to the next.

### Real-Life Example: Supermarket Line 🛒

Imagine a supermarket line with **a single checkout**:

1. Person 1 reaches the checkout
2. The cashier scans all their items (⏳ 5 minutes)
3. Person 1 pays and leaves
4. **Only now** can Person 2 move forward
5. The cashier scans their items (⏳ 3 minutes)
6. And so on...

**Problem**: If one operation takes a long time, everything blocks waiting for it.

### Synchronous Code in JavaScript

```javascript
console.log('1. Inicio');
console.log('2. Procesando...');
console.log('3. Fin');

// Output:
// 1. Inicio
// 2. Procesando...
// 3. Fin
```

Everything runs in order, no surprises.

---

## What Is Asynchronous Code?

**Asynchronous code** lets the program **keep running** while it waits for a slow operation to finish.

### Real-Life Example: Restaurant 🍽️

Imagine a restaurant where:

1. The waiter takes your order
2. They **don't stand around waiting** for the kitchen to prepare your meal
3. They take orders from other tables
4. When your food is ready, they bring it to you
5. Meanwhile, they've served 10 more tables

**Advantage**: The waiter (your program) doesn't block waiting. They can do other things.

### Asynchronous Code in JavaScript

```javascript
console.log('1. Inicio');

// This runs LATER (asynchronous)
setTimeout(() => {
  console.log('2. Procesando...');
}, 2000);

console.log('3. Fin');

// Output:
// 1. Inicio
// 3. Fin
// (waits 2 seconds)
// 2. Procesando...
```

See the difference? The execution order **isn't the same as the order you wrote the code in**.

---

## Visual Comparison

### Synchronous
```
Task 1 ━━━━━━━━━━━━━> [FINISHES]
                          │
                          ▼
                      Task 2 ━━━━━> [FINISHES]
                                       │
                                       ▼
                                   Task 3 ━━━> [FINISHES]
```

Everything in sequence. One task **blocks** the next.

### Asynchronous
```
Task 1 ━━━━━━━━━━━━━> [FINISHES]
                          │
                          ├─> Task 2 (waiting) ━━━━━━━> [FINISHES]
                          │
                          └─> Task 3 ━━━> [FINISHES]
```

Several tasks can be "in progress" at the same time.

---

## Why Do We Need Asynchrony?

In web development, many operations **take time**:

- 🌐 Asking a server for data over the internet
- 📁 Reading files from the system
- 💾 Querying databases
- ⏱️ Waiting a set amount of time (timers)

If we used synchronous code, **your application would freeze** waiting for each operation.

### Example: Without Asynchrony (Blocking Code)

```javascript
console.log('Pidiendo datos al servidor...');
// Imagine this takes 5 seconds
esperarRespuestaDelServidor(); // ⏸️ EVERYTHING FREEZES HERE
console.log('Datos recibidos');
```

During those 5 seconds:
- ❌ You can't click any buttons
- ❌ You can't type into inputs
- ❌ The app is "dead"

### Example: With Asynchrony (Non-Blocking Code)

```javascript
console.log('Pidiendo datos al servidor...');

// Async operation (we'll see how it works in the next steps)
pedirDatosAlServidor(function(datos) {
  console.log('Datos recibidos:', datos);
});

console.log('Mientras tanto, puedo hacer otras cosas');

// Immediate output:
// Pidiendo datos al servidor...
// Mientras tanto, puedo hacer otras cosas
// (a few seconds later)
// Datos recibidos: {...}
```

Your app **keeps working** while it waits for the response.

---

## Common Synchronous Operations

```javascript
// Math operations
let suma = 5 + 3; // Instant

// Conditionals
if (suma > 5) {
  console.log('Mayor');
}

// Loops
for (let i = 0; i < 10; i++) {
  console.log(i); // Runs entirely immediately
}

// Variables
let nombre = 'Juan';
console.log(nombre); // Instant
```

All of these operations **run instantly**.

---

## Common Asynchronous Operations

```javascript
// setTimeout (wait some time)
setTimeout(() => {
  console.log('Después de 1 segundo');
}, 1000);

// Request data from a server
pedirDatos('url', (datos) => {
  console.log(datos); // Runs when data arrives
});

// User events
button.addEventListener('click', () => {
  console.log('Clic!'); // Runs when the user clicks
});

// Read files
leerArchivo('archivo.txt', (contenido) => {
  console.log(contenido); // Runs when reading is done
});
```

These operations **don't complete immediately**.

---

## Practical Example: Cooking 🍳

### Synchronous Version (Inefficient)
```javascript
console.log('Poner agua a hervir'); // ⏳ 5 minutes
esperarQueHierva(); // BLOCK - you do nothing else

console.log('Cortar verduras'); // ⏳ 3 minutes
esperarQueTermines(); // BLOCK

console.log('Cocinar pasta'); // ⏳ 10 minutes
esperarQueSeCocine(); // BLOCK

// Total time: 5 + 3 + 10 = 18 minutes
```

### Asynchronous Version (Efficient)
```javascript
console.log('Poner agua a hervir'); // ⏳ 5 minutes in the background

// While the water heats up...
console.log('Cortar verduras'); // ⏳ 3 minutes

// When the water boils (callback)
cuandoHierva(() => {
  console.log('Cocinar pasta'); // ⏳ 10 minutes
});

// Total time: ~13 minutes (tasks in parallel)
```

---

## Key Points ✨

1. **Synchronous** = One thing after another, in order
2. **Asynchronous** = Multiple things can be "in progress"
3. **JavaScript is asynchronous** for slow operations (asking a server for data, setTimeout, etc.)
4. **Non-blocking** = Your app keeps working while it waits
5. **Execution order** can differ from the code's order

---

## Your Exercise 🎯

Predict the output of this code:

```javascript
console.log('A');

setTimeout(() => {
  console.log('B');
}, 0); // ⚠️ 0 milliseconds

console.log('C');

// ❓ What gets printed first?
```

**Answer**: A, C, B

**Why?** Even though setTimeout has 0ms, it's still **asynchronous**. JavaScript runs all synchronous code first (A, C) and then processes the async operations (B).

---

## Next Steps

Once you understand synchronous vs asynchronous:

✅ The concept of blocking vs non-blocking code  
✅ Why JavaScript needs asynchrony  
✅ The difference between instant and slow operations  

You'll be ready for:
- **Step 2**: setTimeout - Your first async tool
- **Step 3**: Callbacks and "Callback Hell"
- **Step 4**: Promises - The modern solution

---

**💡 Tip**: This is the MOST IMPORTANT concept of the day. If you get this, everything else will make sense.

**🎯 Golden rule**: If an operation takes time (network, files, timers), JavaScript makes it asynchronous so it doesn't block your application.
