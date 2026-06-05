[🇪🇸 Español](cheatsheet.md) | 🇬🇧 **English**

# useState Cheatsheet - Quick Reference 📋

Quick reference guide for the `useState` Hook in React.

---

## 🎯 Basic Syntax

```jsx
import { useState } from 'react';

const [estado, setEstado] = useState(initialValue);
```

**Parts:**
- `estado` → Variable holding the current value
- `setEstado` → Function to change the value
- `initialValue` → Initial state value

---

## 📦 Common State Types

### Number
```jsx
const [contador, setContador] = useState(0);

// Use
setContador(5);                    // Absolute value
setContador(contador + 1);         // Based on the current value
setContador(prev => prev + 1);     // Functional form (better)
```

### String
```jsx
const [nombre, setNombre] = useState("");

// Use
setNombre("Juan");
setNombre(nombre.toUpperCase());
```

### Boolean
```jsx
const [activo, setActivo] = useState(false);

// Use
setActivo(true);
setActivo(!activo);           // Toggle
```

### Array
```jsx
const [lista, setLista] = useState([]);

// Add
setLista([...lista, nuevoItem]);

// Remove
setLista(lista.filter(item => item.id !== idAEliminar));

// Modify
setLista(lista.map(item => 
    item.id === id ? { ...item, nombre: "Nuevo" } : item
));

// Clear
setLista([]);
```

### Object
```jsx
const [usuario, setUsuario] = useState({ nombre: "", edad: 0 });

// Change one field
setUsuario({ ...usuario, nombre: "Ana" });

// Change multiple fields
setUsuario({ ...usuario, nombre: "Ana", edad: 25 });

// Replace everything
setUsuario({ nombre: "Luis", edad: 30 });
```

---

## 🔄 Common Patterns

### Controlled Input
```jsx
const [texto, setTexto] = useState("");

<input 
    value={texto}
    onChange={(e) => setTexto(e.target.value)}
/>
```

### Toggle
```jsx
const [visible, setVisible] = useState(false);

<button onClick={() => setVisible(!visible)}>
    Toggle
</button>
```

### Counter
```jsx
const [count, setCount] = useState(0);

<button onClick={() => setCount(count + 1)}>+</button>
<button onClick={() => setCount(count - 1)}>-</button>
<button onClick={() => setCount(0)}>Reset</button>
```

### Multiple States
```jsx
const [nombre, setNombre] = useState("");
const [edad, setEdad] = useState(0);
const [email, setEmail] = useState("");
```

### Derived State (no useState needed)
```jsx
const [precio, setPrecio] = useState(100);
const [cantidad, setCantidad] = useState(2);

// ✅ DON'T do this:
// const [total, setTotal] = useState(0);

// ✅ DO this:
const total = precio * cantidad;
```

---

## ⚠️ Important Rules

### ❌ NEVER do this

```jsx
// ❌ Mutate directly
estado = nuevoValor;
estado.push(item);
estado.nombre = "Nuevo";

// ❌ Mutate arrays
lista.push(item);
lista[0] = "Nuevo";

// ❌ Mutate objects
usuario.nombre = "Nuevo";
```

### ✅ ALWAYS do this

```jsx
// ✅ Use setEstado
setEstado(nuevoValor);

// ✅ Copy arrays
setLista([...lista, item]);

// ✅ Copy objects
setUsuario({ ...usuario, nombre: "Nuevo" });
```

---

## 🎨 Conditional Rendering

### If with &&
```jsx
{activo && <p>Estoy activo</p>}
```

### If-Else with the ternary operator
```jsx
{activo ? <p>Activo</p> : <p>Inactivo</p>}
```

### Multiple conditions
```jsx
{count === 0 && <p>Cero</p>}
{count > 0 && count < 10 && <p>Entre 1 y 9</p>}
{count >= 10 && <p>Mayor o igual a 10</p>}
```

---

## 🔢 Functional Form (update based on previous value)

### When to use it?
When the new value depends on the previous value.

```jsx
// ❌ May fail
setCount(count + 1);
setCount(count + 1);  // Only adds 1

// ✅ Always works
setCount(prev => prev + 1);
setCount(prev => prev + 1);  // Adds 2
```

### Examples
```jsx
// With numbers
setContador(prev => prev + 5);
setContador(prev => prev * 2);

// With strings
setTexto(prev => prev + " más texto");

// With arrays
setLista(prev => [...prev, nuevoItem]);

// With objects
setUsuario(prev => ({ ...prev, edad: prev.edad + 1 }));
```

---

## 📝 Common Events

### onClick
```jsx
<button onClick={() => setCount(count + 1)}>
    Click
</button>

// Or with a separate function
const incrementar = () => {
    setCount(count + 1);
};

<button onClick={incrementar}>Click</button>
```

