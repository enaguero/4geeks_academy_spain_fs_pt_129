🇪🇸 **Español** | [🇬🇧 English](index.en.md)

# Día 11: El DOM y Eventos en JavaScript

## ¿Qué es el DOM?

Imagina que tu página web es una casa. El **DOM** (Document Object Model) es como un plano detallado de esa casa que JavaScript puede leer y modificar.

**DOM = Document Object Model** (Modelo de Objetos del Documento)

Es una representación en forma de **árbol** de tu documento HTML que JavaScript puede manipular.

### Analogía: El DOM como un Árbol Genealógico

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Mi Página</title>
    </head>
    <body>
        <h1>Bienvenido</h1>
        <p>Este es un párrafo</p>
    </body>
</html>
```

El navegador convierte esto en un árbol:

```
document
  └── html
      ├── head
      │   └── title
      │       └── "Mi Página"
      └── body
          ├── h1
          │   └── "Bienvenido"
          └── p
              └── "Este es un párrafo"
```

### ¿Por qué es Importante el DOM?

| Sin DOM | Con DOM |
|---------|---------|
| Páginas estáticas | Páginas dinámicas |
| No hay interacción | Reacciona a acciones del usuario |
| Contenido fijo | Contenido que cambia |
| Aburrido 😴 | Interactivo 🎮 |

**El DOM permite:**
- ✅ Cambiar el contenido de la página
- ✅ Cambiar los estilos CSS
- ✅ Añadir o eliminar elementos
- ✅ Responder a acciones del usuario (clicks, teclas, etc.)
- ✅ Crear aplicaciones web interactivas

---

## Estructura del DOM: Los Nodos

El DOM está formado por **nodos** (nodes). Hay varios tipos:

### Tipos de Nodos

```html
<div id="container" class="box">
    Hola mundo
    <span>Texto dentro de span</span>
</div>
```

| Tipo | Ejemplo | Descripción |
|------|---------|-------------|
| **Element Node** | `<div>`, `<span>` | Etiquetas HTML |
| **Text Node** | `"Hola mundo"` | Texto dentro de elementos |
| **Attribute Node** | `id="container"` | Atributos de elementos |
| **Document Node** | `document` | Raíz del árbol |

### Relaciones en el DOM: Familia de Nodos

```html
<div id="padre">
    <h1 id="hermano1">Título</h1>
    <p id="hermano2">Párrafo</p>
</div>
```

```
     #padre (parent)
        |
    ----+----
    |       |
#hermano1  #hermano2
(sibling)  (sibling)
(child)    (child)
```

- **Parent** (padre): `<div>` es padre de `<h1>` y `<p>`
- **Children** (hijos): `<h1>` y `<p>` son hijos de `<div>`
- **Siblings** (hermanos): `<h1>` y `<p>` son hermanos entre sí

---

## Acceder a Elementos del DOM

JavaScript ofrece varios métodos para "encontrar" elementos en el DOM.

### 1. `getElementById()` - Por ID (Único)

```html
<h1 id="titulo">Hola Mundo</h1>
<p id="descripcion">Este es un párrafo</p>
```

```javascript
// Obtener elemento por su ID
const titulo = document.getElementById('titulo');
console.log(titulo);  // <h1 id="titulo">Hola Mundo</h1>

const descripcion = document.getElementById('descripcion');
console.log(descripcion.textContent);  // "Este es un párrafo"
```

**Ventajas:**
- ✅ Muy rápido
- ✅ Retorna UN solo elemento
- ✅ Fácil de usar

**Limitación:**
- ⚠️ Solo funciona con IDs (que deben ser únicos)

### 2. `getElementsByClassName()` - Por Clase

```html
<p class="destacado">Párrafo 1</p>
<p class="destacado">Párrafo 2</p>
<p class="normal">Párrafo 3</p>
```

```javascript
// Obtener TODOS los elementos con esa clase
const destacados = document.getElementsByClassName('destacado');

console.log(destacados.length);  // 2

// Es una colección (como un array)
console.log(destacados[0].textContent);  // "Párrafo 1"
console.log(destacados[1].textContent);  // "Párrafo 2"

// Recorrer todos los elementos
for (let i = 0; i < destacados.length; i++) {
    console.log(destacados[i].textContent);
}
```

**Ventajas:**
- ✅ Encuentra múltiples elementos a la vez
- ✅ Útil para elementos con la misma clase

**Nota:**
- ⚠️ Retorna una **HTMLCollection** (similar a un array, pero no es un array real)

### 3. `getElementsByTagName()` - Por Etiqueta

```html
<p>Párrafo 1</p>
<p>Párrafo 2</p>
<div>Un div</div>
```

```javascript
// Obtener TODOS los elementos <p>
const parrafos = document.getElementsByTagName('p');

