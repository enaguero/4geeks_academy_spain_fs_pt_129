# Step 6: TodoList con API 💾

## Proyecto Final

Construirás un TodoList que **persiste datos en una API**, no solo en localStorage.

### Requisitos

✅ Obtener tareas de una API  
✅ Crear nuevas tareas vía API  
✅ Actualizar tareas (completar/editar)  
✅ Eliminar tareas de la API  
✅ Mostrar estados: cargando, éxito, error  
✅ Sincronizar UI con servidor  

### Estructura

```javascript
import { useState, useEffect } from 'react';

function TodoListAPI() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  // 1. Cargar tareas al montar
  useEffect(() => {
    cargarTareas();
  }, []);

  // 2. Función para cargar
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

  // 3. Agregar nueva tarea
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

  // 4. Completar/Descomplete tarea
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

  // 5. Eliminar tarea
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
  if (cargando) return <p>Cargando tareas...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>TodoList con API</h1>

      <form onSubmit={agregarTarea}>
        <input
          value={nuevaTarea}
          onChange={(e) => setNuevaTarea(e.target.value)}
          placeholder="Nueva tarea"
        />
        <button>Agregar</button>
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
              Eliminar
            </button>
          </li>
        ))}
      </ul>

      <p>Total: {tareas.length} | Completadas: {tareas.filter(t => t.completed).length}</p>
    </div>
  );
}

export default TodoListAPI;
```

## Conceptos Clave

### CRUD Operations
- **Create**: POST /todos
- **Read**: GET /todos
- **Update**: PUT /todos/:id
- **Delete**: DELETE /todos/:id

### Estados de UI
```javascript
if (cargando) return <LoadingSpinner />;
if (error) return <ErrorMessage error={error} />;
return <TareasList tareas={tareas} />;
```

### Sincronización Optimista
```javascript
// Actualizar UI inmediatamente, después validar con servidor
setTareas([...tareas, nuevaTarea]); // Optimista

fetch(api)
  .then(...)
  .catch(() => {
    // Si falla, revertir
    setTareas(tareas.filter(t => t.id !== nuevaTarea.id));
  });
```

## Errores Comunes

### Error 1: No manejar errores de red
```javascript
// ❌ MALO
const tareas = await fetch(url).then(r => r.json());

// ✅ BIEN
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error(res.statusText);
  const tareas = await res.json();
} catch (error) {
  console.log('Error:', error);
}
```

### Error 2: Estado desincronizado
```javascript
// ❌ MALO - Optimista pero sin rollback
setTareas([...tareas, nuevaTarea]);
// Si falla, la tarea se queda en la UI

// ✅ BIEN - Con rollback
const tareasAntes = tareas;
setTareas([...tareas, nuevaTarea]);

fetch(...).catch(() => {
  setTareas(tareasAntes);
});
```

### Error 3: Race conditions
```javascript
// ❌ MALO - Múltiples cargas simultáneas
useEffect(() => {
  cargarTareas(); // Se ejecuta múltiples veces
});

// ✅ BIEN - Controlar cargas
useEffect(() => {
  cargarTareas(); // Se ejecuta una vez
}, []);
```

## Mejoras Opcionales

- 🔄 Reintentar peticiones que fallan
- 💾 Caché local (localStorage como fallback)
- 🔍 Búsqueda/Filtrado
- 📝 Editar tareas inline
- ⏱️ Paginación
- 🔐 Autenticación/Tokens

## Puntos Clave ✨

1. **API First**: El servidor es fuente de verdad
2. **Estados Claros**: Loading, Success, Error
3. **Error Handling**: Siempre manejar fallos
4. **UI Responsiva**: Feedback inmediato del usuario
5. **Sincronización**: UI ↔ Servidor

## Próximos Pasos

Completaste el Día 19. Ahora dominas:

✅ Promises y Async/Await  
✅ Fetch API completa  
✅ REST APIs  
✅ Integración con React  
✅ Proyecto real con API  

**¡Estás listo para proyectos profesionales!**

---

**💡 Consejo**: Una aplicación profesional tiene estos patrones. Practica hasta hacerlos automáticos.
