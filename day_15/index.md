🇪🇸 **Español** | [🇬🇧 English](index.en.md)

# Día 15: Módulos JavaScript y React ⚛️

## Introducción

Hoy daremos dos pasos importantes en tu camino como desarrollador:
1. **Módulos en JavaScript**: Aprenderás a organizar tu código en archivos separados
2. **React**: Conocerás la librería más popular para construir interfaces web modernas

---

## Parte 1: ¿Qué son los Módulos?

### El Problema: Todo en un Solo Archivo 😰

Imagina que estás construyendo una aplicación grande:

```javascript
// app.js - TODO EL CÓDIGO AQUÍ (¡5000 líneas!)

function sum(a, b) { return a + b; }
function subtract(a, b) { return a - b; }
function multiply(a, b) { return a * b; }
function getUserData() { /* ... */ }
function processPayment() { /* ... */ }
function sendEmail() { /* ... */ }
// ... 200 funciones más ...
```

**Problemas**:
- ❌ Imposible de navegar
- ❌ Difícil de mantener
- ❌ No puedes reutilizar código en otros proyectos
- ❌ Varios desarrolladores no pueden trabajar al mismo tiempo

### La Solución: Módulos 🎯

Los **módulos** te permiten dividir tu código en archivos separados, cada uno con su propia responsabilidad.

```
proyecto/
├── calculator.js      ← Funciones matemáticas
├── user.js           ← Gestión de usuarios
├── payment.js        ← Procesamiento de pagos
└── app.js            ← Archivo principal
```

### ¿Qué es un Módulo?

**Módulo** = Un archivo JavaScript que **exporta** funciones, variables u objetos para que otros archivos puedan **importarlos**.

---

## Parte 2: Export - Compartir tu Código

### Export Básico (Named Export)

**Archivo: `math.js`**
```javascript
// Exportar funciones individuales
export function sum(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export const PI = 3.14159;
```

### 🔍 Explicación

```javascript
export function sum(a, b) { ... }
```

La palabra `export` dice: **"Esta función puede ser usada por otros archivos"**.

### Export al Final del Archivo

También puedes exportar todo al final:

**Archivo: `math.js`**
```javascript
function sum(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

const PI = 3.14159;

// Exportar todo al final
export { sum, subtract, PI };
```

### 📊 Comparación

| Método | Cuándo usar |
|--------|-------------|
| `export function sum()` | Cuando exportas pocas cosas |
| `export { sum, subtract }` | Cuando exportas muchas cosas al final |

---

## Parte 3: Import - Usar Código de Otros Archivos

### Import Básico

**Archivo: `app.js`**
```javascript
// Importar funciones específicas
import { sum, subtract, PI } from './math.js';

console.log(sum(5, 3));       // 8
console.log(subtract(10, 4)); // 6
console.log(PI);              // 3.14159
```

### 🔍 Explicación

```javascript
import { sum, subtract } from './math.js';
```

- **`import`**: Palabra clave para importar
- **`{ sum, subtract }`**: Lo que quieres importar (entre llaves)
- **`from './math.js'`**: De dónde importar

### Rutas en Import

```javascript
// Mismo directorio
import { sum } from './math.js';

// Subdirectorio
import { getUserData } from './utils/user.js';

// Directorio padre
import { config } from '../config.js';
```

---

## Parte 4: Export Default - El Export Principal

### ¿Qué es Export Default?

Cuando un archivo tiene **una cosa principal** para exportar, usas `export default`.

**Archivo: `calculator.js`**
```javascript
// Una clase principal
class Calculator {
    sum(a, b) {
        return a + b;
    }
    
    subtract(a, b) {
        return a - b;
    }
}

export default Calculator;
```

**Archivo: `app.js`**
```javascript
// ¡Sin llaves al importar!
import Calculator from './calculator.js';

const calc = new Calculator();
console.log(calc.sum(5, 3)); // 8
```

### 🔍 Diferencia Clave

| Export Type | Sintaxis Export | Sintaxis Import |
|-------------|-----------------|-----------------|
| **Named** | `export function sum()` | `import { sum } from './file.js'` |
| **Default** | `export default Calculator` | `import Calculator from './file.js'` |

### Regla de Oro

