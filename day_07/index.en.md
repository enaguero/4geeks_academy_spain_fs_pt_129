[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 7: Intro to JavaScript

## So what is programming?

**Programming** is the art of giving a computer instructions to perform specific tasks. It's like writing a cooking recipe: step by step, you tell the machine what to do.

When you program, you create **algorithms**: logical sequences of steps that solve a problem. JavaScript is one of the languages we use to write those instructions, especially in the web browser.

**Why JavaScript?**
- It's the only language every browser understands
- It lets you build interactive web pages
- It's relatively easy to learn for beginners
- It has a huge developer community

---

## Variables

**Variables** are like boxes where we store information. Imagine you have a box labeled "name" where you keep a person's name. In JavaScript, variables work exactly that way.

### Assigning a value to variables

To create a variable and assign a value to it, we use the `=` sign:

```javascript
let nombre = "Ana";
let edad = 25;
let estaEstudiando = true;
```

The `=` sign does NOT mean "equals", it means **"assign"**. We're assigning the value `"Ana"` to the variable `nombre`.

### var vs let vs const

JavaScript has three ways to declare variables:

#### **var** (the old one)
```javascript
var apellido = "García";
```
- The old way to declare variables
- Has scoping issues that can cause bugs
- **Recommendation**: Don't use `var` in new code

#### **let** (for values that change)
```javascript
let contador = 0;
contador = 1;  // ✅ We can change the value
contador = 2;  // ✅ And change it again
```
- For variables whose values will change
- Block scope (safer)

#### **const** (for constant values)
```javascript
const PI = 3.14159;
PI = 3.14;  // ❌ Error: can't reassign
```
- For values that will NOT change
- **Recommendation**: Use `const` by default, only use `let` when you know the value will change

---

## Data Types

JavaScript has several basic data types:

### 1. **String (Text)**
```javascript
const saludo = "Hola Mundo";
const mensaje = 'También con comillas simples';
const nombre = `Mi nombre es ${nombre}`;  // Template literals
```

### 2. **Number**
```javascript
const edad = 30;
const precio = 19.99;
const temperatura = -5;
```

### 3. **Boolean**
```javascript
const esMayorDeEdad = true;
const estaLloviendo = false;
```

### 4. **Undefined**
```javascript
let resultado;  // undefined (declared but no value)
```

### 5. **Null**
```javascript
const dato = null;  // Intentionally empty
```

### 6. **Array (Lists)**
```javascript
const frutas = ["manzana", "banana", "naranja"];
const numeros = [1, 2, 3, 4, 5];
```

### 7. **Object**
```javascript
const persona = {
  nombre: "Carlos",
  edad: 28,
  ciudad: "Madrid"
};
```

---

## Operations

### Math Operations

```javascript
const suma = 5 + 3;           // 8
const resta = 10 - 4;         // 6
const multiplicacion = 6 * 7; // 42
const division = 20 / 4;      // 5
const modulo = 17 % 5;        // 2 (remainder of the division)
const potencia = 2 ** 3;      // 8 (2 to the power of 3)
```

### String Operations

```javascript
const nombre = "Juan";
const apellido = "Pérez";
const nombreCompleto = nombre + " " + apellido;  // "Juan Pérez"

// With template literals (more modern):
const saludo = `Hola, ${nombre} ${apellido}`;  // "Hola, Juan Pérez"
```

### Increment/Decrement Operations

```javascript
let contador = 0;
contador++;      // contador = 1 (increment by 1)
contador--;      // contador = 0 (decrement by 1)
contador += 5;   // contador = 5 (add 5)
contador -= 2;   // contador = 3 (subtract 2)
contador *= 2;   // contador = 6 (multiply by 2)
```

---

## Functions

**Functions** are reusable blocks of code that perform a specific task. They're like mini-programs inside your program.

### Declaring a Function

```javascript
// Traditional function declaration
function saludar() {
  console.log("¡Hola!");
}

// Call/execute the function
saludar();  // Prints: ¡Hola!
```

### Functions with Parameters and Scope

**Parameters** are values we pass to the function so it can work with them:

```javascript
function saludarPersona(nombre) {
  console.log(`Hola, ${nombre}!`);
}

saludarPersona("Ana");     // Prints: Hola, Ana!
saludarPersona("Carlos");  // Prints: Hola, Carlos!
```

**Function Scope**: Variables declared inside a function only exist inside that function.

```javascript
function ejemplo() {
  let variableLocal = "Solo existo aquí";
  console.log(variableLocal);  // ✅ Works
}

ejemplo();
console.log(variableLocal);  // ❌ Error: variableLocal is not defined
```

### Functions That Return Values

```javascript
function sumar(a, b) {
  return a + b;
}

const resultado = sumar(5, 3);  // resultado = 8
console.log(resultado);
```

### Anonymous Functions

These are functions without a name, usually assigned to a variable:

```javascript
const multiplicar = function(a, b) {
  return a * b;
};

console.log(multiplicar(4, 5));  // 20
```

### Arrow Functions (Modern)

```javascript
const dividir = (a, b) => {
  return a / b;
};

// Short version (when there's only a return):
const restar = (a, b) => a - b;

console.log(dividir(10, 2));  // 5
console.log(restar(10, 3));   // 7
```

---

## Logical Operations

### Comparison Operators

```javascript
5 == "5"    // true  (compares value only)
5 === "5"   // false (compares value AND type)
5 != "5"    // false
5 !== "5"   // true
5 > 3       // true  (greater than)
5 < 3       // false (less than)
5 >= 5      // true  (greater than or equal)
5 <= 4      // false (less than or equal)
```

**⚠️ Important**: Always use `===` and `!==` instead of `==` and `!=` to avoid bugs.

### AND and OR Operators

#### **AND (`&&`)**: All conditions must be true

```javascript
const edad = 20;
const tieneCarnet = true;

if (edad >= 18 && tieneCarnet) {
  console.log("Puede conducir");  // ✅ Runs
}
```

#### **OR (`||`)**: At least one condition must be true

```javascript
const esFinDeSemana = true;
const esVacaciones = false;

if (esFinDeSemana || esVacaciones) {
  console.log("Puede descansar");  // ✅ Runs
}
```

#### **NOT (`!`)**: Inverts the value

```javascript
const estaLloviendo = false;

if (!estaLloviendo) {
  console.log("Puedes salir");  // ✅ Runs
}
```

---

## Controlling the Flow of Your Code

### if / else if / else

```javascript
const nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Bien");  // ✅ This one runs
} else if (nota >= 50) {
  console.log("Suficiente");
} else {
  console.log("Insuficiente");
}
```

### Switch

Useful when you have many conditions based on the same value:

```javascript
const diaSemana = "lunes";

switch (diaSemana) {
  case "lunes":
    console.log("Inicio de semana");
    break;
  case "viernes":
    console.log("Casi fin de semana");
    break;
  case "sabado":
  case "domingo":
    console.log("Fin de semana");
    break;
  default:
    console.log("Día regular");
}
```

### Ternary Operator (Inline conditions)

A compact way to write `if/else`:

```javascript
// Syntax: condition ? valueIfTrue : valueIfFalse

const edad = 20;
const mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(mensaje);  // "Mayor de edad"

// Equivalent to:
let mensajeTradicional;
if (edad >= 18) {
  mensajeTradicional = "Mayor de edad";
} else {
  mensajeTradicional = "Menor de edad";
}
```

---

## Loops

Loops let us repeat code multiple times.

### While

Runs as long as the condition is true:

```javascript
let contador = 0;

while (contador < 5) {
  console.log(`Contador: ${contador}`);
  contador++;
}
// Prints: 0, 1, 2, 3, 4
```

### For

The most common loop, ideal when you know how many times you want to repeat:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Iteración: ${i}`);
}
// Prints: 0, 1, 2, 3, 4
```

**Breakdown**:
- `let i = 0`: Initialization
- `i < 5`: Condition (while true, keep going)
- `i++`: Increment (after each iteration)

### For...of (Iterating Arrays)

```javascript
const frutas = ["manzana", "banana", "naranja"];

for (const fruta of frutas) {
  console.log(fruta);
}
// Prints: manzana, banana, naranja
```

### For...in (Iterating Objects)

```javascript
const persona = {
  nombre: "Ana",
  edad: 25,
  ciudad: "Madrid"
};

for (const propiedad in persona) {
  console.log(`${propiedad}: ${persona[propiedad]}`);
}
// Prints:
// nombre: Ana
// edad: 25
// ciudad: Madrid
```

---

## Why Use Functions?

Imagine you need to calculate the area of several rectangles in your code:

### ❌ Without functions (repetitive code)

```javascript
// Rectangle 1
const base1 = 5;
const altura1 = 3;
const area1 = base1 * altura1;
console.log(area1);

// Rectangle 2
const base2 = 8;
const altura2 = 4;
const area2 = base2 * altura2;
console.log(area2);

// Rectangle 3
const base3 = 6;
const altura3 = 2;
const area3 = base3 * altura3;
console.log(area3);
```

### ✅ With functions (reusable code)

```javascript
function calcularArea(base, altura) {
  return base * altura;
}

console.log(calcularArea(5, 3));  // 15
console.log(calcularArea(8, 4));  // 32
console.log(calcularArea(6, 2));  // 12
```

**Advantages of using functions**:
1. **Reuse**: Write once, use many times
2. **Organization**: Cleaner, easier-to-understand code
3. **Maintenance**: If there's a bug, you fix it in one place
4. **Abstraction**: You hide complexity behind a descriptive name

---

## Nested Function Calls

You can call functions inside other functions:

```javascript
function saludar(nombre) {
  return `Hola, ${nombre}`;
}

function despedir(nombre) {
  return `Adiós, ${nombre}`;
}

function conversacionCompleta(nombre) {
  const saludo = saludar(nombre);
  const despedida = despedir(nombre);
  return `${saludo}. Fue un placer. ${despedida}`;
}

console.log(conversacionCompleta("María"));
// "Hola, María. Fue un placer. Adiós, María"
```

### A more complex example:

```javascript
function calcularIVA(precio) {
  return precio * 0.21;
}

function calcularDescuento(precio, porcentaje) {
  return precio * (porcentaje / 100);
}

function precioFinal(precioBase, descuentoPorcentaje) {
  const precioConDescuento = precioBase - calcularDescuento(precioBase, descuentoPorcentaje);
  const iva = calcularIVA(precioConDescuento);
  return precioConDescuento + iva;
}

console.log(precioFinal(100, 10));
// Price: 100€
// 10% discount: 90€
// 21% VAT: 108.9€
```

---

## Conditional Rendering

In web development, you often need to show or hide elements based on conditions:

```javascript
function mostrarMensajeBienvenida(usuario) {
  if (usuario) {
    return `Bienvenido, ${usuario.nombre}`;
  } else {
    return "Por favor, inicia sesión";
  }
}

const usuarioActual = { nombre: "Carlos", edad: 30 };
console.log(mostrarMensajeBienvenida(usuarioActual));
// "Bienvenido, Carlos"

console.log(mostrarMensajeBienvenida(null));
// "Por favor, inicia sesión"
```

### With the ternary operator:

```javascript
function obtenerEstadoUsuario(estaLogueado) {
  return estaLogueado ? "Usuario activo" : "Usuario invitado";
}

console.log(obtenerEstadoUsuario(true));   // "Usuario activo"
console.log(obtenerEstadoUsuario(false));  // "Usuario invitado"
```

---

## So... did you enjoy programming?

Programming is like learning a new language. At first it can feel complicated, but with practice it becomes more and more natural.

**Remember**:
- ✅ **Practice every day**: Even 15 minutes
- ✅ **Experiment**: Change values, break the code, learn from the errors
- ✅ **Read other people's code**: You'll learn different ways to solve problems
- ✅ **Build small projects**: The best way to learn is by making things

### The fundamental question: What to ask?

Programming is 70% **asking the right questions** and 30% writing code. Before you write code, ask yourself:

1. **What problem am I solving?**
2. **What information do I need?** (variables)
3. **What decisions do I have to make?** (conditionals)
4. **Do I need to repeat something?** (loops)
5. **Can I reuse this?** (functions)

---

## Hands-on Exercises

Now that you know the basic concepts, it's time to practice. In the `javascript-intro` folder you'll find incremental exercises that will help you master each concept.

**Exercise structure**:
- `step1-variables.html`: Variables and data types
- `step2-functions.html`: Basic functions
- `step3-conditionals.html`: Conditionals and logical operators
- `step4-loops.html`: Loops
- `step5-final-project.html`: Capstone project

**Let's go! 🚀**

---

## How HTML, CSS, and JavaScript Work Together

### The Web Development Trinity

When you browse the web, your browser works with **three fundamental technologies** that operate in perfect harmony:

- **HTML** (HyperText Markup Language): The **structure** - The bones
- **CSS** (Cascading Style Sheets): The **presentation** - The skin and clothes
- **JavaScript**: The **behavior** - The muscles and brain

### Analogy: Building a House

```
HTML  = Structure (walls, doors, windows)
CSS   = Decoration (paint, furniture, curtains)
JS    = Functionality (electricity, water, heating)
```

---

## Browser Processing Order

### What happens when you visit a web page?

When you type a URL in the browser (for example, `www.ejemplo.com`), the following sequence happens:

#### **1. HTTP Request**
```
Browser → Request → Server
           ↓
     "Give me index.html"
```

#### **2. The Server Responds**
```
Server → Response → Browser
           ↓
   index.html file
```

#### **3. HTML Processing** (Parsing)

The browser reads the HTML **from top to bottom**, line by line:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <!-- 1. First it reads the head -->
    <link rel="stylesheet" href="styles.css">
    <!-- 2. Finds the CSS and requests it from the server -->
</head>
<body>
    <!-- 3. Then it reads the body -->
    <h1>Hello World</h1>
    <button id="miBoton">Click here</button>
    
    <!-- 4. Finds the script at the end -->
    <script src="app.js"></script>
</body>
</html>
```

#### **4. Building the DOM (Document Object Model)**

The browser turns the HTML into a **tree of objects**:

```
Document
  └── html
      ├── head
      │   ├── title
      │   └── link (CSS)
      └── body
          ├── h1
          └── button
```

#### **5. Applying CSS (Rendering)**

The browser applies CSS styles to each DOM element:

```css
/* styles.css */
h1 {
    color: blue;
    font-size: 32px;
}

button {
    background-color: green;
    padding: 10px;
}
```

#### **6. JavaScript Execution**

Finally, JavaScript runs and can **modify** the DOM and CSS:

```javascript
// app.js
const boton = document.getElementById('miBoton');
boton.addEventListener('click', function() {
    alert('¡Hola!');
});
```

---

## JavaScript Loading Strategies

There are **three main ways** to load JavaScript in your HTML page:

### 1. Script at the End of Body (Traditional)

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Content</h1>
    <button id="btn">Click</button>
    
    <!-- ✅ Script at the end -->
    <script src="app.js"></script>
</body>
</html>
```

**Advantages**:
- Simple and always works
- HTML and CSS are ready when JS runs

**Disadvantages**:
- The browser can't start downloading the script until it reaches the end of the HTML

### 2. Script with `defer` (Recommended)

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <!-- ✅ Script with defer in the head -->
    <script src="app.js" defer></script>
</head>
<body>
    <h1>Content</h1>
    <button id="btn">Click</button>
</body>
</html>
```

**What does `defer` do?**
- The browser downloads the script **in parallel** while processing the HTML
- The script runs **after** the DOM is fully built
- Scripts with `defer` run in order

**Timeline with `defer`:**
```
HTML parsing:    |===============================|
                                                ↓ DOM Ready
Script download: |=====|
                       ↓ (waits)
Script execute:                                 |==|
```

### 3. Script with `async`

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <!-- Script with async -->
    <script src="analytics.js" async></script>
</head>
<body>
    <h1>Content</h1>
</body>
</html>
```

**What does `async` do?**
- The browser downloads the script **in parallel**
- The script runs **as soon as it's downloaded**
- No guaranteed execution order

**Timeline with `async`:**
```
HTML parsing:    |===============================|
Script download: |=====|
                       ↓ (runs immediately)
Script execute:        |==|
HTML parsing:              |==================|
```

**Use `async` for**: Standalone scripts like Google Analytics that don't need to touch the DOM

### 4. JavaScript Modules (Modern)

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <!-- ✅ JavaScript module -->
    <script type="module" src="app.js"></script>
</head>
<body>
    <h1>Content</h1>
    <button id="btn">Click</button>
</body>
</html>
```

**What does `type="module"` do?**
- Behaves like `defer` by default (waits for the DOM to be ready)
- Lets you use `import` and `export`
- Has its own scope (doesn't pollute the global scope)
- Runs in strict mode automatically

**Module example:**

**utils.js**
```javascript
export function saludar(nombre) {
    return `Hola, ${nombre}`;
}

export function sumar(a, b) {
    return a + b;
}
```

**app.js**
```javascript
import { saludar, sumar } from './utils.js';

const boton = document.getElementById('btn');
boton.addEventListener('click', function() {
    console.log(saludar('Usuario'));
    console.log(sumar(5, 3));
});
```

### Visual Comparison

```
┌─────────────────────────────────────────────────────────────┐
│ Method         │ Download  │ Execution │ Order │ DOM Ready │
├─────────────────────────────────────────────────────────────┤
│ End of body    │ Blocking  │ Immediate │  ✅   │    ✅     │
│ defer          │ Parallel  │ After     │  ✅   │    ✅     │
│ async          │ Parallel  │ Immediate │  ❌   │    ❌     │
│ type="module"  │ Parallel  │ After     │  ✅   │    ✅     │
└─────────────────────────────────────────────────────────────┘
```

**Recommendations**:
- **Beginners**: Script at the end of body
- **Modern production**: `defer` or `type="module"`
- **Standalone scripts**: `async`

---

## Connecting JavaScript with HTML

### Method 1: Inline Script

```html
<!DOCTYPE html>
<html>
<body>
    <h1 id="titulo">Hola</h1>
    <button onclick="cambiarTexto()">Cambiar</button>
    
    <script>
        function cambiarTexto() {
            document.getElementById('titulo').textContent = '¡Cambiado!';
        }
    </script>
</body>
</html>
```

### Method 2: External Script (Recommended)

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <script src="app.js" defer></script>
</head>
<body>
    <h1 id="titulo">Hola</h1>
    <button id="boton">Cambiar</button>
</body>
</html>
```

**app.js**
```javascript
function cambiarTexto() {
    document.getElementById('titulo').textContent = '¡Cambiado!';
}

const boton = document.getElementById('boton');
boton.addEventListener('click', cambiarTexto);
```

---

## Binding Functions to HTML Elements

### Option 1: `onclick` attribute (Inline) ❌

```html
<button onclick="saludar()">Saludar</button>

<script>
function saludar() {
    alert('¡Hola!');
}
</script>
```

**Advantages**: Simple and direct  
**Disadvantages**: Mixes HTML with JavaScript (not a good practice)

### Option 2: `addEventListener` (Recommended) ✅

```html
<button id="miBoton">Saludar</button>

<script>
// 1. Get a reference to the element
const boton = document.getElementById('miBoton');

// 2. Bind a function to the event
boton.addEventListener('click', function() {
    alert('¡Hola!');
});
</script>
```

**Advantages**: Separates HTML from JavaScript, more flexible  
**Disadvantages**: Slightly more code

### Option 3: `addEventListener` with an External Function

```html
<button id="miBoton">Saludar</button>

<script>
function saludar() {
    alert('¡Hola!');
}

const boton = document.getElementById('miBoton');
boton.addEventListener('click', saludar);  // ⚠️ No parentheses
</script>
```

**⚠️ Important**: When you pass a function to `addEventListener`, **do NOT** use parentheses:

```javascript
// ❌ Wrong: runs immediately
boton.addEventListener('click', saludar());

// ✅ Correct: runs when you click
boton.addEventListener('click', saludar);
```

---

## Manipulating the DOM with JavaScript

### Selecting HTML Elements

```javascript
// By ID (unique)
const titulo = document.getElementById('titulo');

// By class (there can be several)
const items = document.getElementsByClassName('item');

// By tag
const parrafos = document.getElementsByTagName('p');

// Query selector (CSS selector) - Modern ✅
const boton = document.querySelector('#miBoton');
const todosLosItems = document.querySelectorAll('.item');
```

### Modifying Content

```javascript
// Change text
elemento.textContent = 'Nuevo texto';

// Change inner HTML
elemento.innerHTML = '<strong>Texto en negrita</strong>';

// Change attributes
elemento.src = 'nueva-imagen.jpg';
elemento.href = 'https://ejemplo.com';
```

### Modifying CSS Styles

```javascript
// Change individual styles
elemento.style.color = 'red';
elemento.style.fontSize = '24px';
elemento.style.backgroundColor = 'yellow';

// Add/remove CSS classes (best practice) ✅
elemento.classList.add('activo');
elemento.classList.remove('inactivo');
elemento.classList.toggle('visible');
```

### Creating and Adding Elements

```javascript
// Create a new element
const nuevoParrafo = document.createElement('p');
nuevoParrafo.textContent = 'Soy un párrafo nuevo';

// Add it to the DOM
document.body.appendChild(nuevoParrafo);
```

---

## Common Events in JavaScript

### Mouse Events

```javascript
elemento.addEventListener('click', function() {
    console.log('Click!');
});

elemento.addEventListener('dblclick', function() {
    console.log('Double click!');
});

elemento.addEventListener('mouseenter', function() {
    console.log('Mouse entered');
});

elemento.addEventListener('mouseleave', function() {
    console.log('Mouse left');
});
```

### Keyboard Events

```javascript
input.addEventListener('keydown', function(event) {
    console.log('Key pressed:', event.key);
});

input.addEventListener('keyup', function(event) {
    console.log('Key released:', event.key);
});
```

### Form Events

```javascript
formulario.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default submission
    console.log('Form submitted');
});

input.addEventListener('input', function(event) {
    console.log('Current value:', event.target.value);
});

input.addEventListener('change', function(event) {
    console.log('Value changed:', event.target.value);
});
```

---

## Full Example: Todo List

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Tareas</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Mi Lista de Tareas</h1>
        
        <input type="text" id="tareaInput" placeholder="Nueva tarea...">
        <button id="agregarBtn">Agregar</button>
        
        <ul id="listaTareas"></ul>
    </div>
</body>
</html>
```

**styles.css**
```css
.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #f5f5f5;
    border-radius: 10px;
}

