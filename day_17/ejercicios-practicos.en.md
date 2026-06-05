[🇪🇸 Español](ejercicios-practicos.md) | 🇬🇧 **English**

# Hands-on Exercises - useState 🎮

This document contains incremental exercises to master `useState` step by step.

---

## 🎯 Level 1: Absolute Beginner

### Exercise 1.1: Click Counter
**Goal**: Learn the basic useState pattern

**Requirements**:
- Display a number that starts at 0
- A button labeled "Click"
- Each click increases the number by 1

**Starter template**:
```jsx
import { useState } from 'react';

function ClickCounter() {
    // Your code here
    
    return (
        <div>
            {/* Your HTML here */}
        </div>
    );
}

export default ClickCounter;
```

<details>
<summary>💡 Hint</summary>

You need to:
1. Create a state with `useState(0)`
2. Display the state's value
3. Create a button with `onClick` that increments the state
</details>

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function ClickCounter() {
    const [clicks, setClicks] = useState(0);
    
    return (
        <div>
            <h1>Clicks: {clicks}</h1>
            <button onClick={() => setClicks(clicks + 1)}>
                Click
            </button>
        </div>
    );
}

export default ClickCounter;
```
</details>

---

### Exercise 1.2: Dynamic Name
**Goal**: Work with controlled inputs

**Requirements**:
- An input where you type your name
- Below it, show "Hola, [name]!"
- If nothing is typed, show "Hola, invitado!"

<details>
<summary>💡 Hint</summary>

You need:
1. A `string` state initialized as empty
2. An `<input>` with `value={state}` and `onChange`
3. Conditional rendering using `||` or the ternary operator
</details>

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function NombreDinamico() {
    const [nombre, setNombre] = useState("");
    
    return (
        <div>
            <input 
                type="text"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                placeholder="Escribe tu nombre"
            />
            <h1>¡Hola, {nombre || "invitado"}!</h1>
        </div>
    );
}

export default NombreDinamico;
```
</details>

---

### Exercise 1.3: On/Off Button
**Goal**: Work with booleans and conditionals

**Requirements**:
- A button that says "Encender" or "Apagar"
- A message saying "💡 Luz encendida" or "🌑 Luz apagada"
- The background color should change (yellow when on, black when off)

<details>
<summary>💡 Hint</summary>

You need:
1. A boolean state
2. Use `!state` to flip the value
3. Use the ternary `? :` to switch the text
4. Use `style={{ backgroundColor: ... }}` to change the color
</details>

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function BotonOnOff() {
    const [encendida, setEncendida] = useState(false);
    
    return (
        <div 
            style={{
                backgroundColor: encendida ? "yellow" : "black",
                color: encendida ? "black" : "white",
                padding: "20px",
                borderRadius: "10px"
            }}
        >
            <h1>{encendida ? "💡 Luz encendida" : "🌑 Luz apagada"}</h1>
            <button onClick={() => setEncendida(!encendida)}>
                {encendida ? "Apagar" : "Encender"}
            </button>
        </div>
    );
}

export default BotonOnOff;
```
</details>

---

## 🎯 Level 2: Beginner with Practice

### Exercise 2.1: Tip Calculator
**Goal**: Multiple pieces of state and derived calculations

**Requirements**:
- Input for the bill total
- Buttons: "10%", "15%", "20%" to pick a tip
- Show: Original total, Tip, Final total

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function CalculadoraPropina() {
    const [total, setTotal] = useState(0);
    const [porcentaje, setPorcentaje] = useState(0);
    
    const propina = (total * porcentaje) / 100;
    const totalFinal = total + propina;
    
    return (
        <div>
            <h2>Calculadora de Propina</h2>
            
            <input 
                type="number"
                value={total}
                onChange={(e) => setTotal(Number(e.target.value))}
                placeholder="Total de la cuenta"
            />
            
            <div>
                <button onClick={() => setPorcentaje(10)}>10%</button>
                <button onClick={() => setPorcentaje(15)}>15%</button>
                <button onClick={() => setPorcentaje(20)}>20%</button>
            </div>
            
            <div>
                <p>Total original: {total.toFixed(2)}€</p>
                <p>Propina ({porcentaje}%): {propina.toFixed(2)}€</p>
                <p><strong>Total final: {totalFinal.toFixed(2)}€</strong></p>
            </div>
        </div>
    );
}

export default CalculadoraPropina;
```
</details>

---

### Exercise 2.2: Color Picker
**Goal**: State with multiple options