- **Named exports**: Múltiples cosas con **nombres específicos** (necesitas llaves `{}`)
- **Default export**: **Una cosa principal** por archivo (sin llaves)

---

## Parte 5: Ejemplo Completo - Sistema de Usuario

### Estructura del Proyecto

```
user-system/
├── user.js           ← Clase de Usuario
├── userService.js    ← Servicios de usuario
├── validator.js      ← Validaciones
└── app.js            ← Archivo principal
```

### Archivo 1: `user.js`

```javascript
// Export default: la clase principal
class User {
    constructor(name, email, age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }
    
    greet() {
        return `Hola, soy ${this.name}`;
    }
}

export default User;
```

### Archivo 2: `validator.js`

```javascript
// Named exports: múltiples funciones de validación
export function isValidEmail(email) {
    return email.includes('@');
}

export function isValidAge(age) {
    return age >= 18 && age <= 120;
}

export function isValidName(name) {
    return name.length >= 2;
}
```

### Archivo 3: `userService.js`

```javascript
// Mezclando imports
import User from './user.js';  // Default import
import { isValidEmail, isValidAge, isValidName } from './validator.js';  // Named imports

export function createUser(name, email, age) {
    // Validar datos
    if (!isValidName(name)) {
        throw new Error('Nombre inválido');
    }
    
    if (!isValidEmail(email)) {
        throw new Error('Email inválido');
    }
    
    if (!isValidAge(age)) {
        throw new Error('Edad inválida');
    }
    
    // Crear y devolver usuario
    return new User(name, email, age);
}

export function getUserInfo(user) {
    return {
        name: user.name,
        email: user.email,
        age: user.age,
        canVote: user.age >= 18
    };
}
```

### Archivo 4: `app.js`

```javascript
import { createUser, getUserInfo } from './userService.js';

// Crear usuarios
try {
    const user1 = createUser('Ana García', 'ana@example.com', 25);
    const user2 = createUser('Pedro López', 'pedro@example.com', 17);
    
    console.log(user1.greet());  // Hola, soy Ana García
    console.log(getUserInfo(user1));
    
} catch (error) {
    console.error('Error:', error.message);
}
```

---

## Parte 6: Import * (Importar Todo)

### Sintaxis

```javascript
import * as MathUtils from './math.js';

console.log(MathUtils.sum(2, 3));      // 5
console.log(MathUtils.subtract(10, 4)); // 6
console.log(MathUtils.PI);              // 3.14159
```

### Cuándo Usar

✅ **Usa** `import *` cuando el módulo tiene muchas funciones relacionadas  
❌ **No uses** si solo necesitas 1-2 funciones (importa específicamente)

---

## 📝 Ejercicio 1: Biblioteca de Strings

Crea un sistema modular para manipular strings.

**Archivo: `stringHelpers.js`**
```javascript
export function toUpperCase(str) {
    return str.toUpperCase();
}

export function toLowerCase(str) {
    return str.toLowerCase();
}

export function reverse(str) {
    return str.split('').reverse().join('');
}

export function countVowels(str) {
    const vowels = str.match(/[aeiouAEIOU]/g);
    return vowels ? vowels.length : 0;
}
```

**Archivo: `app.js`**
```javascript
// TODO: Importa las funciones y úsalas
```

<details>
<summary>Solución</summary>

```javascript
import { toUpperCase, toLowerCase, reverse, countVowels } from './stringHelpers.js';

const texto = 'Hola Mundo';

console.log(toUpperCase(texto));  // HOLA MUNDO
console.log(toLowerCase(texto));  // hola mundo
console.log(reverse(texto));      // odnuM aloH
console.log(countVowels(texto));  // 4
```
</details>

---

## Parte 7: Introducción a React ⚛️

### ¿Qué es React?

**React** es una **librería de JavaScript** creada por Facebook para construir interfaces de usuario (UI) de forma eficiente.

### El Problema que React Resuelve

#### Antes de React (Vanilla JS)

```javascript
// Código tedioso y difícil de mantener
document.querySelector('#app').innerHTML = 
    '<div class="card">' +
    '  <h2>' + user.name + '</h2>' +
    '  <p>' + user.email + '</p>' +
    '</div>';

// ¡Repetir esto para cada elemento del DOM! 😰
```

#### Con React