console.log(parrafos.length);  // 2

for (let i = 0; i < parrafos.length; i++) {
    console.log(parrafos[i].textContent);
}

// Obtener TODOS los divs
const divs = document.getElementsByTagName('div');
console.log(divs.length);  // 1
```

### 4. `querySelector()` - Selector CSS (Moderno) ✨

```html
<div class="container">
    <h1 id="titulo">Mi Título</h1>
    <p class="texto">Primer párrafo</p>
    <p class="texto importante">Segundo párrafo</p>
</div>
```

```javascript
// Usando selectores CSS (retorna EL PRIMERO que encuentre)
const titulo = document.querySelector('#titulo');  // Por ID
const primerTexto = document.querySelector('.texto');  // Por clase
const primerParrafo = document.querySelector('p');  // Por etiqueta

// Selectores más complejos
const textoImportante = document.querySelector('.texto.importante');
const parrafoEnContainer = document.querySelector('.container p');
```

**Ventajas:**
- ✅ Sintaxis de CSS (muy familiar)
- ✅ Muy flexible y poderoso
- ✅ Retorna UN elemento (el primero)

### 5. `querySelectorAll()` - Todos los Elementos (Moderno) ✨

```html
<p class="item">Item 1</p>
<p class="item">Item 2</p>
<p class="item">Item 3</p>
```

```javascript
// Obtener TODOS los elementos que coincidan
const items = document.querySelectorAll('.item');

console.log(items.length);  // 3

// Retorna un NodeList (puede usar forEach)
items.forEach(function(item, index) {
    console.log(`Item ${index}: ${item.textContent}`);
});

// También con arrow function
items.forEach((item, index) => {
    console.log(`Item ${index}: ${item.textContent}`);
});
```

**Ventajas:**
- ✅ Sintaxis de CSS
- ✅ Retorna TODOS los elementos
- ✅ Puedes usar `.forEach()`

### Tabla Comparativa de Métodos

| Método | Retorna | Sintaxis | Velocidad | Recomendación |
|--------|---------|----------|-----------|---------------|
| `getElementById()` | 1 elemento | `getElementById('id')` | Muy rápida | ✅ Cuando tienes ID |
| `getElementsByClassName()` | Colección | `getElementsByClassName('class')` | Rápida | ⚠️ Usar querySelector mejor |
| `getElementsByTagName()` | Colección | `getElementsByTagName('tag')` | Rápida | ⚠️ Usar querySelector mejor |
| `querySelector()` | 1 elemento | `querySelector('selector')` | Normal | ✅✅ **Recomendado** |
| `querySelectorAll()` | NodeList | `querySelectorAll('selector')` | Normal | ✅✅ **Recomendado** |

### Ejemplos Prácticos de Selectores

```javascript
// Por ID
document.querySelector('#miId')

// Por clase
document.querySelector('.miClase')

// Por etiqueta
document.querySelector('p')

// Combinaciones
document.querySelector('div.container')  // div CON clase container
document.querySelector('.container p')   // p DENTRO de .container
document.querySelector('p.destacado')    // p CON clase destacado

// Pseudo-clases
document.querySelector('p:first-child')  // Primer p
document.querySelector('li:nth-child(2)') // Segundo li

// Atributos
document.querySelector('[type="text"]')  // Elementos con type="text"
document.querySelector('input[name="email"]')  // Input con name="email"
```

---

## Manipular Contenido: innerHTML vs textContent

Una vez que tienes un elemento, puedes cambiar su contenido.

### `textContent` - Solo Texto

```html
<p id="parrafo">Texto original</p>
```

```javascript
const parrafo = document.getElementById('parrafo');

// Leer el texto
console.log(parrafo.textContent);  // "Texto original"

// Cambiar el texto
parrafo.textContent = "Nuevo texto";
// Resultado: <p id="parrafo">Nuevo texto</p>

// Si intentas HTML, lo muestra como texto
parrafo.textContent = "<strong>Negrita</strong>";
// Resultado: <p id="parrafo">&lt;strong&gt;Negrita&lt;/strong&gt;</p>
```

### `innerHTML` - HTML Completo

```html
<div id="contenedor">Contenido original</div>
```

```javascript
const contenedor = document.getElementById('contenedor');

// Leer el HTML
console.log(contenedor.innerHTML);  // "Contenido original"