### onChange (inputs)
```jsx
<input 
    value={texto}
    onChange={(e) => setTexto(e.target.value)}
/>
```

### onSubmit (forms)
```jsx
const handleSubmit = (e) => {
    e.preventDefault();
    // Process data
};

<form onSubmit={handleSubmit}>
    {/* inputs */}
</form>
```

### onKeyPress (detect keys)
```jsx
<input 
    onKeyPress={(e) => {
        if (e.key === 'Enter') {
            agregarItem();
        }
    }}
/>
```

---

## 🧩 Working with Arrays

### Add to the end
```jsx
setLista([...lista, nuevoItem]);
```

### Add to the start
```jsx
setLista([nuevoItem, ...lista]);
```

### Remove by index
```jsx
setLista(lista.filter((_, index) => index !== indiceAEliminar));
```

### Remove by ID
```jsx
setLista(lista.filter(item => item.id !== idAEliminar));
```

### Modify an element
```jsx
setLista(lista.map(item => 
    item.id === id 
        ? { ...item, nombre: "Nuevo nombre" } 
        : item
));
```

### Clear
```jsx
setLista([]);
```

---

## 🧩 Working with Objects

### Change one field
```jsx
setUsuario({ ...usuario, nombre: "Nuevo" });
```

### Change a nested field
```jsx
setUsuario({
    ...usuario,
    direccion: {
        ...usuario.direccion,
        ciudad: "Madrid"
    }
});
```

### Increment a number inside the object
```jsx
setUsuario({ ...usuario, edad: usuario.edad + 1 });
```

---

## 🐛 Debugging

### Console.log the state
```jsx
const [count, setCount] = useState(0);

console.log("Current state:", count);
```

### See state changes
```jsx
const incrementar = () => {
    console.log("Before:", count);
    setCount(count + 1);
    console.log("After (not updated yet):", count);
};
```

### useEffect to watch changes (advanced)
```jsx
import { useState, useEffect } from 'react';

useEffect(() => {
    console.log("State changed to:", count);
}, [count]);
```

---

## 💡 Tips and Tricks

### Descriptive names
```jsx
// ❌ Bad
const [x, setX] = useState(0);

// ✅ Good
const [contador, setContador] = useState(0);
```

### Initialize with a function (for expensive computations)
```jsx
// Only runs once
const [estado, setEstado] = useState(() => {
    const valorCalculado = calcularAlgo();
    return valorCalculado;
});
```

### Reset multiple states
```jsx
const resetear = () => {
    setNombre("");
    setEdad(0);
    setEmail("");
};
```

### Simple validation
```jsx
const [email, setEmail] = useState("");
const esValido = email.includes("@");

<button disabled={!esValido}>Enviar</button>
```

---

## 🎯 Full Example

```jsx
import { useState } from 'react';

function TodoApp() {
    const [tareas, setTareas] = useState([]);
    const [inputText, setInputText] = useState("");
    
    const agregarTarea = () => {
        if (inputText.trim() === "") return;
        
        const nuevaTarea = {
            id: Date.now(),
            texto: inputText,
            completada: false
        };
        
        setTareas([...tareas, nuevaTarea]);
        setInputText("");
    };
    
    const toggleCompletada = (id) => {
        setTareas(tareas.map(tarea =>
            tarea.id === id 
                ? { ...tarea, completada: !tarea.completada }
                : tarea
        ));
    };
    
    const eliminarTarea = (id) => {
        setTareas(tareas.filter(tarea => tarea.id !== id));
    };
    
    return (
        <div>
            <h1>Todo List</h1>
            
            <input 
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && agregarTarea()}
            />
            <button onClick={agregarTarea}>Agregar</button>
            
            <ul>
                {tareas.map(tarea => (
                    <li key={tarea.id}>
                        <input 
                            type="checkbox"
                            checked={tarea.completada}
                            onChange={() => toggleCompletada(tarea.id)}
                        />
                        <span style={{
                            textDecoration: tarea.completada ? 'line-through' : 'none'
                        }}>
                            {tarea.texto}
                        </span>
                        <button onClick={() => eliminarTarea(tarea.id)}>
                            🗑️
                        </button>
                    </li>
                ))}
            </ul>
            
            <p>Total: {tareas.length} | Pendientes: {tareas.filter(t => !t.completada).length}</p>
        </div>
    );
}

export default TodoApp;
```

---

## 📚 Resources

- [Official useState docs](https://react.dev/reference/react/useState)
- [Interactive React tutorial](https://react.dev/learn)

---

**Save this cheatsheet and check it whenever you need to! 📌**
