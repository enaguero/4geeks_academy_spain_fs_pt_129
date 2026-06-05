🇪🇸 **Español** | [🇬🇧 English](index.en.md)

# Día 13: Random Card Generator - Proyecto Paso a Paso 🃏

## Introducción

Hoy vamos a construir un **generador de cartas aleatorias** desde cero, aplicando todo lo que hemos aprendido sobre el DOM, eventos y JavaScript. Lo haremos de forma **incremental**, construyendo el proyecto paso a paso.

### ¿Qué vamos a construir?

Una aplicación web que:
- Muestra una carta de póker aleatoria
- Permite generar nuevas cartas haciendo click
- Tiene modo automático que genera cartas cada 3 segundos
- Es visualmente atractiva con animaciones

---

## Paso 1: Estructura HTML Básica

Empecemos con lo más simple: crear la estructura HTML.

### 📝 Crea el archivo `index.html`

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
    </div>
    
    <script src="app.js"></script>
</body>
</html>
```

### 🔍 Análisis del HTML

| Elemento | Propósito |
|----------|-----------|
| `.container` | Contenedor principal para centrar todo |
| `#card` | La carta que vamos a modificar dinámicamente |
| `.top-suit` | Palo en la esquina superior |
| `.number` | Valor de la carta (A, 2, 3... K) |
| `.bottom-suit` | Palo en la esquina inferior (invertido) |
| `#btnGenerate` | Botón para generar cartas |

**💡 Nota importante**: Los palos (♠ ♥ ♦ ♣) son caracteres Unicode que puedes copiar directamente.

---

## Paso 2: Estilos CSS Básicos

Ahora vamos a darle estilo a nuestra carta.