// Cambiar con HTML
contenedor.innerHTML = "<strong>Texto en negrita</strong>";
// Resultado: <div id="contenedor"><strong>Texto en negrita</strong></div>

// Añadir elementos complejos
contenedor.innerHTML = `
    <h2>Título Nuevo</h2>
    <p>Párrafo con <em>énfasis</em></p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
`;
```

### Template Strings (Plantillas) con innerHTML

Las **template strings** (usando backticks \`) son perfectas para crear HTML dinámico:

```javascript
const nombre = "Ana";
const edad = 25;
const ciudad = "Madrid";

const contenedor = document.getElementById('perfil');

// ✅ Usando template strings
contenedor.innerHTML = `
    <div class="tarjeta">
        <h2>Perfil de ${nombre}</h2>
        <p>Edad: ${edad} años</p>
        <p>Ciudad: ${ciudad}</p>
        <button>Contactar</button>
    </div>
`;
```

### Ejemplo Práctico: Lista de Productos

```html
<div id="productos"></div>
```

```javascript
const productos = [
    { nombre: "Laptop", precio: 999 },
    { nombre: "Mouse", precio: 25 },
    { nombre: "Teclado", precio: 75 }
];

const contenedor = document.getElementById('productos');

// Construir HTML dinámicamente
let html = '<ul class="lista-productos">';

productos.forEach(producto => {
    html += `
        <li class="producto">
            <span class="nombre">${producto.nombre}</span>
            <span class="precio">$${producto.precio}</span>
        </li>
    `;
});

html += '</ul>';

contenedor.innerHTML = html;
```

**Resultado:**
```html
<div id="productos">
    <ul class="lista-productos">
        <li class="producto">
            <span class="nombre">Laptop</span>
            <span class="precio">$999</span>
        </li>
        <li class="producto">
            <span class="nombre">Mouse</span>
            <span class="precio">$25</span>
        </li>
        <li class="producto">
            <span class="nombre">Teclado</span>
            <span class="precio">$75</span>
        </li>
    </ul>
</div>
```

### Comparación: textContent vs innerHTML

| Aspecto | `textContent` | `innerHTML` |
|---------|---------------|-------------|
| **Contenido** | Solo texto plano | HTML completo |
| **Etiquetas HTML** | Las muestra como texto | Las interpreta como HTML |
| **Seguridad** | ✅ Seguro | ⚠️ Riesgo XSS si usas datos del usuario |
| **Velocidad** | Más rápido | Más lento (interpreta HTML) |
| **Uso típico** | Cambiar texto simple | Crear estructuras HTML |

### ⚠️ Advertencia de Seguridad

```javascript
// ❌ PELIGROSO: NO hagas esto con datos del usuario
const inputUsuario = "<script>alert('Hackeado!')</script>";
contenedor.innerHTML = inputUsuario;  // ¡Ejecuta el script!

// ✅ SEGURO: Usa textContent para datos del usuario
contenedor.textContent = inputUsuario;  // Lo muestra como texto
```

---

## ¿Qué es un Evento?

Un **evento** es algo que sucede en tu página web. Es como cuando presionas el timbre de una casa y alguien responde.

### Ejemplos de Eventos Comunes

| Evento | Cuándo Ocurre | Ejemplo |
|--------|---------------|---------|
| **click** | Usuario hace click | Botón presionado |
| **change** | Valor de input cambia | Seleccionar opción en select |
| **input** | Usuario escribe en input | Cada tecla presionada |
| **submit** | Formulario se envía | Dar click en "Enviar" |
| **load** | Página/imagen termina de cargar | Página lista |
| **keydown** | Usuario presiona una tecla | Escribir en input |
| **mouseover** | Mouse entra en elemento | Hover sobre botón |
| **mouseout** | Mouse sale de elemento | Dejar de hacer hover |

### Anatomía de un Evento

```javascript
elemento.addEventListener('tipo-evento', function() {
    // Código que se ejecuta cuando ocurre el evento
});
```

**Partes:**
1. **Elemento**: El elemento HTML que escucha el evento
2. **Tipo de evento**: Qué evento esperar (click, change, etc.)
3. **Función**: Qué hacer cuando ocurre el evento (también llamada "event handler")

---

## El Evento `load` - Esperar a que la Página Cargue

### ¿Por qué es Importante?

Si JavaScript se ejecuta ANTES de que el HTML esté listo, no encontrará los elementos:

```html
<head>
    <script>
        // ❌ MAL: Este código se ejecuta ANTES de que exista el botón
        const boton = document.getElementById('miBoton');
        console.log(boton);  // null - ¡No existe aún!
    </script>
