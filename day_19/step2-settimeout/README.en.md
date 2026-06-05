[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 2: setTimeout - Your First Async Tool ⏱️

## 🔗 Why Are We Studying setTimeout?

Now that you understand the difference between synchronous and asynchronous code (Step 1), you need to see how it works in practice.

**setTimeout** is JavaScript's **simplest** async tool. Learning it is crucial because:

1. 🎯 **It's the foundation**: All async code runs on the same principles
2. 🎯 **It simulates real operations**: Many things in programming "take time" (reading files, requesting data from a server, waiting for a response)
3. 🎯 **Understanding the Event Loop**: See how JavaScript handles tasks that "take time"

### Why Is It Important?

In the real world, many operations **aren't instant**:

```javascript
// Operations that "take time":
- Reading a file from disk
- Requesting data from a server over the internet
- Waiting for the user to click a button
- Processing an image or video
- Querying a database
```

**setTimeout lets us simulate these waits** so we can learn how to handle them:

```javascript
// Simulate requesting data from a server
function obtenerDatosDelServidor() {
  console.log('Pidiendo datos al servidor...');
  
  setTimeout(() => {
    // Simulates that the server took 2 seconds to respond
    console.log('✅ Datos recibidos del servidor');
  }, 2000);
}

obtenerDatosDelServidor();
console.log('Mientras tanto, sigo ejecutando otro código...');

// Output:
// Pidiendo datos al servidor...
// Mientras tanto, sigo ejecutando otro código...
// (waits 2 seconds)
// ✅ Datos recibidos del servidor
```

**Key concept**: The code **doesn't block** while waiting. It keeps running, and when the operation finishes, it runs the callback.

### What Is the Event Loop?

The **Event Loop** is the mechanism that lets JavaScript run async code without blocking.

**Simple analogy**: Imagine a restaurant:
- **Cook (Call Stack)**: Prepares one dish at a time
- **Waiters (Web APIs)**: Take orders that take time (timers, server requests)
- **Ready-order tray (Task Queue)**: Orders waiting to be served
- **Manager (Event Loop)**: When the cook is free, picks the next order from the tray

```
Your code (client) places an order (setTimeout)
    ↓
Waiter takes it and waits (Web API handles the timer)
    ↓
When it's ready, places it on the tray (Task Queue)
    ↓
Manager sees the cook is free (Call Stack empty)
    ↓
Hands the order to the cook (runs the callback)
```

**That's why setTimeout(fn, 0) doesn't run immediately** — it has to wait until the cook (Call Stack) is free.

We'll cover this in detail later in this step.

---

## What Is setTimeout?

**setTimeout** is a function that runs code **after** a set amount of time. It's your first async tool.

```javascript
setTimeout(() => {
  console.log('¡Hola después de 2 segundos!');
}, 2000); // 2000 milliseconds = 2 seconds
```

---

## Basic Syntax

```javascript
setTimeout(función, milisegundos, parámetro1, parámetro2, ...);
```

### Parameters:
1. **función**: What to run when the time elapses
2. **milisegundos**: How long to wait (1000ms = 1 second)
3. **parámetros** (optional): Values passed to the function

---

## Example 1: Basic

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Ejecuto después de 1 segundo');
}, 1000);

console.log('Fin');

// Output:
// Inicio
// Fin
// (waits 1 second)
// Ejecuto después de 1 segundo
```

**Note**: `Fin` prints first because setTimeout is **asynchronous**.

---

## Example 2: With Parameters

```javascript
function saludar(nombre, edad) {
  console.log(`Hola ${nombre}, tienes ${edad} años`);
}

// Pass parameters after the time
setTimeout(saludar, 2000, 'Ana', 25);

// After 2 seconds:
// Hola Ana, tienes 25 años
```

---

## Example 3: Cancel setTimeout

You can **cancel** a setTimeout before it runs:

```javascript
const timer = setTimeout(() => {
  console.log('Esto nunca se ejecutará');
}, 3000);

// Cancel before the 3 seconds elapse
clearTimeout(timer);

console.log('Timer cancelado');
```

---

## setInterval: Repeat Code

**setInterval** runs code **repeatedly** at a set interval.

```javascript
let contador = 0;

const intervalo = setInterval(() => {
  contador++;
  console.log(`Han pasado ${contador} segundos`);
  
  // Stop after 5 seconds
  if (contador === 5) {
    clearInterval(intervalo);
    console.log('¡Detenido!');
  }
}, 1000); // Every 1 second

// Output:
// Han pasado 1 segundos
// Han pasado 2 segundos
// Han pasado 3 segundos
// Han pasado 4 segundos
// Han pasado 5 segundos
// ¡Detenido!
```

---

## Difference: setTimeout vs setInterval

### setTimeout
```javascript
setTimeout(() => {
  console.log('Se ejecuta UNA VEZ después de 2 segundos');
}, 2000);
```

### setInterval
```javascript
setInterval(() => {
  console.log('Se ejecuta CADA 2 segundos');
}, 2000);
```

| Function | When? | Cancel |
|---------|----------|----------|
| **setTimeout** | Once after X ms | `clearTimeout()` |
| **setInterval** | Every X ms | `clearInterval()` |

---

## Practical Example: Countdown from 5 to 0

```javascript
let tiempo = 5;

const cuentaRegresiva = setInterval(() => {
  console.log(tiempo);
  tiempo--;
  
  if (tiempo < 0) {
    clearInterval(cuentaRegresiva);
    console.log('¡Tiempo terminado!');
  }
}, 1000);

