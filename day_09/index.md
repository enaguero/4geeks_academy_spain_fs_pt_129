# Día 9: Arrays en JavaScript

## ¿Por qué los Arrays Merecen una Lección Aparte?

Imagina que necesitas guardar los nombres de todos tus estudiantes. Podrías hacer esto:

```javascript
const estudiante1 = "Ana";
const estudiante2 = "Carlos";
const estudiante3 = "María";
const estudiante4 = "Juan";
const estudiante5 = "Laura";
// ... y así con 50 estudiantes? 😱
```

**¡Hay una forma mucho mejor!** Los **arrays** (arreglos o listas) te permiten guardar múltiples valores en una sola variable:

```javascript
const estudiantes = ["Ana", "Carlos", "María", "Juan", "Laura"];
```

### ¿Por qué son tan importantes?

1. **Organización**: Agrupa datos relacionados en un solo lugar
2. **Eficiencia**: Maneja cientos o miles de elementos fácilmente
3. **Iteración**: Puedes recorrer todos los elementos automáticamente
4. **Manipulación**: Añadir, quitar o modificar elementos es sencillo
5. **Ubicuidad**: Los arrays están en todas partes en programación

**Los arrays son fundamentales** porque:
- Tu lista de tareas: array
- Publicaciones en redes sociales: array
- Productos en un carrito de compra: array
- Resultados de búsqueda: array
- Comentarios en un post: array

---

## ¿Cómo Declarar un Array?

Hay dos formas de crear arrays en JavaScript:

### Forma 1: Literal de Array (Recomendada) ✅

```javascript
const frutas = ["manzana", "banana", "naranja"];
const numeros = [1, 2, 3, 4, 5];
const mixto = ["texto", 42, true, null];
const vacio = [];
```

### Forma 2: Constructor Array (Menos común)

```javascript
const colores = new Array("rojo", "azul", "verde");
const numerosVacios = new Array(5);  // Crea array con 5 espacios vacíos
```

**Recomendación**: Usa siempre la forma literal `[]` - es más corta, clara y rápida.

### Tipos de Datos en Arrays

Los arrays pueden contener cualquier tipo de dato, incluso **mezclas**:

```javascript
const arrayMixto = [
    "texto",           // String
    42,                // Number
    true,              // Boolean
    null,              // Null
    undefined,         // Undefined
    [1, 2, 3],         // Array dentro de array
    { nombre: "Ana" }  // Objeto
];
```

---

## Índices: La Clave para Entender Arrays

### ¿Qué es un Índice?

Un **índice** es la **posición** de un elemento dentro del array. **¡IMPORTANTE!** Los índices empiezan en **0**, no en 1.

```javascript
const frutas = ["manzana", "banana", "naranja", "uva"];
//              ↓           ↓         ↓          ↓
//           índice 0    índice 1  índice 2   índice 3
```

### Visualización Completa

```
┌───────────┬──────────┬──────────┬──────────┬──────────┐
│ Elemento  │ manzana  │  banana  │ naranja  │   uva    │
├───────────┼──────────┼──────────┼──────────┼──────────┤
│ Índice    │    0     │    1     │    2     │    3     │
├───────────┼──────────┼──────────┼──────────┼──────────┤
│ Posición  │ 1°       │ 2°       │ 3°       │ 4°       │
└───────────┴──────────┴──────────┴──────────┴──────────┘
```

### ⚠️ Diferencia CLAVE: Índice vs Posición

```javascript
const letras = ["A", "B", "C", "D"];
```

| Concepto | "A" | "B" | "C" | "D" |
|----------|-----|-----|-----|-----|
| **Índice** (programación) | 0 | 1 | 2 | 3 |
| **Posición** (humanos) | 1° | 2° | 3° | 4° |

**Recuerda**: 
- **Índice 0** = Primer elemento
- **Índice 1** = Segundo elemento
- **Índice 2** = Tercer elemento
- Y así sucesivamente...

### Ejemplos Prácticos

```javascript
const dias = ["lunes", "martes", "miércoles", "jueves", "viernes"];

console.log("Índice 0:", dias[0]);       // "lunes" - primer día
console.log("Índice 2:", dias[2]);       // "miércoles" - tercer día
console.log("Índice 4:", dias[4]);       // "viernes" - quinto día

// Posición NO es lo mismo que índice
console.log("El 1er día está en el índice:", 0);
console.log("El 3er día está en el índice:", 2);
```

---

## Acceder a Elementos del Array

Para obtener un elemento específico, usamos **corchetes `[]`** con el índice:

```javascript
const colores = ["rojo", "azul", "verde", "amarillo"];

// Acceder por índice
console.log(colores[0]);  // "rojo"    (primer elemento)
console.log(colores[1]);  // "azul"    (segundo elemento)
console.log(colores[2]);  // "verde"   (tercer elemento)
console.log(colores[3]);  // "amarillo" (cuarto elemento)

// ¿Qué pasa si accedemos a un índice que no existe?
console.log(colores[10]); // undefined (no hay elemento en ese índice)
```

### Acceder al Primer Elemento

```javascript
const animales = ["perro", "gato", "loro", "pez"];

const primerAnimal = animales[0];
console.log(primerAnimal);  // "perro"
```

### Acceder al Último Elemento

Hay **dos formas** de obtener el último elemento:

#### Opción 1: Usando `length - 1`

```javascript
const numeros = [10, 20, 30, 40, 50];

const ultimoNumero = numeros[numeros.length - 1];
console.log(ultimoNumero);  // 50
```

**¿Por qué `length - 1`?**
- `numeros.length` = 5 (cantidad total de elementos)
- Los índices van del 0 al 4
- El último índice es: 5 - 1 = 4
- `numeros[4]` = 50

#### Opción 2: Usando `at(-1)` (Moderno) ✨

```javascript
const numeros = [10, 20, 30, 40, 50];

const ultimoNumero = numeros.at(-1);
console.log(ultimoNumero);  // 50

// También puedes acceder desde el final
console.log(numeros.at(-2));  // 40 (penúltimo)
console.log(numeros.at(-3));  // 30 (antepenúltimo)
```

### Comparación Visual

```javascript
const letras = ["A", "B", "C", "D", "E"];
//             ↑               ↑         ↑
//          índice 0         índice 2  índice 4 (último)

// Primer elemento
console.log(letras[0]);              // "A"
console.log(letras.at(0));           // "A"

// Último elemento
console.log(letras[letras.length - 1]);  // "E"
console.log(letras.at(-1));              // "E" ✅ Más simple!
```

### Tabla Resumen: Acceder a Elementos

| Qué quieres | Sintaxis | Ejemplo |
|-------------|----------|---------|
| **Primer elemento** | `array[0]` | `frutas[0]` |
| **Segundo elemento** | `array[1]` | `frutas[1]` |
| **Elemento específico** | `array[indice]` | `frutas[3]` |
| **Último elemento** | `array[array.length - 1]` | `frutas[frutas.length - 1]` |
| **Último elemento (moderno)** | `array.at(-1)` | `frutas.at(-1)` ✅ |
| **Penúltimo elemento** | `array.at(-2)` | `frutas.at(-2)` |

---

## Actualizar Elementos del Array

Puedes **modificar** elementos existentes asignándoles un nuevo valor:

```javascript
const frutas = ["manzana", "banana", "naranja"];

console.log(frutas);  // ["manzana", "banana", "naranja"]

// Cambiar el segundo elemento (índice 1)
frutas[1] = "fresa";

console.log(frutas);  // ["manzana", "fresa", "naranja"]
```

### Ejemplo Práctico: Actualizar Calificaciones

```javascript
const calificaciones = [85, 90, 78, 92];

console.log("Antes:", calificaciones);  // [85, 90, 78, 92]

// El profesor corrigió la tercera calificación (índice 2)
calificaciones[2] = 88;

console.log("Después:", calificaciones);  // [85, 90, 88, 92]
```

### ⚠️ Arrays con `const`

Aunque declares un array con `const`, **puedes modificar sus elementos**:

```javascript
const numeros = [1, 2, 3];

numeros[0] = 100;  // ✅ Funciona
console.log(numeros);  // [100, 2, 3]

numeros = [4, 5, 6];  // ❌ Error: no puedes reasignar el array completo
```

**¿Por qué?**
- `const` protege la **referencia** del array (no puedes asignarle un array nuevo)
- NO protege el **contenido** del array (puedes cambiar sus elementos)

---

## Añadir Elementos: Función `push()`

La función `push()` **añade uno o más elementos al final** del array.

### Sintaxis

```javascript
array.push(elemento1, elemento2, ...);
```

### Ejemplo Básico

```javascript
const tareas = ["estudiar", "hacer ejercicio"];

console.log(tareas);  // ["estudiar", "hacer ejercicio"]

// Añadir una tarea
tareas.push("leer libro");

console.log(tareas);  // ["estudiar", "hacer ejercicio", "leer libro"]
```

### Añadir Múltiples Elementos

```javascript
const numeros = [1, 2, 3];

numeros.push(4, 5, 6);

console.log(numeros);  // [1, 2, 3, 4, 5, 6]
```

### Valor de Retorno

`push()` devuelve la **nueva longitud** del array:

```javascript
const frutas = ["manzana"];

const nuevaLongitud = frutas.push("banana", "naranja");

console.log(nuevaLongitud);  // 3
console.log(frutas);         // ["manzana", "banana", "naranja"]
```