</head>
<body>
    <button id="miBoton">Click aquí</button>
</body>
```

### Solución 1: `window.onload`

```html
<head>
    <script>
        // ✅ BIEN: Esperar a que TODO cargue
        window.onload = function() {
            const boton = document.getElementById('miBoton');
            console.log(boton);  // <button id="miBoton">Click aquí</button>
        };
    </script>
</head>
<body>
    <button id="miBoton">Click aquí</button>
</body>
```

### Solución 2: `DOMContentLoaded` (Más rápido)

```html
<head>
    <script>
        // ✅ MEJOR: Esperar solo a que el DOM cargue (no las imágenes)
        document.addEventListener('DOMContentLoaded', function() {
            const boton = document.getElementById('miBoton');
            console.log(boton);  // Funciona!
        });
    </script>
</head>
<body>
    <button id="miBoton">Click aquí</button>
</body>
```

### Solución 3: Script al Final del Body (Más Simple)

```html
<head>
    <!-- Sin JavaScript aquí -->
</head>
<body>
    <button id="miBoton">Click aquí</button>
    
    <!-- ✅ SIMPLE: Script al final -->
    <script>
        const boton = document.getElementById('miBoton');
        console.log(boton);  // Funciona porque el botón ya existe
    </script>
</body>
```

### Solución 4: Usar `defer` (Moderno) ✨

```html
<head>
    <!-- ✅ MODERNO: defer espera automáticamente -->
    <script src="app.js" defer></script>
</head>
<body>
    <button id="miBoton">Click aquí</button>
</body>
```

```javascript
// app.js - No necesitas window.onload
const boton = document.getElementById('miBoton');
console.log(boton);  // Funciona!
```

### Comparación de Métodos

| Método | Cuándo Usar | Ventaja | Desventaja |
|--------|-------------|---------|------------|
| `window.onload` | Necesitas que imágenes carguen | Espera TODO | Más lento |
| `DOMContentLoaded` | Solo necesitas el HTML | Más rápido que onload | Un poco de código extra |
| Script al final | Proyectos simples | Muy simple | HTML y JS separados |
| `defer` | Proyectos modernos | Limpio y estándar | Requiere archivo externo |

---

## Evento `onclick` - El Click del Mouse

### Forma 1: En el HTML (Inline) ❌

```html
<!-- ❌ NO RECOMENDADO: Mezcla HTML con JavaScript -->
<button onclick="saludar()">Saludar</button>

<script>
function saludar() {
    alert('¡Hola!');
}
</script>
```

**Desventajas:**
- Mezcla HTML con JavaScript
- Difícil de mantener
- No es buena práctica

### Forma 2: Con `onclick` en JavaScript

```html
<button id="miBoton">Saludar</button>

<script>
const boton = document.getElementById('miBoton');

// Asignar función al evento
boton.onclick = function() {
    alert('¡Hola!');
};
</script>
```

**Problema:**
- Solo puedes asignar UNA función por evento

### Forma 3: Con `addEventListener()` (Recomendado) ✅

```html
<button id="miBoton">Saludar</button>

<script>
const boton = document.getElementById('miBoton');

// ✅ MEJOR: addEventListener
boton.addEventListener('click', function() {
    alert('¡Hola!');
});

// Puedes añadir múltiples listeners
boton.addEventListener('click', function() {
    console.log('Click registrado');
});
</script>
```

**Ventajas:**
- Puedes asignar múltiples funciones al mismo evento
- Es el estándar moderno
- Más flexible

### Ejemplo Completo: Contador de Clicks

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contador</title>
</head>
<body>
    <h1>Contador de Clicks</h1>
    <p>Has hecho click <span id="contador">0</span> veces</p>
    <button id="btnContar">Hacer Click</button>
    <button id="btnReset">Resetear</button>

    <script>
        let clicks = 0;
        
        const contadorElemento = document.getElementById('contador');
        const btnContar = document.getElementById('btnContar');
        const btnReset = document.getElementById('btnReset');
        
        // Incrementar contador
        btnContar.addEventListener('click', function() {
            clicks++;
            contadorElemento.textContent = clicks;
        });
        
        // Resetear contador
        btnReset.addEventListener('click', function() {
            clicks = 0;
            contadorElemento.textContent = clicks;
        });
    </script>
</body>
</html>
```

### Acceder a Información del Evento

```html
<button id="miBoton">Click aquí</button>

<script>
const boton = document.getElementById('miBoton');

boton.addEventListener('click', function(event) {
    console.log('Elemento clickeado:', event.target);
    console.log('Tipo de evento:', event.type);
    console.log('Coordenadas X:', event.clientX);
    console.log('Coordenadas Y:', event.clientY);
});
</script>
```

