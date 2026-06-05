[🇪🇸 Español](PROYECTO-FINAL.md) | 🇬🇧 **English**

# 🎓 Final Project: TodoList Application

After completing the 6 steps, it's time to put everything together into a real application.

## Project Requirements

Your TodoList Application must include:

### 1. Core Features
- ✅ Add a new task
- ✅ Mark a task as completed
- ✅ Delete a task
- ✅ Edit a task
- ✅ Show a counter of total and completed tasks

### 2. Validation
- ✅ Disallow empty tasks
- ✅ Disallow duplicate tasks
- ✅ Show clear error messages

### 3. Storage
- ✅ Save tasks in `localStorage`
- ✅ Load tasks when the app starts
- ✅ Data persistence

### 4. UI/UX
- ✅ Clean, intuitive interface
- ✅ Visual indicators for completed tasks (strikethrough, color)
- ✅ Buttons with icons or clear text
- ✅ Responsive design

### 5. Hooks You Must Use
- ✅ `useState` - For task state
- ✅ `useEffect` - For loading/saving to localStorage
- ✅ Manual validation OR React Hook Form
- ✅ Event handling (onChange, onClick)

---

## Suggested Structure

```
day_18/
├── PROYECTO-FINAL.md (this file)
├── MiTodoList.jsx (main component)
├── MiTodoList.css (styles)
└── index.jsx (entry point)
```

---

## Data Structure

Each task should have:

```javascript
{
  id: 1,
  texto: 'Comprar leche',
  completada: false,
  fechaCreacion: '2026-02-01'
}
```

---

## Base Component Example

```javascript
import { useState, useEffect } from 'react';
import './MiTodoList.css';

function MiTodoList() {
  const [tareas, setTareas] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [errores, setErrores] = useState('');

  // Load tasks from localStorage on mount
  useEffect(() => {
    const tareasGuardadas = localStorage.getItem('tareas');
    if (tareasGuardadas) {
      try {
        setTareas(JSON.parse(tareasGuardadas));
      } catch (error) {
        console.error('Error al cargar tareas:', error);
      }
    }
  }, []);

  // Save tasks to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('tareas', JSON.stringify(tareas));
  }, [tareas]);

  // ❓ TODO: Implement functions:
  // - agregarTarea()
  // - eliminarTarea(id)
  // - completarTarea(id)
  // - editarTarea(id, nuevoTexto)
  // - validarTarea(texto)

  return (
    <div className="container">
      <h1>Mi TodoList</h1>
      
      {/* Form */}
      <div className="formulario">
        <input
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Nueva tarea..."
        />
        <button onClick={() => {/* agregarTarea */}}>
          Agregar
        </button>
      </div>

      {/* Errors */}
      {errores && <p className="error">{errores}</p>}

      {/* Counter */}
      <div className="stats">
        <p>Total: {tareas.length}</p>
        <p>Completadas: {tareas.filter(t => t.completada).length}</p>
      </div>

      {/* List */}
      <ul className="lista">
        {tareas.map(tarea => (
          <li key={tarea.id} className={tarea.completada ? 'completada' : ''}>
            <span>{tarea.texto}</span>
            <button onClick={() => {/* completar */}}>✓</button>
            <button onClick={() => {/* editar */}}>✏️</button>
            <button onClick={() => {/* eliminar */}}>✕</button>
          </li>
        ))}
      </ul>

      {tareas.length === 0 && (
        <p className="vacio">No hay tareas. ¡Crea una!</p>
      )}
    </div>
  );
}

export default MiTodoList;
```

---

## Key Points to Remember

### State
```javascript
// Each task needs a unique ID
const agregarTarea = () => {
  const nuevaTarea = {
    id: Date.now(), // unique ID
    texto: inputValue,
    completada: false
  };
  setTareas([...tareas, nuevaTarea]);
};
```

### Validation
```javascript
const validarTarea = (texto) => {
  if (texto.trim() === '') {
    setErrores('La tarea no puede estar vacía');
    return false;
  }
  
  if (tareas.some(t => t.texto === texto)) {
    setErrores('Esta tarea ya existe');
    return false;
  }
  
  setErrores('');
  return true;
};
```

### localStorage
```javascript
// Save
localStorage.setItem('key', JSON.stringify(datos));

// Load
const datos = JSON.parse(localStorage.getItem('key'));
```

### Filtering/Updating Arrays
```javascript
// Delete
const nuevoArray = tareas.filter(t => t.id !== idAEliminar);

// Update
const nuevoArray = tareas.map(t =>
  t.id === idAEditar ? { ...t, completada: !t.completada } : t
);
```

---

## Style Suggestions (CSS)

```css
.container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  font-family: 'Segoe UI', sans-serif;
}

.lista li {
  padding: 15px;
  margin: 10px 0;
  background: #f5f5f5;
  border-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.lista li.completada {
  text-decoration: line-through;
  opacity: 0.6;
  background: #e8f5e9;
}

button {
  padding: 5px 10px;
  margin: 0 5px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  background: #007bff;
  color: white;
}

button:hover {
  background: #0056b3;
}

.error {
  color: red;
  padding: 10px;
  background: #ffe8e8;
  border-radius: 3px;
}

.vacio {
  text-align: center;
  color: #999;
  padding: 20px;
}
```

---

## Advanced Features (Optional)

If you want to go further:

- 🌟 Filter tasks (All / Active / Completed)
- 🌟 Sort tasks (by date, by name)
- 🌟 Categories or tags
- 🌟 Inline task editing
- 🌟 Backend/API persistence
- 🌟 Light/dark theme
- 🌟 Animations on add/delete

---

## Development Checklist

- [ ] Base component structure
- [ ] `useState` for tasks and inputs
- [ ] `useEffect` for localStorage
- [ ] Add task function
- [ ] Delete task function
- [ ] Complete task function
- [ ] Input validation
- [ ] Display tasks in a list
- [ ] Show counter
- [ ] Basic CSS styles
- [ ] Test in browser
- [ ] localStorage persists data
- [ ] No errors in console

---

## How to Submit the Project

1. **Create a folder**: `day_18/mi-proyecto-todolist/`
2. **Include**:
   - `index.jsx` - Main component
   - `index.css` - Styles
   - `README.md` - Features overview
3. **Commit to Git**: `git add . && git commit -m "Proyecto final: TodoList Application"`
4. **Push to GitHub**: `git push origin main`

---

## Reflection Questions

After completing it, answer:

1. What was the hardest part?
2. Which hooks did you use most?
3. How did you handle localStorage?
4. What would you improve in the future?
5. Where did you use useState vs useEffect?

---

## Useful Resources

- [localStorage MDN](https://developer.mozilla.org/es/docs/Web/API/Window/localStorage)
- [useState React Docs](https://react.dev/reference/react/useState)
- [useEffect React Docs](https://react.dev/reference/react/useEffect)

---

## Success 🚀

Completing this project means you have mastered:

✅ React Hooks  
✅ State management  
✅ Validation  
✅ Data persistence  
✅ Event handling  
✅ Arrays and objects in JavaScript  
✅ Basic CSS  

**Congratulations! You're ready for more complex projects.**
