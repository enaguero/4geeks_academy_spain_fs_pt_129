# Día 12: El DOM y Programación Event-Driven

## Parte 1: ¿Qué es el Front-End Development?

### De Páginas Estáticas a Aplicaciones Dinámicas

Imagina que construyes una casa. El **front-end development** es como diseñar y construir todo lo que los visitantes pueden **ver y tocar**: las puertas, ventanas, interruptores, colores de las paredes, y cómo reacciona todo cuando interactúas con la casa.

**Front-end development = Crear HTML dinámicamente usando JavaScript**

### Antes vs Ahora

| Antes (Páginas Estáticas) | Ahora (Aplicaciones Dinámicas) |
|---------------------------|-------------------------------|
| HTML escrito a mano | HTML generado por código |
| Contenido fijo | Contenido que cambia en tiempo real |
| Sin interacción | Totalmente interactivo |
| Aburrido 😴 | Emocionante 🎮 |

### Ejemplo: Del HTML Estático al Dinámico

**❌ Forma antigua (estática)**:
```html
<!-- Tienes que escribir esto manualmente para cada producto -->
<div class="product">
    <h3>Laptop</h3>
    <p>$999</p>
</div>
<div class="product">
    <h3>Mouse</h3>
    <p>$25</p>
</div>
<!-- ...y así para 100 productos más 😱 -->
```

**✅ Forma moderna (dinámica)**:
```javascript
// JavaScript genera todo el HTML automáticamente
const products = [
    { name: "Laptop", price: 999 },
    { name: "Mouse", price: 25 },
    { name: "Teclado", price: 75 }
    // ...¡puedes tener miles!
];

const container = document.getElementById('products');

products.forEach(product => {
    container.innerHTML += `
        <div class="product">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
        </div>
    `;
});
```

### Los Dos Conceptos Clave del Front-End

#### 1. **Rendering** (Renderizado)

El proceso de crear el HTML + CSS necesario para mostrar cualquier información en el sitio web.

```javascript
// Ejemplo: Renderizar un empleado
function renderEmployee(employee) {
    return `
        <div class="employee-card">
            <img src="${employee.photo}">
            <h3>${employee.name}</h3>
            <p>${employee.position}</p>
        </div>
    `;
}
```

#### 2. **Runtime** (Tiempo de Ejecución)

Es la línea de tiempo de tu sitio web desde que termina de cargar hasta que el usuario sale.

```
Usuario entra → (RUNTIME COMIENZA) → Hace clicks → Escribe → Navega → (RUNTIME TERMINA) → Usuario sale
```

Durante el runtime, JavaScript está escuchando y reaccionando a todo lo que sucede.

---

## Parte 2: El DOM - Tu Puente hacia el HTML

### ¿Qué es el DOM?

**DOM = Document Object Model** (Modelo de Objetos del Documento)

> El DOM es espectacular porque permite que JavaScript y HTML hablen entre sí.

Sin el DOM, sería imposible:
- Cambiar el contenido de la página
- Responder a clicks
- Crear aplicaciones interactivas
- Mostrar datos dinámicamente

### El DOM como un Árbol Familiar

Cuando escribes HTML:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Mi Página</title>
    </head>
    <body>
        <h1>Bienvenido</h1>
        <div class="container">
            <p>Párrafo 1</p>
            <p>Párrafo 2</p>
        </div>
    </body>
</html>
```

El navegador lo convierte en este árbol:
```
document (raíz)
  └── html
      ├── head
      │   └── title
      │       └── "Mi Página"
      └── body
          ├── h1
          │   └── "Bienvenido"
          └── div.container
              ├── p
              │   └── "Párrafo 1"
              └── p
                  └── "Párrafo 2"
```

### Relaciones Familiares en el DOM

```html
<div id="padre">
    <h1 id="hijo1">Título</h1>
    <p id="hijo2">Párrafo</p>
</div>
```

- **`#padre`** es el **parent** (padre) de `h1` y `p`
- **`#hijo1`** y **`#hijo2`** son **children** (hijos) de `div`
- **`#hijo1`** y **`#hijo2`** son **siblings** (hermanos) entre sí