// Output:
// 5
// 4
// 3
// 2
// 1
// 0
// ¡Tiempo terminado!
```

---

## How Does It Work? Simplified Event Loop 🔄

JavaScript has an **Event Loop** that handles async code:

### 1. Call Stack
Where synchronous code runs.

```javascript
console.log('A');    // ← Runs immediately
console.log('B');    // ← Then this
```

### 2. Web APIs
Where async operations go (setTimeout, server requests, etc.).

```javascript
setTimeout(() => {
  console.log('C');  // ← Goes to Web APIs
}, 1000);
```

### 3. Task Queue
When the time is up, the function goes here.

### 4. Event Loop
When the Call Stack is empty, it moves tasks from the Queue to the Stack.

---

## Event Loop Visualization

```javascript
console.log('1');

setTimeout(() => {
  console.log('2');
}, 0); // ⚠️ 0 milliseconds

console.log('3');
```

**What happens?**

```
1. Call Stack: console.log('1')           → Prints "1"
2. Call Stack: setTimeout(...)            → Goes to Web APIs
3. Call Stack: console.log('3')           → Prints "3"
4. Call Stack is empty                    → Event Loop activates
5. Task Queue: setTimeout callback        → Moves to Call Stack
6. Call Stack: console.log('2')           → Prints "2"
```

**Output**: 1, 3, 2

**Conclusion**: Even with 0ms, setTimeout is asynchronous and runs after the synchronous code.

---

## Real Example: Show a Message After Loading

```javascript
console.log('Cargando datos...');

setTimeout(() => {
  console.log('✅ Datos cargados exitosamente');
}, 2000);

console.log('Continúa usando la app mientras carga...');

// Immediate output:
// Cargando datos...
// Continúa usando la app mientras carga...
// (waits 2 seconds)
// ✅ Datos cargados exitosamente
```

---

## React Example

```javascript
import { useState, useEffect } from 'react';

function ContadorTiempo() {
  const [segundos, setSegundos] = useState(0);

  useEffect(() => {
    // Increment every second
    const intervalo = setInterval(() => {
      setSegundos(prev => prev + 1);
    }, 1000);

    // Clean up on unmount
    return () => clearInterval(intervalo);
  }, []);

  return (
    <div>
      <h2>Han pasado {segundos} segundos</h2>
    </div>
  );
}

export default ContadorTiempo;
```

---

## Common Mistakes

### Mistake 1: Not saving the ID to cancel

```javascript
// ❌ BAD - You can't cancel it
setTimeout(() => {
  console.log('No puedo cancelar esto');
}, 5000);

// ✅ GOOD
const timer = setTimeout(() => {
  console.log('Puedo cancelar esto');
}, 5000);

// If I need to cancel:
clearTimeout(timer);
```

### Mistake 2: Forgetting clearInterval

```javascript
// ❌ BAD - Runs forever
setInterval(() => {
  console.log('Esto nunca se detiene');
}, 1000);

// ✅ GOOD
const intervalo = setInterval(() => {
  console.log('Esto puedo detener');
}, 1000);

// Stop after 5 seconds
setTimeout(() => {
  clearInterval(intervalo);
}, 5000);
```

### Mistake 3: Mixing up seconds and milliseconds

```javascript
// ❌ BAD - Waits 3 milliseconds (almost instant)
setTimeout(() => {
  console.log('Muy rápido');
}, 3); // 3ms

// ✅ GOOD - Waits 3 seconds
setTimeout(() => {
  console.log('Después de 3 segundos');
}, 3000); // 3000ms = 3 seconds
```

---

## Nested setTimeouts (Sequence)

If you want to run things in sequence:

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Paso 1');
  
  setTimeout(() => {
    console.log('Paso 2');
    
    setTimeout(() => {
      console.log('Paso 3');
    }, 1000);
  }, 1000);
}, 1000);

// Output (with 1 second between each):
// Inicio
// Paso 1
// Paso 2
// Paso 3
```

**Problem**: This gets hard to read (sneak peek of "Callback Hell" in Step 3!).

---

## Key Points ✨

1. **setTimeout**: Runs code after X milliseconds
2. **setInterval**: Runs code every X milliseconds
3. **clearTimeout/clearInterval**: Cancel timers
4. **Event Loop**: JavaScript processes async work when the Call Stack is empty
5. **1000ms = 1 second**: Always use milliseconds
6. **Always clean up**: Use clear when you no longer need the timer

---

## Your Exercise 🎯

Build a countdown that:

1. ✅ Starts at 10
2. ✅ Prints the number every second
3. ✅ When it reaches 0, prints "🚀 ¡Despegue!"
4. ✅ Stops automatically

**Hint**: Use `setInterval` and `clearInterval`

---

## Next Steps

Once you've mastered setTimeout/setInterval:

✅ setTimeout for async code  
✅ setInterval for repeating code  
✅ Basic Event Loop  
✅ How to cancel timers  

You'll be ready for:
- **Step 3**: Callbacks and the "Callback Hell" problem
- **Step 4**: Promises - A more elegant solution

---

**💡 Tip**: setTimeout is your first async tool. It's simple, but it's the foundation for understanding more complex async code.

**⚠️ Important**: Always remember that setTimeout/setInterval are **approximate**. If the Call Stack is busy, they can run later than the specified time.