### 📝 Crea el archivo `style.css`

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
```

### ✅ Checkpoint 1

**Abre `index.html` en tu navegador**. Deberías ver:
- Un fondo degradado morado
- El título centrado
- Una carta (todavía sin estilo)
- Un botón

---

## Paso 3: Estilizar la Carta

Vamos a hacer que la carta parezca una carta real de póker.

### 📝 Añade esto a `style.css`

```css
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
```

### 🔍 Conceptos clave de CSS

```css
display: flex;
flex-direction: column;      /* Organiza los elementos verticalmente */
justify-content: space-between; /* Separa los elementos */
```

Esto crea el layout de la carta: palo arriba, número centro, palo abajo.

```css
transform: rotate(180deg);  /* Voltea el palo inferior */
```

### ✅ Checkpoint 2

Refresca el navegador. Ahora deberías ver una carta bonita con:
- Fondo blanco y bordes redondeados
- Sombra que la hace "flotar"
- Palo superior, número central, palo inferior invertido

---

## Paso 4: Estilizar el Botón

Hagamos que el botón se vea profesional.

### 📝 Añade a `style.css`

```css
button {
    background: #3498db;
    color: white;
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
```

### 🔍 Efectos interactivos

- **`:hover`** - Cuando pasas el mouse, el botón sube un poco
- **`:active`** - Cuando haces click, vuelve a su posición
- **`transition`** - Hace que los cambios sean suaves

### ✅ Checkpoint 3

Pasa el mouse sobre el botón y haz click. Deberías ver las animaciones.

---

## Paso 5: JavaScript - Estructura Básica

Ahora viene la parte emocionante: ¡dar vida a la carta!

### 📝 Crea el archivo `app.js`

```javascript
// Paso 1: Obtener elementos del DOM
const card = document.getElementById('card');
const btnGenerate = document.getElementById('btnGenerate');

// Paso 2: Definir los datos de las cartas
const suits = [
    { symbol: '♠', name: 'spade', color: 'black' },
    { symbol: '♣', name: 'club', color: 'black' },
    { symbol: '♥', name: 'heart', color: 'red' },
    { symbol: '♦', name: 'diamond', color: 'red' }
];

const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

// Paso 3: Mensaje de prueba
console.log('JavaScript cargado correctamente');
console.log('Palos disponibles:', suits.length);
console.log('Valores disponibles:', values.length);
```

### 🔍 Explicación paso a paso

#### 1. Obtener elementos del DOM

```javascript
const card = document.getElementById('card');
```

Esto guarda una referencia al elemento HTML con `id="card"`. Ahora podemos manipularlo desde JavaScript.

#### 2. Arrays de datos

```javascript
const suits = [
    { symbol: '♠', name: 'spade', color: 'black' },
    ...
];
```

Cada palo es un **objeto** con 3 propiedades:
- `symbol`: El carácter visual (♠)
- `name`: Nombre en inglés
- `color`: 'black' o 'red' (para aplicar CSS)

### ✅ Checkpoint 4

Abre la **Consola del Navegador** (F12 → Console). Deberías ver:
```
JavaScript cargado correctamente
Palos disponibles: 4
Valores disponibles: 13
```

---

## Paso 6: Generar Números Aleatorios

Antes de generar cartas, necesitamos entender cómo funcionan los números aleatorios.

### 📝 Añade a `app.js`

```javascript
// Función auxiliar: generar número aleatorio
function getRandomNumber(max) {
    return Math.floor(Math.random() * max);
}

// Prueba en la consola
console.log('Número aleatorio entre 0-3:', getRandomNumber(4));
console.log('Número aleatorio entre 0-12:', getRandomNumber(13));
```

### 🔍 ¿Cómo funciona?

```javascript
Math.random()              // Genera número entre 0 y 1
                          // Ejemplos: 0.234, 0.891, 0.012

Math.random() * 4         // Multiplica por 4
                          // Ejemplos: 0.936, 3.564, 0.048

Math.floor(Math.random() * 4)  // Redondea hacia abajo
                                // Ejemplos: 0, 3, 0
```

**Resultado**: Números enteros entre 0 y 3 (perfecto para índices de arrays)

### 📊 Tabla de ejemplos

| `Math.random()` | `* 4` | `Math.floor()` | Resultado |
|-----------------|-------|----------------|-----------|
| 0.123 | 0.492 | 0.492 | **0** |
| 0.456 | 1.824 | 1.824 | **1** |
| 0.789 | 3.156 | 3.156 | **3** |
| 0.999 | 3.996 | 3.996 | **3** |

---

## Paso 7: Generar una Carta Aleatoria

Ahora sí, vamos a generar cartas aleatorias.

### 📝 Añade a `app.js`

```javascript
// Función para generar una carta aleatoria
function generateRandomCard() {
    // 1. Seleccionar palo aleatorio
    const randomSuitIndex = getRandomNumber(suits.length);
    const randomSuit = suits[randomSuitIndex];
    
    // 2. Seleccionar valor aleatorio
    const randomValueIndex = getRandomNumber(values.length);
    const randomValue = values[randomValueIndex];
    
    // 3. Mostrar en consola (para verificar)
    console.log('Carta generada:', randomValue + randomSuit.symbol);
    
    // 4. Actualizar la carta en pantalla
    renderCard(randomSuit, randomValue);
}

// Probar la función
generateRandomCard();
```

### 🔍 Desglose del código

```javascript
const randomSuitIndex = getRandomNumber(suits.length);
```
- `suits.length` = 4
- `getRandomNumber(4)` devuelve 0, 1, 2 o 3
- Es un índice válido para el array `suits`

```javascript
const randomSuit = suits[randomSuitIndex];
```
- Obtiene el objeto completo: `{ symbol: '♠', name: 'spade', color: 'black' }`

### ✅ Checkpoint 5

Guarda el archivo y refresca el navegador. En la consola deberías ver algo como:
```
Carta generada: 7♥
```

(El valor cambia cada vez que refrescas porque es aleatorio)

---

## Paso 8: Renderizar la Carta

Ahora vamos a actualizar el HTML para mostrar la carta generada.

### 📝 Añade a `app.js`

```javascript
// Función para renderizar la carta en el DOM
function renderCard(suit, value) {
    // 1. Obtener los elementos internos de la carta
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');
    
    // 2. Actualizar el contenido
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;
    
    // 3. Actualizar el color (rojo o negro)
    card.className = 'card';  // Resetear clases
    card.classList.add(suit.color);  // Añadir 'red' o 'black'
    
    console.log('Carta renderizada:', value + suit.symbol, '(' + suit.color + ')');
}
```

### 🔍 Métodos del DOM usados

| Método | Qué hace |
|--------|----------|
| `querySelector('.top-suit')` | Busca el elemento con clase `.top-suit` dentro de `card` |
| `textContent = '♥'` | Cambia el texto del elemento |
| `className = 'card'` | Resetea todas las clases a solo 'card' |
| `classList.add('red')` | Añade la clase 'red' (sin quitar 'card') |

### 📊 Ejemplo visual

**Antes** (HTML estático):
```html
<div id="card" class="card">
    <div class="top-suit">♠</div>
    <div class="number">A</div>
    <div class="bottom-suit">♠</div>
</div>
```

**Después** (JavaScript dinámico con 7♥):
```html
<div id="card" class="card red">
    <div class="top-suit">♥</div>
    <div class="number">7</div>
    <div class="bottom-suit">♥</div>
</div>
```

### ✅ Checkpoint 6

Refresca el navegador varias veces. Cada vez deberías ver una carta diferente generada automáticamente.

---

## Paso 9: Conectar el Botón

Hagamos que el botón funcione con un evento click.

### 📝 Añade a `app.js`

```javascript
// Event Listener para el botón
btnGenerate.addEventListener('click', function() {
    console.log('¡Botón clickeado!');
    generateRandomCard();
});

// Generar una carta inicial al cargar
generateRandomCard();
```

### 🔍 Event-Driven Programming

```javascript
btnGenerate.addEventListener('click', function() {
    // Este código SOLO se ejecuta cuando haces click
    generateRandomCard();
});
```

**Anatomía del Event Listener:**
1. **Elemento**: `btnGenerate` (el botón)
2. **Evento**: `'click'` (cuando se hace click)
3. **Handler**: `function() { ... }` (qué hacer cuando ocurre)

### ✅ Checkpoint 7

Haz click en el botón varias veces. Cada click debería generar una nueva carta aleatoria.

---

## Paso 10: Añadir Animación

Hagamos que la carta tenga una pequeña animación al cambiar.

### 📝 Modifica la función `renderCard` en `app.js`

```javascript
function renderCard(suit, value) {
    // 1. Obtener los elementos internos de la carta
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');
    
    // 2. Actualizar el contenido
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;
    
    // 3. Actualizar el color
    card.className = 'card';
    card.classList.add(suit.color);
    
    // 4. ⭐ NUEVO: Animación de entrada
    card.style.transform = 'scale(0.9)';
    setTimeout(function() {
        card.style.transform = 'scale(1)';
    }, 100);
    
    console.log('Carta renderizada:', value + suit.symbol);
}
```

### 🔍 ¿Cómo funciona la animación?

```javascript
card.style.transform = 'scale(0.9)';  // Hace la carta más pequeña (90%)
```

```javascript
setTimeout(function() {
    card.style.transform = 'scale(1)';  // Vuelve al tamaño normal (100%)
}, 100);  // Después de 100 milisegundos
```

**Efecto visual**: La carta se "encoge" y luego vuelve a su tamaño, dando sensación de movimiento.

### 📝 Añade transición en `style.css`

```css
.card {
    /* ... estilos existentes ... */
    transition: transform 0.3s ease;  /* ⭐ NUEVO */
}
```

### ✅ Checkpoint 8

Haz click en el botón. Ahora deberías ver una suave animación cuando la carta cambia.

---

## Paso 11: Modo Automático (Avanzado)

Añadamos un modo que genera cartas automáticamente cada 3 segundos.

### 📝 Actualiza el HTML

```html
<button id="btnGenerate">Generar Nueva Carta</button>
<button id="btnAuto">Auto-Generar (cada 3s)</button>
<button id="btnStop">Detener</button>
```

### 📝 Añade estilos en `style.css`

```css
#btnAuto {
    background: #2ecc71;
    color: white;
}

