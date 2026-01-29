# useState Cheatsheet - Referencia Rápida 📋

Guía de referencia rápida para el Hook `useState` en React.

---

## 🎯 Sintaxis Básica

```jsx
import { useState } from 'react';

const [estado, setEstado] = useState(valorInicial);
```

**Partes:**
- `estado` → Variable que contiene el valor actual
- `setEstado` → Función para cambiar el valor
- `valorInicial` → Valor inicial del estado

---

## 📦 Tipos de Estado Comunes

### Número
```jsx
const [contador, setContador] = useState(0);

// Usar
setContador(5);                    // Valor absoluto
setContador(contador + 1);         // Basado en valor actual
setContador(prev => prev + 1);     // Forma funcional (mejor)
```

### String (texto)
```jsx
const [nombre, setNombre] = useState("");

// Usar
setNombre("Juan");
setNombre(nombre.toUpperCase());
```

### Boolean
```jsx
const [activo, setActivo] = useState(false);

// Usar
setActivo(true);
setActivo(!activo);           // Toggle (alternar)
```

### Array
```jsx
const [lista, setLista] = useState([]);

// Agregar
setLista([...lista, nuevoItem]);

// Eliminar
setLista(lista.filter(item => item.id !== idAEliminar));

// Modificar
setLista(lista.map(item => 
    item.id === id ? { ...item, nombre: "Nuevo" } : item
));

// Limpiar
setLista([]);
```

### Objeto
```jsx
const [usuario, setUsuario] = useState({ nombre: "", edad: 0 });

// Cambiar un campo
setUsuario({ ...usuario, nombre: "Ana" });

// Cambiar múltiples campos
setUsuario({ ...usuario, nombre: "Ana", edad: 25 });

// Reemplazar todo
setUsuario({ nombre: "Luis", edad: 30 });
```

---

## 🔄 Patrones Comunes

### Input Controlado
```jsx
const [texto, setTexto] = useState("");

<input 
    value={texto}
    onChange={(e) => setTexto(e.target.value)}
/>
```

### Toggle (Alternar)
```jsx
const [visible, setVisible] = useState(false);

<button onClick={() => setVisible(!visible)}>
    Toggle
</button>
```

### Contador
```jsx
const [count, setCount] = useState(0);

<button onClick={() => setCount(count + 1)}>+</button>
<button onClick={() => setCount(count - 1)}>-</button>
<button onClick={() => setCount(0)}>Reset</button>
```

### Múltiples Estados
```jsx
const [nombre, setNombre] = useState("");
const [edad, setEdad] = useState(0);
const [email, setEmail] = useState("");
```

### Estado Derivado (no necesita useState)
```jsx
const [precio, setPrecio] = useState(100);
const [cantidad, setCantidad] = useState(2);

// ✅ NO hagas esto:
// const [total, setTotal] = useState(0);

// ✅ HAZ esto:
const total = precio * cantidad;
```

---

## ⚠️ Reglas Importantes

### ❌ NUNCA hagas esto

```jsx
// ❌ Modificar directamente
estado = nuevoValor;
estado.push(item);
estado.nombre = "Nuevo";

// ❌ Mutar arrays
lista.push(item);
lista[0] = "Nuevo";

// ❌ Mutar objetos
usuario.nombre = "Nuevo";
```

### ✅ SIEMPRE haz esto

```jsx
// ✅ Usar setEstado
setEstado(nuevoValor);

// ✅ Copiar arrays
setLista([...lista, item]);

// ✅ Copiar objetos
setUsuario({ ...usuario, nombre: "Nuevo" });
```

---

## 🎨 Renderizado Condicional

### If con &&
```jsx
{activo && <p>Estoy activo</p>}
```

### If-Else con operador ternario
```jsx
{activo ? <p>Activo</p> : <p>Inactivo</p>}
```

### Múltiples condiciones
```jsx
{count === 0 && <p>Cero</p>}
{count > 0 && count < 10 && <p>Entre 1 y 9</p>}
{count >= 10 && <p>Mayor o igual a 10</p>}
```

