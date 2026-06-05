🇪🇸 **Español** | [🇬🇧 English](index.en.md)

# Día 7: Introducción a JavaScript

## ¿Pero qué es programar?

**Programar** es el arte de darle instrucciones a una computadora para que realice tareas específicas. Es como escribir una receta de cocina: paso a paso, le dices a la máquina qué hacer.

Cuando programas, estás creando **algoritmos**: secuencias lógicas de pasos que resuelven un problema. JavaScript es uno de los lenguajes que usamos para escribir estas instrucciones, especialmente en el navegador web.

**¿Por qué JavaScript?**
- Es el único lenguaje que entienden todos los navegadores
- Permite hacer páginas web interactivas
- Es relativamente fácil de aprender para principiantes
- Tiene una comunidad enorme de desarrolladores

---

## Variables

Las **variables** son como cajas donde guardamos información. Imagina que tienes una caja etiquetada "nombre" donde guardas el nombre de una persona. En JavaScript, las variables funcionan exactamente así.

### Asignar un valor a las variables

Para crear una variable y asignarle un valor, usamos el signo `=`:

```javascript
let nombre = "Ana";
let edad = 25;
let estaEstudiando = true;
```

El signo `=` NO significa "igual", significa **"asignar"**. Estamos asignando el valor `"Ana"` a la variable `nombre`.

### var vs let vs const

JavaScript tiene tres formas de declarar variables:

#### **var** (la antigua)
```javascript
var apellido = "García";
```
- Es la forma antigua de declarar variables
- Tiene problemas de alcance (scope) que pueden causar errores
- **Recomendación**: No uses `var` en código nuevo

#### **let** (para valores que cambian)
```javascript
let contador = 0;
contador = 1;  // ✅ Podemos cambiar el valor
contador = 2;  // ✅ Y volverlo a cambiar
```
- Para variables cuyos valores van a cambiar
- Alcance de bloque (más seguro)

#### **const** (para valores constantes)
```javascript
const PI = 3.14159;
PI = 3.14;  // ❌ Error: no se puede reasignar
```
- Para valores que NO van a cambiar
- **Recomendación**: Usa `const` por defecto, solo usa `let` cuando sepas que el valor cambiará

---

## Tipos de Datos

JavaScript tiene varios tipos de datos básicos:

### 1. **String (Cadenas de texto)**
```javascript
const saludo = "Hola Mundo";
const mensaje = 'También con comillas simples';
const nombre = `Mi nombre es ${nombre}`;  // Template literals
```

### 2. **Number (Números)**
```javascript
const edad = 30;
const precio = 19.99;
const temperatura = -5;
```

### 3. **Boolean (Booleanos)**
```javascript
const esMayorDeEdad = true;
const estaLloviendo = false;
```

### 4. **Undefined (Indefinido)**
```javascript
let resultado;  // undefined (declarada pero sin valor)
```

### 5. **Null (Nulo)**
```javascript
const dato = null;  // Intencionalmente vacío
```

### 6. **Array (Arreglos/Listas)**
```javascript
const frutas = ["manzana", "banana", "naranja"];
const numeros = [1, 2, 3, 4, 5];
```

### 7. **Object (Objetos)**
```javascript
const persona = {
  nombre: "Carlos",
  edad: 28,
  ciudad: "Madrid"
};
```

---

## Operaciones

### Operaciones Matemáticas

```javascript
const suma = 5 + 3;           // 8
const resta = 10 - 4;         // 6
const multiplicacion = 6 * 7; // 42
const division = 20 / 4;      // 5
const modulo = 17 % 5;        // 2 (resto de la división)
const potencia = 2 ** 3;      // 8 (2 elevado a 3)
```

### Operaciones con Strings

```javascript
const nombre = "Juan";
const apellido = "Pérez";
const nombreCompleto = nombre + " " + apellido;  // "Juan Pérez"

// Con template literals (más moderno):
const saludo = `Hola, ${nombre} ${apellido}`;  // "Hola, Juan Pérez"
```