h1 {
    color: #333;
    text-align: center;
}

input {
    width: 70%;
    padding: 10px;
    font-size: 16px;
}

button {
    padding: 10px 20px;
    background: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #45a049;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    padding: 10px;
    margin: 10px 0;
    background: white;
    border-radius: 5px;
    display: flex;
    justify-content: space-between;
}

.completada {
    text-decoration: line-through;
    opacity: 0.6;
}
```

**app.js**
```javascript
// 1. Get references to DOM elements
const tareaInput = document.getElementById('tareaInput');
const agregarBtn = document.getElementById('agregarBtn');
const listaTareas = document.getElementById('listaTareas');

// 2. Function to add a task
function agregarTarea() {
    const textoTarea = tareaInput.value.trim();
    
    // Validate that it's not empty
    if (textoTarea === '') {
        alert('Por favor escribe una tarea');
        return;
    }
    
    // Create elements
    const li = document.createElement('li');
    const span = document.createElement('span');
    const btnEliminar = document.createElement('button');
    
    span.textContent = textoTarea;
    btnEliminar.textContent = 'Eliminar';
    btnEliminar.style.background = '#f44336';
    
    // Mark as completed on click
    span.addEventListener('click', function() {
        li.classList.toggle('completada');
    });
    
    // Remove task
    btnEliminar.addEventListener('click', function() {
        li.remove();
    });
    
    // Add to the DOM
    li.appendChild(span);
    li.appendChild(btnEliminar);
    listaTareas.appendChild(li);
    
    // Clear input
    tareaInput.value = '';
    tareaInput.focus();
}

