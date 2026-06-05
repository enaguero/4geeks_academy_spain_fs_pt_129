[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Tutorial: React Components, Props, setInterval, and Lifecycle

## 📺 Reference Videos

- [¿Qué es React?](https://www.youtube.com/watch?v=MPLN1ahXgcs)
- [Componentes y Props en React](https://www.youtube.com/watch?v=Y2hgEGPzTZY)
- [Ciclo de vida en React](https://www.youtube.com/watch?v=qnN_FuFNq2g)

---

## 🎯 What are we learning today?

In this tutorial you'll learn the core concepts needed to build a **seconds counter** in React:

1. ✅ What **components** are and how to build reusable ones
2. ✅ What **props** are and how to pass information between components
3. ✅ How to use **setInterval** to run code repeatedly
4. ✅ The **lifecycle** of a React component
5. ✅ How to put it all together to build a visual counter

---

## 🧩 Part 1: Components in React

### What is a component?

A **component** is like a **LEGO block** you can use and reuse in different parts of your web app. It's an independent piece of your UI with its own look and behavior.

### Real-world analogy

Imagine you're building a house out of LEGO:
- 🧱 A **window** is a component (it always has the same design)
- 🚪 A **door** is another component
- 🏠 The **whole house** is made of many components together

React works the same way: your web page is built from many small components combined together.

### Your first component: A simple greeting

```jsx
function Saludo() {
    return <h1>¡Hola Mundo!</h1>;
}
```

**What's going on here?**
- `function Saludo()` → You define a component (it's just a JavaScript function)
- `return` → It returns what the component should render
- `<h1>¡Hola Mundo!</h1>` → This is JSX (HTML inside JavaScript)

### Use your component

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

function Saludo() {
    return <h1>¡Hola Mundo!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Saludo />);
```

**Result in the browser:**
```
¡Hola Mundo!
```

### ✏️ Exercise 1: Your first component

Create a component called `MiPresentacion` that shows:
- Your name in an `<h1>`
- Your age in a `<p>`
- Your city in a `<p>`

<details>
<summary>💡 See solution</summary>

```jsx
function MiPresentacion() {
    return (
        <div>
            <h1>Ana García</h1>
            <p>Edad: 25 años</p>
            <p>Ciudad: Madrid</p>
        </div>
    );
}
```
</details>

---

## 📦 Part 2: Props - Passing Information to Components

### What are props?

**Props** (properties) are like the **arguments of a function**, but for components. They let you pass information from a parent component to a child component.

### Analogy

Imagine you have a **birthday card-making machine**:
- The machine is the **component**
- You pass it the **name** and **age** as **props**
- The machine produces a personalized card with that info

### Basic props example

```jsx
// Component that RECEIVES props
function Saludo(props) {
    return <h1>¡Hola, {props.nombre}!</h1>;
}

// Using the component - SENDING props
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Saludo nombre="Carlos" />);
```

**Result:**
```
¡Hola, Carlos!
```

### How does it work?

1. When you write `<Saludo nombre="Carlos" />`, you're passing the prop `nombre` with the value `"Carlos"`
2. Inside the component, you access that value with `props.nombre`
3. The curly braces `{}` let you insert JavaScript inside JSX

### Multiple props

```jsx
function TarjetaUsuario(props) {
    return (
        <div className="tarjeta">
            <h2>{props.nombre}</h2>
            <p>Edad: {props.edad} años</p>
            <p>Ciudad: {props.ciudad}</p>
            <p>Profesión: {props.profesion}</p>
        </div>
    );
}

// Use
<TarjetaUsuario 
    nombre="María López" 
    edad={28} 
    ciudad="Barcelona" 
    profesion="Desarrolladora"
/>
```

**⚠️ Important:**
- Text goes inside quotes: `nombre="María"`
- Numbers and JavaScript go inside curly braces: `edad={28}`

### Reusing a component with different props

```jsx
function Tarjeta(props) {
    return (
        <div className="tarjeta">
            <h3>{props.titulo}</h3>
            <p>{props.descripcion}</p>
        </div>
    );
}

// You can use the same component many times with different data!
<div>
    <Tarjeta titulo="React" descripcion="Librería de JavaScript" />
    <Tarjeta titulo="Python" descripcion="Lenguaje de programación" />
    <Tarjeta titulo="HTML" descripcion="Lenguaje de marcado" />
</div>
```

### ✏️ Exercise 2: Component with props

Create a `ProductoCard` component that receives these props:
- `nombre` (product name)
- `precio` (price in euros)
- `stock` (available quantity)

And displays this information in a nice format.

<details>
<summary>💡 See solution</summary>

```jsx
function ProductoCard(props) {
    return (
        <div className="producto">
            <h3>{props.nombre}</h3>
            <p className="precio">{props.precio}€</p>
            <p className="stock">Disponibles: {props.stock} unidades</p>
        </div>
    );
}

// Use
<ProductoCard nombre="Teclado mecánico" precio={89} stock={15} />
```
</details>

---

## ⏱️ Part 3: The setInterval Function

### What is setInterval?

`setInterval` is a JavaScript function that **runs code repeatedly** at a given time interval.

### Basic syntax

```javascript
setInterval(function, timeInMilliseconds)
```

- **function**: What you want to run repeatedly
- **timeInMilliseconds**: How often (1000 ms = 1 second)

### Example 1: Counter in the console

```javascript
let contador = 0;

setInterval(() => {
    contador = contador + 1;
    console.log("Han pasado " + contador + " segundos");
}, 1000);
```

**What happens:**
- Every 1 second (1000 ms), the function runs
- The counter goes up by 1
- It's printed in the console

**Console output:**
```
Han pasado 1 segundos
Han pasado 2 segundos
Han pasado 3 segundos
Han pasado 4 segundos
...
```

### Example 2: Show it in HTML (without React yet)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Contador: <span id="contador">0</span></h1>
    
    <script>
        let segundos = 0;
        
        setInterval(() => {
            segundos = segundos + 1;
            document.getElementById('contador').textContent = segundos;
        }, 1000);
    </script>
</body>
</html>
```

### Example 3: setInterval at different speeds

```javascript
// Every half a second (fast)
setInterval(() => {
    console.log("¡Rápido!");
}, 500);

// Every 2 seconds (slow)
setInterval(() => {
    console.log("Lento...");
}, 2000);

// Every 5 seconds (very slow)
setInterval(() => {
    console.log("Muy lento......");
}, 5000);
```

### Stopping an interval: clearInterval

Sometimes you need to **stop** a `setInterval`. For that, you use `clearInterval`.

```javascript
let contador = 0;

// Save the interval's ID
const miIntervalo = setInterval(() => {
    contador = contador + 1;
    console.log(contador);
    
    // Stop when it reaches 10
    if (contador === 10) {
        clearInterval(miIntervalo);
        console.log("¡Contador detenido!");
    }
}, 1000);
```

**What happens:**
- The counter counts up to 10
- When it reaches 10, it stops automatically

### Example 4: Simple digital clock

```javascript
setInterval(() => {
    const ahora = new Date();
    const horas = ahora.getHours();
    const minutos = ahora.getMinutes();
    const segundos = ahora.getSeconds();
    
    console.log(`${horas}:${minutos}:${segundos}`);
}, 1000);
```

### ✏️ Exercise 3: Practice setInterval

Create a counter that:
1. Starts at 0
2. Goes up by 1 every second
3. Stops when it reaches 5
4. Logs "¡Terminado!" when it stops

<details>
<summary>💡 See solution</summary>

```javascript
let numero = 0;

const intervalo = setInterval(() => {
    console.log(numero);
    numero = numero + 1;
    
    if (numero > 5) {
        clearInterval(intervalo);
        console.log("¡Terminado!");
    }
}, 1000);
```
</details>

---

## 🔄 Part 4: setInterval + React

### Basic concept

Now we're going to combine `setInterval` with React to build a visual counter.

### Simple example: Counter that updates every second

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

// Component that shows the number of seconds
function ContadorSimple(props) {
    return (
        <div>
            <h1>Segundos transcurridos: {props.segundos}</h1>
        </div>
    );
}

// Get the root element
const root = ReactDOM.createRoot(document.getElementById('root'));

// Variable that counts the seconds
let segundosTranscurridos = 0;

// setInterval re-renders the component every second
setInterval(() => {
    segundosTranscurridos = segundosTranscurridos + 1;
    
    // Re-render with the new value
    root.render(<ContadorSimple segundos={segundosTranscurridos} />);
}, 1000);
```

**What's happening?**
1. We create a `ContadorSimple` component that receives `segundos` as a prop
2. Every second, `setInterval` runs its function
3. We increment `segundosTranscurridos`
4. We call `root.render()` again with the new value
5. React updates only what changed on screen (efficient ✨)

### Example with a nicer format

```jsx
function ContadorBonito(props) {
    return (
        <div className="contador-container">
            <h1>⏱️ Contador de Segundos</h1>
            <div className="numero-grande">
                {props.segundos}
            </div>
            <p>segundos transcurridos</p>
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
let tiempo = 0;

setInterval(() => {
    tiempo++;
    root.render(<ContadorBonito segundos={tiempo} />);
}, 1000);
```

### Why re-render instead of using state?

Right now we're learning the basics. In the Simple Counter project, this is the **correct** approach per the instructions:

> "The component does not need a local state, you can pass the number of seconds as props"

Later on you'll learn about `useState` and `useEffect`, which are more advanced ways to handle this.

---

## 🔄 Part 5: Component Lifecycle

### What is the lifecycle?

Every React component goes through different **phases** from when it's created to when it's removed. We call this the **component lifecycle**.

### The 3 main phases

```
   MOUNTING      →        UPDATING         →      UNMOUNTING
(Mount/Mounting)      (Update/Updating)         (Unmount)
     ↓                       ↓                        ↓
 Is created and        Gets updated             Is removed
 added to the DOM     (props or state            from the DOM
                          change)
```

### Real-life analogy

Think of an **actor in a play**:

1. **MOUNTING**: The actor **steps onto the stage** 🎭
   - Gets ready, takes their position
   
2. **UPDATING**: The actor **changes during the play** 🎬
   - Says different lines
   - Changes costume
   - Moves around the stage

3. **UNMOUNTING**: The actor **leaves the stage** 🚪
   - Walks off
   - Cleans up their space

### Phase 1: Mount

The component is **created** and **added to the DOM** for the first time.

```jsx
function MiComponente() {
    console.log("Estoy renderizando por primera vez");
    return <h1>¡Hola!</h1>;
}

// When you do this, the component MOUNTS:
root.render(<MiComponente />);
```

### Phase 2: Update

The component **re-renders** because:
- Its props changed
- Its internal state changed

```jsx
function Contador(props) {
    console.log("Me estoy actualizando, ahora seconds = " + props.seconds);
    return <h1>Segundos: {props.seconds}</h1>;
}

// First time (MOUNT):
root.render(<Contador seconds={0} />);

// One second later (UPDATE):
root.render(<Contador seconds={1} />);

// Two seconds later (UPDATE):
root.render(<Contador seconds={2} />);
```

### Phase 3: Unmount

The component is **removed** from the DOM.

```jsx
// The component is in the DOM
root.render(<MiComponente />);

// Now we remove it (UNMOUNT)
root.render(null);

// Or render a different component
root.render(<OtroComponente />);
```

### Full lifecycle visualization

```
Time 0s: root.render(<Contador seconds={0} />)
           ↓
        MOUNT - The component shows up for the first time
           
Time 1s: root.render(<Contador seconds={1} />)
           ↓
        UPDATE - Props changed (0 → 1)
           
Time 2s: root.render(<Contador seconds={2} />)
           ↓
        UPDATE - Props changed (1 → 2)
           
Time 3s: root.render(null)
           ↓
        UNMOUNT - The component is removed
```

---

## 🎣 Part 6: Hooks and useEffect (Advanced concept)

### What is a Hook?

**Hooks** are special React functions that let you "hook into" the lifecycle and other React features.

### The most important Hook for the lifecycle: useEffect

`useEffect` lets you run code at different moments in the lifecycle.

### Basic syntax

```jsx
import { useEffect } from 'react';

function MiComponente() {
    useEffect(() => {
        // Code that runs
    }, [dependencies]);
    
    return <h1>Componente</h1>;
}
```

### Case 1: Run only on MOUNT (once)

```jsx
import { useEffect } from 'react';

function MiComponente() {
    useEffect(() => {
        console.log("¡El componente se montó!");
        console.log("Esto solo se ejecuta UNA VEZ");
    }, []); // Empty array [] = only on mount
    
    return <h1>¡Hola Mundo!</h1>;
}
```

**Explanation of `[]`:**
- The empty array `[]` tells React: "run this only once, when the component mounts"

### Case 2: Run on every UPDATE

```jsx
import { useEffect } from 'react';

function Contador(props) {
    useEffect(() => {
        console.log("El componente se actualizó");
        console.log("Nuevo valor de segundos:", props.segundos);
    }); // No array = runs on every render
    
    return <h1>Segundos: {props.segundos}</h1>;
}
```

### Case 3: Run only when a specific prop changes

```jsx
import { useEffect } from 'react';

function Usuario(props) {
    useEffect(() => {
        console.log("El nombre cambió a:", props.nombre);
    }, [props.nombre]); // Only when props.nombre changes
    
    return (
        <div>
            <h1>{props.nombre}</h1>
            <p>Edad: {props.edad}</p>
        </div>
    );
}
```

**Explanation:**
- `[props.nombre]` = "run this only when `props.nombre` changes"
- If `props.edad` changes, this `useEffect` does NOT run

### Case 4: Cleanup on UNMOUNT

This is **super important** for `setInterval`.

```jsx
import { useEffect } from 'react';

function ContadorConLimpieza() {
    useEffect(() => {
        console.log("Iniciando intervalo...");
        
        const intervalo = setInterval(() => {
            console.log("Tick");
        }, 1000);
        
        // Cleanup function
        return () => {
            console.log("Deteniendo intervalo...");
            clearInterval(intervalo);
        };
    }, []);
    
    return <h1>Contador activo</h1>;
}
```

**Why is cleanup important?**

Without cleanup:
```jsx
// ❌ PROBLEM
useEffect(() => {
    setInterval(() => {
        console.log("Esto nunca se detiene!");
    }, 1000);
}, []);
// If the component unmounts, the interval keeps running
// This causes memory leaks
```

With cleanup:
```jsx
// ✅ CORRECT
useEffect(() => {
    const intervalo = setInterval(() => {
        console.log("Esto se detendrá");
    }, 1000);
    
    return () => {
        clearInterval(intervalo);
    };
}, []);
// When the component unmounts, the interval stops
```

### Visual summary of useEffect

```jsx
useEffect(() => {
    // Code that runs
    
    return () => {
        // Cleanup code (optional)
    };
}, []);
   ↑
   Dependencies:
   - [] = only on mount
   - [variable] = when variable changes
   - no array = on every render
```

---

## 🎯 Part 7: Applying It All to the Simple Counter Project

### Project concept

You're going to build a **visual seconds counter** that shows each digit in its own box, like a digital clock.

```
┌─────┬─────┬─────┬─────┬─────┬─────┐
│  ⏱  │  0  │  0  │  0  │  1  │  2  │
└─────┴─────┴─────┴─────┴─────┴─────┘
```

### Conceptual structure

```jsx
// 1. Component that displays the counter
function SecondsCounter(props) {
    // Receives props.seconds (e.g., 123)
    // It must split 123 into [1, 2, 3]
    // Show each digit in a box
    
    return (
        <div>
            {/* Your design here */}
        </div>
    );
}

// 2. In your main file (index.js)
const root = ReactDOM.createRoot(document.getElementById('root'));

let segundos = 0;

setInterval(() => {
    segundos = segundos + 1;
    root.render(<SecondsCounter seconds={segundos} />);
}, 1000);
```

### Challenge 1: Split a number into digits

If you have `seconds = 1234`, you need to get: `[1, 2, 3, 4]`

**Method 1: Convert to string**
```javascript
let numero = 1234;
let digitos = numero.toString().split('');
// Result: ['1', '2', '3', '4']
```

**Method 2: Math**
```javascript
let numero = 1234;

let unidades = numero % 10;                           // 4
let decenas = Math.floor(numero / 10) % 10;          // 3
let centenas = Math.floor(numero / 100) % 10;        // 2
let miles = Math.floor(numero / 1000) % 10;          // 1
```

### Challenge 2: Always show 6 digits

The counter should always display 6 digits, padding with leading zeros:

```
seconds = 5     →  000005
seconds = 42    →  000042
seconds = 1234  →  001234
```

**Hint:** Use `padStart()`
```javascript
let numero = 5;
let conCeros = numero.toString().padStart(6, '0');
// Result: "000005"
```

### Challenge 3: Render multiple boxes

You need to create one box per digit:

```jsx
function SecondsCounter(props) {
    // Split into digits
    const digitosArray = props.seconds.toString().padStart(6, '0').split('');
    
    return (
        <div className="contador-container">
            <div className="digito">⏱️</div>
            
            {digitosArray.map((digito, index) => (
                <div key={index} className="digito">
                    {digito}
                </div>
            ))}
        </div>
    );
}
```

**What does `.map()` do?**
- It loops through each element of the array
- It creates a JSX element for each one
- `key={index}` is needed so React can identify each element

### CSS example (to make it look nice)

```css
.contador-container {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 50px;
}

.digito {
    background-color: #282c34;
    color: white;
    font-size: 48px;
    font-family: 'Courier New', monospace;
    width: 60px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

---

## 📚 Part 8: Additional Concepts

### Font Awesome (for the clock icon)

To add the clock icon ⏱️, you need Font Awesome:

**Option 1: CDN in your HTML**
```html
<head>
    <link rel="stylesheet" 
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
```

**Option 2: NPM**
```bash
npm install @fortawesome/fontawesome-free
```

```jsx
import '@fortawesome/fontawesome-free/css/all.min.css';

function SecondsCounter(props) {
    return (
        <div>
            <div className="digito">
                <i className="far fa-clock"></i>
            </div>
            {/* rest of the code */}
        </div>
    );
}
```

### Bonus: Stop, restart, and resume

For the project bonuses, you'll need:

**1. A variable to store the interval**
```javascript
let intervaloActual = null;

function iniciarContador() {
    intervaloActual = setInterval(() => {
        segundos++;
        root.render(<SecondsCounter seconds={segundos} />);
    }, 1000);
}

function pararContador() {
    clearInterval(intervaloActual);
}

function reiniciarContador() {
    pararContador();
    segundos = 0;
    root.render(<SecondsCounter seconds={segundos} />);
}
```

**2. Buttons in your component**
```jsx
function SecondsCounter(props) {
    return (
        <div>
            {/* Visual counter */}
            <div className="controles">
                <button onClick={props.onPausar}>Pausar</button>
                <button onClick={props.onReanudar}>Reanudar</button>
                <button onClick={props.onReiniciar}>Reiniciar</button>
            </div>
        </div>
    );
}
```

---

## 🎓 Concept Summary

| Concept | Description | Example |
|----------|-------------|---------|
| **Component** | Reusable UI block | `function Card() { return <div>...</div> }` |
| **Props** | Data you pass to the component | `<Card nombre="Ana" edad={25} />` |
| **setInterval** | Runs code repeatedly | `setInterval(() => {...}, 1000)` |
| **clearInterval** | Stops an interval | `clearInterval(miIntervalo)` |
| **Lifecycle** | Phases: Mount → Update → Unmount | See section 5 |
| **useEffect** | Hook to run code in the lifecycle | `useEffect(() => {...}, [])` |
| **JSX** | HTML inside JavaScript | `<h1>{variable}</h1>` |
| **map()** | Renders arrays in JSX | `array.map(item => <div>{item}</div>)` |

---

## ✅ Project Checklist

Before you start, make sure you understand:

- [ ] How to create a function component in React
- [ ] How to pass and receive props
- [ ] How setInterval and clearInterval work
- [ ] What the component lifecycle is
- [ ] How to split a number into individual digits
- [ ] How to use .map() to render arrays
- [ ] How to use ReactDOM.createRoot and root.render

---

## 🔗 Additional Resources

### Official docs
- [React Docs - Passing Props to a Component](https://react.dev/learn/passing-props-to-a-component)
- [MDN - setInterval](https://developer.mozilla.org/en-US/docs/Web/API/setInterval)
- [React Docs - useEffect](https://react.dev/reference/react/useEffect)

### Recommended tutorials
- [Interactive React tutorial](https://react.dev/learn/tutorial-tic-tac-toe)
- [JavaScript.info - setInterval and setTimeout](https://javascript.info/settimeout-setinterval)

---

## 💡 Final Tips

1. **Start simple**: First, just get the counter working with a single number
2. **Then improve**: Add the digit splitting
3. **Then style**: Make it look nice with CSS
4. **Finally, bonus**: Add the extra features

**Good luck with your project! 🚀**

---

## ❓ FAQ

### Why do I use root.render() instead of useState?

In this specific project, the instructions tell you **not to use local state**. This is to learn the basics first. Later you'll use `useState` and `useEffect` for this.

### How often does setInterval run?

The second parameter is in milliseconds:
- 1000 ms = 1 second
- 500 ms = 0.5 seconds
- 2000 ms = 2 seconds

### What happens if I don't use clearInterval?

If you don't stop an interval when the component unmounts, it will keep running in the background, causing performance issues (memory leak).

### Can I use let/const inside setInterval?

Yes, but be careful with scope:

```javascript
// ❌ Doesn't work
setInterval(() => {
    let contador = 0;  // Resets to 0 every time
    contador++;
}, 1000);

// ✅ Works
let contador = 0;  // Outside the setInterval
setInterval(() => {
    contador++;
}, 1000);
```

---

**Made with ❤️ for 4Geeks Academy - Cohort España FS PT 129**