### Ejemplo Práctico: Carrito de Compras

```javascript
const carrito = [];

console.log("Carrito vacío:", carrito);  // []

carrito.push("Laptop");
console.log("Carrito:", carrito);  // ["Laptop"]

carrito.push("Mouse", "Teclado");
console.log("Carrito:", carrito);  // ["Laptop", "Mouse", "Teclado"]

carrito.push("Monitor");
console.log("Carrito final:", carrito);  // ["Laptop", "Mouse", "Teclado", "Monitor"]
```

---

## Eliminar Elementos: Función `pop()`

La función `pop()` **elimina y devuelve el último elemento** del array.

### Sintaxis

```javascript
const elementoEliminado = array.pop();
```

### Ejemplo Básico

```javascript
const frutas = ["manzana", "banana", "naranja"];

console.log("Antes:", frutas);  // ["manzana", "banana", "naranja"]

const frutaEliminada = frutas.pop();

console.log("Eliminada:", frutaEliminada);  // "naranja"
console.log("Después:", frutas);             // ["manzana", "banana"]
```

### Pop en Array Vacío

```javascript
const vacio = [];
const resultado = vacio.pop();

console.log(resultado);  // undefined
console.log(vacio);      // []
```

### Ejemplo Práctico: Pila de Libros

```javascript
const pilaLibros = ["Libro 1", "Libro 2", "Libro 3", "Libro 4"];

console.log("Pila:", pilaLibros);  // ["Libro 1", "Libro 2", "Libro 3", "Libro 4"]

// Tomar el libro de arriba
const libro = pilaLibros.pop();
console.log("Tomé:", libro);       // "Libro 4"
console.log("Pila:", pilaLibros);  // ["Libro 1", "Libro 2", "Libro 3"]

// Tomar otro libro
const otroLibro = pilaLibros.pop();
console.log("Tomé:", otroLibro);   // "Libro 3"
console.log("Pila:", pilaLibros);  // ["Libro 1", "Libro 2"]
```

---

## Añadir/Eliminar desde el Inicio

### `unshift()`: Añadir al Inicio

Añade uno o más elementos al **principio** del array:

```javascript
const numeros = [2, 3, 4];

console.log("Antes:", numeros);  // [2, 3, 4]

numeros.unshift(1);

console.log("Después:", numeros);  // [1, 2, 3, 4]
```

### Añadir Múltiples Elementos al Inicio

```javascript
const letras = ["C", "D"];

letras.unshift("A", "B");

console.log(letras);  // ["A", "B", "C", "D"]
```

### `shift()`: Eliminar del Inicio

Elimina y devuelve el **primer elemento** del array:

```javascript
const tareas = ["lavar platos", "estudiar", "ejercicio"];

console.log("Antes:", tareas);  // ["lavar platos", "estudiar", "ejercicio"]

const tareaCompletada = tareas.shift();

console.log("Completada:", tareaCompletada);  // "lavar platos"
console.log("Después:", tareas);              // ["estudiar", "ejercicio"]
```

### Comparación Visual: push vs unshift / pop vs shift

```javascript
const array = [2, 3, 4];

// AÑADIR
array.push(5);     // [2, 3, 4, 5]   → Añade al FINAL
array.unshift(1);  // [1, 2, 3, 4, 5] → Añade al INICIO

// ELIMINAR
array.pop();       // [1, 2, 3, 4]   → Elimina del FINAL
array.shift();     // [2, 3, 4]      → Elimina del INICIO
```

### Tabla Resumen: Métodos de Modificación

| Método | Qué hace | Dónde actúa | Retorna | Ejemplo |
|--------|----------|-------------|---------|---------|
| **push()** | Añade elemento(s) | Final | Nueva longitud | `arr.push(5)` |
| **pop()** | Elimina elemento | Final | Elemento eliminado | `arr.pop()` |
| **unshift()** | Añade elemento(s) | Inicio | Nueva longitud | `arr.unshift(1)` |
| **shift()** | Elimina elemento | Inicio | Elemento eliminado | `arr.shift()` |

---

## Recorrer un Array (Looping)

Hay varias formas de recorrer (iterar) todos los elementos de un array.

### Método 1: `for` Tradicional

```javascript
const frutas = ["manzana", "banana", "naranja"];

for (let i = 0; i < frutas.length; i++) {
    console.log(`Índice ${i}: ${frutas[i]}`);
}

// Salida:
// Índice 0: manzana
// Índice 1: banana
// Índice 2: naranja
```

**Ventajas**: Tienes acceso al índice explícitamente.

### Método 2: `for...of` (Recomendado para Arrays) ✅

```javascript
const frutas = ["manzana", "banana", "naranja"];

for (const fruta of frutas) {
    console.log(fruta);
}

// Salida:
// manzana
// banana
// naranja
```

