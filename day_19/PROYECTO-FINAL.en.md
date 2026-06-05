[🇪🇸 Español](PROYECTO-FINAL.md) | 🇬🇧 **English**

# 🎓 Final Project: TodoList with API and React

## Description

You'll build a complete TodoList application that connects to a real API to persist data on a server.

## Functional Requirements

### 1. Load Tasks
- ✅ GET `/todos?userId=1` when the component mounts
- ✅ Show "Loading..." while data is being fetched
- ✅ Handle network errors

### 2. Create Tasks
- ✅ POST `/todos` with title, completed, userId
- ✅ Add the new task to the list immediately
- ✅ Clear the input after creating
- ✅ Show an error if it fails

### 3. Update Tasks
- ✅ Allow marking/unmarking as completed
- ✅ PUT `/todos/:id` with the new state
- ✅ Update the UI immediately
- ✅ Show visual feedback (strikethrough) when completed

### 4. Delete Tasks
- ✅ DELETE `/todos/:id`
- ✅ Remove from the UI list
- ✅ Show confirmation or feedback

### 5. UI States
- ✅ **Loading**: Spinner or message while loading
- ✅ **Success**: Show tasks normally
- ✅ **Error**: Show an error message
- ✅ **Creating**: Show "Creating..." on the button while submitting

### 6. General Info
- ✅ Show total number of tasks
- ✅ Show number of completed tasks

## API to Use

**JSONPlaceholder** (free fake API):
- Base URL: `https://jsonplaceholder.typicode.com`
- Endpoints:
  - GET `/todos?userId=1` - Get tasks for user 1
  - POST `/todos` - Create a new task
  - PUT `/todos/:id` - Update a task
  - DELETE `/todos/:id` - Delete a task

## Recommended Structure

```
day_19/
├── PROYECTO-FINAL.md (this file)
├── src/
│   ├── TodoApp.jsx (main component)
│   ├── TodoForm.jsx (form to create)
│   ├── TodoList.jsx (task list)
│   ├── TodoItem.jsx (individual task)
│   └── App.css (styles)
└── index.jsx
```

## Base Component Structure

```javascript
import { useState, useEffect } from 'react';

function TodoApp() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);
  const [creando, setCreando] = useState(false);

  // ❓ TODO: Load tasks in useEffect
  // ❓ TODO: Function to add a task
  // ❓ TODO: Function to complete a task
  // ❓ TODO: Function to delete a task

  if (cargando) return <div className="loading">Loading tasks...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="todo-container">
      <h1>My TodoList</h1>

      {/* Form */}
      <form onSubmit={(e) => {/* agregarTarea */}}>
        <input
          value={nuevaTarea}
          onChange={(e) => setNuevaTarea(e.target.value)}
          placeholder="New task"
          disabled={creando}
        />
        <button disabled={creando}>
          {creando ? 'Creating...' : 'Add'}
        </button>
      </form>

      {/* Stats */}
      <div className="stats">
        <p>Total: {tareas.length}</p>
        <p>Completed: {tareas.filter(t => t.completed).length}</p>
      </div>

      {/* List */}
      <ul className="todo-list">
        {tareas.map(tarea => (
          <li key={tarea.id} className={tarea.completed ? 'completed' : ''}>
            <input
              type="checkbox"
              checked={tarea.completed}
              onChange={() => {/* toggleTarea */}}
            />
            <span>{tarea.title}</span>
            <button onClick={() => {/* eliminarTarea */}}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
```

## Suggested Styles

```css
.todo-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.loading, .error {
  text-align: center;
  padding: 20px;
  margin: 20px 0;
}

.error {
  color: red;
  background: #ffe8e8;
  border-radius: 4px;
}

.todo-list {
  list-style: none;
  padding: 0;
}

.todo-list li {
  display: flex;
  align-items: center;
  padding: 10px;
  margin: 5px 0;
  background: #f5f5f5;
  border-radius: 4px;
  gap: 10px;
}

.todo-list li.completed {
  text-decoration: line-through;
  opacity: 0.6;
}

.stats {
  margin: 20px 0;
  padding: 10px;
  background: #e8f5e9;
  border-radius: 4px;
}

button {
  padding: 8px 12px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

## Implementation Checklist

- [ ] Base component structure with useState
- [ ] useEffect to load tasks on mount
- [ ] States: loading, error, data
- [ ] Show loading and error in the UI
- [ ] Form to create tasks
- [ ] agregarTarea function (POST)
- [ ] completarTarea function (PUT)
- [ ] eliminarTarea function (DELETE)
- [ ] Show task list
- [ ] Show total and completed counters
- [ ] Basic CSS styling
- [ ] Test in the browser
- [ ] No console errors
- [ ] All CRUD operations working

## Optional Improvements

- Edit tasks inline
- Filter (all, active, completed)
- Sort by date or state
- Success message on create
- Loading animations
- Retry failed requests
- Local cache (localStorage as a fallback)
- JWT authentication

## Resources

- JSONPlaceholder: https://jsonplaceholder.typicode.com/
- [React Docs - useEffect](https://react.dev/reference/react/useEffect)
- [Fetch API - MDN](https://developer.mozilla.org/es/docs/Web/API/Fetch_API)

## How to Submit

1. Create a `mi-todolist-api/` folder inside `day_19/`
2. Include:
   - `TodoApp.jsx` - Main component
   - `App.css` - Styles
   - `README.md` - Explanation of your implementation
3. Commit: `git add . && git commit -m "Final project: TodoList with API"`
4. Push: `git push origin main`

---

## Final Reflection

By completing this project, you will have learned:

✅ Promises and Async/Await  
✅ The full Fetch API (GET, POST, PUT, DELETE)  
✅ Integration with React hooks  
✅ State handling (loading, error, success)  
✅ Real CRUD pattern with a server  
✅ UI/UX best practices  

**Congratulations! You can now build professional apps that connect to real APIs.** 🚀