### Operaciones de Incremento/Decremento

```javascript
let contador = 0;
contador++;      // contador = 1 (incrementa en 1)
contador--;      // contador = 0 (decrementa en 1)
contador += 5;   // contador = 5 (suma 5)
contador -= 2;   // contador = 3 (resta 2)
contador *= 2;   // contador = 6 (multiplica por 2)
```

---

## Funciones

Las **funciones** son bloques de código reutilizables que realizan una tarea específica. Son como mini-programas dentro de tu programa.

### Declarar una Función

```javascript
// Declaración de función tradicional
function saludar() {
  console.log("¡Hola!");
}

// Llamar/ejecutar la función
saludar();  // Imprime: ¡Hola!
```

### Funciones con Parámetros y Alcance

Los **parámetros** son valores que pasamos a la función para que trabaje con ellos:

```javascript
function saludarPersona(nombre) {
  console.log(`Hola, ${nombre}!`);
}

saludarPersona("Ana");     // Imprime: Hola, Ana!
saludarPersona("Carlos");  // Imprime: Hola, Carlos!
```

**Función Scope (Alcance)**: Las variables declaradas dentro de una función solo existen dentro de esa función.

```javascript
function ejemplo() {
  let variableLocal = "Solo existo aquí";
  console.log(variableLocal);  // ✅ Funciona
}

ejemplo();
console.log(variableLocal);  // ❌ Error: variableLocal no está definida
```

### Funciones que Retornan Valores

```javascript
function sumar(a, b) {
  return a + b;
}

const resultado = sumar(5, 3);  // resultado = 8
console.log(resultado);
```

### Funciones Anónimas

Son funciones sin nombre, generalmente asignadas a variables:

```javascript
const multiplicar = function(a, b) {
  return a * b;
};

console.log(multiplicar(4, 5));  // 20
```

### Arrow Functions (Funciones Flecha) - Moderno

```javascript
const dividir = (a, b) => {
  return a / b;
};

// Versión corta (cuando solo hay un return):
const restar = (a, b) => a - b;

console.log(dividir(10, 2));  // 5
console.log(restar(10, 3));   // 7
```

---

## Operaciones Lógicas

### Operadores de Comparación

```javascript
5 == "5"    // true  (compara solo valor)
5 === "5"   // false (compara valor Y tipo)
5 != "5"    // false
5 !== "5"   // true
5 > 3       // true  (mayor que)
5 < 3       // false (menor que)
5 >= 5      // true  (mayor o igual)
5 <= 4      // false (menor o igual)
```

**⚠️ Importante**: Usa siempre `===` y `!==` en lugar de `==` y `!=` para evitar errores.

### Operadores AND y OR

#### **AND (`&&`)**: Todas las condiciones deben ser verdaderas

```javascript
const edad = 20;
const tieneCarnet = true;

if (edad >= 18 && tieneCarnet) {
  console.log("Puede conducir");  // ✅ Se ejecuta
}
```

#### **OR (`||`)**: Al menos una condición debe ser verdadera

```javascript
const esFinDeSemana = true;
const esVacaciones = false;

if (esFinDeSemana || esVacaciones) {
  console.log("Puede descansar");  // ✅ Se ejecuta
}
```

#### **NOT (`!`)**: Invierte el valor

```javascript
const estaLloviendo = false;

if (!estaLloviendo) {
  console.log("Puedes salir");  // ✅ Se ejecuta
}
```

---

## Controlar el Flujo de tu Código

### if / else if / else

```javascript
const nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Bien");  // ✅ Se ejecuta esto
} else if (nota >= 50) {
  console.log("Suficiente");
} else {
  console.log("Insuficiente");
}
```

### Switch

Útil cuando tienes muchas condiciones basadas en el mismo valor:

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

### Operador Ternario (Condiciones inline)

Una forma compacta de escribir `if/else`:

```javascript
// Sintaxis: condicion ? valorSiTrue : valorSiFalse

const edad = 20;
const mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(mensaje);  // "Mayor de edad"

// Equivalente a:
let mensajeTradicional;
if (edad >= 18) {
  mensajeTradicional = "Mayor de edad";
} else {
  mensajeTradicional = "Menor de edad";
}
```

---

## Bucles (Loops)

Los bucles nos permiten repetir código múltiples veces.

### While

Se ejecuta mientras la condición sea verdadera:

```javascript
let contador = 0;

while (contador < 5) {
  console.log(`Contador: ${contador}`);
  contador++;
}
// Imprime: 0, 1, 2, 3, 4
```

### For

El bucle más común, ideal cuando sabes cuántas veces quieres repetir:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Iteración: ${i}`);
}
// Imprime: 0, 1, 2, 3, 4
```

**Explicación**:
- `let i = 0`: Inicialización
- `i < 5`: Condición (mientras sea true, continúa)
- `i++`: Incremento (después de cada iteración)

### For...of (Recorrer Arrays)

```javascript
const frutas = ["manzana", "banana", "naranja"];

for (const fruta of frutas) {
  console.log(fruta);
}
// Imprime: manzana, banana, naranja
```

### For...in (Recorrer Objetos)

```javascript
const persona = {
  nombre: "Ana",
  edad: 25,
  ciudad: "Madrid"
};

for (const propiedad in persona) {
  console.log(`${propiedad}: ${persona[propiedad]}`);
}
// Imprime:
// nombre: Ana
// edad: 25
// ciudad: Madrid
```

---

## ¿Por qué usar Funciones?

Imagina que necesitas calcular el área de varios rectángulos en tu código:

### ❌ Sin funciones (código repetitivo)

```javascript
// Rectángulo 1
const base1 = 5;
const altura1 = 3;
const area1 = base1 * altura1;
console.log(area1);

// Rectángulo 2
const base2 = 8;
const altura2 = 4;
const area2 = base2 * altura2;
console.log(area2);

// Rectángulo 3
const base3 = 6;
const altura3 = 2;
const area3 = base3 * altura3;
console.log(area3);
```

### ✅ Con funciones (código reutilizable)

```javascript
function calcularArea(base, altura) {
  return base * altura;
}

console.log(calcularArea(5, 3));  // 15
console.log(calcularArea(8, 4));  // 32
console.log(calcularArea(6, 2));  // 12
```

**Ventajas de usar funciones**:
1. **Reutilización**: Escribe una vez, usa muchas veces
2. **Organización**: Código más limpio y fácil de entender
3. **Mantenimiento**: Si hay un error, lo corriges en un solo lugar
4. **Abstracción**: Ocultas la complejidad detrás de un nombre descriptivo

---

## Llamadas de Funciones Anidadas

Puedes llamar funciones dentro de otras funciones:

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

### Ejemplo más complejo:

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
// Precio: 100€
// Descuento 10%: 90€
// IVA 21%: 108.9€
```

---

## Renderizado Condicional

En desarrollo web, muchas veces necesitas mostrar u ocultar elementos según condiciones:

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

### Con operador ternario:

```javascript
function obtenerEstadoUsuario(estaLogueado) {
  return estaLogueado ? "Usuario activo" : "Usuario invitado";
}

