[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 9: TodoList with API 💾

## Final Project

You'll build a TodoList that **persists data in an API**, not just localStorage.

### Requirements

✅ Get tasks from an API  
✅ Create new tasks via the API  
✅ Update tasks (complete/edit)  
✅ Delete tasks from the API  
✅ Show states: loading, success, error  
✅ Sync UI with server  

### Structure

```javascript
import { useState, useEffect } from 'react';

function TodoListAPI() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  // 1. Load tasks on mount
  useEffect(() => {
    cargarTareas();
  }, []);

  // 2. Load function
  async function cargarTareas() {
    try {
      const res = await fetch('https://jsonplaceholder.typicode.com/todos?userId=1');
      if (!res.ok) throw new Error('Error al cargar');
      const datos = await res.json();
      setTareas(datos);
    } catch (err) {
      setError(err.message);
    } finally {
      setCargando(false);
    }
  }

  // 3. Add a new task
  async function agregarTarea(e) {
    e.preventDefault();
    if (!nuevaTarea.trim()) return;

    try {
      const res = await fetch('https://jsonplaceholder.typicode.com/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: nuevaTarea,
          completed: false,
          userId: 1
        })
      });

      if (!res.ok) throw new Error('Error al crear');
      const tarea = await res.json();
      setTareas([...tareas, tarea]);
      setNuevaTarea('');
    } catch (err) {
      setError(err.message);
    }
  }

  // 4. Toggle task completion
  async function toggleTarea(id, completada) {
    try {
      const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed: !completada })
      });

      if (!res.ok) throw new Error('Error al actualizar');
      
      setTareas(tareas.map(t =>
        t.id === id ? { ...t, completed: !t.completed } : t
      ));
    } catch (err) {
      setError(err.message);
    }
  }

  // 5. Delete a task
  async function eliminarTarea(id) {
    try {
      await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`, {
        method: 'DELETE'
      });

      setTareas(tareas.filter(t => t.id !== id));
    } catch (err) {
      setError(err.message);
    }
  }

  // UI
  if (cargando) return <p>Loading tasks...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>TodoList with API</h1>

      <form onSubmit={agregarTarea}>
        <input
          value={nuevaTarea}
          onChange={(e) => setNuevaTarea(e.target.value)}
          placeholder="New task"
        />
        <button>Add</button>
      </form>

      <ul>
        {tareas.map(tarea => (
          <li key={tarea.id} style={{
            textDecoration: tarea.completed ? 'line-through' : 'none'
          }}>
            <input
              type="checkbox"
              checked={tarea.completed}
              onChange={() => toggleTarea(tarea.id, tarea.completed)}
            />
            {tarea.title}
            <button onClick={() => eliminarTarea(tarea.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>

      <p>Total: {tareas.length} | Completed: {tareas.filter(t => t.completed).length}</p>
    </div>
  );
}

export default TodoListAPI;
```

## Key Concepts

### CRUD Operations
- **Create**: POST /todos
- **Read**: GET /todos
- **Update**: PUT /todos/:id
- **Delete**: DELETE /todos/:id

### UI States
```javascript
if (cargando) return <LoadingSpinner />;
if (error) return <ErrorMessage error={error} />;
return <TareasList tareas={tareas} />;
```

### Optimistic Sync
```javascript
// Update UI immediately, then validate with the server
setTareas([...tareas, nuevaTarea]); // Optimistic

fetch(api)
  .then(...)
  .catch(() => {
    // If it fails, roll back
    setTareas(tareas.filter(t => t.id !== nuevaTarea.id));
  });
```

## Common Mistakes

### Mistake 1: Not handling network errors
```javascript
// ❌ BAD
const tareas = await fetch(url).then(r => r.json());

// ✅ GOOD
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error(res.statusText);
  const tareas = await res.json();
} catch (error) {
  console.log('Error:', error);
}
```

### Mistake 2: Out-of-sync state
```javascript
// ❌ BAD - Optimistic but no rollback
setTareas([...tareas, nuevaTarea]);
// If it fails, the task stays in the UI

// ✅ GOOD - With rollback
const tareasAntes = tareas;
setTareas([...tareas, nuevaTarea]);

fetch(...).catch(() => {
  setTareas(tareasAntes);
});
```

### Mistake 3: Race conditions
```javascript
// ❌ BAD - Multiple simultaneous loads
useEffect(() => {
  cargarTareas(); // Runs multiple times
});

// ✅ GOOD - Control loads
useEffect(() => {
  cargarTareas(); // Runs once
}, []);
```

## Optional Improvements

- 🔄 Retry failed requests
- 💾 Local cache (localStorage as a fallback)
- 🔍 Search/Filter
- 📝 Edit tasks inline
- ⏱️ Pagination
- 🔐 Authentication/Tokens

## Key Points ✨

1. **API First**: The server is the source of truth
2. **Clear States**: Loading, Success, Error
3. **Error Handling**: Always handle failures
4. **Responsive UI**: Immediate user feedback
5. **Sync**: UI ↔ Server

## Next Steps

You finished Day 19. You now master:

✅ Promises and Async/Await  
✅ Full Fetch API  
✅ REST APIs  
✅ Integration with React  
✅ Real project with an API  

**You're ready for professional projects!**

---

**💡 Tip**: A professional application uses these patterns. Practice until they become automatic.