#btnStop {
    background: #e74c3c;
    color: white;
}
```

### 📝 Añade al principio de `app.js`

```javascript
const btnAuto = document.getElementById('btnAuto');
const btnStop = document.getElementById('btnStop');

// Variable para controlar el intervalo
let autoGenerateInterval = null;
```

### 📝 Añade al final de `app.js`

```javascript
// Botón Auto-Generar
btnAuto.addEventListener('click', function() {
    // Si ya está corriendo, mostrar mensaje
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
    
    console.log('Modo automático activado');
});

// Botón Detener
btnStop.addEventListener('click', function() {
    // Detener el intervalo
    if (autoGenerateInterval) {
        clearInterval(autoGenerateInterval);
        autoGenerateInterval = null;
        
        // Restaurar botón
        btnAuto.textContent = 'Auto-Generar (cada 3s)';
        btnAuto.style.opacity = '1';
        
        console.log('Modo automático detenido');
    }
});
```

### 🔍 Conceptos clave: Timers en JavaScript

#### `setInterval()` - Repetir algo cada X tiempo

```javascript
let intervalo = setInterval(function() {
    console.log('¡Hola cada 3 segundos!');
}, 3000);
```

#### `clearInterval()` - Detener la repetición

```javascript
clearInterval(intervalo);
```

### 📊 Flujo del modo automático

```
Usuario hace click en "Auto-Generar"
    ↓
Se crea un intervalo que ejecuta generateRandomCard() cada 3000ms
    ↓
La carta cambia automáticamente cada 3 segundos
    ↓
Usuario hace click en "Detener"
    ↓