---

## Evento `onchange` - Detectar Cambios

El evento `change` se dispara cuando el valor de un input cambia y el usuario **sale del campo** (blur).

### Con Input de Texto

```html
<label>Nombre:</label>
<input type="text" id="nombre">
<p id="saludo"></p>

<script>
const inputNombre = document.getElementById('nombre');
const saludo = document.getElementById('saludo');

inputNombre.addEventListener('change', function() {
    const valor = inputNombre.value;
    saludo.textContent = `Hola, ${valor}!`;
});
</script>
```

### Con Select (Dropdown)

```html
<label>Elige tu ciudad:</label>
<select id="ciudad">
    <option value="">Selecciona...</option>
    <option value="madrid">Madrid</option>
    <option value="barcelona">Barcelona</option>
    <option value="valencia">Valencia</option>
</select>
<p id="resultado"></p>

<script>
const selectCiudad = document.getElementById('ciudad');
const resultado = document.getElementById('resultado');

selectCiudad.addEventListener('change', function() {
    const ciudadSeleccionada = selectCiudad.value;
    
    if (ciudadSeleccionada) {
        resultado.textContent = `Has seleccionado: ${ciudadSeleccionada}`;
    } else {
        resultado.textContent = '';
    }
});
</script>
```

### Con Checkbox

```html
<label>
    <input type="checkbox" id="acepto">
    Acepto los términos y condiciones
</label>
<button id="enviar" disabled>Enviar</button>

<script>
const checkbox = document.getElementById('acepto');
const botonEnviar = document.getElementById('enviar');

checkbox.addEventListener('change', function() {
    // checkbox.checked es true o false
    if (checkbox.checked) {
        botonEnviar.disabled = false;
        botonEnviar.textContent = 'Enviar ✅';
    } else {
        botonEnviar.disabled = true;
        botonEnviar.textContent = 'Enviar';
    }
});
</script>
```

### Con Radio Buttons

```html
<p>Selecciona tu plan:</p>
<label>
    <input type="radio" name="plan" value="basico"> Básico ($10/mes)
</label>
<label>
    <input type="radio" name="plan" value="premium"> Premium ($20/mes)
</label>
<label>
    <input type="radio" name="plan" value="empresarial"> Empresarial ($50/mes)
</label>
<p id="planSeleccionado"></p>

<script>
const radios = document.querySelectorAll('input[name="plan"]');
const planSeleccionado = document.getElementById('planSeleccionado');

radios.forEach(radio => {
    radio.addEventListener('change', function() {
        const plan = radio.value;
        
        let precio;
        if (plan === 'basico') precio = 10;
        else if (plan === 'premium') precio = 20;
        else precio = 50;
        
        planSeleccionado.innerHTML = `
            <strong>Plan seleccionado:</strong> ${plan.toUpperCase()}<br>
            <strong>Precio:</strong> $${precio}/mes
        `;
    });
});
</script>
```

---

## Evento `input` - Detectar Cada Tecla

A diferencia de `change`, `input` se dispara **en cada cambio** (cada tecla presionada).

```html
<label>Buscar:</label>
<input type="text" id="busqueda" placeholder="Escribe para buscar...">
<p id="resultado"></p>

<script>
const inputBusqueda = document.getElementById('busqueda');
const resultado = document.getElementById('resultado');

inputBusqueda.addEventListener('input', function() {
    const texto = inputBusqueda.value;
    resultado.textContent = `Buscando: "${texto}" (${texto.length} caracteres)`;
});
</script>
```

### Ejemplo: Validación en Tiempo Real

```html
<label>Contraseña:</label>
<input type="password" id="password">
<div id="validacion"></div>

<script>
const inputPassword = document.getElementById('password');
const validacion = document.getElementById('validacion');

inputPassword.addEventListener('input', function() {
    const password = inputPassword.value;
    const longitud = password.length;
    
    let mensaje = '';
    let color = '';
    
    if (longitud === 0) {
        mensaje = '';
    } else if (longitud < 6) {
        mensaje = '❌ Muy corta (mínimo 6 caracteres)';
        color = 'red';
    } else if (longitud < 10) {
        mensaje = '⚠️ Aceptable';
        color = 'orange';
    } else {
        mensaje = '✅ Fuerte';
        color = 'green';
    }
    
    validacion.textContent = mensaje;
    validacion.style.color = color;
});
</script>
```

---

## Evento `submit` - Enviar Formularios

