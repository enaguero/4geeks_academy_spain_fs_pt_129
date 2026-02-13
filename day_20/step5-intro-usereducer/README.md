# 🧠 Step 5: Introducción a useReducer

## 🎯 Objetivo

Entender **qué es useReducer**, cuándo usarlo en lugar de `useState`, y cómo funciona el patrón de **actions** y **reducers**.

---

## 📖 ¿Qué es useReducer?

`useReducer` es un Hook de React que te permite manejar estado complejo de una manera más **predecible y organizada**.

### Analogía del Restaurante 🍽️

Imagina que estás en un restaurante:

**Con useState** (el mesero hace todo):
- Tú le dices al mesero: "Quiero esto cocido, sin sal, con extra queso"
- El mesero debe recordar TODO y ejecutarlo
- Si hay muchas peticiones, se complica

**Con useReducer** (el mesero lleva tu orden a la cocina):
- Tú: "Orden #5 con modificación A"
- El mesero solo lleva el mensaje
- La cocina tiene un **sistema** (reducer) que sabe qué hacer con cada orden
- Más organizado y predecible

---

## 🆚 useState vs useReducer

### Usa `useState` cuando:
- ✅ El estado es simple (un string, un número, un booleano)
- ✅ Solo hay 1-2 formas de actualizar el estado
- ✅ La lógica de actualización es trivial

**Ejemplo**:
```jsx
const [count, setCount] = useState(0);
const [isOpen, setIsOpen] = useState(false);
const [name, setName] = useState('');
```

### Usa `useReducer` cuando:
- ✅ El estado es complejo (objetos con múltiples propiedades)
- ✅ Hay MUCHAS formas de actualizar el estado
- ✅ La próxima actualización depende del estado anterior
- ✅ Quieres centralizar la lógica de actualización

**Ejemplo**: Todo list, carrito de compras, formulario complejo, juego

---

## 🔧 Sintaxis Básica

```jsx
import { useReducer } from 'react';

// 1. Definir el reducer (la "cocina")
function reducer(state, action) {
  switch (action.type) {
    case 'ACTION_TYPE':
      return { ...state, /* cambios */ };
    default:
      return state;
  }
}

// 2. Usar en tu componente
function MyComponent() {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  // 3. Despachar acciones
  dispatch({ type: 'ACTION_TYPE', payload: data });
}
```

### Conceptos Clave

1. **`reducer`**: Función que recibe `(state, action)` y retorna el nuevo estado
2. **`state`**: El estado actual (como con useState)
3. **`dispatch`**: Función para enviar acciones (reemplaza a `setState`)
4. **`action`**: Objeto que describe QUÉ pasó (debe tener `type`)
5. **`payload`**: Datos adicionales en la acción (opcional)

---

## 💡 Ejemplo 1: Contador Simple

Comparemos el mismo contador con ambos enfoques:

### Con useState
```jsx
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(count - 1)}>-1</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

### Con useReducer
```jsx
// Reducer function
function counterReducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    case 'RESET':
      return { count: 0 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+1</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-1</button>
      <button onClick={() => dispatch({ type: 'RESET' })}>Reset</button>
    </div>
  );
}
```

**¿Cuál es mejor aquí?** Para un contador simple, **useState es mejor** (más simple).

Pero nota cómo useReducer centraliza TODA la lógica en un solo lugar (el reducer).

---

## 💡 Ejemplo 2: Contador con Más Acciones

Ahora agreguemos más funcionalidad:

```jsx
function counterReducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    case 'INCREMENT_BY':
      // Nota el uso de payload para datos adicionales
      return { count: state.count + action.payload };
    case 'DECREMENT_BY':
      return { count: state.count - action.payload };
    case 'MULTIPLY':
      return { count: state.count * action.payload };
    case 'RESET':
      return { count: 0 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+1</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-1</button>
      <button onClick={() => dispatch({ type: 'INCREMENT_BY', payload: 5 })}>+5</button>
      <button onClick={() => dispatch({ type: 'DECREMENT_BY', payload: 10 })}>-10</button>
      <button onClick={() => dispatch({ type: 'MULTIPLY', payload: 2 })}>x2</button>
      <button onClick={() => dispatch({ type: 'RESET' })}>Reset</button>
    </div>
  );
}
```

Ahora empieza a tener más sentido: toda la lógica está centralizada y es más fácil de leer.

---

## 🎨 Patrón de Actions

### Convención: Actions como Objetos

```javascript
// ✅ BIEN: Action con type
{ type: 'INCREMENT' }

// ✅ BIEN: Action con type y payload
{ type: 'ADD_TODO', payload: 'Comprar leche' }