// 3. Bind events
agregarBtn.addEventListener('click', agregarTarea);

// Allow adding with Enter
tareaInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        agregarTarea();
    }
});
```

---

## Execution Order: Visual Summary

```
┌─────────────────────────────────────────┐
│ 1. User types URL in the browser        │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 2. Browser requests HTML from server    │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 3. Server sends index.html              │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 4. Browser reads HTML line by line      │
│    - Builds the DOM                     │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 5. Finds <link> CSS                     │
│    - Requests styles.css (parallel)     │
│    - Applies styles to the DOM          │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 6. Finds <script>                       │
│    • No attributes: blocks and runs     │
│    • defer: downloads in parallel,      │
│      runs after the DOM                 │
│    • async: downloads and runs ASAP     │
│    • type="module": like defer + ES6    │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 7. JavaScript manipulates DOM and CSS   │
│    - Adds interactivity                 │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 8. Page fully loaded                    │
│    - User can interact                  │
└─────────────────────────────────────────┘
```

---

## Best Practices

### 1. **Use `defer` or `type="module"` in the head**

```html
<!-- ✅ MODERN AND RECOMMENDED -->
<!DOCTYPE html>
<html>
<head>
    <script src="app.js" defer></script>
    <!-- or -->
    <script type="module" src="app.js"></script>