console.log(obtenerEstadoUsuario(true));   // "Usuario activo"
console.log(obtenerEstadoUsuario(false));  // "Usuario invitado"
```

---

## Entonces... ¿Te gustó programar?

La programación es como aprender un nuevo idioma. Al principio puede parecer complicado, pero con práctica se vuelve cada vez más natural.

**Recuerda**:
- ✅ **Practica todos los días**: Aunque sea 15 minutos
- ✅ **Experimenta**: Cambia los valores, rompe el código, aprende de los errores
- ✅ **Lee código de otros**: Aprenderás diferentes formas de resolver problemas
- ✅ **Construye proyectos pequeños**: La mejor forma de aprender es creando cosas

### La pregunta fundamental: ¿Qué preguntar?

Programar es un 70% **hacer las preguntas correctas** y un 30% escribir código. Antes de escribir código, pregúntate:

1. **¿Qué problema estoy resolviendo?**
2. **¿Qué información necesito?** (variables)
3. **¿Qué decisiones debo tomar?** (condicionales)
4. **¿Necesito repetir algo?** (bucles)
5. **¿Puedo reutilizar esto?** (funciones)

---

## Ejercicios Prácticos

Ahora que conoces los conceptos básicos, es momento de practicar. En la carpeta `javascript-intro` encontrarás ejercicios incrementales que te ayudarán a dominar cada concepto.

**Estructura de los ejercicios**:
- `step1-variables.html`: Variables y tipos de datos
- `step2-functions.html`: Funciones básicas
- `step3-conditionals.html`: Condicionales y operadores lógicos
- `step4-loops.html`: Bucles
- `step5-final-project.html`: Proyecto integrador

**¡Adelante! 🚀**

---

## Cómo Trabajan Juntos HTML, CSS y JavaScript

### La Trinidad del Desarrollo Web

Cuando navegas por internet, tu navegador trabaja con **tres tecnologías fundamentales** que funcionan en perfecta armonía:

- **HTML** (HyperText Markup Language): La **estructura** - Los huesos
- **CSS** (Cascading Style Sheets): La **presentación** - La piel y ropa
- **JavaScript**: El **comportamiento** - Los músculos y cerebro

### Analogía: Construyendo una Casa

```
HTML  = Estructura (paredes, puertas, ventanas)
CSS   = Decoración (pintura, muebles, cortinas)
JS    = Funcionalidad (luz, agua, calefacción)
```

---

## Orden de Procesamiento del Navegador

### ¿Qué sucede cuando visitas una página web?

Cuando escribes una URL en el navegador (por ejemplo, `www.ejemplo.com`), ocurre la siguiente secuencia:

#### **1. Solicitud HTTP**
```
Navegador → Solicitud → Servidor
           ↓
     "Dame index.html"
```

#### **2. El Servidor Responde**
```
Servidor → Respuesta → Navegador
           ↓
   Archivo index.html
```

#### **3. Procesamiento del HTML** (Parsing)

El navegador lee el HTML **de arriba hacia abajo**, línea por línea:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página</title>
    <!-- 1. Primero lee el head -->
    <link rel="stylesheet" href="styles.css">
    <!-- 2. Encuentra el CSS y lo solicita al servidor -->
</head>
<body>
    <!-- 3. Luego lee el body -->
    <h1>Hola Mundo</h1>
    <button id="miBoton">Click aquí</button>
    
    <!-- 4. Encuentra el script al final -->
    <script src="app.js"></script>
</body>
</html>
```

#### **4. Construcción del DOM (Document Object Model)**

El navegador convierte el HTML en un **árbol de objetos**:

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

#### **5. Aplicación del CSS (Rendering)**

El navegador aplica los estilos CSS a cada elemento del DOM:

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

#### **6. Ejecución de JavaScript**

Finalmente, JavaScript se ejecuta y puede **modificar** el DOM y CSS:

```javascript
// app.js
const boton = document.getElementById('miBoton');
boton.addEventListener('click', function() {
    alert('¡Hola!');
});
```

---

## Estrategias de Carga de JavaScript

Existen **tres formas principales** de cargar JavaScript en tu página HTML:

### 1. Script al Final del Body (Tradicional)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Contenido</h1>
    <button id="btn">Click</button>
    
    <!-- ✅ Script al final -->
    <script src="app.js"></script>