**Requirements**:
- A large square that displays a color
- Buttons: Red, Blue, Green, Yellow, Purple
- Clicking a button changes the square's color
- Show the current color's name

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function SelectorColor() {
    const [color, setColor] = useState("gray");
    
    const colores = {
        rojo: "red",
        azul: "blue",
        verde: "green",
        amarillo: "yellow",
        morado: "purple"
    };
    
    return (
        <div style={{ textAlign: "center" }}>
            <h2>Color actual: {color}</h2>
            
            <div 
                style={{
                    width: "300px",
                    height: "300px",
                    backgroundColor: color,
                    margin: "20px auto",
                    border: "3px solid black",
                    borderRadius: "10px"
                }}
            />
            
            <div>
                {Object.entries(colores).map(([nombre, valor]) => (
                    <button 
                        key={nombre}
                        onClick={() => setColor(valor)}
                        style={{ margin: "5px" }}
                    >
                        {nombre.charAt(0).toUpperCase() + nombre.slice(1)}
                    </button>
                ))}
            </div>
        </div>
    );
}

export default SelectorColor;
```
</details>

---

### Exercise 2.3: Counter with Limits
**Goal**: Conditional logic in state

**Requirements**:
- A counter that goes from 0 to 10
- A "+" button (only works if below 10)
- A "-" button (only works if above 0)
- A "Reset" button (goes back to 0)
- When it reaches 10, show "¡Máximo alcanzado!"
- When at 0, show "En el mínimo"

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function ContadorLimites() {
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
    
    return (
        <div style={{ textAlign: "center" }}>
            <h1>Contador: {contador}</h1>
            
            {contador === 10 && <p style={{ color: "red" }}>¡Máximo alcanzado!</p>}
            {contador === 0 && <p style={{ color: "blue" }}>En el mínimo</p>}
            
            <button onClick={decrementar} disabled={contador === 0}>
                -
            </button>
            <button onClick={() => setContador(0)}>
                Reset
            </button>
            <button onClick={incrementar} disabled={contador === 10}>
                +
            </button>
        </div>
    );
}

export default ContadorLimites;
```
</details>

---

## 🎯 Level 3: Intermediate

### Exercise 3.1: Simple Todo List
**Goal**: Work with arrays

**Requirements**:
- An input to type a task
- An "Agregar" button
- Show all tasks in a list
- An "Eliminar" button on each task

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function ListaTareas() {
    const [tareas, setTareas] = useState([]);
    const [nuevaTarea, setNuevaTarea] = useState("");
    
    const agregarTarea = () => {
        if (nuevaTarea.trim() === "") return;
        
        setTareas([...tareas, { id: Date.now(), texto: nuevaTarea }]);
        setNuevaTarea("");
    };
    
    const eliminarTarea = (id) => {
        setTareas(tareas.filter(tarea => tarea.id !== id));
    };
    
    return (
        <div>
            <h2>Lista de Tareas</h2>
            
            <div>
                <input 
                    value={nuevaTarea}
                    onChange={(e) => setNuevaTarea(e.target.value)}
                    placeholder="Nueva tarea"
                    onKeyPress={(e) => e.key === 'Enter' && agregarTarea()}
                />
                <button onClick={agregarTarea}>Agregar</button>
            </div>
            
            <ul>
                {tareas.map(tarea => (
                    <li key={tarea.id}>
                        {tarea.texto}
                        <button onClick={() => eliminarTarea(tarea.id)}>
                            🗑️
                        </button>
                    </li>
                ))}
            </ul>
            
            <p>Total de tareas: {tareas.length}</p>
        </div>
    );
}