</head>
<body>
    <button id="btn">Click</button>
</body>
</html>
```

```html
<!-- ✅ ALSO WORKS (traditional) -->
<body>
    <button id="btn">Click</button>
    <script src="app.js"></script>
</body>
```

### 2. **Use `addEventListener` instead of `onclick`**

```html
<!-- ❌ Avoid this -->
<button onclick="miFunction()">Click</button>

<!-- ✅ Better -->
<button id="miBtn">Click</button>
<script defer>
    document.getElementById('miBtn').addEventListener('click', miFunction);
</script>
```

### 3. **Separate HTML, CSS, and JavaScript**

```
📁 mi-proyecto/
  ├── index.html      (Structure)
  ├── styles.css      (Presentation)
  └── app.js          (Behavior)
```

### 4. **Use Semantic IDs and Classes**

```html
<!-- ✅ GOOD -->
<button id="btnAgregar" class="btn-primary">Agregar</button>

<!-- ❌ BAD -->
<button id="btn1" class="azul">Agregar</button>
```

### 5. **Always Check That the Element Exists**

```javascript
const boton = document.getElementById('miBoton');

if (boton) {
    boton.addEventListener('click', function() {
        console.log('Click!');
    });
} else {
    console.error('Element not found');
}
```

---

## Conclusion

Now you understand how **HTML**, **CSS**, and **JavaScript** work together:

1. **HTML** builds the structure (what's on the page)
2. **CSS** defines the look (how it looks)
3. **JavaScript** adds behavior (what it does)

The browser processes them in order, builds the DOM, applies styles, and runs scripts. With modern techniques like `defer` or `type="module"`, you can place your scripts in the `<head>` and the browser will run them at the right moment.

**Key points**:
- ✅ Use `defer` for regular scripts
- ✅ Use `type="module"` for modern code with import/export
- ✅ Use `async` only for standalone scripts
- ✅ Use `addEventListener` instead of inline attributes
- ✅ Only manipulate the DOM after it's ready