```javascript
// Código limpio y fácil de mantener
function UserCard() {
    return (
        <div className="card">
            <h2>{user.name}</h2>
            <p>{user.email}</p>
        </div>
    );
}
```

### ¿Por Qué React es Popular?

| Beneficio | Explicación |
|-----------|-------------|
| 🧩 **Componentes** | Divide la UI en piezas reutilizables |
| ⚡ **Rápido** | Solo actualiza lo que cambia en el DOM |
| 📝 **JSX** | Escribe HTML dentro de JavaScript |
| 🔄 **Reactivo** | Los cambios se reflejan automáticamente |
| 🌐 **Popular** | Usado por Facebook, Instagram, Netflix, Airbnb |

---

## Parte 8: Componentes - Los Bloques de React

### ¿Qué es un Componente?

Un **componente** es una pieza reutilizable de la interfaz. Es como un LEGO: juntas muchos componentes pequeños para construir algo grande.

### Analogía: Una Casa 🏠

```
Casa
├── Navbar (navegación)
├── Header (encabezado)
├── Main (contenido principal)
│   ├── Card (tarjeta)
│   ├── Card (tarjeta)
│   └── Card (tarjeta)
└── Footer (pie de página)
```

Cada parte es un componente independiente que puedes reutilizar.

### Tu Primer Componente

```javascript
function Welcome() {
    return <h1>¡Hola Mundo!</h1>;
}
```

### 🔍 Anatomía de un Componente

```javascript
function Welcome() {        // 1. Nombre en PascalCase
    return (                // 2. return devuelve JSX
        <h1>¡Hola!</h1>    // 3. JSX (parece HTML)
    );
}
```

**Reglas**:
1. Nombre en **PascalCase** (`Welcome`, no `welcome`)
2. Debe **retornar** JSX
3. Un solo elemento raíz

---

## Parte 9: JSX - HTML dentro de JavaScript

### ¿Qué es JSX?

**JSX** = JavaScript + XML. Te permite escribir HTML dentro de JavaScript.

```javascript
// JSX (lo que escribes)
const element = <h1>Hola, {nombre}</h1>;

// JavaScript puro (lo que React genera)
const element = React.createElement('h1', null, 'Hola, ', nombre);
```

### Reglas de JSX

#### 1. **Un solo elemento raíz**

```javascript
// ❌ INCORRECTO: Dos elementos raíz
function App() {
    return (
        <h1>Título</h1>
        <p>Párrafo</p>
    );
}

// ✅ CORRECTO: Envuelto en un div
function App() {
    return (
        <div>
            <h1>Título</h1>
            <p>Párrafo</p>
        </div>
    );
}

// ✅ CORRECTO: Usando Fragment (<>)
function App() {
    return (
        <>
            <h1>Título</h1>
            <p>Párrafo</p>
        </>
    );
}
```

#### 2. **Cerrar todas las etiquetas**

```javascript
// ❌ INCORRECTO en JSX
<img src="foto.jpg">
<br>

// ✅ CORRECTO en JSX
<img src="foto.jpg" />
<br />
```

#### 3. **className en lugar de class**

```javascript
// ❌ INCORRECTO
<div class="card">Contenido</div>

// ✅ CORRECTO
<div className="card">Contenido</div>
```

**Razón**: `class` es una palabra reservada en JavaScript.

#### 4. **Expresiones JavaScript con {}**

```javascript
function Greeting() {
    const name = "Ana";
    const age = 25;
    
    return (
        <div>
            <h1>Hola, {name}</h1>
            <p>Tienes {age} años</p>
            <p>¿Puedes votar? {age >= 18 ? 'Sí' : 'No'}</p>
        </div>
    );
}
```

---

## Parte 10: Componentes con Props

### ¿Qué son las Props?

**Props** (properties) son **parámetros** que le pasas a un componente para personalizarlo.

### Ejemplo Sin Props (Código Repetitivo)

```javascript
function UserCard1() {
    return <h2>Ana García</h2>;
}

function UserCard2() {
    return <h2>Pedro López</h2>;
}

function UserCard3() {
    return <h2>María Rodríguez</h2>;
}

// ¡Tienes que crear 100 componentes para 100 usuarios! 😱
```

### Ejemplo Con Props (Reutilizable)