</body>
</html>
```

**Ventajas**:
- Simple y funciona siempre
- HTML y CSS ya están listos cuando se ejecuta JS

**Desventajas**:
- El navegador no puede empezar a descargar el script hasta llegar al final del HTML

### 2. Script con `defer` (Recomendado)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página</title>
    <link rel="stylesheet" href="styles.css">
    <!-- ✅ Script con defer en el head -->
    <script src="app.js" defer></script>
</head>
<body>
    <h1>Contenido</h1>
    <button id="btn">Click</button>
</body>
</html>
```

**¿Qué hace `defer`?**
- El navegador descarga el script **en paralelo** mientras procesa el HTML
- El script se ejecuta **después** de que el DOM esté completamente construido
- Los scripts con `defer` se ejecutan en orden

**Timeline con `defer`:**
```
HTML parsing:    |===============================|
                                                ↓ DOM Ready
Script download: |=====|
                       ↓ (espera)
Script execute:                                 |==|
```

### 3. Script con `async`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página</title>
    <!-- Script con async -->
    <script src="analytics.js" async></script>
</head>
<body>
    <h1>Contenido</h1>
</body>
</html>
```

**¿Qué hace `async`?**
- El navegador descarga el script **en paralelo**
- El script se ejecuta **tan pronto como se descarga**
- No garantiza orden de ejecución

**Timeline con `async`:**
```
HTML parsing:    |===============================|
Script download: |=====|
                       ↓ (se ejecuta inmediatamente)
Script execute:        |==|
HTML parsing:              |==================|
```

**Usa `async` para**: Scripts independientes como Google Analytics, que no necesitan manipular el DOM

### 4. Módulos JavaScript (Moderno)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página</title>
    <!-- ✅ Módulo JavaScript -->
    <script type="module" src="app.js"></script>
</head>
<body>
    <h1>Contenido</h1>
    <button id="btn">Click</button>
</body>
</html>
```

**¿Qué hace `type="module"`?**
- Se comporta como `defer` por defecto (espera a que el DOM esté listo)
- Permite usar `import` y `export`
- Tiene su propio scope (no contamina el scope global)
- Se ejecuta en modo estricto automáticamente

**Ejemplo de módulo:**

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

### Comparación Visual

```
┌─────────────────────────────────────────────────────────────┐
│ Método         │ Descarga │ Ejecución │ Orden │ DOM Ready │
├─────────────────────────────────────────────────────────────┤
│ Final del body │ Bloqueante│ Inmediata │  ✅   │    ✅     │
│ defer          │ Paralela  │ Después   │  ✅   │    ✅     │
│ async          │ Paralela  │ Inmediata │  ❌   │    ❌     │
│ type="module"  │ Paralela  │ Después   │  ✅   │    ✅     │
└─────────────────────────────────────────────────────────────┘
```

**Recomendaciones**:
- **Principiantes**: Script al final del body
- **Producción moderna**: `defer` o `type="module"`
- **Scripts independientes**: `async`

---

## Conectando JavaScript con HTML

### Método 1: Script Interno

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

### Método 2: Script Externo (Recomendado)

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

## Asociando Funciones a Elementos HTML

### Opción 1: Atributo `onclick` (Inline) ❌

```html
<button onclick="saludar()">Saludar</button>

<script>
function saludar() {
    alert('¡Hola!');
}
</script>
```

**Ventajas**: Simple y directo  
**Desventajas**: Mezcla HTML con JavaScript (no es una buena práctica)

### Opción 2: `addEventListener` (Recomendado) ✅

```html
<button id="miBoton">Saludar</button>

<script>
// 1. Obtener referencia al elemento
const boton = document.getElementById('miBoton');

// 2. Asociar función al evento
boton.addEventListener('click', function() {
    alert('¡Hola!');
});
</script>
```

**Ventajas**: Separa HTML de JavaScript, más flexible  
**Desventajas**: Un poco más de código

### Opción 3: `addEventListener` con Función Externa