**Ventajas**: Sintaxis más simple y clara.

### Método 3: `forEach()` (Moderno)

```javascript
const frutas = ["manzana", "banana", "naranja"];

frutas.forEach(function(fruta, indice) {
    console.log(`${indice}: ${fruta}`);
});

// Salida:
// 0: manzana
// 1: banana
// 2: naranja
```

**Con arrow function** (más moderno):

```javascript
frutas.forEach((fruta, indice) => {
    console.log(`${indice}: ${fruta}`);
});
```

### Ejemplo Práctico: Sumar Todos los Números

```javascript
const numeros = [10, 20, 30, 40, 50];
let suma = 0;

for (const numero of numeros) {
    suma += numero;
}

console.log("Suma total:", suma);  // 150
```

### Ejemplo Práctico: Filtrar Elementos

```javascript
const calificaciones = [85, 92, 78, 95, 88, 76];

console.log("Calificaciones aprobadas (>= 80):");

for (const nota of calificaciones) {
    if (nota >= 80) {
        console.log(nota);
    }
}

// Salida:
// 85
// 92
// 95
// 88
```

---

## `for...in` vs `for...of`

### ⚠️ Diferencia IMPORTANTE

```javascript
const colores = ["rojo", "azul", "verde"];

// for...in → Recorre ÍNDICES (no recomendado para arrays)
for (const indice in colores) {
    console.log(indice);  // "0", "1", "2" (strings!)
}

// for...of → Recorre VALORES ✅ (recomendado)
for (const color of colores) {
    console.log(color);  // "rojo", "azul", "verde"
}
```

### Cuándo Usar Cada Uno

| Loop | Para | Itera sobre | Ejemplo |
|------|------|-------------|---------|
| **for...of** | Arrays | Valores | `for (const item of array)` ✅ |
| **for...in** | Objetos | Propiedades (keys) | `for (const key in objeto)` ✅ |

**Recomendación**: Para arrays, usa **`for...of`**, NO `for...in`.

### Ejemplo con Objeto (for...in)

```javascript
const persona = {
    nombre: "Ana",
    edad: 25,
    ciudad: "Madrid"
};

for (const propiedad in persona) {
    console.log(`${propiedad}: ${persona[propiedad]}`);
}

// Salida:
// nombre: Ana
// edad: 25
// ciudad: Madrid
```

---

## Eliminar Elementos Específicos

### Método 1: `splice()` (Modifica el array original)

`splice()` puede **añadir, eliminar o reemplazar** elementos en cualquier posición.

#### Sintaxis

```javascript
array.splice(inicio, cantidadAEliminar, elementoNuevo1, elementoNuevo2, ...);
```

#### Eliminar Elementos

```javascript
const frutas = ["manzana", "banana", "naranja", "uva", "sandía"];
//             ↓           ↓         ↓          ↓     ↓
//          índice 0    índice 1  índice 2   índice 3  índice 4

// Eliminar "naranja" (índice 2) - eliminar 1 elemento
frutas.splice(2, 1);

console.log(frutas);  // ["manzana", "banana", "uva", "sandía"]
```

#### Eliminar Varios Elementos

```javascript
const numeros = [1, 2, 3, 4, 5, 6];

// Desde índice 2, eliminar 3 elementos
numeros.splice(2, 3);

console.log(numeros);  // [1, 2, 6]
```

#### Reemplazar Elementos

```javascript
const dias = ["lunes", "martes", "miércoles", "jueves"];

// Desde índice 1, eliminar 2 elementos y añadir "LUNES", "MARTES"
dias.splice(1, 2, "MARTES", "MIÉRCOLES");

console.log(dias);  // ["lunes", "MARTES", "MIÉRCOLES", "jueves"]
```

#### Añadir Sin Eliminar

```javascript
const letras = ["A", "B", "D"];

// En índice 2, eliminar 0 elementos y añadir "C"
letras.splice(2, 0, "C");

console.log(letras);  // ["A", "B", "C", "D"]
```

### Método 2: `slice()` (NO modifica el array original)

`slice()` **crea una copia** de una porción del array.

#### Sintaxis

```javascript
const nuevoArray = array.slice(inicio, fin);
```

- `inicio`: Índice donde empezar (incluido)
- `fin`: Índice donde terminar (**NO incluido**)

#### Ejemplos

```javascript
const frutas = ["manzana", "banana", "naranja", "uva", "sandía"];
//             ↓           ↓         ↓          ↓     ↓
//          índice 0    índice 1  índice 2   índice 3  índice 4

// Desde índice 1 hasta 3 (NO incluye 3)
const algunasFrutas = frutas.slice(1, 3);

console.log(algunasFrutas);  // ["banana", "naranja"]
console.log(frutas);         // ["manzana", "banana", "naranja", "uva", "sandía"] (sin cambios)
```