export default ListaTareas;
```
</details>

---

### Exercise 3.2: Contact Form
**Goal**: Multiple inputs with validation

**Requirements**:
- Inputs: Name, Email, Message
- An "Enviar" button
- Validation: all fields must be filled in
- On submit, show a summary of the data
- A "Limpiar" button to reset the form

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function FormularioContacto() {
    const [nombre, setNombre] = useState("");
    const [email, setEmail] = useState("");
    const [mensaje, setMensaje] = useState("");
    const [enviado, setEnviado] = useState(false);
    
    const esValido = nombre && email && mensaje;
    
    const enviar = () => {
        if (!esValido) {
            alert("Por favor completa todos los campos");
            return;
        }
        setEnviado(true);
    };
    
    const limpiar = () => {
        setNombre("");
        setEmail("");
        setMensaje("");
        setEnviado(false);
    };
    
    if (enviado) {
        return (
            <div>
                <h2>✅ Mensaje enviado</h2>
                <p><strong>Nombre:</strong> {nombre}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Mensaje:</strong> {mensaje}</p>
                <button onClick={limpiar}>Enviar otro mensaje</button>
            </div>
        );
    }
    
    return (
        <div>
            <h2>Formulario de Contacto</h2>
            
            <div>
                <input 
                    type="text"
                    value={nombre}
                    onChange={(e) => setNombre(e.target.value)}
                    placeholder="Tu nombre"
                />
            </div>
            
            <div>
                <input 
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Tu email"
                />
            </div>
            
            <div>
                <textarea 
                    value={mensaje}
                    onChange={(e) => setMensaje(e.target.value)}
                    placeholder="Tu mensaje"
                    rows="4"
                />
            </div>
            
            <button onClick={enviar} disabled={!esValido}>
                Enviar
            </button>
            <button onClick={limpiar}>
                Limpiar
            </button>
        </div>
    );
}

export default FormularioContacto;
```
</details>

---

### Exercise 3.3: Image Gallery
**Goal**: State with objects and navigation

**Requirements**:
- Array of image URLs
- Show one image at a time
- "Anterior" and "Siguiente" buttons
- Display "Imagen X de Y"
- The "Anterior" button is disabled on the first image
- The "Siguiente" button is disabled on the last image

<details>
<summary>✅ Solution</summary>

```jsx
import { useState } from 'react';

function GaleriaImagenes() {
    const imagenes = [
        "https://picsum.photos/400/300?random=1",
        "https://picsum.photos/400/300?random=2",
        "https://picsum.photos/400/300?random=3",
        "https://picsum.photos/400/300?random=4",
        "https://picsum.photos/400/300?random=5"
    ];
    
    const [indiceActual, setIndiceActual] = useState(0);
    
    const siguiente = () => {
        if (indiceActual < imagenes.length - 1) {
            setIndiceActual(indiceActual + 1);
        }
    };
    
    const anterior = () => {
        if (indiceActual > 0) {
            setIndiceActual(indiceActual - 1);
        }
    };
    
    return (
        <div style={{ textAlign: "center" }}>
            <h2>Galería de Imágenes</h2>
            
            <div>
                <img 
                    src={imagenes[indiceActual]} 
                    alt={`Imagen ${indiceActual + 1}`}
                    style={{ maxWidth: "100%", border: "3px solid black" }}
                />
            </div>
            
            <p>Imagen {indiceActual + 1} de {imagenes.length}</p>
            
            <button 
                onClick={anterior} 
                disabled={indiceActual === 0}
            >
                ⬅️ Anterior
            </button>
            <button 
                onClick={siguiente} 
                disabled={indiceActual === imagenes.length - 1}
            >
                Siguiente ➡️
            </button>
        </div>
    );
}

export default GaleriaImagenes;
```
</details>

---

## 🎯 Level 4: Advanced

### Exercise 4.1: Shopping Cart
**Goal**: Complex state with arrays of objects

**Requirements**:
- List of products (name, price)
- "Add to cart" button on each product
- Show the cart with the quantity of each product
- "+" and "-" buttons to change quantities
- Show the grand total
- "Empty cart" button

<details>
<summary>✅ Full solution in the main README</summary>

See the final challenge in `README.md`
</details>

---

## 💡 General Tips

1. **Start simple**: Get it working first, then improve
2. **Console.log is your friend**: Use `console.log(state)` to see what's happening
3. **Read the errors**: React's error messages are very descriptive
4. **Practice every day**: 15 minutes a day beats 3 hours once a week

---

## 📝 Debugging Notes

### Common error 1: State doesn't update
```jsx
// ❌ BAD
const incrementar = () => {
    numero = numero + 1;  // Doesn't work
};

// ✅ GOOD
const incrementar = () => {
    setNumero(numero + 1);  // Works
};
```

### Common error 2: Input doesn't type
```jsx
// ❌ BAD - Missing onChange
<input value={nombre} />

// ✅ GOOD
<input 
    value={nombre}
    onChange={(e) => setNombre(e.target.value)}
/>
```

### Common error 3: Forgetting `key` in lists
```jsx
// ❌ BAD
{tareas.map(tarea => <li>{tarea}</li>)}

// ✅ GOOD
{tareas.map((tarea, index) => <li key={index}>{tarea}</li>)}
```

---

**Practice all the exercises and you'll become a useState pro! 💪**
