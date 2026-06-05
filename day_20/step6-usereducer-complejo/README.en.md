[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 📦 Step 6: useReducer for Complex State

## 🎯 Goal

Use `useReducer` to manage complex state with **multiple CRUD actions** (Create, Read, Update, Delete) in a Todo List.

---

## 💡 Real Use Case: Todo List

A todo list needs to handle:
- ✅ Add tasks
- ✅ Mark as completed/uncompleted
- ✅ Edit a task's text
- ✅ Delete tasks
- ✅ Clear all completed tasks

With `useState` you'd need several functions. With `useReducer` everything is centralized.

---

## 🔧 State Structure

```javascript
const initialState = {
  todos: [
    { id: 1, text: 'Learn React Router', completed: false },
    { id: 2, text: 'Understand useReducer', completed: true },
    { id: 3, text: 'Practice Context API', completed: false }
  ],
  filter: 'all' // 'all', 'active', 'completed'
};
```

---

## 🎨 Define Action Types

First we define constants to prevent typos:

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

## 🧠 The Reducer

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

## 📝 TodoList Component

```jsx
import { useReducer, useState } from 'react';

function TodoList() {
  const [state, dispatch] = useReducer(todoReducer, initialState);
  const [inputValue, setInputValue] = useState('');

  // Add task
  const handleAddTodo = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      dispatch({ type: ACTIONS.ADD_TODO, payload: inputValue });
      setInputValue('');
    }
  };

  // Filter todos by the current filter
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
      
      {/* Form to add */}
      <form onSubmit={handleAddTodo}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Add new task..."
        />
        <button type="submit">Add</button>
      </form>

      {/* Filters */}
      <div>
        <button onClick={() => dispatch({ type: ACTIONS.SET_FILTER, payload: 'all' })}>
          All
        </button>
        <button onClick={() => dispatch({ type: ACTIONS.SET_FILTER, payload: 'active' })}>
          Active
        </button>
        <button onClick={() => dispatch({ type: ACTIONS.SET_FILTER, payload: 'completed' })}>
          Completed
        </button>
      </div>

      {/* Todo list */}
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
              Delete
            </button>
          </li>
        ))}
      </ul>

      {/* Clear completed */}
      <button onClick={() => dispatch({ type: ACTIONS.CLEAR_COMPLETED })}>
        Clear Completed
      </button>

      {/* Counter */}
      <p>
        {state.todos.filter(t => !t.completed).length} active tasks
      </p>
    </div>
  );
}
```

---

## 🎯 Advantages of useReducer Here

### ✅ Centralization
All update logic is in one place (the reducer).

### ✅ Predictability
Every action is explicit. You know exactly what `TOGGLE_TODO` does.

### ✅ Testability
You can test the reducer independently:

```javascript
test('ADD_TODO adds a task', () => {
  const state = { todos: [], filter: 'all' };
  const action = { type: 'ADD_TODO', payload: 'New task' };
  const newState = todoReducer(state, action);
  
  expect(newState.todos).toHaveLength(1);
  expect(newState.todos[0].text).toBe('New task');
});
```

### ✅ Scalability
Adding new actions is easy: just add a new `case` to the reducer.

---

## 🆚 Compared with useState

### With useState (multiple functions):

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

// ... more functions
```

### With useReducer (one centralized function):

```jsx
const [state, dispatch] = useReducer(todoReducer, initialState);

// Call actions
dispatch({ type: 'ADD_TODO', payload: text });
dispatch({ type: 'TOGGLE_TODO', payload: id });
dispatch({ type: 'DELETE_TODO', payload: id });
```

Cleaner, especially when there are many actions.

---

## 💡 Common Patterns

### 1. Simple Payload (ID, String, Number)

```javascript
// Action
dispatch({ type: 'DELETE_TODO', payload: 123 });

// In reducer
case 'DELETE_TODO':
  return {
    ...state,
    todos: state.todos.filter(todo => todo.id !== action.payload)
  };
```

### 2. Complex Payload (Object)

```javascript
// Action
dispatch({
  type: 'EDIT_TODO',
  payload: { id: 123, text: 'New text' }
});

// In reducer
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

### 3. No Payload

```javascript
// Action
dispatch({ type: 'CLEAR_COMPLETED' });

// In reducer
case 'CLEAR_COMPLETED':
  return {
    ...state,
    todos: state.todos.filter(todo => !todo.completed)
  };
```

---

## 📝 Practice Exercise

Extend the Todo List with these features:

### New Actions:
1. **`MARK_ALL_COMPLETED`**: Mark all tasks as completed
2. **`SORT_TODOS`**: Sort alphabetically (use payload: 'asc' or 'desc')
3. **`DUPLICATE_TODO`**: Duplicate an existing task (with a new ID)

### Hint:

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

## ⚠️ Common Mistakes

### 1. Mutating state directly

```javascript
// ❌ BAD
case 'ADD_TODO':
  state.todos.push(newTodo); // Mutation!
  return state;

// ✅ GOOD
case 'ADD_TODO':
  return {
    ...state,
    todos: [...state.todos, newTodo]
  };
```

### 2. Forgetting to return the complete state

```javascript
// ❌ BAD: Only returns todos, filter is lost
case 'ADD_TODO':
  return {
    todos: [...state.todos, newTodo]
  };

// ✅ GOOD: Spread the previous state
case 'ADD_TODO':
  return {
    ...state, // Keeps filter and other properties
    todos: [...state.todos, newTodo]
  };
```

### 3. Not using the default case

```javascript
// ❌ BAD: No default
function reducer(state, action) {
  switch (action.type) {
    case 'ADD_TODO':
      return { ...state, /* ... */ };
  }
  // What happens with other actions? undefined!
}

// ✅ GOOD
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

## 🔗 Resources

### Official Documentation
- [useReducer - React Docs](https://react.dev/reference/react/useReducer)
- [Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer)

### 4Geeks Academy
- [What is and How to Use The useReducer Hook](https://4geeks.com/lesson/what-is-usereducer-react)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ useReducer shines with complex state (CRUD operations)
- ✅ All actions are centralized in the reducer
- ✅ Each `case` handles ONE specific action
- ✅ Always use immutability (`...state`, `.map()`, `.filter()`)
- ✅ The payload can be simple or complex depending on what you need
- ✅ It's easier to test than multiple `setState` calls

### Next Step

In **Step 7** you'll learn about the **Context API** to share state (including useReducer's dispatch) between components without prop drilling.

---

**Practice by building your own Todo List with useReducer! 🚀**