#### Copiar Todo el Array

```javascript
const original = [1, 2, 3];
const copia = original.slice();

console.log(copia);  // [1, 2, 3]

copia.push(4);
console.log(original);  // [1, 2, 3] (original no cambió)
console.log(copia);     // [1, 2, 3, 4]
```

#### Desde un Índice hasta el Final

```javascript
const numeros = [10, 20, 30, 40, 50];

const ultimos = numeros.slice(2);  // Desde índice 2 hasta el final

console.log(ultimos);  // [30, 40, 50]
```

#### Con Índices Negativos

```javascript
const letras = ["A", "B", "C", "D", "E"];

const ultimas = letras.slice(-2);  // Últimos 2 elementos

console.log(ultimas);  // ["D", "E"]
```

### Tabla Comparativa: `splice()` vs `slice()`

| Aspecto | `splice()` | `slice()` |
|---------|------------|-----------|
| **Modifica original** | ✅ Sí | ❌ No |
| **Devuelve** | Elementos eliminados | Nueva copia |
| **Para** | Modificar array | Copiar porción |
| **Puede añadir** | ✅ Sí | ❌ No |
| **Sintaxis** | `splice(inicio, cantidad, ...elementos)` | `slice(inicio, fin)` |

### Ejemplo Completo

```javascript
const tareas = ["dormir", "estudiar", "comer", "ejercicio", "leer"];

console.log("Original:", tareas);

// slice: copiar elementos 1 al 3 (NO modifica original)
const algunas = tareas.slice(1, 3);
console.log("Copia (slice):", algunas);  // ["estudiar", "comer"]
console.log("Original:", tareas);        // Sin cambios

// splice: eliminar "comer" (índice 2)
tareas.splice(2, 1);
console.log("Después de splice:", tareas);  // ["dormir", "estudiar", "ejercicio", "leer"]

// splice: añadir "trabajar" en índice 2
tareas.splice(2, 0, "trabajar");
console.log("Después de añadir:", tareas);  // ["dormir", "estudiar", "trabajar", "ejercicio", "leer"]
```

---

## Ordenar Arrays: `sort()`

El método `sort()` ordena los elementos de un array **alfabéticamente** por defecto.

### Ordenar Strings

```javascript
const frutas = ["naranja", "manzana", "uva", "banana"];

frutas.sort();

console.log(frutas);  // ["banana", "manzana", "naranja", "uva"]
```

### ⚠️ Problema con Números

```javascript
const numeros = [10, 5, 40, 25, 1000, 1];

numeros.sort();

console.log(numeros);  // [1, 10, 1000, 25, 40, 5] ❌ ¡Incorrecto!
```

**¿Por qué?** `sort()` convierte los números a strings y los ordena alfabéticamente: "1", "10", "1000", "25", etc.

### Solución: Función de Comparación

Para ordenar números correctamente, usa una **función de comparación**:

```javascript
const numeros = [10, 5, 40, 25, 1000, 1];

// Orden ascendente (menor a mayor)
numeros.sort(function(a, b) {
    return a - b;
});

console.log(numeros);  // [1, 5, 10, 25, 40, 1000] ✅
```

**Con arrow function** (más corto):

```javascript
numeros.sort((a, b) => a - b);  // Ascendente
```

### Orden Descendente

```javascript
const numeros = [10, 5, 40, 25, 1000, 1];

// Orden descendente (mayor a menor)
numeros.sort((a, b) => b - a);

console.log(numeros);  // [1000, 40, 25, 10, 5, 1]
```

### Cómo Funciona la Función de Comparación

```javascript
function comparar(a, b) {
    // Si devuelve negativo: a va antes que b
    // Si devuelve positivo: b va antes que a
    // Si devuelve 0: no se cambia el orden
    return a - b;
}
```

### Ordenar Objetos por Propiedad

```javascript
const estudiantes = [
    { nombre: "Ana", edad: 22 },
    { nombre: "Carlos", edad: 19 },
    { nombre: "María", edad: 25 }
];

// Ordenar por edad
estudiantes.sort((a, b) => a.edad - b.edad);

console.log(estudiantes);
// [
//   { nombre: "Carlos", edad: 19 },
//   { nombre: "Ana", edad: 22 },
//   { nombre: "María", edad: 25 }
// ]
```

### Orden Alfabético Inverso

```javascript
const nombres = ["Carlos", "Ana", "María", "Beatriz"];

nombres.sort();  // Orden alfabético normal
console.log(nombres);  // ["Ana", "Beatriz", "Carlos", "María"]

nombres.reverse();  // Invertir el orden
console.log(nombres);  // ["María", "Carlos", "Beatriz", "Ana"]
```

