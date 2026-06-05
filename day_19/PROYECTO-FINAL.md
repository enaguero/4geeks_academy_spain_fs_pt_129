🇪🇸 **Español** | [🇬🇧 English](PROYECTO-FINAL.en.md)

# 🎓 Proyecto Final: TodoList con API y React

## Descripción

Crearás una aplicación TodoList completa que se conecta con una API real para persistir datos en un servidor.

## Requisitos Funcionales

### 1. Cargar Tareas
- ✅ GET a `/todos?userId=1` al montar el componente
- ✅ Mostrar "Cargando..." mientras se obtienen datos
- ✅ Manejar errores de red

### 2. Crear Tareas
- ✅ POST a `/todos` con title, completed, userId
- ✅ Añadir la nueva tarea a la lista inmediatamente
- ✅ Limpiar el input después de crear
- ✅ Mostrar error si falla

### 3. Actualizar Tareas
- ✅ Permitir marcar/desmarcar como completada
- ✅ PUT a `/todos/:id` con el nuevo estado
- ✅ Actualizar UI inmediatamente
- ✅ Mostrar visual (tachado) cuando está completada

### 4. Eliminar Tareas
- ✅ DELETE a `/todos/:id`
- ✅ Remover de la lista UI
- ✅ Mostrar confirmación o feedback

### 5. Estados de UI
- ✅ **Cargando**: Spinner o mensaje mientras carga
- ✅ **Éxito**: Mostrar tareas normalmente
- ✅ **Error**: Mostrar mensaje de error
- ✅ **Crear**: Mostrar "Creando..." en botón mientras se envía

### 6. Información General
- ✅ Mostrar total de tareas
- ✅ Mostrar cantidad de completadas

## API a Usar

**JSONPlaceholder** (API Fake gratuita):
- Base URL: `https://jsonplaceholder.typicode.com`
- Endpoints:
  - GET `/todos?userId=1` - Obtener tareas del usuario 1
  - POST `/todos` - Crear nueva tarea
  - PUT `/todos/:id` - Actualizar tarea
  - DELETE `/todos/:id` - Eliminar tarea

## Estructura Recomendada

```
day_19/
├── PROYECTO-FINAL.md (este archivo)
├── src/
│   ├── TodoApp.jsx (componente principal)
│   ├── TodoForm.jsx (formulario para crear)
│   ├── TodoList.jsx (lista de tareas)
│   ├── TodoItem.jsx (tarea individual)
│   └── App.css (estilos)
└── index.jsx
```

## Estructura Base del Componente

```javascript
import { useState, useEffect } from 'react';

function TodoApp() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);
  const [creando, setCreando] = useState(false);

  // ❓ TODO: Cargar tareas en useEffect
  // ❓ TODO: Función para agregar tarea
  // ❓ TODO: Función para completar tarea
  // ❓ TODO: Función para eliminar tarea

  if (cargando) return <div className="loading">Cargando tareas...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="todo-container">
      <h1>Mi TodoList</h1>

      {/* Formulario */}
      <form onSubmit={(e) => {/* agregarTarea */}}>
        <input
          value={nuevaTarea}
          onChange={(e) => setNuevaTarea(e.target.value)}
          placeholder="Nueva tarea"
          disabled={creando}
        />
        <button disabled={creando}>
          {creando ? 'Creando...' : 'Agregar'}
        </button>
      </form>

      {/* Stats */}
      <div className="stats">
        <p>Total: {tareas.length}</p>
        <p>Completadas: {tareas.filter(t => t.completed).length}</p>
      </div>

      {/* Lista */}
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
              Eliminar
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
```

## Estilos Sugeridos

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

## Checklist de Implementación

- [ ] Estructura base del componente con useState
- [ ] useEffect para cargar tareas al montar
- [ ] Estados: cargando, error, datos
- [ ] Mostrar loading y error en UI
- [ ] Formulario para crear tareas
- [ ] Función agregarTarea (POST)
- [ ] Función completarTarea (PUT)
- [ ] Función eliminarTarea (DELETE)
- [ ] Mostrar lista de tareas
- [ ] Mostrar contador de total y completadas
- [ ] Estilos CSS básicos
- [ ] Prueba en navegador
- [ ] Sin errores en consola
- [ ] Todas las operaciones CRUD funcionan

## Mejoras Opcionales

- Editar tareas inline
- Filtrar (todas, activas, completadas)
- Ordenar por fecha o estado
- Mensaje de éxito al crear
- Animaciones de carga
- Reintentar peticiones fallidas
- Caché local (localStorage como fallback)
- Autenticación con JWT

## Recursos

- JSONPlaceholder: https://jsonplaceholder.typicode.com/
- [React Docs - useEffect](https://react.dev/reference/react/useEffect)
- [Fetch API - MDN](https://developer.mozilla.org/es/docs/Web/API/Fetch_API)

## Cómo Presentar

1. Crea carpeta `mi-todolist-api/` en `day_19/`
2. Incluye:
   - `TodoApp.jsx` - Componente principal
   - `App.css` - Estilos
   - `README.md` - Explicación de tu implementación
3. Commit: `git add . && git commit -m "Proyecto final: TodoList con API"`
4. Push: `git push origin main`

---

## Reflexión Final

Al completar este proyecto, habrás aprendido:

✅ Promesas y Async/Await  
✅ Fetch API completa (GET, POST, PUT, DELETE)  
✅ Integración con React hooks  
✅ Manejo de estados (loading, error, success)  
✅ Patrón CRUD real con servidor  
✅ Buenas prácticas de UI/UX  

**¡Felicitaciones! Ahora puedes construir aplicaciones profesionales que se conectan con APIs reales.** 🚀
