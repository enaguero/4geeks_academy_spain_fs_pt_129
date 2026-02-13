# 📦 Step 6: useReducer para Estado Complejo

## 🎯 Objetivo

Usar `useReducer` para manejar estado complejo con **múltiples acciones CRUD** (Create, Read, Update, Delete) en una Todo List.

---

## 💡 Caso Real: Todo List

Una todo list necesita manejar:
- ✅ Agregar tareas
- ✅ Marcar como completada/incompleta
- ✅ Editar texto de una tarea
- ✅ Eliminar tareas
- ✅ Limpiar todas las completadas

Con `useState` necesitarías múltiples funciones. Con `useReducer` todo está centralizado.

---

## 🔧 Estructura del Estado

```javascript
const initialState = {
  todos: [
    { id: 1, text: 'Aprender React Router', completed: false },
    { id: 2, text: 'Entender useReducer', completed: true },
    { id: 3, text: 'Practicar Context API', completed: false }
  ],
  filter: 'all' // 'all', 'active', 'completed'
};
```

---

## 🎨 Definir Action Types

Primero definimos constantes para evitar errores de tipeo:

```javascript
const ACTIONS = {
  ADD_TODO: 'ADD_TODO',
  TOGGLE_TODO: 'TOGGLE_TODO',
  DELETE_TODO: 'DELETE_TODO',
  EDIT_TODO: 'EDIT_TODO',
  CLEAR_COMPLETED: 'CLEAR_COMPLETED',
  SET_FILTER: 'SET_FILTER'
};
```

---

## 🧠 El Reducer

```javascript
function todoReducer(state, action) {
  switch (action.type) {
    
    case ACTIONS.ADD_TODO:
      return {
        ...state,
        todos: [
          ...state.todos,
          {
            id: Date.now(), // Simple ID generator
            text: action.payload,
            completed: false
          }
        ]
      };
    
    case ACTIONS.TOGGLE_TODO:
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload
            ? { ...todo, completed: !todo.completed }
            : todo
        )
      };
    
    case ACTIONS.DELETE_TODO:
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.payload)
      };
    
    case ACTIONS.EDIT_TODO:
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload.id
            ? { ...todo, text: action.payload.text }
            : todo
        )
      };
    
    case ACTIONS.CLEAR_COMPLETED:
      return {
        ...state,
        todos: state.todos.filter(todo => !todo.completed)
      };
    
    case ACTIONS.SET_FILTER:
      return {
        ...state,
        filter: action.payload
      };
    
    default:
      return state;
  }
}
```

---

## 📝 Componente TodoList

```jsx
import { useReducer, useState } from 'react';

function TodoList() {
  const [state, dispatch] = useReducer(todoReducer, initialState);
  const [inputValue, setInputValue] = useState('');

  // Agregar tarea
  const handleAddTodo = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      dispatch({ type: ACTIONS.ADD_TODO, payload: inputValue });
      setInputValue('');
    }
  };

  // Filtrar todos según el filtro actual
  const getFilteredTodos = () => {
    switch (state.filter) {
      case 'active':
        return state.todos.filter(todo => !todo.completed);
      case 'completed':
        return state.todos.filter(todo => todo.completed);
      default:
        return state.todos;
    }
  };

  const filteredTodos = getFilteredTodos();

  return (
    <div>
      <h1>Todo List</h1>
      
      {/* Formulario para agregar */}
      <form onSubmit={handleAddTodo}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Agregar nueva tarea..."
        />
        <button type="submit">Agregar</button>
      </form>

      {/* Filtros */}
      <div>
        <button onClick={() => dispatch({ type: ACTIONS.SET_FILTER, payload: 'all' })}>
          Todas
        </button>
        <button onClick={() => dispatch({ type: ACTIONS.SET_FILTER, payload: 'active' })}>
          Activas
        </button>
        <button onClick={() => dispatch({ type: ACTIONS.SET_FILTER, payload: 'completed' })}>
          Completadas
        </button>
      </div>

      {/* Lista de todos */}
      <ul>
        {filteredTodos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => dispatch({ type: ACTIONS.TOGGLE_TODO, payload: todo.id })}
            />
            <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
              {todo.text}
            </span>
            <button onClick={() => dispatch({ type: ACTIONS.DELETE_TODO, payload: todo.id })}>
              Eliminar
            </button>
          </li>
        ))}
      </ul>

      {/* Limpiar completadas */}
      <button onClick={() => dispatch({ type: ACTIONS.CLEAR_COMPLETED })}>
        Limpiar Completadas
      </button>

      {/* Contador */}
      <p>
        {state.todos.filter(t => !t.completed).length} tareas activas
      </p>
    </div>
  );
}
```

---

## 🎯 Ventajas de useReducer Aquí

### ✅ Centralización
Toda la lógica de actualización está en un solo lugar (el reducer).

### ✅ Predecibilidad
Cada acción es explícita. Sabes exactamente qué hace `TOGGLE_TODO`.

### ✅ Testeable
Puedes testear el reducer independientemente:

```javascript
test('ADD_TODO agrega una tarea', () => {
  const state = { todos: [], filter: 'all' };
  const action = { type: 'ADD_TODO', payload: 'Nueva tarea' };
  const newState = todoReducer(state, action);
  
  expect(newState.todos).toHaveLength(1);
  expect(newState.todos[0].text).toBe('Nueva tarea');
});
```