// ✅ BIEN: Payload puede ser cualquier cosa
{ type: 'UPDATE_USER', payload: { name: 'Juan', age: 25 } }

// ❌ MAL: Sin type
{ value: 5 }
```

### Convención: TYPES en MAYÚSCULAS

```javascript
// ✅ BIEN
case 'ADD_TODO':
case 'DELETE_TODO':
case 'TOGGLE_TODO':

// ❌ MAL (funciona, pero no es convencional)
case 'addTodo':
case 'deleteTodo':
```

### Tip: Constantes para Types

Para evitar errores de tipeo:

```javascript
// Definir constantes
const ACTIONS = {
  INCREMENT: 'INCREMENT',
  DECREMENT: 'DECREMENT',
  RESET: 'RESET'
};

// Usar en reducer
function counterReducer(state, action) {
  switch (action.type) {
    case ACTIONS.INCREMENT:
      return { count: state.count + 1 };
    case ACTIONS.DECREMENT:
      return { count: state.count - 1 };
    case ACTIONS.RESET:
      return { count: 0 };
    default:
      return state;
  }
}

// Usar al despachar
dispatch({ type: ACTIONS.INCREMENT });
```

---

## ⚠️ Reglas Importantes del Reducer

### 1. Debe ser una función PURA
- ✅ Retorna nuevo estado basado en inputs
- ❌ NO modificar el estado directamente
- ❌ NO hacer llamadas asíncronas (fetch, setTimeout)
- ❌ NO generar valores random

```javascript
// ❌ MAL: Modifica el estado directamente
function badReducer(state, action) {
  state.count++; // ¡NO!
  return state;
}

// ✅ BIEN: Retorna nuevo objeto
function goodReducer(state, action) {
  return { ...state, count: state.count + 1 };
}
```

### 2. Siempre retorna un estado

```javascript
// ✅ BIEN: Siempre hay return
function reducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    default:
      return state; // Importante
  }
}

// ❌ MAL: Olvidó el default
function badReducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    // ¿Qué pasa si action.type no es 'INCREMENT'? undefined!
  }
}
```

### 3. Usa spread operator para inmutabilidad

```javascript
// ✅ BIEN
return { ...state, count: state.count + 1 };

// ❌ MAL
state.count = state.count + 1;
return state;
```

---

## 🤔 ¿Cuándo Usar Cada Uno?

### Usa `useState` para:
- ✅ Estado simple
- ✅ Componentes pequeños
- ✅ Pocas actualizaciones

### Usa `useReducer` para:
- ✅ Estado complejo (objetos/arrays)
- ✅ Muchas formas de actualizar estado
- ✅ Lógica de actualización compleja
- ✅ Cuando quieres testear la lógica fácilmente

---

## 📝 Ejercicio Práctico

Crea un componente que maneje el estado de un semáforo:

### Requisitos:
- Estado: `{ light: 'red' }` (puede ser 'red', 'yellow', 'green')
- Acciones:
  - `NEXT`: Cambia al siguiente color (red → yellow → green → red)
  - `RESET`: Vuelve a red
  - `SET_COLOR`: Cambia a un color específico (usa payload)

### Estructura:

```jsx
// 1. Define el reducer
function trafficLightReducer(state, action) {
  // Tu código aquí
}

// 2. Crea el componente
function TrafficLight() {
  const [state, dispatch] = useReducer(trafficLightReducer, { light: 'red' });

  return (
    <div>
      {/* Muestra el semáforo */}
      {/* Botones para cambiar el estado */}
    </div>
  );
}
```

---

## 🔗 Recursos

### Documentación Oficial
- [useReducer - React Docs](https://react.dev/reference/react/useReducer)

### 4Geeks Academy
- [What is and How to Use The useReducer Hook](https://4geeks.com/lesson/what-is-usereducer-react)

### Videos
- [useReducer en 100 segundos](https://www.youtube.com/watch?v=kK_Wqx3RnHk)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ useReducer es para estado complejo
- ✅ Un reducer es una función pura: `(state, action) => newState`
- ✅ dispatch envía acciones: `dispatch({ type: 'ACTION' })`
- ✅ Las acciones describen QUÉ pasó, no CÓMO actualizarlo
- ✅ El reducer decide CÓMO actualizar el estado
- ✅ Siempre retorna un nuevo estado (inmutabilidad)

### Siguiente Paso

En el **Step 6** verás cómo usar useReducer para manejar estado REALMENTE complejo (una todo list con múltiples acciones).

---

**¡Practica y experimenta! 🚀**

Si useReducer aún no tiene sentido, es normal. Se entiende mejor cuando ves casos de uso reales (próximo step).