### Tabla Resumen: `sort()`

| Tipo de datos | Sintaxis | Orden |
|---------------|----------|-------|
| **Strings** | `array.sort()` | Alfabético A-Z |
| **Strings inverso** | `array.sort().reverse()` | Alfabético Z-A |
| **Números ascendente** | `array.sort((a, b) => a - b)` | Menor a mayor |
| **Números descendente** | `array.sort((a, b) => b - a)` | Mayor a menor |
| **Objetos por propiedad** | `array.sort((a, b) => a.prop - b.prop)` | Según propiedad |

---

## Métodos Útiles de Arrays

### `length`: Obtener Longitud

```javascript
const frutas = ["manzana", "banana", "naranja"];

console.log(frutas.length);  // 3
```

### `includes()`: Verificar si Existe

```javascript
const numeros = [1, 2, 3, 4, 5];

console.log(numeros.includes(3));   // true
console.log(numeros.includes(10));  // false
```

### `indexOf()`: Encontrar Índice

```javascript
const colores = ["rojo", "azul", "verde", "amarillo"];

console.log(colores.indexOf("verde"));    // 2
console.log(colores.indexOf("naranja"));  // -1 (no existe)
```

### `join()`: Convertir a String

```javascript
const palabras = ["Hola", "mundo", "desde", "JavaScript"];

const frase = palabras.join(" ");
console.log(frase);  // "Hola mundo desde JavaScript"

const conComas = palabras.join(", ");
console.log(conComas);  // "Hola, mundo, desde, JavaScript"
```

### `concat()`: Unir Arrays

```javascript
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const array3 = [7, 8, 9];

const combinado = array1.concat(array2, array3);
console.log(combinado);  // [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### `reverse()`: Invertir Orden

```javascript
const numeros = [1, 2, 3, 4, 5];

numeros.reverse();
console.log(numeros);  // [5, 4, 3, 2, 1]
```

### `find()`: Encontrar Primer Elemento que Cumple Condición

```javascript
const numeros = [5, 12, 8, 130, 44];

const encontrado = numeros.find(num => num > 10);
console.log(encontrado);  // 12 (primer número mayor a 10)
```

### `filter()`: Filtrar Elementos

```javascript
const numeros = [5, 12, 8, 130, 44];

const mayoresA10 = numeros.filter(num => num > 10);
console.log(mayoresA10);  // [12, 130, 44]
```

### `map()`: Transformar Elementos

```javascript
const numeros = [1, 2, 3, 4, 5];

const duplicados = numeros.map(num => num * 2);
console.log(duplicados);  // [2, 4, 6, 8, 10]
```

### `reduce()`: Reducir a un Solo Valor

```javascript
const numeros = [1, 2, 3, 4, 5];

const suma = numeros.reduce((acumulador, num) => acumulador + num, 0);
console.log(suma);  // 15
```

---

## Tabla Resumen: Métodos de Arrays

| Método | Qué hace | Modifica original | Ejemplo |
|--------|----------|-------------------|---------|
| **push()** | Añade al final | ✅ Sí | `arr.push(5)` |
| **pop()** | Elimina del final | ✅ Sí | `arr.pop()` |
| **unshift()** | Añade al inicio | ✅ Sí | `arr.unshift(1)` |
| **shift()** | Elimina del inicio | ✅ Sí | `arr.shift()` |
| **splice()** | Añade/elimina/reemplaza | ✅ Sí | `arr.splice(2, 1)` |
| **slice()** | Copia porción | ❌ No | `arr.slice(1, 3)` |
| **sort()** | Ordena elementos | ✅ Sí | `arr.sort((a,b) => a-b)` |
| **reverse()** | Invierte orden | ✅ Sí | `arr.reverse()` |
| **concat()** | Une arrays | ❌ No | `arr1.concat(arr2)` |
| **join()** | Convierte a string | ❌ No | `arr.join(", ")` |
| **includes()** | Verifica si existe | ❌ No | `arr.includes(3)` |
| **indexOf()** | Encuentra índice | ❌ No | `arr.indexOf("rojo")` |
| **find()** | Primer elemento que cumple | ❌ No | `arr.find(x => x > 10)` |
| **filter()** | Filtra elementos | ❌ No | `arr.filter(x => x > 10)` |
| **map()** | Transforma elementos | ❌ No | `arr.map(x => x * 2)` |
| **forEach()** | Itera elementos | ❌ No | `arr.forEach(x => {...})` |

---

## Ejercicios Prácticos

### Ejercicio 1: Lista de Compras

Crea un array vacío `listaCompras` y:
1. Añade "leche", "pan" y "huevos"
2. Añade "manzanas" al inicio
3. Elimina el último elemento
4. Imprime el array completo

```javascript
const listaCompras = [];