---

## 🔢 Forma Funcional (Actualización basada en valor anterior)

### ¿Cuándo usar?
Cuando el nuevo valor depende del valor anterior.

```jsx
// ❌ Puede fallar
setCount(count + 1);
setCount(count + 1);  // Solo suma 1

// ✅ Siempre funciona
setCount(prev => prev + 1);
setCount(prev => prev + 1);  // Suma 2
```

### Ejemplos
```jsx
// Con números
setContador(prev => prev + 5);
setContador(prev => prev * 2);

// Con strings
setTexto(prev => prev + " más texto");

// Con arrays
setLista(prev => [...prev, nuevoItem]);

// Con objetos
setUsuario(prev => ({ ...prev, edad: prev.edad + 1 }));
```

---

## 📝 Eventos Comunes

### onClick
```jsx
<button onClick={() => setCount(count + 1)}>
    Click
</button>

// O con función separada
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

### onSubmit (formularios)
```jsx
const handleSubmit = (e) => {
    e.preventDefault();
    // Procesar datos
};

<form onSubmit={handleSubmit}>
    {/* inputs */}
</form>
```

### onKeyPress (detectar teclas)
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

## 🧩 Trabajando con Arrays

### Agregar al final
```jsx
setLista([...lista, nuevoItem]);
```

### Agregar al inicio
```jsx
setLista([nuevoItem, ...lista]);
```

### Eliminar por índice
```jsx
setLista(lista.filter((_, index) => index !== indiceAEliminar));
```

### Eliminar por ID
```jsx
setLista(lista.filter(item => item.id !== idAEliminar));
```

### Modificar un elemento
```jsx
setLista(lista.map(item => 
    item.id === id 
        ? { ...item, nombre: "Nuevo nombre" } 
        : item
));
```

### Vaciar
```jsx
setLista([]);
```

---

## 🧩 Trabajando con Objetos

### Cambiar un campo
```jsx
setUsuario({ ...usuario, nombre: "Nuevo" });
```

### Cambiar campo anidado
```jsx
setUsuario({
    ...usuario,
    direccion: {
        ...usuario.direccion,
        ciudad: "Madrid"
    }
});
```

### Incrementar un número dentro del objeto
```jsx
setUsuario({ ...usuario, edad: usuario.edad + 1 });
```

---

## 🐛 Debugging

### Console.log del estado
```jsx
const [count, setCount] = useState(0);

console.log("Estado actual:", count);
```

### Ver cambios de estado
```jsx
const incrementar = () => {
    console.log("Antes:", count);
    setCount(count + 1);
    console.log("Después (aún no actualizado):", count);
};
```

### useEffect para ver cambios (avanzado)
```jsx
import { useState, useEffect } from 'react';

useEffect(() => {
    console.log("Estado cambió a:", count);
}, [count]);
```

---

## 💡 Tips y Trucos

### Nombres descriptivos
```jsx
// ❌ Mal
const [x, setX] = useState(0);

// ✅ Bien
const [contador, setContador] = useState(0);
```

### Inicialización con función (para cálculos pesados)
```jsx
// Solo se ejecuta una vez
const [estado, setEstado] = useState(() => {
    const valorCalculado = calcularAlgo();
    return valorCalculado;
});
```

### Resetear múltiples estados
```jsx
const resetear = () => {
    setNombre("");
    setEdad(0);
    setEmail("");
};
```

### Validación simple
```jsx
const [email, setEmail] = useState("");
const esValido = email.includes("@");

<button disabled={!esValido}>Enviar</button>
```

---

## 🎯 Ejemplo Completo

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

## 📚 Recursos

- [Documentación oficial de useState](https://react.dev/reference/react/useState)
- [Tutorial interactivo de React](https://react.dev/learn)

---

**¡Guarda esta cheatsheet y consúltala cuando lo necesites! 📌**