```javascript
function UserCard(props) {
    return <h2>{props.name}</h2>;
}

// Usar el componente con diferentes props
<UserCard name="Ana García" />
<UserCard name="Pedro López" />
<UserCard name="María Rodríguez" />
```

### Props con Múltiples Valores

```javascript
function UserCard(props) {
    return (
        <div className="card">
            <h2>{props.name}</h2>
            <p>Email: {props.email}</p>
            <p>Edad: {props.age}</p>
        </div>
    );
}

// Uso
<UserCard 
    name="Ana García" 
    email="ana@example.com" 
    age={25} 
/>
```

### 🔍 Tipos de Props

```javascript
<UserCard 
    name="Ana"           // String (entre comillas)
    age={25}            // Número (entre llaves)
    isActive={true}     // Boolean (entre llaves)
    hobbies={['leer', 'correr']}  // Array (entre llaves)
/>
```

---

## Parte 11: Destructuring de Props

### Sin Destructuring

```javascript
function UserCard(props) {
    return (
        <div>
            <h2>{props.name}</h2>
            <p>{props.email}</p>
            <p>{props.age}</p>
        </div>
    );
}
```

### Con Destructuring (Más Limpio)

```javascript
function UserCard({ name, email, age }) {
    return (
        <div>
            <h2>{name}</h2>
            <p>{email}</p>
            <p>{age}</p>
        </div>
    );
}
```

**Ventaja**: Escribes menos y el código es más legible.

---

## Parte 12: Componente Completo - Card de Producto

```javascript
function ProductCard({ name, price, image, inStock }) {
    return (
        <div className="product-card">
            <img src={image} alt={name} />
            <h3>{name}</h3>
            <p className="price">${price}</p>
            {inStock ? (
                <button>Comprar</button>
            ) : (
                <p className="out-of-stock">Agotado</p>
            )}
        </div>
    );
}

// Uso
function App() {
    return (
        <div>
            <ProductCard 
                name="Laptop"
                price={999}
                image="laptop.jpg"
                inStock={true}
            />
            <ProductCard 
                name="Mouse"
                price={25}
                image="mouse.jpg"
                inStock={false}
            />
        </div>
    );
}
```

---

## 📝 Ejercicio 2: Tarjeta de Perfil

Crea un componente `ProfileCard` que muestre:
- Foto de perfil
- Nombre
- Profesión
- Botón "Seguir" si no lo sigues, "Siguiendo" si ya lo sigues

```javascript
function ProfileCard({ name, profession, photo, isFollowing }) {
    // TODO: Implementa el componente
}

// Debe usarse así:
<ProfileCard 
    name="Ana García"
    profession="Desarrolladora Frontend"
    photo="ana.jpg"
    isFollowing={false}
/>
```

<details>
<summary>Solución</summary>

```javascript
function ProfileCard({ name, profession, photo, isFollowing }) {
    return (
        <div className="profile-card">
            <img src={photo} alt={name} className="profile-photo" />
            <h2>{name}</h2>
            <p className="profession">{profession}</p>
            {isFollowing ? (
                <button className="btn-following">Siguiendo</button>
            ) : (
                <button className="btn-follow">Seguir</button>
            )}
        </div>
    );
}
```
</details>

---

## Parte 13: Renderizado de Listas

### Problema: Muchos Elementos

```javascript
function App() {
    return (
        <div>
            <UserCard name="Ana" />
            <UserCard name="Pedro" />
            <UserCard name="María" />
            // ... ¿Y si tengo 1000 usuarios?
        </div>
    );
}
```

### Solución: map()

```javascript
function App() {
    const users = [
        { id: 1, name: 'Ana García' },
        { id: 2, name: 'Pedro López' },
        { id: 3, name: 'María Rodríguez' }
    ];
    
    return (
        <div>
            {users.map(user => (
                <UserCard 
                    key={user.id}
                    name={user.name}
                />
            ))}
        </div>
    );
}
```

### 🔍 La Prop `key`

```javascript
<UserCard key={user.id} name={user.name} />
```

**`key`** es especial: React la usa para identificar cada elemento de forma única.

**Regla**: Siempre usa un ID único, nunca el índice del array.

---

## Parte 14: Ejemplo Completo - Lista de Productos

