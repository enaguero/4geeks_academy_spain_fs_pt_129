# Ejercicios Prácticos - useState 🎮

Este documento contiene ejercicios incrementales para dominar `useState` paso a paso.

---

## 🎯 Nivel 1: Principiante Absoluto

### Ejercicio 1.1: Click Counter
**Objetivo**: Aprender el patrón básico de useState

**Requisitos**:
- Muestra un número que empiece en 0
- Un botón que diga "Click"
- Cada vez que hagas click, el número aumenta en 1

**Plantilla inicial**:
```jsx
import { useState } from 'react';

function ClickCounter() {
    // Tu código aquí
    
    return (
        <div>
            {/* Tu HTML aquí */}
        </div>
    );
}

export default ClickCounter;
```

<details>
<summary>💡 Pista</summary>

Necesitas:
1. Crear un estado con `useState(0)`
2. Mostrar el valor del estado
3. Crear un botón con `onClick` que incremente el estado
</details>

<details>
<summary>✅ Solución</summary>

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

### Ejercicio 1.2: Nombre Dinámico
**Objetivo**: Trabajar con inputs controlados

**Requisitos**:
- Un input donde escribir tu nombre
- Debajo debe aparecer "Hola, [nombre]!"
- Si no hay nada escrito, mostrar "Hola, invitado!"

<details>
<summary>💡 Pista</summary>

Necesitas:
1. Un estado tipo `string` vacío
2. Un `<input>` con `value={estado}` y `onChange`
3. Renderizar condicionalmente con `||` o el operador ternario
</details>

<details>
<summary>✅ Solución</summary>

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

### Ejercicio 1.3: Botón On/Off
**Objetivo**: Trabajar con booleanos y condicionales

**Requisitos**:
- Un botón que diga "Encender" o "Apagar"
- Un mensaje que diga "💡 Luz encendida" o "🌑 Luz apagada"
- El color de fondo debe cambiar (amarillo cuando está encendida, negro cuando está apagada)

<details>
<summary>💡 Pista</summary>

Necesitas:
1. Un estado booleano
2. Usar `!estado` para invertir el valor
3. Usar el operador ternario `? :` para cambiar el texto
4. Usar `style={{ backgroundColor: ... }}` para cambiar el color
</details>

<details>
<summary>✅ Solución</summary>

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

## 🎯 Nivel 2: Principiante con Práctica

### Ejercicio 2.1: Calculadora de Propina
**Objetivo**: Múltiples estados y cálculos derivados

**Requisitos**:
- Input para el total de la cuenta
- Botones: "10%", "15%", "20%" para seleccionar propina
- Mostrar: Total original, Propina, Total final

<details>
<summary>✅ Solución</summary>

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

### Ejercicio 2.2: Selector de Color
**Objetivo**: Estado con múltiples opciones

**Requisitos**:
- Un cuadrado grande que muestre un color
- Botones: Rojo, Azul, Verde, Amarillo, Morado
- Al hacer click, cambia el color del cuadrado
- Mostrar el nombre del color actual

<details>
<summary>✅ Solución</summary>

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

### Ejercicio 2.3: Contador con Límites
**Objetivo**: Lógica condicional en el estado

**Requisitos**:
- Contador que va de 0 a 10
- Botón "+" (solo funciona si está por debajo de 10)
- Botón "-" (solo funciona si está por encima de 0)
- Botón "Reset" (vuelve a 0)
- Cuando llegue a 10, mostrar "¡Máximo alcanzado!"
- Cuando esté en 0, mostrar "En el mínimo"

<details>
<summary>✅ Solución</summary>

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

## 🎯 Nivel 3: Intermedio

### Ejercicio 3.1: Lista de Tareas Simple
**Objetivo**: Trabajar con arrays

**Requisitos**:
- Input para escribir una tarea
- Botón "Agregar"
- Mostrar todas las tareas en una lista
- Botón "Eliminar" por cada tarea

<details>
<summary>✅ Solución</summary>

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

### Ejercicio 3.2: Formulario de Contacto
**Objetivo**: Múltiples inputs con validación

**Requisitos**:
- Inputs: Nombre, Email, Mensaje
- Botón "Enviar"
- Validación: todos los campos deben estar llenos
- Al enviar, mostrar un resumen de los datos
- Botón "Limpiar" para resetear el formulario

<details>
<summary>✅ Solución</summary>

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

### Ejercicio 3.3: Galería de Imágenes
**Objetivo**: Estado con objetos y navegación

**Requisitos**:
- Array de URLs de imágenes
- Mostrar una imagen a la vez
- Botones "Anterior" y "Siguiente"
- Mostrar "Imagen X de Y"
- El botón "Anterior" se desactiva en la primera imagen
- El botón "Siguiente" se desactiva en la última imagen

<details>
<summary>✅ Solución</summary>

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

## 🎯 Nivel 4: Avanzado

### Ejercicio 4.1: Carrito de Compras
**Objetivo**: Estado complejo con arrays de objetos

**Requisitos**:
- Lista de productos (nombre, precio)
- Botón "Agregar al carrito" por cada producto
- Mostrar carrito con cantidad de cada producto
- Botones "+" y "-" para cambiar cantidad
- Mostrar total a pagar
- Botón "Vaciar carrito"

<details>
<summary>✅ Solución completa en el README principal</summary>

Ver el desafío final en `README.md`
</details>

---

## 💡 Consejos Generales

1. **Empieza simple**: Haz que funcione primero, luego mejora
2. **Console.log es tu amigo**: Usa `console.log(estado)` para ver qué está pasando
3. **Lee los errores**: Los errores de React son muy descriptivos
4. **Practica cada día**: 15 minutos diarios es mejor que 3 horas una vez a la semana

---

## 📝 Notas de Debugging

### Error común 1: Estado no se actualiza
```jsx
// ❌ MAL
const incrementar = () => {
    numero = numero + 1;  // No funciona
};

// ✅ BIEN
const incrementar = () => {
    setNumero(numero + 1);  // Funciona
};
```

### Error común 2: Input no escribe
```jsx
// ❌ MAL - Falta onChange
<input value={nombre} />

// ✅ BIEN
<input 
    value={nombre}
    onChange={(e) => setNombre(e.target.value)}
/>
```

### Error común 3: Olvidar key en listas
```jsx
// ❌ MAL
{tareas.map(tarea => <li>{tarea}</li>)}

// ✅ BIEN
{tareas.map((tarea, index) => <li key={index}>{tarea}</li>)}
```

---

**¡Practica todos los ejercicios y serás un experto en useState! 💪**