```html
<form id="miFormulario">
    <label>Nombre:</label>
    <input type="text" id="nombre" required>
    
    <label>Email:</label>
    <input type="email" id="email" required>
    
    <button type="submit">Enviar</button>
</form>

<div id="mensaje"></div>

<script>
const formulario = document.getElementById('miFormulario');
const mensaje = document.getElementById('mensaje');

formulario.addEventListener('submit', function(event) {
    // ¡IMPORTANTE! Prevenir el envío por defecto
    event.preventDefault();
    
    // Obtener valores
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    
    // Mostrar mensaje
    mensaje.innerHTML = `
        <h3>Formulario enviado:</h3>
        <p><strong>Nombre:</strong> ${nombre}</p>
        <p><strong>Email:</strong> ${email}</p>
    `;
    
    // Limpiar formulario
    formulario.reset();
});
</script>
```

**⚠️ Importante:** `event.preventDefault()` evita que el formulario se envíe y recargue la página.

---

## Eventos del Mouse

### `mouseover` y `mouseout` - Hover

```html
<div id="caja" style="width: 200px; height: 200px; background: blue;">
    Pasa el mouse aquí
</div>

<script>
const caja = document.getElementById('caja');

caja.addEventListener('mouseover', function() {
    caja.style.background = 'red';
    caja.textContent = 'Mouse encima!';
});

caja.addEventListener('mouseout', function() {
    caja.style.background = 'blue';
    caja.textContent = 'Pasa el mouse aquí';
});
</script>
```

### `mouseenter` y `mouseleave` (Similar pero diferente)

```html
<div id="contenedor" style="padding: 20px; background: lightgray;">
    <p>Contenedor externo</p>
    <div id="interno" style="padding: 20px; background: white;">
        <p>Contenedor interno</p>
    </div>
</div>

<script>
const contenedor = document.getElementById('contenedor');

// mouseenter NO se dispara en elementos hijos
contenedor.addEventListener('mouseenter', function() {
    console.log('Entraste al contenedor');
});

contenedor.addEventListener('mouseleave', function() {
    console.log('Saliste del contenedor');
});
</script>
```

### `mousemove` - Seguir el Mouse

```html
<div id="area" style="width: 400px; height: 300px; background: lightblue; position: relative;">
    Mueve el mouse
</div>
<p id="coordenadas"></p>

<script>
const area = document.getElementById('area');
const coordenadas = document.getElementById('coordenadas');

area.addEventListener('mousemove', function(event) {
    const x = event.offsetX;
    const y = event.offsetY;
    coordenadas.textContent = `X: ${x}px, Y: ${y}px`;
});
</script>
```

---

## Eventos del Teclado

### `keydown` - Cuando Presionas una Tecla

```html
<input type="text" id="teclado" placeholder="Presiona teclas...">
<p id="info"></p>

<script>
const input = document.getElementById('teclado');
const info = document.getElementById('info');

input.addEventListener('keydown', function(event) {
    info.innerHTML = `
        <strong>Tecla:</strong> ${event.key}<br>
        <strong>Código:</strong> ${event.code}<br>
        <strong>Ctrl:</strong> ${event.ctrlKey}<br>
        <strong>Shift:</strong> ${event.shiftKey}
    `;
});
</script>
```

### Detectar Teclas Especiales

```html
<input type="text" id="campo">
<p id="mensaje"></p>

<script>
const campo = document.getElementById('campo');
const mensaje = document.getElementById('mensaje');

campo.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        mensaje.textContent = '¡Presionaste Enter!';
    } else if (event.key === 'Escape') {
        campo.value = '';
        mensaje.textContent = 'Campo limpiado con Escape';
    } else if (event.ctrlKey && event.key === 's') {
        event.preventDefault();  // Evitar guardar página
        mensaje.textContent = '¡Atajo Ctrl+S detectado!';
    }
});
</script>
```

---