```javascript
function ProductList() {
    const products = [
        { id: 1, name: 'Laptop', price: 999, image: 'laptop.jpg', inStock: true },
        { id: 2, name: 'Mouse', price: 25, image: 'mouse.jpg', inStock: true },
        { id: 3, name: 'Teclado', price: 75, image: 'keyboard.jpg', inStock: false },
        { id: 4, name: 'Monitor', price: 299, image: 'monitor.jpg', inStock: true }
    ];
    
    return (
        <div className="container">
            <h1>Nuestros Productos</h1>
            <div className="product-grid">
                {products.map(product => (
                    <ProductCard 
                        key={product.id}
                        name={product.name}
                        price={product.price}
                        image={product.image}
                        inStock={product.inStock}
                    />
                ))}
            </div>
        </div>
    );
}

function ProductCard({ name, price, image, inStock }) {
    return (
        <div className="product-card">
            <img src={image} alt={name} />
            <h3>{name}</h3>
            <p className="price">${price}</p>
            {inStock ? (
                <button className="btn-primary">Añadir al carrito</button>
            ) : (
                <p className="out-of-stock">Agotado</p>
            )}
        </div>
    );
}

export default ProductList;
```

---

## 📝 Ejercicio 3: Lista de Tareas

Crea una lista de tareas con React.

```javascript
function TodoList() {
    const todos = [
        { id: 1, text: 'Aprender JavaScript', completed: true },
        { id: 2, text: 'Estudiar React', completed: false },
        { id: 3, text: 'Hacer ejercicios', completed: false }
    ];
    
    // TODO: Renderiza cada tarea con un componente TodoItem
}

function TodoItem({ text, completed }) {
    // TODO: Muestra el texto
    // TODO: Muestra "✓" si está completada, "○" si no
}
```

<details>
<summary>Solución</summary>

```javascript
function TodoList() {
    const todos = [
        { id: 1, text: 'Aprender JavaScript', completed: true },
        { id: 2, text: 'Estudiar React', completed: false },
        { id: 3, text: 'Hacer ejercicios', completed: false }
    ];
    
    return (
        <div className="todo-list">
            <h2>Mis Tareas</h2>
            <ul>
                {todos.map(todo => (
                    <TodoItem 
                        key={todo.id}
                        text={todo.text}
                        completed={todo.completed}
                    />
                ))}
            </ul>
        </div>
    );
}

function TodoItem({ text, completed }) {
    return (
        <li className={completed ? 'completed' : ''}>
            <span>{completed ? '✓' : '○'}</span>
            <span>{text}</span>
        </li>
    );
}
```
</details>

---

## Resumen: Conceptos Clave

### Módulos JavaScript
✅ **Módulo** = Archivo que exporta código  
✅ **`export`** = Compartir funciones/variables  
✅ **`import`** = Usar código de otros archivos  
✅ **Named export** = `export function sum()` → `import { sum }`  
✅ **Default export** = `export default` → `import Calculator`  
✅ Organiza código en archivos separados

### React
✅ **React** = Librería para construir UIs  
✅ **Componente** = Pieza reutilizable de UI  
✅ **JSX** = HTML dentro de JavaScript  
✅ **Props** = Parámetros para personalizar componentes  
✅ **key** = Identificador único en listas  
✅ Todo es un componente

### JSX
✅ Un solo elemento raíz  
✅ Cerrar todas las etiquetas (`<br />`)  
✅ `className` en lugar de `class`  
✅ `{}` para expresiones JavaScript

---

## Cheat Sheet

```javascript
// ============ MÓDULOS ============

// EXPORT (math.js)
export function sum(a, b) { return a + b; }
export const PI = 3.14;
export default class Calculator { }

// IMPORT (app.js)
import { sum, PI } from './math.js';
import Calculator from './calculator.js';
import * as Math from './math.js';

// ============ REACT ============

// COMPONENTE BÁSICO
function Welcome() {
    return <h1>¡Hola!</h1>;
}

// COMPONENTE CON PROPS
function UserCard({ name, age }) {
    return (
        <div>
            <h2>{name}</h2>
            <p>{age} años</p>
        </div>
    );
}

// USO
<UserCard name="Ana" age={25} />

// RENDERIZAR LISTA
{users.map(user => (
    <UserCard key={user.id} name={user.name} />
))}

// CONDICIONAL EN JSX
{isLoggedIn ? <Dashboard /> : <Login />}

// EXPRESIONES JS
<h1>Hola, {nombre}</h1>
<p>Total: ${price * quantity}</p>
```