### ✅ Escalable
Agregar nuevas acciones es fácil: solo añades un nuevo `case` en el reducer.

---

## 🆚 Comparación con useState

### Con useState (múltiples funciones):

```jsx
const [todos, setTodos] = useState([]);
const [filter, setFilter] = useState('all');

const addTodo = (text) => {
  setTodos([...todos, { id: Date.now(), text, completed: false }]);
};

const toggleTodo = (id) => {
  setTodos(todos.map(todo =>
    todo.id === id ? { ...todo, completed: !todo.completed } : todo
  ));
};

const deleteTodo = (id) => {
  setTodos(todos.filter(todo => todo.id !== id));
};

// ... más funciones
```

### Con useReducer (una función centralizada):

```jsx
const [state, dispatch] = useReducer(todoReducer, initialState);

// Llamar acciones
dispatch({ type: 'ADD_TODO', payload: text });
dispatch({ type: 'TOGGLE_TODO', payload: id });
dispatch({ type: 'DELETE_TODO', payload: id });
```

Más limpio, especialmente cuando hay muchas acciones.

---

## 💡 Patrones Comunes

### 1. Payload Simple (ID, String, Number)

```javascript
// Acción
dispatch({ type: 'DELETE_TODO', payload: 123 });

// En reducer
case 'DELETE_TODO':
  return {
    ...state,
    todos: state.todos.filter(todo => todo.id !== action.payload)
  };
```

### 2. Payload Complejo (Objeto)

```javascript
// Acción
dispatch({
  type: 'EDIT_TODO',
  payload: { id: 123, text: 'Nuevo texto' }
});

// En reducer
case 'EDIT_TODO':
  return {
    ...state,
    todos: state.todos.map(todo =>
      todo.id === action.payload.id
        ? { ...todo, text: action.payload.text }
        : todo
    )
  };
```

### 3. Sin Payload

```javascript
// Acción
dispatch({ type: 'CLEAR_COMPLETED' });

// En reducer
case 'CLEAR_COMPLETED':
  return {
    ...state,
    todos: state.todos.filter(todo => !todo.completed)
  };
```

---

## 📝 Ejercicio Práctico

Extiende la Todo List con estas funcionalidades:

### Nuevas Acciones:
1. **`MARK_ALL_COMPLETED`**: Marca todas las tareas como completadas
2. **`SORT_TODOS`**: Ordena alfabéticamente (usa payload: 'asc' o 'desc')
3. **`DUPLICATE_TODO`**: Duplica una tarea existente (con nuevo ID)

### Pista:

```javascript
case ACTIONS.MARK_ALL_COMPLETED:
  return {
    ...state,
    todos: state.todos.map(todo => ({ ...todo, completed: true }))
  };

case ACTIONS.SORT_TODOS:
  const sorted = [...state.todos].sort((a, b) => {
    if (action.payload === 'asc') {
      return a.text.localeCompare(b.text);
    } else {
      return b.text.localeCompare(a.text);
    }
  });
  return { ...state, todos: sorted };

case ACTIONS.DUPLICATE_TODO:
  const todoToDuplicate = state.todos.find(t => t.id === action.payload);
  if (!todoToDuplicate) return state;
  return {
    ...state,
    todos: [...state.todos, { ...todoToDuplicate, id: Date.now() }]
  };
```

---

## ⚠️ Errores Comunes

### 1. Mutar el estado directamente

```javascript
// ❌ MAL
case 'ADD_TODO':
  state.todos.push(newTodo); // ¡Mutación!
  return state;

// ✅ BIEN
case 'ADD_TODO':
  return {
    ...state,
    todos: [...state.todos, newTodo]
  };
```

### 2. Olvidar retornar el estado completo

```javascript
// ❌ MAL: Solo retorna todos, se pierde filter
case 'ADD_TODO':
  return {
    todos: [...state.todos, newTodo]
  };

// ✅ BIEN: Spread del estado anterior
case 'ADD_TODO':
  return {
    ...state, // Mantiene filter y otras propiedades
    todos: [...state.todos, newTodo]
  };
```

### 3. No usar el default case

```javascript
// ❌ MAL: Sin default
function reducer(state, action) {
  switch (action.type) {
    case 'ADD_TODO':
      return { ...state, /* ... */ };
  }
  // ¿Qué pasa con otras acciones? undefined!
}

// ✅ BIEN
function reducer(state, action) {
  switch (action.type) {
    case 'ADD_TODO':
      return { ...state, /* ... */ };
    default:
      return state; // Crucial
  }
}
```

---

## 🔗 Recursos

### Documentación Oficial
- [useReducer - React Docs](https://react.dev/reference/react/useReducer)
- [Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer)

### 4Geeks Academy
- [What is and How to Use The useReducer Hook](https://4geeks.com/lesson/what-is-usereducer-react)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ useReducer brilla con estado complejo (CRUD operations)
- ✅ Todas las acciones están centralizadas en el reducer
- ✅ Cada `case` maneja UNA acción específica
- ✅ Siempre usa inmutabilidad (`...state`, `.map()`, `.filter()`)
- ✅ El payload puede ser simple o complejo según necesites
- ✅ Es más fácil de testear que múltiples `setState`

### Siguiente Paso

En el **Step 7** aprenderás sobre **Context API** para compartir estado (incluyendo el dispatch de useReducer) entre componentes sin prop drilling.

---

**¡Practica creando tu propia Todo List con useReducer! 🚀**