// Tu código aquí
```

<details>
<summary>Ver solución</summary>

```javascript
const listaCompras = [];

listaCompras.push("leche", "pan", "huevos");
console.log(listaCompras);  // ["leche", "pan", "huevos"]

listaCompras.unshift("manzanas");
console.log(listaCompras);  // ["manzanas", "leche", "pan", "huevos"]

listaCompras.pop();
console.log(listaCompras);  // ["manzanas", "leche", "pan"]
```
</details>

### Ejercicio 2: Calificaciones

Dado el array `calificaciones = [78, 92, 85, 88, 95, 73]`:
1. Imprime la primera calificación
2. Imprime la última calificación
3. Calcula el promedio
4. Encuentra cuántas calificaciones son mayores a 80

```javascript
const calificaciones = [78, 92, 85, 88, 95, 73];

// Tu código aquí
```

<details>
<summary>Ver solución</summary>

```javascript
const calificaciones = [78, 92, 85, 88, 95, 73];

// 1. Primera calificación
console.log("Primera:", calificaciones[0]);  // 78

// 2. Última calificación
console.log("Última:", calificaciones[calificaciones.length - 1]);  // 73
// o usando at():
console.log("Última:", calificaciones.at(-1));  // 73

// 3. Promedio
let suma = 0;
for (const nota of calificaciones) {
    suma += nota;
}
const promedio = suma / calificaciones.length;
console.log("Promedio:", promedio);  // 85.16...

// 4. Mayores a 80
const mayoresA80 = calificaciones.filter(nota => nota > 80);
console.log("Mayores a 80:", mayoresA80.length);  // 4
```
</details>

### Ejercicio 3: Nombres en Orden

Dado `nombres = ["Carlos", "Ana", "Beatriz", "David"]`:
1. Ordena alfabéticamente
2. Imprime en orden inverso
3. Encuentra el índice de "Beatriz"

```javascript
const nombres = ["Carlos", "Ana", "Beatriz", "David"];

// Tu código aquí
```

<details>
<summary>Ver solución</summary>

```javascript
const nombres = ["Carlos", "Ana", "Beatriz", "David"];

// 1. Ordenar alfabéticamente
nombres.sort();
console.log("Ordenado:", nombres);  // ["Ana", "Beatriz", "Carlos", "David"]

// 2. Orden inverso
nombres.reverse();
console.log("Inverso:", nombres);  // ["David", "Carlos", "Beatriz", "Ana"]

// 3. Índice de "Beatriz"
const indice = nombres.indexOf("Beatriz");
console.log("Índice de Beatriz:", indice);  // 2
```
</details>

### Ejercicio 4: Filtrar Números Pares

Dado `numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, crea un nuevo array solo con números pares.

```javascript
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Tu código aquí
```

<details>
<summary>Ver solución</summary>

```javascript
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const pares = numeros.filter(num => num % 2 === 0);
console.log(pares);  // [2, 4, 6, 8, 10]

// Alternativa con for...of
const paresAlt = [];
for (const num of numeros) {
    if (num % 2 === 0) {
        paresAlt.push(num);
    }
}
console.log(paresAlt);  // [2, 4, 6, 8, 10]
```
</details>

### Ejercicio 5: Duplicar Valores

Dado `precios = [10, 20, 30, 40]`, crea un nuevo array con todos los precios duplicados.

```javascript
const precios = [10, 20, 30, 40];

// Tu código aquí
```

<details>
<summary>Ver solución</summary>

```javascript
const precios = [10, 20, 30, 40];

const duplicados = precios.map(precio => precio * 2);
console.log(duplicados);  // [20, 40, 60, 80]
```
</details>

---

## Proyecto Integrador: Gestor de Estudiantes

Crea un sistema para gestionar estudiantes con las siguientes funcionalidades:

```javascript
const estudiantes = [];

// Funciones a implementar:

function agregarEstudiante(nombre) {
    // Añadir estudiante al array
}

function eliminarEstudiante(nombre) {
    // Encontrar y eliminar estudiante
}

function buscarEstudiante(nombre) {
    // Buscar si existe el estudiante
}

function listarEstudiantes() {
    // Imprimir todos los estudiantes
}

function estudiantesOrdenados() {
    // Devolver estudiantes en orden alfabético
}

// Pruebas
agregarEstudiante("Ana");
agregarEstudiante("Carlos");
agregarEstudiante("Beatriz");
listarEstudiantes();
console.log("¿Está Carlos?", buscarEstudiante("Carlos"));
eliminarEstudiante("Carlos");
console.log("Ordenados:", estudiantesOrdenados());
```

<details>
<summary>Ver solución completa</summary>