---

## Parte 3: Seleccionar Elementos del DOM

Para manipular elementos HTML con JavaScript, primero necesitas "encontrarlos" en el DOM.

### Método 1: `getElementById()` ✅

```html
<h1 id="titulo">Hola Mundo</h1>
<button id="btnSaludar">Saludar</button>
```

```javascript
const titulo = document.getElementById('titulo');
const boton = document.getElementById('btnSaludar');

console.log(titulo.textContent);  // "Hola Mundo"
```

**Cuándo usar**: Cuando el elemento tiene un ID único.

### Método 2: `querySelector()` ✅✅ (Recomendado)

```javascript
// Por ID
const titulo = document.querySelector('#titulo');

// Por clase
const card = document.querySelector('.card');

// Por etiqueta
const primerParrafo = document.querySelector('p');

// Selectores complejos
const primerItemDeLista = document.querySelector('.menu li:first-child');
const inputEmail = document.querySelector('input[type="email"]');
```

**Cuándo usar**: Para todo. Es el más flexible y poderoso.

### Método 3: `querySelectorAll()` ✅✅ (Para Múltiples Elementos)

```html
<ul>
    <li class="item">Item 1</li>
    <li class="item">Item 2</li>
    <li class="item">Item 3</li>
</ul>
```

```javascript
const items = document.querySelectorAll('.item');

console.log(items.length);  // 3

// Recorrer con forEach
items.forEach((item, index) => {
    console.log(`Item ${index + 1}: ${item.textContent}`);
});
```

---

## Parte 4: Manipular Contenido con innerHTML

Una vez que tienes un elemento, puedes cambiar su contenido dinámicamente.

### Ejemplo Básico

```html
<div id="mensaje"></div>
<button id="btnMostrar">Mostrar Mensaje</button>
```

```javascript
const mensaje = document.getElementById('mensaje');
const boton = document.getElementById('btnMostrar');

boton.addEventListener('click', function() {
    mensaje.innerHTML = `
        <h2>¡Hola!</h2>
        <p>Este contenido fue creado por JavaScript</p>
    `;
});
```

### Ejemplo: Lista Dinámica de Productos

```html
<div id="productos"></div>
```

```javascript
const productos = [
    { nombre: "Laptop", precio: 999, stock: 5 },
    { nombre: "Mouse", precio: 25, stock: 50 },
    { nombre: "Teclado", precio: 75, stock: 30 }
];

const contenedor = document.getElementById('productos');

function renderizarProductos() {
    let html = '<h2>Nuestros Productos</h2>';
    html += '<div class="productos-grid">';
    
    productos.forEach(producto => {
        html += `
            <div class="producto-card">
                <h3>${producto.nombre}</h3>
                <p class="precio">$${producto.precio}</p>
                <p class="stock">Stock: ${producto.stock} unidades</p>
                <button onclick="comprar('${producto.nombre}')">Comprar</button>
            </div>
        `;
    });
    
    html += '</div>';
    contenedor.innerHTML = html;
}

function comprar(nombreProducto) {
    alert(`Has agregado ${nombreProducto} al carrito`);
}

// Renderizar al cargar la página
renderizarProductos();
```

---

## Parte 5: Programación Event-Driven (Dirigida por Eventos)

### El Cambio de Paradigma

Hasta ahora, tu código se ejecutaba **de arriba hacia abajo**, línea por línea:

```javascript
// Código tradicional (secuencial)
console.log("Línea 1");
console.log("Línea 2");
console.log("Línea 3");
// Siempre se ejecuta en orden
```

Con **Event-Driven Programming**, tu código se ejecuta **cuando algo sucede**:

```javascript
// Código event-driven (asíncrono)
button.addEventListener('click', function() {
    console.log("¡Me ejecuto SOLO cuando haces click!");
});

console.log("Yo me ejecuto inmediatamente");
// El código del click solo se ejecuta cuando el usuario hace click
```

### ¿Qué es un Evento?

