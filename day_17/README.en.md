[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Tutorial: Component State in React with useState 🎣

## 📺 Reference Videos

- [React Hooks - useState](https://www.youtube.com/watch?v=O6P86uwfdR0)
- [Estado en React explicado](https://www.youtube.com/watch?v=4pO-HcG2igk)
- [Props vs State](https://www.youtube.com/watch?v=IYvD9oBCuJI)

---

## 🎯 What are we learning today?

In this tutorial you'll learn the core concepts of **state** in React:

1. ✅ What is **state** and why do we need it?
2. ✅ The difference between **props** and **state**
3. ✅ How to use the **useState** Hook
4. ✅ How to **update state** correctly
5. ✅ Common patterns with useState
6. ✅ Incremental hands-on exercises

---

## 🤔 Part 1: What is State?

### The problem state solves

On Day 16, we learned how to create components that receive **props** and get re-rendered every second with `setInterval`. But there's a problem:

```jsx
// Day 16 - Without local state
let contador = 0; // ❌ Variable OUTSIDE the component

setInterval(() => {
    contador++;
    root.render(<Contador value={contador} />); // ❌ Manually re-render EVERYTHING
}, 1000);
```

**Problems:**
- ❌ The variable lives outside the component (it's not "its own")
- ❌ You have to call `root.render()` manually every time
- ❌ It doesn't scale (imagine 10 different counters)

### The solution: Local component state

**State** is **a component's own memory** that it can hold and control.

```jsx
// Day 17 - With local state
function Contador() {
    const [contador, setContador] = useState(0); // ✅ State INSIDE the component
    
    // ✅ React re-renders automatically when state changes
    return <h1>{contador}</h1>;
}
```

---

## 🧠 Part 2: Props vs State

### Key differences

| Feature | Props | State |
|----------------|-------|-------|
| **Who controls it?** | The parent component | The component itself |
| **Can it change?** | ❌ No (read-only) | ✅ Yes (via setState) |
| **Where is it defined?** | Outside the component | Inside the component |
| **Is it passed to others?** | ✅ Yes (parent to child) | ❌ No (it's private) |

### Real-world analogy

#### Props = Ingredients you receive

Imagine you're a **chef**:
- Your boss hands you ingredients (props): tomatoes, cheese, pasta
- You **can't change** the ingredients you were given
- You can only **use them** to cook

```jsx
function Chef(props) {
    // props.ingredientes = ["tomate", "queso", "pasta"]
    // I can't do: props.ingredientes = ["chocolate"] ❌
    return <h1>Cocinando con {props.ingredientes}</h1>;
}
```

#### State = Your recipe / cooking process

- **You control** how long you cook (state)
- **You decide** when to add salt (state)
- **You can change** the temperature (state)

```jsx
function Chef() {
    const [temperatura, setTemperatura] = useState(100); // ✅ I can change it
    const [tiempo, setTiempo] = useState(0); // ✅ I can change it
    
    return <h1>Cocinando a {temperatura}° por {tiempo} minutos</h1>;
}
```

### Visual example

```jsx
// Parent component (App)
function App() {
    return <Tarjeta nombre="Ana" edad={25} />; // Passes PROPS
}

// Child component (Tarjeta)
function Tarjeta(props) {
    const [megusta, setMegusta] = useState(0); // Local STATE
    
    return (
        <div>
            <h1>{props.nombre}</h1> {/* Props (from parent) */}
            <p>Edad: {props.edad}</p> {/* Props (from parent) */}
            <p>❤️ Me gusta: {megusta}</p> {/* State (its own) */}
            <button onClick={() => setMegusta(megusta + 1)}>
                Dar like
            </button>
        </div>
    );
}
```

**Result:**
- `nombre` and `edad` come from the parent component → **props**
- `megusta` is controlled by the component itself → **state**

---

## 🎣 Part 3: The useState Hook - Basic Concepts

### What is useState?

`useState` is a **Hook** that gives **memory** to your component.

### Syntax

```jsx
import { useState } from 'react';

function MiComponente() {
    const [variable, setVariable] = useState(initialValue);
    
    return <div>{variable}</div>;
}
```

### Breaking down the syntax

```jsx
const [contador, setContador] = useState(0);
      ↑         ↑                   ↑
      │         │                   │
      │         │                   └─ Initial value (0)
      │         └───────────────────── Function to change the state
      └─────────────────────────────── Variable holding the current state
```

**Important:** The names are up to you, but the convention is:
- Variable: descriptive `name`
- Function: `setName` (set + capitalized name)

### Examples of correct naming

```jsx
const [contador, setContador] = useState(0);
const [nombre, setNombre] = useState("");
const [activo, setActivo] = useState(false);
const [color, setColor] = useState("rojo");
const [usuarios, setUsuarios] = useState([]);
```

---

## 🚀 Part 4: Your First State - Simple Counter

### Step 1: Basic state without interaction

```jsx
import { useState } from 'react';

function Contador() {
    const [numero, setNumero] = useState(0);
    
    return (
        <div>
            <h1>Contador: {numero}</h1>
        </div>
    );
}
```

**Result on screen:**
```
Contador: 0
```

### Step 2: Add a button that changes the state

```jsx
import { useState } from 'react';

function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementar = () => {
        setNumero(numero + 1); // Changes the state
    };
    
    return (
        <div>
            <h1>Contador: {numero}</h1>
            <button onClick={incrementar}>Incrementar</button>
        </div>
    );
}
```

### What happens when you click?

```
1. User clicks the button
   ↓
2. The incrementar() function runs
   ↓
3. setNumero(numero + 1) is called
   ↓
4. React detects that the state changed
   ↓
5. React re-renders the component AUTOMATICALLY
   ↓
6. The new number appears on the screen ✨
```

### Step 3: Multiple buttons

```jsx
import { useState } from 'react';

function Contador() {
    const [numero, setNumero] = useState(0);
    
    return (
        <div>
            <h1>Contador: {numero}</h1>
            <button onClick={() => setNumero(numero + 1)}>
                Incrementar
            </button>
            <button onClick={() => setNumero(numero - 1)}>
                Decrementar
            </button>
            <button onClick={() => setNumero(0)}>
                Reiniciar
            </button>
        </div>
    );
}
```

**⚠️ Note:** You can use inline functions with `onClick={() => ...}` for simple cases.

### ✏️ Exercise 1: Your first counter

Create a `ContadorPersonal` component that:
1. Starts at 10
2. Has a "Sumar 5" button that increases by 5
3. Has a "Restar 5" button that decreases by 5
4. Has a "Reset" button that goes back to 10

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function ContadorPersonal() {
    const [valor, setValor] = useState(10);
    
    return (
        <div>
            <h1>Valor: {valor}</h1>
            <button onClick={() => setValor(valor + 5)}>
                Sumar 5
            </button>
            <button onClick={() => setValor(valor - 5)}>
                Restar 5
            </button>
            <button onClick={() => setValor(10)}>
                Reset
            </button>
        </div>
    );
}
```
</details>

---

## 💡 Part 5: Types of State

### State with Numbers

```jsx
function Edad() {
    const [edad, setEdad] = useState(0);
    
    return (
        <div>
            <p>Edad: {edad} años</p>
            <button onClick={() => setEdad(edad + 1)}>
                Cumplir años
            </button>
        </div>
    );
}
```

### State with Strings (text)

```jsx
function Saludo() {
    const [nombre, setNombre] = useState("");
    
    return (
        <div>
            <input 
                type="text"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                placeholder="Escribe tu nombre"
            />
            <h1>¡Hola, {nombre}!</h1>
        </div>
    );
}
```

**What is `e.target.value`?**
- `e` = the input event
- `e.target` = the input element
- `e.target.value` = the text you typed

### State with Booleans (true/false)

```jsx
function Interruptor() {
    const [encendido, setEncendido] = useState(false);
    
    return (
        <div>
            <h1>La luz está: {encendido ? "🟢 Encendida" : "🔴 Apagada"}</h1>
            <button onClick={() => setEncendido(!encendido)}>
                {encendido ? "Apagar" : "Encender"}
            </button>
        </div>
    );
}
```

**What `!` does:**
- `!` flips the boolean value
- If `encendido = true` → `!encendido = false`
- If `encendido = false` → `!encendido = true`

### State with Arrays (lists)

```jsx
function ListaDeTareas() {
    const [tareas, setTareas] = useState(["Estudiar React", "Hacer ejercicio"]);
    
    const agregarTarea = () => {
        setTareas([...tareas, "Nueva tarea"]);
    };
    
    return (
        <div>
            <ul>
                {tareas.map((tarea, index) => (
                    <li key={index}>{tarea}</li>
                ))}
            </ul>
            <button onClick={agregarTarea}>Agregar tarea</button>
        </div>
    );
}
```

**What is `...tareas`?**
- It's called the "spread operator"
- Copies all the items from the previous array
- Example: `[...tareas, "Nueva"]` = copies all the tasks + adds a new one

### State with Objects

```jsx
function PerfilUsuario() {
    const [usuario, setUsuario] = useState({
        nombre: "Ana",
        edad: 25,
        ciudad: "Madrid"
    });
    
    const cumplirAños = () => {
        setUsuario({
            ...usuario,       // Copy everything from before
            edad: usuario.edad + 1  // But only change the age
        });
    };
    
    return (
        <div>
            <h1>{usuario.nombre}</h1>
            <p>Edad: {usuario.edad}</p>
            <p>Ciudad: {usuario.ciudad}</p>
            <button onClick={cumplirAños}>Cumplir años</button>
        </div>
    );
}
```

---

## ⚠️ Part 6: Important State Rules

### Rule 1: NEVER mutate state directly

```jsx
// ❌ BAD - Doesn't work
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementar = () => {
        numero = numero + 1;  // ❌ Error: you can't change numero directly
    };
    
    return <button onClick={incrementar}>+1</button>;
}

// ✅ GOOD - Use setNumero
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementar = () => {
        setNumero(numero + 1);  // ✅ Correct
    };
    
    return <button onClick={incrementar}>+1</button>;
}
```

### Rule 2: State is asynchronous

```jsx
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementarDosVeces = () => {
        setNumero(numero + 1);
        setNumero(numero + 1); // ❌ Doesn't add 2, only adds 1!
        
        console.log(numero); // ❌ Still shows the OLD value
    };
    
    return <button onClick={incrementarDosVeces}>+2</button>;
}
```

**Why?**
- React **batches** state updates
- It doesn't update immediately

**Solution: Use the functional form**

```jsx
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementarDosVeces = () => {
        setNumero(prev => prev + 1); // ✅ Correct
        setNumero(prev => prev + 1); // ✅ Correct
    };
    
    return <button onClick={incrementarDosVeces}>+2</button>;
}
```

**`prev` explained:**
- `prev` = previous state value
- React guarantees it's always the most up-to-date value

### Rule 3: No mutations with arrays or objects

```jsx
// ❌ BAD - Direct mutation
const agregarTarea = () => {
    tareas.push("Nueva tarea");  // ❌ Mutates the original array
    setTareas(tareas);  // ❌ React doesn't detect the change
};

// ✅ GOOD - Create a new array
const agregarTarea = () => {
    setTareas([...tareas, "Nueva tarea"]);  // ✅ New array
};
```

---

## 🎮 Part 7: Incremental Hands-on Exercises

### Exercise 2: Name field

Create a component that:
- Has an input for typing your name
- Shows "Hola, [name]!" below it
- The greeting updates as you type

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function CampoNombre() {
    const [nombre, setNombre] = useState("");
    
    return (
        <div>
            <input 
                type="text"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                placeholder="Tu nombre"
            />
            <h1>¡Hola, {nombre || "desconocido"}!</h1>
        </div>
    );
}
```
</details>

### Exercise 3: Like button

Create a component that:
- Shows a button with "❤️ Like (0)"
- Each click increases the number of likes
- When it reaches 10, displays "¡Popular!" below

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function BotonLike() {
    const [likes, setLikes] = useState(0);
    
    return (
        <div>
            <button onClick={() => setLikes(likes + 1)}>
                ❤️ Like ({likes})
            </button>
            {likes >= 10 && <p>¡Popular!</p>}
        </div>
    );
}
```
</details>

### Exercise 4: Color changer

Create a component that:
- Displays a square with a background color
- Has buttons: "Rojo", "Azul", "Verde"
- On click, changes the square's color

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function CambiadorColor() {
    const [color, setColor] = useState("gray");
    
    return (
        <div>
            <div 
                style={{
                    width: "200px",
                    height: "200px",
                    backgroundColor: color,
                    border: "2px solid black"
                }}
            />
            <button onClick={() => setColor("red")}>Rojo</button>
            <button onClick={() => setColor("blue")}>Azul</button>
            <button onClick={() => setColor("green")}>Verde</button>
        </div>
    );
}
```
</details>

### Exercise 5: Show/Hide content

Create a component that:
- Has a "Show/Hide" button
- On click, shows or hides a text paragraph

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function MostrarOcultar() {
    const [visible, setVisible] = useState(false);
    
    return (
        <div>
            <button onClick={() => setVisible(!visible)}>
                {visible ? "Ocultar" : "Mostrar"}
            </button>
            
            {visible && (
                <p>
                    ¡Este es el contenido secreto! 🎉
                </p>
            )}
        </div>
    );
}
```
</details>

### Exercise 6: Simple signup form

Create a component with:
- An input for name
- An input for email
- A "Registrar" button
- When you click "Registrar", show the data below

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function FormularioRegistro() {
    const [nombre, setNombre] = useState("");
    const [email, setEmail] = useState("");
    const [registrado, setRegistrado] = useState(false);
    
    const handleRegistro = () => {
        setRegistrado(true);
    };
    
    return (
        <div>
            <h2>Registro</h2>
            <input 
                type="text"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                placeholder="Nombre"
            />
            <br />
            <input 
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
            />
            <br />
            <button onClick={handleRegistro}>Registrar</button>
            
            {registrado && (
                <div>
                    <h3>✅ Registro exitoso</h3>
                    <p>Nombre: {nombre}</p>
                    <p>Email: {email}</p>
                </div>
            )}
        </div>
    );
}
```
</details>

---

## 🎯 Part 8: Project - Interactive Traffic Light

### Project concept

You're going to build a **traffic light** that changes color via buttons or automatically.

```
     ┌───────┐
     │       │
     │  🔴   │  ← Red (default)
     │       │
     ├───────┤
     │       │
     │  🟡   │  ← Yellow
     │       │
     ├───────┤
     │       │
     │  🟢   │  ← Green
     │       │
     └───────┘
```

### Level 1: Basic traffic light with buttons

```jsx
import { useState } from 'react';

function Semaforo() {
    const [colorActivo, setColorActivo] = useState("rojo");
    
    return (
        <div>
            <div style={{ textAlign: "center" }}>
                <div 
                    style={{
                        width: "100px",
                        height: "100px",
                        borderRadius: "50%",
                        backgroundColor: colorActivo === "rojo" ? "red" : "gray",
                        margin: "10px auto",
                        border: "3px solid black"
                    }}
                />
                <div 
                    style={{
                        width: "100px",
                        height: "100px",
                        borderRadius: "50%",
                        backgroundColor: colorActivo === "amarillo" ? "yellow" : "gray",
                        margin: "10px auto",
                        border: "3px solid black"
                    }}
                />
                <div 
                    style={{
                        width: "100px",
                        height: "100px",
                        borderRadius: "50%",
                        backgroundColor: colorActivo === "verde" ? "green" : "gray",
                        margin: "10px auto",
                        border: "3px solid black"
                    }}
                />
            </div>
            
            <div style={{ textAlign: "center", marginTop: "20px" }}>
                <button onClick={() => setColorActivo("rojo")}>Rojo</button>
                <button onClick={() => setColorActivo("amarillo")}>Amarillo</button>
                <button onClick={() => setColorActivo("verde")}>Verde</button>
            </div>
        </div>
    );
}
```

### Level 2: Automatic cycle

Add an "Auto" button that changes the color automatically every 2 seconds.

**Hint:** Use `useEffect` with `setInterval`

```jsx
import { useState, useEffect } from 'react';

function SemaforoAuto() {
    const [colorActivo, setColorActivo] = useState("rojo");
    const [auto, setAuto] = useState(false);
    
    useEffect(() => {
        if (!auto) return;
        
        const intervalo = setInterval(() => {
            setColorActivo(prev => {
                if (prev === "rojo") return "amarillo";
                if (prev === "amarillo") return "verde";
                return "rojo";
            });
        }, 2000);
        
        return () => clearInterval(intervalo);
    }, [auto]);
    
    return (
        <div>
            {/* ... same traffic light HTML ... */}
            
            <button onClick={() => setAuto(!auto)}>
                {auto ? "Detener" : "Automático"}
            </button>
        </div>
    );
}
```

---

## 📚 Part 9: Common Patterns

### Pattern 1: Toggle

```jsx
const [activo, setActivo] = useState(false);

// Toggle between true and false
<button onClick={() => setActivo(!activo)}>
    {activo ? "Activado" : "Desactivado"}
</button>
```

### Pattern 2: Counter with limits

```jsx
const [contador, setContador] = useState(0);

const incrementar = () => {
    if (contador < 10) {
        setContador(contador + 1);
    }
};

const decrementar = () => {
    if (contador > 0) {
        setContador(contador - 1);
    }
};
```

### Pattern 3: Controlled input

```jsx
const [texto, setTexto] = useState("");

<input 
    value={texto}
    onChange={(e) => setTexto(e.target.value)}
/>
```

### Pattern 4: Derived state (computed)

```jsx
const [precio, setPrecio] = useState(100);
const [cantidad, setCantidad] = useState(1);

// You don't need state for this:
const total = precio * cantidad;

return <p>Total: {total}€</p>;
```

### Pattern 5: Reset multiple states

```jsx
const [nombre, setNombre] = useState("");
const [email, setEmail] = useState("");
const [edad, setEdad] = useState(0);

const resetear = () => {
    setNombre("");
    setEmail("");
    setEdad(0);
};
```

---

## 🎓 Concept Summary

| Concept | Description | Example |
|----------|-------------|---------|
| **State** | A component's own memory | `const [x, setX] = useState(0)` |
| **useState** | Hook to create state | `useState(initialValue)` |
| **Props** | Data from the parent (read-only) | `<Card nombre="Ana" />` |
| **setState** | Function to change state | `setContador(5)` |
| **Functional form** | Use the previous state value | `setState(prev => prev + 1)` |
| **Toggle** | Flip a boolean | `setActivo(!activo)` |
| **Spread** | Copy an array/object | `[...array, nuevo]` |

---

## ✅ Learning Checklist

Before moving on to the next day, make sure you can:

- [ ] Understand what state is and what it's for
- [ ] Tell the difference between props and state
- [ ] Use `useState` with different data types
- [ ] Never mutate state directly
- [ ] Use the functional form `setState(prev => ...)`
- [ ] Build components with multiple pieces of state
- [ ] Handle events (onClick, onChange)
- [ ] Create controlled inputs

---

## 🔗 Additional Resources

### Official docs
- [React Docs - useState](https://react.dev/reference/react/useState)
- [React Docs - State: A Component's Memory](https://react.dev/learn/state-a-components-memory)
- [React Docs - Render and Commit](https://react.dev/learn/render-and-commit)

### Recommended tutorials
- [useState in 100 Seconds](https://www.youtube.com/watch?v=O6P86uwfdR0)
- [Thinking in React](https://react.dev/learn/thinking-in-react)

---

## 💡 Final Tips

1. **Practice each type of state**: number, string, boolean, array, object
2. **Don't use state if you don't need it**: If something can be computed, it doesn't need state
3. **One piece of state per concern**: Better to have a few simple states than one complex one
4. **Descriptive names**: `[contador, setContador]` is better than `[c, setC]`

---

## ❓ FAQ

### How many useState can I have in one component?

As many as you need. You can have 1, 5, 10... React has no limit.

```jsx
function MiComponente() {
    const [nombre, setNombre] = useState("");
    const [edad, setEdad] = useState(0);
    const [activo, setActivo] = useState(false);
    const [colores, setColores] = useState([]);
    // ... etc
}
```

### Why use setState instead of just changing the variable?

Because React needs to **know** something changed in order to re-render. If you change the variable directly, React doesn't detect it.

### Can I use state in any component?

Yes, but **only in function components** with Hooks. Class components use `this.state`.

### When to use props vs state?

- **Props**: If the data comes from the parent
- **State**: If the component needs to remember or change the data

---

## 🏆 Final Challenge

Build a **shopping list** app that lets you:
1. Add items via an input and a button
2. Show all items in a list
3. Mark items as bought (strikethrough)
4. Delete items
5. Show the total of pending items

<details>
<summary>💡 See solution</summary>

```jsx
import { useState } from 'react';

function ListaCompras() {
    const [items, setItems] = useState([]);
    const [nuevoItem, setNuevoItem] = useState("");
    
    const agregarItem = () => {
        if (nuevoItem.trim() === "") return;
        
        setItems([
            ...items,
            { id: Date.now(), texto: nuevoItem, comprado: false }
        ]);
        setNuevoItem("");
    };
    
    const toggleComprado = (id) => {
        setItems(items.map(item =>
            item.id === id ? { ...item, comprado: !item.comprado } : item
        ));
    };
    
    const eliminar = (id) => {
        setItems(items.filter(item => item.id !== id));
    };
    
    const pendientes = items.filter(item => !item.comprado).length;
    
    return (
        <div>
            <h1>🛒 Lista de Compras</h1>
            
            <div>
                <input 
                    value={nuevoItem}
                    onChange={(e) => setNuevoItem(e.target.value)}
                    placeholder="Nuevo item"
                    onKeyPress={(e) => e.key === 'Enter' && agregarItem()}
                />
                <button onClick={agregarItem}>Agregar</button>
            </div>
            
            <ul>
                {items.map(item => (
                    <li key={item.id} style={{ marginBottom: "10px" }}>
                        <input 
                            type="checkbox"
                            checked={item.comprado}
                            onChange={() => toggleComprado(item.id)}
                        />
                        <span 
                            style={{
                                textDecoration: item.comprado ? "line-through" : "none",
                                marginLeft: "10px"
                            }}
                        >
                            {item.texto}
                        </span>
                        <button 
                            onClick={() => eliminar(item.id)}
                            style={{ marginLeft: "10px" }}
                        >
                            🗑️
                        </button>
                    </li>
                ))}
            </ul>
            
            <p>Pendientes: {pendientes}</p>
        </div>
    );
}

export default ListaCompras;
```
</details>

---

**Congrats! 🎉 You now understand state in React.**

On the next day, you'll learn about **useEffect** and how to combine state with side effects.

---

**Made with ❤️ for 4Geeks Academy - Cohort España FS PT 129**