## Proyecto Práctico: Lista de Tareas Interactiva

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Tareas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
        }
        
        .tarea {
            padding: 10px;
            margin: 10px 0;
            background: #f0f0f0;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .tarea.completada {
            text-decoration: line-through;
            opacity: 0.6;
        }
        
        button {
            padding: 10px 20px;
            cursor: pointer;
        }
        
        .btn-eliminar {
            background: #ff4444;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>📝 Mi Lista de Tareas</h1>
    
    <div>
        <input type="text" id="nuevaTarea" placeholder="Escribe una nueva tarea...">
        <button id="btnAgregar">Agregar</button>
    </div>
    
    <div id="listaTareas"></div>
    
    <script>
        const inputNuevaTarea = document.getElementById('nuevaTarea');
        const btnAgregar = document.getElementById('btnAgregar');
        const listaTareas = document.getElementById('listaTareas');
        
        let tareas = [];
        
        // Agregar tarea
        btnAgregar.addEventListener('click', agregarTarea);
        
        // También agregar con Enter
        inputNuevaTarea.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                agregarTarea();
            }
        });
        
        function agregarTarea() {
            const texto = inputNuevaTarea.value.trim();
            
            if (texto === '') {
                alert('Por favor escribe una tarea');
                return;
            }
            
            // Crear objeto tarea
            const tarea = {
                id: Date.now(),
                texto: texto,
                completada: false
            };
            
            // Agregar al array
            tareas.push(tarea);
            
            // Limpiar input
            inputNuevaTarea.value = '';
            
            // Renderizar lista
            renderizarTareas();
        }
        
        function renderizarTareas() {
            // Construir HTML con template strings
            let html = '';
            
            tareas.forEach(tarea => {
                html += `
                    <div class="tarea ${tarea.completada ? 'completada' : ''}" data-id="${tarea.id}">
                        <span>${tarea.texto}</span>
                        <div>
                            <button onclick="toggleCompletada(${tarea.id})">
                                ${tarea.completada ? '↩️ Deshacer' : '✅ Completar'}
                            </button>
                            <button class="btn-eliminar" onclick="eliminarTarea(${tarea.id})">
                                🗑️ Eliminar
                            </button>
                        </div>
                    </div>
                `;
            });
            
            listaTareas.innerHTML = html;
        }
        
        function toggleCompletada(id) {
            const tarea = tareas.find(t => t.id === id);
            if (tarea) {
                tarea.completada = !tarea.completada;
                renderizarTareas();
            }
        }
        
        function eliminarTarea(id) {
            tareas = tareas.filter(t => t.id !== id);
            renderizarTareas();
        }
    </script>
</body>
</html>
```

---

## Resumen de Eventos Más Comunes

### Eventos del Mouse

| Evento | Cuándo Ocurre | Uso Común |
|--------|---------------|-----------|
| `click` | Click del mouse | Botones, links |
| `dblclick` | Doble click | Abrir elementos |
| `mouseover` | Mouse entra al elemento | Tooltips, hover |
| `mouseout` | Mouse sale del elemento | Quitar hover |
| `mouseenter` | Mouse entra (no bubbling) | Menús desplegables |
| `mouseleave` | Mouse sale (no bubbling) | Menús desplegables |
| `mousemove` | Mouse se mueve sobre elemento | Seguir cursor |
| `mousedown` | Presionar botón del mouse | Drag and drop |
| `mouseup` | Soltar botón del mouse | Drag and drop |

### Eventos del Teclado

| Evento | Cuándo Ocurre | Uso Común |
|--------|---------------|-----------|
| `keydown` | Presionar tecla | Detectar teclas especiales |
| `keyup` | Soltar tecla | Ejecutar después de escribir |
| `keypress` | Tecla de carácter presionada | ⚠️ Deprecated, usar keydown |

### Eventos de Formularios

| Evento | Cuándo Ocurre | Uso Común |
|--------|---------------|-----------|
| `submit` | Formulario enviado | Validar antes de enviar |
| `change` | Valor cambia y pierde foco | Select, checkbox, radio |
| `input` | Valor cambia (cada tecla) | Validación en tiempo real |
| `focus` | Elemento recibe foco | Resaltar campo activo |
| `blur` | Elemento pierde foco | Validar al salir del campo |

### Eventos de la Página

| Evento | Cuándo Ocurre | Uso Común |
|--------|---------------|-----------|
| `load` | Página/elemento cargado | Inicializar app |
| `DOMContentLoaded` | DOM listo (sin imágenes) | Inicializar más rápido |
| `resize` | Ventana cambia tamaño | Responsive JavaScript |
| `scroll` | Usuario hace scroll | Infinite scroll, animations |

---

## Buenas Prácticas con Eventos

### ✅ DO - Hacer

```javascript
// ✅ Usar addEventListener
elemento.addEventListener('click', miFuncion);

// ✅ Prevenir comportamiento por defecto cuando sea necesario
formulario.addEventListener('submit', function(event) {
    event.preventDefault();
    // Tu código...
});

// ✅ Usar event delegation para elementos dinámicos
document.addEventListener('click', function(event) {
    if (event.target.matches('.boton-dinamico')) {
        // Manejar click
    }
});