Un **evento** es algo que sucede en tu aplicación:

| Evento | Cuándo Ocurre |
|--------|---------------|
| `load` | La página termina de cargar |
| `click` | Usuario hace click en algo |
| `mouseover` | Mouse pasa sobre un elemento |
| `keydown` | Usuario presiona una tecla |
| `change` | Valor de un input cambia |
| `submit` | Formulario se envía |

### Los 3 Componentes del Event-Driven Programming

1. **Evento**: Algo que sucede (click, tecla, etc.)
2. **Listener** (Escuchador): Código que está "vigilando" si ocurre el evento
3. **Handler** (Manejador): Función que se ejecuta cuando ocurre el evento

```javascript
const boton = document.querySelector('#miBoton');

// Listener: addEventListener está "escuchando"
boton.addEventListener('click', function() {
    // Handler: Esta función se ejecuta cuando ocurre el click
    console.log('¡Click detectado!');
});
```

---

## Parte 6: Eventos Comunes y Cómo Usarlos

### Evento: `click`

```html
<button id="contador">Clicks: 0</button>
```

```javascript
const boton = document.getElementById('contador');
let clicks = 0;

boton.addEventListener('click', function() {
    clicks++;
    boton.textContent = `Clicks: ${clicks}`;
});
```

### Evento: `mouseover` y `mouseout`

```html
<div id="caja" style="width: 200px; height: 200px; background: lightblue;">
    Pasa el mouse aquí
</div>
```

```javascript
const caja = document.getElementById('caja');

caja.addEventListener('mouseover', function() {
    caja.style.background = 'lightcoral';
    caja.textContent = '¡Hola!';
});

caja.addEventListener('mouseout', function() {
    caja.style.background = 'lightblue';
    caja.textContent = 'Pasa el mouse aquí';
});
```

### Evento: `input` (Tiempo Real)

```html
<input type="text" id="busqueda" placeholder="Buscar...">
<p id="resultado"></p>
```

```javascript
const input = document.getElementById('busqueda');
const resultado = document.getElementById('resultado');

input.addEventListener('input', function() {
    const texto = input.value;
    resultado.textContent = `Buscando: "${texto}" (${texto.length} caracteres)`;
});
```

### Evento: `change` (Cuando Cambia y Sale del Campo)

```html
<select id="pais">
    <option value="">Selecciona...</option>
    <option value="es">España</option>
    <option value="mx">México</option>
    <option value="ar">Argentina</option>
</select>
<p id="seleccion"></p>
```

```javascript
const select = document.getElementById('pais');
const seleccion = document.getElementById('seleccion');

select.addEventListener('change', function() {
    const paisSeleccionado = select.value;
    const nombrePais = select.options[select.selectedIndex].text;
    
    seleccion.textContent = `Has seleccionado: ${nombrePais} (${paisSeleccionado})`;
});
```

---

## Proyecto Práctico: Random Card Generator 🃏

Vamos a crear un generador aleatorio de cartas de póker que aplica todo lo aprendido.

### Paso 1: Estructura HTML

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Card Generator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🃏 Generador de Cartas Aleatorias</h1>
        
        <div id="card" class="card">
            <div class="top-suit">♠</div>
            <div class="number">A</div>
            <div class="bottom-suit">♠</div>
        </div>
        
        <button id="btnGenerate">Generar Nueva Carta</button>
        <button id="btnAuto">Auto-Generar (cada 3s)</button>
        <button id="btnStop">Detener</button>
    </div>
    
    <script src="app.js"></script>