---

## 🎯 Proyecto Guiado: Galería de Perfiles

Vamos a crear una galería de perfiles de equipo usando todo lo aprendido.

### Estructura de Archivos

```
team-gallery/
├── data.js          ← Datos del equipo
├── ProfileCard.js   ← Componente de tarjeta
├── App.js           ← Componente principal
└── index.html       ← HTML base
```

### `data.js`

```javascript
const teamMembers = [
    {
        id: 1,
        name: 'Ana García',
        role: 'Frontend Developer',
        photo: 'https://i.pravatar.cc/150?img=1',
        skills: ['React', 'CSS', 'JavaScript']
    },
    {
        id: 2,
        name: 'Pedro López',
        role: 'Backend Developer',
        photo: 'https://i.pravatar.cc/150?img=2',
        skills: ['Node.js', 'Python', 'SQL']
    },
    {
        id: 3,
        name: 'María Rodríguez',
        role: 'UX Designer',
        photo: 'https://i.pravatar.cc/150?img=3',
        skills: ['Figma', 'Sketch', 'Photoshop']
    }
];

export default teamMembers;
```

### `ProfileCard.js`

```javascript
function ProfileCard({ name, role, photo, skills }) {
    return (
        <div className="profile-card">
            <img src={photo} alt={name} className="profile-photo" />
            <h2>{name}</h2>
            <p className="role">{role}</p>
            <div className="skills">
                {skills.map((skill, index) => (
                    <span key={index} className="skill-tag">
                        {skill}
                    </span>
                ))}
            </div>
            <button className="btn-contact">Contactar</button>
        </div>
    );
}

export default ProfileCard;
```

### `App.js`

```javascript
import teamMembers from './data.js';
import ProfileCard from './ProfileCard.js';

function App() {
    return (
        <div className="container">
            <header>
                <h1>Nuestro Equipo</h1>
                <p>Conoce a las personas que hacen posible nuestro proyecto</p>
            </header>
            
            <div className="profile-grid">
                {teamMembers.map(member => (
                    <ProfileCard 
                        key={member.id}
                        name={member.name}
                        role={member.role}
                        photo={member.photo}
                        skills={member.skills}
                    />
                ))}
            </div>
        </div>
    );
}

export default App;
```

---

## 🔗 Recursos Adicionales

- **MDN - Modules**: https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Modules
- **React Docs**: https://react.dev/learn
- **4Geeks - React Tutorial**: https://4geeks.com/lesson/learn-react-js-tutorial
- **4Geeks - Creating Components**: https://4geeks.com/lesson/making-react-components

---

## 🎉 ¡Felicidades!

Ahora sabes:

- ✅ Qué son los módulos y por qué son importantes
- ✅ Usar `export` e `import` para organizar código
- ✅ Diferencia entre named y default exports
- ✅ Qué es React y por qué es popular
- ✅ Crear componentes reutilizables
- ✅ Usar JSX para escribir HTML en JavaScript
- ✅ Pasar datos con props
- ✅ Renderizar listas con `map()`
- ✅ Aplicar condicionales en JSX

**Próximo paso**: En las siguientes clases aprenderás sobre el **estado** (state) en React, que permite crear componentes interactivos que responden a acciones del usuario.

---

## 💡 Pensamiento Final

> "React no es solo una librería, es una forma de pensar sobre cómo construir interfaces"  
> — Dan Abramov (co-creador de Redux y parte del equipo de React)

Los módulos y React son fundamentales en el desarrollo web moderno. Dominarlos te abre las puertas a:
- 🚀 Aplicaciones web de una sola página (SPA)
- 📱 Aplicaciones móviles con React Native
- 💼 Oportunidades laborales en empresas tech

**¡Sigue practicando y construyendo proyectos!**

<citations>
  <document>
      <document_type>RULE</document_type>
      <document_id>/Users/erwinaguero/teaching/4geeks_academy_spain_fs_pt_129/WARP.md</document_id>
  </document>
</citations>