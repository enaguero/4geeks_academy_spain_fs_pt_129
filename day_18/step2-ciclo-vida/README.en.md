[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 2: Component Lifecycle 🔄

## What is the Lifecycle?

The lifecycle is the set of phases a React component goes through from creation to destruction.

## The 3 Lifecycle Phases

### 1️⃣ Mounting 🚀
The component is created and appears on the screen

**Events that occur**:
- The component renders for the first time
- Initial data loads
- You can set up subscriptions (listeners, API calls, etc.)

**useEffect equivalent**:
```javascript
useEffect(() => {
  console.log('Componente montado!');
}, []); // Empty array = only on mount
```

---

### 2️⃣ Updating 🔄
The component detects changes and updates

**Events that occur**:
- State changes
- Props change
- The component re-renders
- You can react to changes

**useEffect equivalent**:
```javascript
useEffect(() => {
  console.log('El componente se actualizó!');
}, [dependencia]); // With dependencies
```

---

### 3️⃣ Unmounting 🗑️
The component disappears from the screen

**Events that occur**:
- The component is removed from the screen
- Resources are cleaned up (listeners, intervals, etc.)
- API connections are closed

**useEffect equivalent**:
```javascript
useEffect(() => {
  return () => {
    console.log('Componente desmontado!');
    // Clean up resources here
  };
}, []);
```

---

## Concrete Lifecycle Examples

### Example 1: The 3 phases in one component

**File**: `Ejemplo1-TresFases.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo1TresFases() {
  const [contador, setContador] = useState(0);

  // PHASE 1: MOUNT
  useEffect(() => {
    console.log('📍 MONTAJE - Componente creado');
    console.log('El componente aparece por primera vez en la pantalla');
  }, []);

  // PHASE 2: UPDATE
  useEffect(() => {
    console.log(`📍 ACTUALIZACIÓN - Contador ahora es: ${contador}`);
    console.log('El componente se actualizó porque el estado cambió');
  }, [contador]);

  // PHASE 3: UNMOUNT
  useEffect(() => {
    return () => {
      console.log('📍 DESMONTAJE - Componente eliminado');
      console.log('El componente desaparece de la pantalla');
    };
  }, []);

  return (
    <div>
      <h2>Contador: {contador}</h2>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>
      <p>Abre la consola para ver las fases</p>
    </div>
  );
}

export default Ejemplo1TresFases;
```

**How to test**:
1. Open the console (F12)
2. The component mounts → you see "MONTAJE"
3. Click → you see "ACTUALIZACIÓN"
4. Navigate away or reload → you see "DESMONTAJE"

---

### Example 2: Loading data on mount

**File**: `Ejemplo2-CargarDatos.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo2CargarDatos() {
  const [usuarios, setUsuarios] = useState([]);
  const [cargando, setCargando] = useState(true);

  // Runs only on MOUNT
  useEffect(() => {
    console.log('Cargando datos...');
    
    // Simulate fetching data from an API
    setTimeout(() => {
      const datosSimulados = [
        { id: 1, nombre: 'Juan' },
        { id: 2, nombre: 'María' },
        { id: 3, nombre: 'Carlos' }
      ];
      
      setUsuarios(datosSimulados);
      setCargando(false);
      console.log('✅ Datos cargados');
    }, 2000); // Wait 2 seconds
  }, []); // Only on mount

  if (cargando) {
    return <p>⏳ Cargando usuarios...</p>;
  }

  return (
    <div>
      <h2>Usuarios:</h2>
      <ul>
        {usuarios.map(user => (
          <li key={user.id}>{user.nombre}</li>
        ))}
      </ul>
    </div>
  );
}

export default Ejemplo2CargarDatos;
```

**Phase**: MOUNT  
**Use**: Load initial data when the component appears

---

### Example 3: Cleaning up on unmount

**File**: `Ejemplo3-Limpiar.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo3Limpiar() {
  const [escuchando, setEscuchando] = useState(false);

  useEffect(() => {
    if (!escuchando) return;

    console.log('📡 Listener activado');
    
    const handleClick = () => {
      console.log('El usuario hizo click en la ventana');
    };

    // MOUNT: Add listener
    window.addEventListener('click', handleClick);

    // UNMOUNT: Remove listener
    return () => {
      console.log('🗑️ Listener removido');
      window.removeEventListener('click', handleClick);
    };
  }, [escuchando]);

  return (
    <div>
      <button onClick={() => setEscuchando(!escuchando)}>
        {escuchando ? 'Dejar de escuchar' : 'Escuchar clicks'}
      </button>
      {escuchando && <p>Haz click en la pantalla</p>}
    </div>
  );
}

export default Ejemplo3Limpiar;
```

**Phases**: MOUNT and UNMOUNT  
**Use**: Add a listener on mount, remove it on unmount to avoid memory leaks

---

### Example 4: Responding to changes

**File**: `Ejemplo4-ResponderCambios.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo4ResponderCambios() {
  const [tema, setTema] = useState('claro');
  const [ancho, setAncho] = useState(window.innerWidth);

  // React to theme changes
  useEffect(() => {
    console.log(`Tema cambió a: ${tema}`);
    document.body.style.backgroundColor = tema === 'claro' ? 'white' : 'black';
    document.body.style.color = tema === 'claro' ? 'black' : 'white';
  }, [tema]); // Runs when tema changes

  // React to window size changes
  useEffect(() => {
    const handleResize = () => {
      setAncho(window.innerWidth);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // Only mount/unmount

  return (
    <div>
      <button onClick={() => setTema(tema === 'claro' ? 'oscuro' : 'claro')}>
        Cambiar a {tema === 'claro' ? 'oscuro' : 'claro'}
      </button>
      <p>Ancho de ventana: {ancho}px</p>
      <p>Tema: {tema}</p>
    </div>
  );
}

export default Ejemplo4ResponderCambios;
```

**Phases**: MOUNT and UPDATE  
**Use**: Take action when the user changes something

---

## Lifecycle Diagram

```
┌─────────────────────────────────────────────────┐
│                    LIFECYCLE                    │
└─────────────────────────────────────────────────┘

         ┌──────────────────┐
         │  1️⃣ MOUNTING    │
         │  (First render)  │
         └────────┬─────────┘
                  ↓
    ┌─────────────────────────────────┐
    │  Component appears on screen     │
    │  - Load initial data             │
    │  - Activate listeners            │
    │  - Initialize variables          │
    └────────────┬────────────────────┘
                 ↓
         ┌──────────────────┐
         │  2️⃣ UPDATING    │
         │  (Re-renders)    │
         └────────┬─────────┘
                  ↓
    ┌─────────────────────────────────┐
    │  Component updates               │
    │  - State changes                 │
    │  - Props change                  │
    │  - The effect runs               │
    └────────────┬────────────────────┘
                 ↓ (when it disappears)
         ┌──────────────────┐
         │  3️⃣ UNMOUNTING  │
         │  (Last render)   │
         └────────┬─────────┘
                  ↓
    ┌─────────────────────────────────┐
    │  Component disappears            │
    │  - Clean up listeners            │
    │  - Close API connections         │
    │  - Cancel timers                 │
    └─────────────────────────────────┘
```

---

## Summary Table: useEffect per phase

| Phase | Code | When | Use |
|-------|------|------|-----|
| **MOUNT** | `useEffect(() => {...}, [])` | Once, on mount | Load data, attach listeners |
| **UPDATE** | `useEffect(() => {...}, [var])` | When var changes | React to changes |
| **UNMOUNT** | `return () => {...}` inside useEffect | On disappear | Clean up resources |

---

## Key Points ✨

1. **Mount**: The component is born (appears on screen)
2. **Update**: The component changes (state or props)
3. **Unmount**: The component dies (disappears)
4. **Cleanup is critical**: Prevents memory leaks and errors
5. **useEffect handles everything**: Replaces the lifecycle methods of classes

---

## Common Errors ⚠️

### Error 1: Forgetting cleanup
```javascript
// ❌ BAD - No cleanup
useEffect(() => {
  window.addEventListener('scroll', handler);
  // What if the component unmounts?
}, []);

// ✅ GOOD - With cleanup
useEffect(() => {
  window.addEventListener('scroll', handler);
  return () => {
    window.removeEventListener('scroll', handler);
  };
}, []);
```

### Error 2: Infinite loop in updates
```javascript
// ❌ BAD
const [count, setCount] = useState(0);
useEffect(() => {
  setCount(count + 1); // No dependencies = infinite loop
});

// ✅ GOOD
useEffect(() => {
  console.log(count);
}, [count]);
```

### Error 3: Losing the reference in cleanup
```javascript
// ❌ BAD - No access to the variable
useEffect(() => {
  const timer = setTimeout(() => {}, 1000);
  // ... code ...
}, []);

// ✅ GOOD - Keep the reference
useEffect(() => {
  const timer = setTimeout(() => {}, 1000);
  return () => {
    clearTimeout(timer);
  };
}, []);
```

---

## Your Exercise 🎯

Create a file `MiEjercicio.jsx` that implements the 3 phases:

**Requirements**:
1. ✅ On **MOUNT**: Print "Componente cargado" to the console
2. ✅ On **UPDATE**: When you change an input, print the value
3. ✅ On **UNMOUNT**: Print "Limpiando recursos"
4. ✅ Use a controlled `input` so you can see the update

**Hint**:
- You'll need a `useState` for the input
- You'll need multiple `useEffect`s (one per phase)
- What is the dependency array for each one?

---

## Next Steps

Once you understand:

✅ The 3 lifecycle phases  
✅ When each one happens  
✅ How to clean up on unmount  

You'll be ready for:
- **Step 3**: Combining useState + useEffect in real apps
- **Step 4**: Building forms

---

## Resources

- [React Lifecycle](https://react.dev/learn/lifecycle-of-reactive-effects)
- [useEffect in React](https://react.dev/reference/react/useEffect)

---

**💡 Tip**: Visualize the lifecycle. Picture the component as a person: born (mount), alive (update), gone (unmount).
