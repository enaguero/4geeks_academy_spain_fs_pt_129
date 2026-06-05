🇪🇸 **Español** | [🇬🇧 English](PROYECTO-FINAL.en.md)

# 🎓 Proyecto Final: TodoList Application

Después de completar los 6 pasos, ahora es momento de poner todo junto en una aplicación real.

## Requisitos del Proyecto

Tu TodoList Application debe incluir:

### 1. Funcionalidades Core
- ✅ Agregar una tarea nueva
- ✅ Marcar tarea como completada
- ✅ Eliminar una tarea
- ✅ Editar una tarea
- ✅ Mostrar contador de tareas totales y completadas

### 2. Validación
- ✅ No permitir tareas vacías
- ✅ No permitir tareas duplicadas
- ✅ Mostrar mensajes de error claros

### 3. Almacenamiento
- ✅ Guardar tareas en `localStorage`
- ✅ Cargar tareas al iniciar la app
- ✅ Persistencia de datos

### 4. UI/UX
- ✅ Interfaz limpia y intuitiva
- ✅ Indicadores visuales de completadas (tachado, color)
- ✅ Botones con iconos o texto claro
- ✅ Diseño responsivo

### 5. Hooks que Debes Usar
- ✅ `useState` - Para el estado de tareas
- ✅ `useEffect` - Para cargar/guardar en localStorage
- ✅ Validación manual O React Hook Form
- ✅ Manejo de eventos (onChange, onClick)

---

## Estructura Sugerida

```
day_18/
├── PROYECTO-FINAL.md (este archivo)
├── MiTodoList.jsx (componente principal)
├── MiTodoList.css (estilos)
└── index.jsx (entrada)
```

---

## Estructura de Datos

Cada tarea debe tener:

```javascript
{
  id: 1,
  texto: 'Comprar leche',
  completada: false,
  fechaCreacion: '2026-02-01'
}
```

---

## Ejemplo de Componente Base

```javascript
import { useState, useEffect } from 'react';
import './MiTodoList.css';

function MiTodoList() {
  const [tareas, setTareas] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [errores, setErrores] = useState('');

  // Cargar tareas de localStorage al montar
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

  // Guardar tareas en localStorage cuando cambian
  useEffect(() => {
    localStorage.setItem('tareas', JSON.stringify(tareas));
  }, [tareas]);

  // ❓ TODO: Implementar funciones:
  // - agregarTarea()
  // - eliminarTarea(id)
  // - completarTarea(id)
  // - editarTarea(id, nuevoTexto)
  // - validarTarea(texto)

  return (
    <div className="container">
      <h1>Mi TodoList</h1>
      
      {/* Formulario */}
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

      {/* Errores */}
      {errores && <p className="error">{errores}</p>}

      {/* Contador */}
      <div className="stats">
        <p>Total: {tareas.length}</p>
        <p>Completadas: {tareas.filter(t => t.completada).length}</p>
      </div>

      {/* Lista */}
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

## Puntos Clave a Recordar

### Estado
```javascript
// Cada tarea necesita un ID único
const agregarTarea = () => {
  const nuevaTarea = {
    id: Date.now(), // ID único
    texto: inputValue,
    completada: false
  };
  setTareas([...tareas, nuevaTarea]);
};
```

### Validación
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
// Guardar
localStorage.setItem('key', JSON.stringify(datos));

// Cargar
const datos = JSON.parse(localStorage.getItem('key'));
```

### Filtrar/Actualizar Arrays
```javascript
// Eliminar
const nuevoArray = tareas.filter(t => t.id !== idAEliminar);

// Actualizar
const nuevoArray = tareas.map(t =>
  t.id === idAEditar ? { ...t, completada: !t.completada } : t
);
```

---

## Sugerencias de Estilos (CSS)

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

## Funcionalidades Avanzadas (Opcionales)

Si quieres ir más allá:

- 🌟 Filtrar tareas (Todas / Activas / Completadas)
- 🌟 Ordenar tareas (por fecha, por nombre)
- 🌟 Categorías o etiquetas
- 🌟 Editar tareas inline
- 🌟 Persistencia en backend/API
- 🌟 Tema claro/oscuro
- 🌟 Animaciones al agregar/eliminar

---

## Checklist de Desarrollo

- [ ] Estructura base del componente
- [ ] `useState` para tareas e inputs
- [ ] `useEffect` para localStorage
- [ ] Función agregar tarea
- [ ] Función eliminar tarea
- [ ] Función completar tarea
- [ ] Validación de inputs
- [ ] Mostrar tareas en lista
- [ ] Mostrar contador
- [ ] Estilos CSS básicos
- [ ] Prueba en navegador
- [ ] localStorage persiste datos
- [ ] Sin errores en consola

---

## Cómo Presentar el Proyecto

1. **Crea una carpeta**: `day_18/mi-proyecto-todolist/`
2. **Incluye**:
   - `index.jsx` - Componente principal
   - `index.css` - Estilos
   - `README.md` - Explicación de features
3. **Commit a Git**: `git add . && git commit -m "Proyecto final: TodoList Application"`
4. **Pushea a GitHub**: `git push origin main`

---

## Preguntas de Reflexión

Después de completar, responde:

1. ¿Qué fue lo más difícil?
2. ¿Qué hooks usaste más?
3. ¿Cómo manejaste localStorage?
4. ¿Qué mejorarías en el futuro?
5. ¿Dónde usaste useState vs useEffect?

---

## Recursos Útiles

- [localStorage MDN](https://developer.mozilla.org/es/docs/Web/API/Window/localStorage)
- [useState React Docs](https://react.dev/reference/react/useState)
- [useEffect React Docs](https://react.dev/reference/react/useEffect)

---

## Éxito 🚀

Completar este proyecto significa que has dominado:

✅ Hooks de React  
✅ Gestión de estado  
✅ Validación  
✅ Persistencia de datos  
✅ Manejo de eventos  
✅ Arrays y objetos en JavaScript  
✅ CSS básico  

**¡Felicitaciones! Estás listo para proyectos más complejos.**