// ✅ Limpiar event listeners cuando no los necesites
elemento.removeEventListener('click', miFuncion);
```

### ❌ DON'T - No Hacer

```javascript
// ❌ Evitar inline event handlers en HTML
<button onclick="alert('No!')">Mal</button>

// ❌ No usar onclick directamente (solo permite una función)
elemento.onclick = function() { };

// ❌ No crear funciones pesadas en eventos que se disparan mucho
window.addEventListener('scroll', function() {
    // ❌ Cálculos pesados en cada scroll
    hacerAlgoMuyPesado();
});
```

---

## Ejercicios Prácticos

### Ejercicio 1: Cambiar Color de Fondo

Crea un botón que cambie el color de fondo de la página cada vez que se hace click.

```html
<button id="btnColor">Cambiar Color</button>
```

<details>
<summary>Ver solución</summary>

```javascript
const btnColor = document.getElementById('btnColor');
const colores = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink'];
let indice = 0;

btnColor.addEventListener('click', function() {
    document.body.style.backgroundColor = colores[indice];
    indice = (indice + 1) % colores.length;
});
```
</details>

### Ejercicio 2: Contador de Caracteres

Crea un textarea que muestre cuántos caracteres ha escrito el usuario en tiempo real.

```html
<textarea id="texto" rows="5" cols="50"></textarea>
<p>Caracteres: <span id="contador">0</span></p>
```

<details>
<summary>Ver solución</summary>

```javascript
const texto = document.getElementById('texto');
const contador = document.getElementById('contador');

texto.addEventListener('input', function() {
    contador.textContent = texto.value.length;
});
```
</details>

### Ejercicio 3: Mostrar/Ocultar Contenido

Crea un botón que muestre u oculte un div.

```html
<button id="btnToggle">Mostrar/Ocultar</button>
<div id="contenido" style="display: none;">
    <p>Este contenido se puede mostrar u ocultar</p>
</div>
```

<details>
<summary>Ver solución</summary>

```javascript
const btnToggle = document.getElementById('btnToggle');
const contenido = document.getElementById('contenido');

btnToggle.addEventListener('click', function() {
    if (contenido.style.display === 'none') {
        contenido.style.display = 'block';
        btnToggle.textContent = 'Ocultar';
    } else {
        contenido.style.display = 'none';
        btnToggle.textContent = 'Mostrar';
    }
});
```
</details>

---

## Conclusión

Has aprendido:

✅ **DOM**: Qué es y cómo está estructurado  
✅ **Seleccionar elementos**: getElementById, querySelector, querySelectorAll  
✅ **Manipular contenido**: innerHTML, textContent, template strings  
✅ **Eventos**: Qué son y cómo funcionan  
✅ **Event listeners**: addEventListener para manejar eventos  
✅ **Eventos comunes**: click, change, input, submit, load  
✅ **Eventos del mouse**: mouseover, mouseout, mousemove  
✅ **Eventos del teclado**: keydown, keyup  
✅ **Proyecto práctico**: Lista de tareas completa

### Próximos Pasos

1. Practica con los ejercicios
2. Crea tu propio proyecto interactivo
3. Experimenta con diferentes eventos
4. Combina eventos con manipulación del DOM
5. Aprende sobre event propagation (bubbling y capturing)

**¡Ahora puedes crear páginas web totalmente interactivas! 🚀**

---

## Recursos Adicionales

- **MDN - DOM**: https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model
- **MDN - Eventos**: https://developer.mozilla.org/es/docs/Web/Events
- **JavaScript.info - DOM**: https://javascript.info/document
- **W3Schools - DOM Tutorial**: https://www.w3schools.com/js/js_htmldom.asp

---

## Cheat Sheet: DOM y Eventos

```javascript
// SELECCIONAR ELEMENTOS
document.getElementById('id')
document.querySelector('.clase')
document.querySelectorAll('p')

// MANIPULAR CONTENIDO
elemento.textContent = 'texto'
elemento.innerHTML = '<strong>HTML</strong>'
elemento.innerHTML = `<p>${variable}</p>`

// EVENTOS BÁSICOS
elemento.addEventListener('click', function() { })
elemento.addEventListener('change', function() { })
elemento.addEventListener('input', function() { })

// ESPERAR A QUE CARGUE
window.onload = function() { }
document.addEventListener('DOMContentLoaded', function() { })

// PREVENIR COMPORTAMIENTO POR DEFECTO
event.preventDefault()

// OBTENER VALORES
input.value
checkbox.checked
select.value

// MODIFICAR ESTILOS
elemento.style.color = 'red'
elemento.style.display = 'none'
```