Se detiene el intervalo
```

### ✅ Checkpoint 9

1. Haz click en "Auto-Generar (cada 3s)"
2. Observa cómo la carta cambia automáticamente cada 3 segundos
3. Haz click en "Detener" para parar

---

## Paso 12: Mejorar la Carta con Hover

Añadamos un efecto cuando pasas el mouse sobre la carta.

### 📝 Añade a `style.css`

```css
.card:hover {
    transform: scale(1.05);
    cursor: pointer;
}
```

### ✅ Checkpoint 10

Pasa el mouse sobre la carta. Debería crecer ligeramente.

---

## 🎯 Código Final Completo

### `index.html`

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

### `style.css`

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
    cursor: pointer;
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

### `app.js`

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

// Función auxiliar: generar número aleatorio
function getRandomNumber(max) {
    return Math.floor(Math.random() * max);
}

// Función para generar una carta aleatoria
function generateRandomCard() {
    const randomSuit = suits[getRandomNumber(suits.length)];
    const randomValue = values[getRandomNumber(values.length)];
    
    renderCard(randomSuit, randomValue);
}

// Función para renderizar la carta en el DOM
function renderCard(suit, value) {
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');
    
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;
    
    card.className = 'card';
    card.classList.add(suit.color);
    
    // Animación
    card.style.transform = 'scale(0.9)';
    setTimeout(function() {
        card.style.transform = 'scale(1)';
    }, 100);
}

// Event Listeners
btnGenerate.addEventListener('click', function() {
    generateRandomCard();
});

btnAuto.addEventListener('click', function() {
    if (autoGenerateInterval) {
        alert('Ya está en modo automático');
        return;
    }
    
    autoGenerateInterval = setInterval(function() {
        generateRandomCard();
    }, 3000);
    
    btnAuto.textContent = '✓ Auto-Generando...';
    btnAuto.style.opacity = '0.5';
});

btnStop.addEventListener('click', function() {
    if (autoGenerateInterval) {
        clearInterval(autoGenerateInterval);
        autoGenerateInterval = null;
        
        btnAuto.textContent = 'Auto-Generar (cada 3s)';
        btnAuto.style.opacity = '1';
    }
});

// Generar una carta inicial
generateRandomCard();
```

---

## 🚀 Ejercicios de Extensión

### Ejercicio 1: Añadir un Contador ⭐

Añade un contador que muestre cuántas cartas se han generado.

**Pista:**
```javascript
let cartasGeneradas = 0;

function generateRandomCard() {
    // ... código existente ...
    cartasGeneradas++;
    document.getElementById('contador').textContent = 
        `Cartas generadas: ${cartasGeneradas}`;
}
```

### Ejercicio 2: Botón de Reset ⭐⭐

Añade un botón que reinicie el contador y genere una carta nueva.

### Ejercicio 3: Historial de Cartas ⭐⭐⭐

Muestra las últimas 5 cartas generadas debajo de la carta principal.

**Pista:**
```javascript
let historial = [];

function generateRandomCard() {
    // ... código existente ...
    
    historial.push(value + suit.symbol);
    if (historial.length > 5) {
        historial.shift(); // Eliminar la primera
    }
    
    mostrarHistorial();
}
```

### Ejercicio 4: Cambiar Velocidad del Auto-Generador ⭐⭐⭐

Añade un input que permita al usuario elegir cada cuántos segundos generar cartas.

---

## 📚 Conceptos Aprendidos

### JavaScript
✅ `Math.random()` y `Math.floor()` para números aleatorios  
✅ `querySelector()` para buscar elementos dentro de otros  
✅ `textContent` para cambiar texto  
✅ `classList.add()` para manipular clases CSS  
✅ `addEventListener()` para eventos  
✅ `setInterval()` y `clearInterval()` para timers  
✅ `setTimeout()` para delays

### CSS
✅ Flexbox con `flex-direction: column`  
✅ `transform: scale()` y `rotate()` para transformaciones  
✅ `transition` para animaciones suaves  
✅ Pseudo-clases `:hover` y `:active`  
✅ `box-shadow` para sombras

### DOM
✅ Manipulación dinámica del HTML  
✅ Event-driven programming  
✅ Separación de lógica (funciones reutilizables)

---

## 🎉 ¡Felicidades!

Has construido una aplicación web interactiva completa desde cero, paso a paso. Ahora entiendes:

- Cómo estructurar un proyecto web
- Cómo hacer que elementos sean interactivos
- Cómo generar contenido aleatorio
- Cómo usar timers para automatización
- Cómo crear animaciones suaves

**Próximo desafío**: Personaliza el proyecto con tus propios estilos y funcionalidades.

---

## 🔗 Recursos Adicionales

- [MDN - Math.random()](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
- [MDN - setInterval()](https://developer.mozilla.org/es/docs/Web/API/setInterval)
- [CSS Tricks - Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [MDN - Transform](https://developer.mozilla.org/es/docs/Web/CSS/transform)