```javascript
const estudiantes = [];

function agregarEstudiante(nombre) {
    estudiantes.push(nombre);
    console.log(`✅ ${nombre} agregado`);
}

function eliminarEstudiante(nombre) {
    const indice = estudiantes.indexOf(nombre);
    if (indice !== -1) {
        estudiantes.splice(indice, 1);
        console.log(`❌ ${nombre} eliminado`);
    } else {
        console.log(`⚠️ ${nombre} no encontrado`);
    }
}

function buscarEstudiante(nombre) {
    return estudiantes.includes(nombre);
}

function listarEstudiantes() {
    console.log("\n📋 Lista de estudiantes:");
    estudiantes.forEach((estudiante, indice) => {
        console.log(`${indice + 1}. ${estudiante}`);
    });
}

function estudiantesOrdenados() {
    return [...estudiantes].sort();  // Copia para no modificar original
}

// Pruebas
agregarEstudiante("Ana");
agregarEstudiante("Carlos");
agregarEstudiante("Beatriz");
agregarEstudiante("David");

listarEstudiantes();
// 📋 Lista de estudiantes:
// 1. Ana
// 2. Carlos
// 3. Beatriz
// 4. David

console.log("¿Está Carlos?", buscarEstudiante("Carlos"));  // true
console.log("¿Está María?", buscarEstudiante("María"));    // false

eliminarEstudiante("Carlos");  // ❌ Carlos eliminado
eliminarEstudiante("Pedro");   // ⚠️ Pedro no encontrado

console.log("Ordenados:", estudiantesOrdenados());  // ["Ana", "Beatriz", "David"]

listarEstudiantes();
// 📋 Lista de estudiantes:
// 1. Ana
// 2. Beatriz
// 3. David
```
</details>

---

## Conclusión

Los **arrays** son una de las estructuras de datos más importantes en JavaScript. Dominarlos te permitirá:

✅ Gestionar colecciones de datos eficientemente  
✅ Crear aplicaciones dinámicas e interactivas  
✅ Manipular listas (tareas, productos, usuarios, etc.)  
✅ Procesar grandes cantidades de información  
✅ Prepararte para conceptos más avanzados (objetos, APIs, etc.)

### Puntos Clave para Recordar

1. **Los índices empiezan en 0** - El primer elemento está en `array[0]`
2. **Índice ≠ Posición** - El índice 0 es la posición 1
3. **Último elemento**: `array[array.length - 1]` o `array.at(-1)`
4. **`push()` / `pop()`**: Añadir/eliminar del final
5. **`unshift()` / `shift()`**: Añadir/eliminar del inicio
6. **`splice()`**: Modifica el original
7. **`slice()`**: Crea una copia
8. **`for...of`**: La mejor forma de recorrer arrays
9. **`sort()`**: Usa función de comparación para números
10. **Métodos avanzados**: `map()`, `filter()`, `reduce()`

### Próximos Pasos

Ahora que dominas los arrays:
1. Practica con los ejercicios diariamente
2. Combina arrays con funciones
3. Explora arrays de objetos
4. Aprende sobre arrays multidimensionales
5. Prepárate para trabajar con APIs (que devuelven arrays)

**¡Sigue practicando! 🚀** Los arrays son fundamentales en el desarrollo web moderno.

---

## Recursos Adicionales

- **MDN Web Docs - Arrays**: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array
- **JavaScript.info - Arrays**: https://javascript.info/array
- **Visualizador de métodos de arrays**: https://arrayexplorer.netlify.app/

---

## Cheat Sheet: Arrays en JavaScript

```javascript
// CREAR
const array = [1, 2, 3];
const vacio = [];

// ACCEDER
array[0]              // Primer elemento
array[array.length-1] // Último elemento
array.at(-1)          // Último elemento (moderno)

// MODIFICAR
array[0] = 100;       // Cambiar elemento

// AÑADIR
array.push(4);        // Final: [1, 2, 3, 4]
array.unshift(0);     // Inicio: [0, 1, 2, 3, 4]

// ELIMINAR
array.pop();          // Elimina del final
array.shift();        // Elimina del inicio
array.splice(2, 1);   // Elimina en índice específico

// RECORRER
for (const item of array) { ... }
array.forEach(item => { ... })

// ORDENAR
array.sort((a, b) => a - b);  // Números ascendente
array.reverse();               // Invertir

// BUSCAR
array.includes(3);    // ¿Existe?
array.indexOf(3);     // ¿En qué índice?
array.find(x => ...)  // Primer elemento que cumple

// FILTRAR/TRANSFORMAR
array.filter(x => x > 2);  // Filtrar
array.map(x => x * 2);     // Transformar
array.slice(1, 3);         // Copiar porción

// OTROS
array.length          // Longitud
array.join(", ")      // Convertir a string
arr1.concat(arr2)     // Unir arrays
```