```html
<button id="miBoton">Saludar</button>

<script>
function saludar() {
    alert('¡Hola!');
}

const boton = document.getElementById('miBoton');
boton.addEventListener('click', saludar);  // ⚠️ Sin paréntesis
</script>
```

**⚠️ Importante**: Cuando pasas una función a `addEventListener`, **NO** uses paréntesis:

```javascript
// ❌ Incorrecto: se ejecuta inmediatamente
boton.addEventListener('click', saludar());

// ✅ Correcto: se ejecuta cuando haces click
boton.addEventListener('click', saludar);
```

---

## Manipulando el DOM con JavaScript

### Seleccionar Elementos HTML

```javascript
// Por ID (único)
const titulo = document.getElementById('titulo');

// Por clase (puede haber varios)
const items = document.getElementsByClassName('item');

// Por etiqueta
const parrafos = document.getElementsByTagName('p');

// Query selector (CSS selector) - Moderno ✅
const boton = document.querySelector('#miBoton');
const todosLosItems = document.querySelectorAll('.item');
```

### Modificar Contenido

```javascript
// Cambiar texto
elemento.textContent = 'Nuevo texto';

// Cambiar HTML interno
elemento.innerHTML = '<strong>Texto en negrita</strong>';

// Cambiar atributos
elemento.src = 'nueva-imagen.jpg';
elemento.href = 'https://ejemplo.com';
```

### Modificar Estilos CSS

```javascript
// Cambiar estilos individuales
elemento.style.color = 'red';
elemento.style.fontSize = '24px';
elemento.style.backgroundColor = 'yellow';

// Añadir/remover clases CSS (mejor práctica) ✅
elemento.classList.add('activo');
elemento.classList.remove('inactivo');
elemento.classList.toggle('visible');
```

### Crear y Añadir Elementos

```javascript
// Crear nuevo elemento
const nuevoParrafo = document.createElement('p');
nuevoParrafo.textContent = 'Soy un párrafo nuevo';

// Añadir al DOM
document.body.appendChild(nuevoParrafo);
```

---

## Eventos Comunes en JavaScript

### Eventos del Mouse

```javascript
elemento.addEventListener('click', function() {
    console.log('Click!');
});

elemento.addEventListener('dblclick', function() {
    console.log('Doble click!');
});

elemento.addEventListener('mouseenter', function() {
    console.log('Mouse entró');
});

elemento.addEventListener('mouseleave', function() {
    console.log('Mouse salió');
});
```

### Eventos del Teclado

```javascript
input.addEventListener('keydown', function(event) {
    console.log('Tecla presionada:', event.key);
});

input.addEventListener('keyup', function(event) {
    console.log('Tecla liberada:', event.key);
});
```

### Eventos de Formularios

```javascript
formulario.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir envío por defecto
    console.log('Formulario enviado');
});

input.addEventListener('input', function(event) {
    console.log('Valor actual:', event.target.value);
});

input.addEventListener('change', function(event) {
    console.log('Valor cambiado:', event.target.value);
});
```

---

## Ejemplo Completo: Lista de Tareas

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
// 1. Obtener referencias a elementos del DOM
const tareaInput = document.getElementById('tareaInput');
const agregarBtn = document.getElementById('agregarBtn');
const listaTareas = document.getElementById('listaTareas');

// 2. Función para agregar tarea
function agregarTarea() {
    const textoTarea = tareaInput.value.trim();
    
    // Validar que no esté vacío
    if (textoTarea === '') {
        alert('Por favor escribe una tarea');
        return;
    }
    
    // Crear elementos
    const li = document.createElement('li');
    const span = document.createElement('span');
    const btnEliminar = document.createElement('button');
    
    span.textContent = textoTarea;
    btnEliminar.textContent = 'Eliminar';
    btnEliminar.style.background = '#f44336';
    
    // Marcar como completada al hacer click
    span.addEventListener('click', function() {
        li.classList.toggle('completada');
    });
    
    // Eliminar tarea
    btnEliminar.addEventListener('click', function() {
        li.remove();
    });
    
    // Añadir al DOM
    li.appendChild(span);
    li.appendChild(btnEliminar);
    listaTareas.appendChild(li);
    
    // Limpiar input
    tareaInput.value = '';
    tareaInput.focus();
}