</body>
</html>
```

### Paso 2: Estilos CSS

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.container {
    text-align: center;
}

h1 {
    color: white;
    margin-bottom: 30px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.card {
    width: 200px;
    height: 300px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    margin: 30px auto;
    padding: 20px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: scale(1.05);
}

.top-suit {
    font-size: 50px;
    text-align: left;
}

.number {
    font-size: 80px;
    font-weight: bold;
    text-align: center;
}

.bottom-suit {
    font-size: 50px;
    text-align: right;
    transform: rotate(180deg);
}

.card.red {
    color: #e74c3c;
}

.card.black {
    color: #2c3e50;
}

button {
    background: white;
    border: none;
    padding: 15px 30px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 25px;
    cursor: pointer;
    margin: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
}

button:active {
    transform: translateY(0);
}

#btnGenerate {
    background: #3498db;
    color: white;
}

#btnAuto {
    background: #2ecc71;
    color: white;
}

#btnStop {
    background: #e74c3c;
    color: white;
}
```

### Paso 3: JavaScript (app.js)

```javascript
// Obtener elementos del DOM
const card = document.getElementById('card');
const btnGenerate = document.getElementById('btnGenerate');
const btnAuto = document.getElementById('btnAuto');
const btnStop = document.getElementById('btnStop');

// Arrays de palos y valores
const suits = [
    { symbol: '♠', name: 'spade', color: 'black' },
    { symbol: '♣', name: 'club', color: 'black' },
    { symbol: '♥', name: 'heart', color: 'red' },
    { symbol: '♦', name: 'diamond', color: 'red' }
];

const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

// Variable para controlar el auto-generador
let autoGenerateInterval = null;

// Función para generar una carta aleatoria
function generateRandomCard() {
    // Seleccionar palo aleatorio
    const randomSuit = suits[Math.floor(Math.random() * suits.length)];
    
    // Seleccionar valor aleatorio
    const randomValue = values[Math.floor(Math.random() * values.length)];
    
    // Actualizar el DOM con la nueva carta
    renderCard(randomSuit, randomValue);
}

// Función para renderizar la carta en el DOM
function renderCard(suit, value) {
    // Actualizar contenido
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');
    
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;
    
    // Actualizar color
    card.className = 'card'; // Resetear clases
    card.classList.add(suit.color); // Añadir clase de color
    
    // Animación de entrada
    card.style.transform = 'scale(0.9)';
    setTimeout(() => {
        card.style.transform = 'scale(1)';
    }, 100);
}

// Event Listeners
btnGenerate.addEventListener('click', function() {
    generateRandomCard();
});

btnAuto.addEventListener('click', function() {
    // Si ya está corriendo, no hacer nada
    if (autoGenerateInterval) {
        alert('Ya está en modo automático');
        return;
    }
    
    // Generar cada 3 segundos
    autoGenerateInterval = setInterval(function() {
        generateRandomCard();
    }, 3000);
    
    // Feedback visual
    btnAuto.textContent = '✓ Auto-Generando...';
    btnAuto.style.opacity = '0.5';
});

btnStop.addEventListener('click', function() {
    // Detener el intervalo
    if (autoGenerateInterval) {
        clearInterval(autoGenerateInterval);
        autoGenerateInterval = null;
        
        // Restaurar botón
        btnAuto.textContent = 'Auto-Generar (cada 3s)';
        btnAuto.style.opacity = '1';
    }
});

// Generar una carta inicial al cargar la página
window.addEventListener('load', function() {
    generateRandomCard();
});
```

---

## Explicación Detallada del Código

### 1. Generación Aleatoria

```javascript
// Math.random() genera un número entre 0 y 1
// Math.random() * array.length genera un número entre 0 y la longitud del array
// Math.floor() redondea hacia abajo para obtener un índice válido

const randomIndex = Math.floor(Math.random() * suits.length);
const randomSuit = suits[randomIndex];
```

### 2. Renderizado Dinámico

```javascript
function renderCard(suit, value) {
    // Obtenemos los elementos internos de la carta
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');
    
    // Actualizamos el contenido
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;
    
    // Cambiamos la clase para aplicar el color correcto
    card.className = 'card';  // Resetear
    card.classList.add(suit.color);  // Añadir rojo o negro
}
```

### 3. Event-Driven Programming