// 3. Asociar eventos
agregarBtn.addEventListener('click', agregarTarea);

// Permitir agregar con Enter
tareaInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        agregarTarea();
    }
});
```

---

## Orden de Ejecución: Resumen Visual

```
┌─────────────────────────────────────────┐
│ 1. Usuario escribe URL en navegador    │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 2. Navegador solicita HTML al servidor │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 3. Servidor envía index.html            │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 4. Navegador lee HTML línea por línea   │
│    - Construye el DOM                   │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 5. Encuentra <link> CSS                 │
│    - Solicita styles.css (paralelo)     │
│    - Aplica estilos al DOM              │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 6. Encuentra <script>                   │
│    • Sin atributos: bloquea y ejecuta   │
│    • defer: descarga en paralelo,       │
│      ejecuta después del DOM            │
│    • async: descarga y ejecuta ASAP     │
│    • type="module": como defer + ES6    │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 7. JavaScript manipula DOM y CSS        │
│    - Añade interactividad               │
└──────────────────┬──────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│ 8. Página completamente cargada         │
│    - Usuario puede interactuar          │
└─────────────────────────────────────────┘
```

---

## Buenas Prácticas

### 1. **Usa `defer` o `type="module"` en el head**

```html
<!-- ✅ MODERNO Y RECOMENDADO -->
<!DOCTYPE html>
<html>
<head>
    <script src="app.js" defer></script>
    <!-- o -->
    <script type="module" src="app.js"></script>
</head>
<body>
    <button id="btn">Click</button>
</body>
</html>
```

```html
<!-- ✅ TAMBIÉN FUNCIONA (tradicional) -->
<body>
    <button id="btn">Click</button>
    <script src="app.js"></script>
</body>
```

### 2. **Usa `addEventListener` en lugar de `onclick`**

```html
<!-- ❌ Evita esto -->
<button onclick="miFunction()">Click</button>

<!-- ✅ Mejor -->
<button id="miBtn">Click</button>
<script defer>
    document.getElementById('miBtn').addEventListener('click', miFunction);
</script>
```

### 3. **Separa HTML, CSS y JavaScript**

```
📁 mi-proyecto/
  ├── index.html      (Estructura)
  ├── styles.css      (Presentación)
  └── app.js          (Comportamiento)
```

### 4. **Usa IDs y Clases Semánticas**

```html
<!-- ✅ BIEN -->
<button id="btnAgregar" class="btn-primary">Agregar</button>

<!-- ❌ MAL -->
<button id="btn1" class="azul">Agregar</button>
```

### 5. **Valida Siempre que el Elemento Existe**

```javascript
const boton = document.getElementById('miBoton');

if (boton) {
    boton.addEventListener('click', function() {
        console.log('Click!');
    });
} else {
    console.error('Elemento no encontrado');
}
```

---

## Conclusión

Ahora entiendes cómo **HTML**, **CSS** y **JavaScript** trabajan juntos:

1. **HTML** crea la estructura (qué hay en la página)
2. **CSS** define la apariencia (cómo se ve)
3. **JavaScript** añade comportamiento (qué hace)

El navegador los procesa en orden, construye el DOM, aplica estilos y ejecuta scripts. Con las técnicas modernas como `defer` o `type="module"`, puedes colocar tus scripts en el `<head>` y el navegador se encargará de ejecutarlos en el momento correcto.

**Puntos clave**:
- ✅ Usa `defer` para scripts normales
- ✅ Usa `type="module"` para código moderno con import/export
- ✅ Usa `async` solo para scripts independientes
- ✅ Usa `addEventListener` en lugar de atributos inline
- ✅ Manipula el DOM solo después de que esté listo