```javascript
// Event Listener para el botón de generar
btnGenerate.addEventListener('click', function() {
    generateRandomCard();
});

// Event Listener para auto-generar con setInterval
btnAuto.addEventListener('click', function() {
    autoGenerateInterval = setInterval(function() {
        generateRandomCard();
    }, 3000);  // Cada 3000 milisegundos (3 segundos)
});

// Event Listener para detener con clearInterval
btnStop.addEventListener('click', function() {
    clearInterval(autoGenerateInterval);
    autoGenerateInterval = null;
});
```

---

## Ejercicios de Extensión

### Ejercicio 1: Añadir Historial de Cartas

Modifica el proyecto para mostrar las últimas 5 cartas generadas debajo de la carta principal.

<details>
<summary>Pista</summary>

```javascript
let historial = [];

function generateRandomCard() {
    // ... código existente ...
    
    // Añadir al historial
    historial.push({ suit: randomSuit, value: randomValue });
    
    // Mantener solo las últimas 5
    if (historial.length > 5) {
        historial.shift();
    }
    
    renderHistorial();
}

function renderHistorial() {
    const historialDiv = document.getElementById('historial');
    historialDiv.innerHTML = '<h3>Últimas cartas:</h3>';
    
    historial.forEach(carta => {
        historialDiv.innerHTML += `<span class="${carta.suit.color}">${carta.value}${carta.suit.symbol}</span> `;
    });
}
```
</details>

### Ejercicio 2: Contador de Cartas por Palo

Añade un contador que muestre cuántas veces ha salido cada palo.

### Ejercicio 3: Generar Manos de Póker

Modifica el generador para mostrar 5 cartas a la vez (una mano de póker).

---

## Resumen: Conceptos Clave

### Front-End Development
✅ Crear HTML dinámicamente con JavaScript  
✅ Renderizar = Generar HTML + CSS para mostrar datos  
✅ Runtime = Ciclo de vida de la aplicación

### DOM (Document Object Model)
✅ Representación en árbol del HTML  
✅ Permite a JavaScript manipular elementos  
✅ Relaciones: parent, children, siblings

### Selección de Elementos
✅ `getElementById()` - Por ID único  
✅ `querySelector()` - Con selectores CSS (recomendado)  
✅ `querySelectorAll()` - Múltiples elementos

### Manipulación del DOM
✅ `innerHTML` - Cambiar contenido HTML  
✅ Template strings con \`${variable}\`  
✅ Actualización dinámica en tiempo real

### Event-Driven Programming
✅ Código que se ejecuta cuando algo sucede  
✅ Eventos: click, mouseover, input, change, load  
✅ addEventListener(evento, función)  
✅ Asíncrono vs Secuencial

---

## Recursos Adicionales

- **MDN - DOM**: https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model
- **MDN - Eventos**: https://developer.mozilla.org/es/docs/Web/Events
- **4Geeks - Event Driven Programming**: https://4geeks.com/lesson/event-driven-programming
- **JavaScript.info - Introduction to browser events**: https://javascript.info/introduction-browser-events

---

## Cheat Sheet: DOM y Eventos

```javascript
// SELECCIONAR ELEMENTOS
document.getElementById('id')
document.querySelector('.clase')
document.querySelectorAll('p')

// MANIPULAR CONTENIDO
elemento.innerHTML = `<p>${variable}</p>`
elemento.textContent = 'texto'

// EVENTOS
elemento.addEventListener('click', function() {
    // Tu código aquí
})

// GENERAR ALEATORIOS
Math.random()  // 0 a 1
Math.floor(Math.random() * max)  // 0 a max-1

// TIMERS
setInterval(funcion, milisegundos)  // Repetir
clearInterval(id)  // Detener
setTimeout(funcion, milisegundos)   // Una vez

// CLASES CSS
elemento.classList.add('clase')
elemento.classList.remove('clase')
elemento.classList.toggle('clase')

// ESTILOS
elemento.style.color = 'red'
elemento.style.background = 'blue'
```

---

¡Felicidades! 🎉 Ahora dominas los conceptos fundamentales del front-end development y estás listo para crear aplicaciones web dinámicas e interactivas.

**Próximo paso**: Practica creando tus propios proyectos pequeños combinando todo lo aprendido.