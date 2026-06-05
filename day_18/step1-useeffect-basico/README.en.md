[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 1: useEffect Basics ⚙️

## What is useEffect?

`useEffect` is a React hook that lets you run code **after** the component renders to the screen.

### Simple analogy

Think of a cook:
- **Rendering**: The cook prepares the dish and places it on the table
- **useEffect**: After placing it on the table, they do something else (add sauce, garnish, etc.)

### Basic syntax

```javascript
import { useEffect } from 'react';

function MiComponente() {
  useEffect(() => {
    // This code runs AFTER the component renders
    console.log('El componente se acaba de dibujar en pantalla!');
  }, []); // The dependency array controls WHEN

  return <div>Hola</div>;
}
```

---

## The Dependency Array 🔑

The **second argument** to `useEffect` is the dependency array. It controls **WHEN** it runs:

| Array | Runs | When |
|-------|------|------|
| (omitted) | After EVERY render | ⚠️ Dangerous if you modify state |
| `[]` | ONLY ONCE | When the component mounts |
| `[variable]` | When variable changes | Every time that variable changes |
| `[var1, var2]` | When var1 OR var2 changes | Every time either changes |

---

## Concrete, Complete Examples

### Example 1: Basic useEffect without state

**File**: `Ejemplo1-BienvenidaConsola.jsx`

```javascript
import { useEffect } from 'react';

function Ejemplo1BienvenidaConsola() {
  useEffect(() => {
    // Runs ONLY ONCE when the component mounts
    console.log('¡Bienvenido! El componente se cargó');
    alert('Componente cargado correctamente');
  }, []); // Empty array = run only once

  return (
    <div>
      <h1>Abre la consola (F12) para ver el mensaje</h1>
    </div>
  );
}

export default Ejemplo1BienvenidaConsola;
```

**How it works**:
1. The component renders for the first time
2. The `alert` appears once
3. The `console.log` runs once
4. If you reload the page, it runs again (it's a new mount)

**Try it**: Reload the page and you'll see it only appears once

---

### Example 2: useEffect with state - Detect changes

**File**: `Ejemplo2-DetectarCambios.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo2DetectarCambios() {
  const [nombre, setNombre] = useState('');

  // Runs when the value of "nombre" changes
  useEffect(() => {
    console.log(`El usuario escribió: "${nombre}"`);
    console.log(`Número de caracteres: ${nombre.length}`);
  }, [nombre]); // Dependency: nombre

  return (
    <div>
      <h2>Escribe tu nombre:</h2>
      <input
        type="text"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        placeholder="Juan"
      />
      <p>Tu nombre: {nombre}</p>
    </div>
  );
}

export default Ejemplo2DetectarCambios;
```

**How it works**:
1. Open the console (F12)
2. Type in the input
3. Each letter you type fires `useEffect` because `nombre` changed
4. In the console you see the name and how many letters it has
5. When you stop typing, `useEffect` stops running

**Try it**: Open the console, type 5 letters, and you'll see 5 separate messages

---

### Example 3: useEffect without dependencies - DANGER ⚠️

**File**: `Ejemplo3-PeligroLoopInfinito.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo3PeligroLoopInfinito() {
  const [contador, setContador] = useState(0);

  // ❌ THIS CAUSES AN INFINITE LOOP
  useEffect(() => {
    console.log(`Contador: ${contador}`);
    setContador(contador + 1); // Modifies state
  }); // NO dependency array - PROBLEM!

  return (
    <div>
      <h1>Contador: {contador}</h1>
      <p>Abre consola - ¡Los números no paran!</p>
    </div>
  );
}

export default Ejemplo3PeligroLoopInfinito;
```

**⚠️ WARNING**:
- Open the console and you'll see endless numbers
- The counter rises without stopping
- The page freezes
- **DO NOT USE THIS CODE IN PRODUCTION**

**Why it happens**:
1. Component renders → contador = 0
2. `useEffect` runs → `setContador(1)`
3. State changed → new render
4. `useEffect` runs AGAIN → `setContador(2)`
5. State changed → new render
6. ... FOREVER ...

See file: `LOOP-INFINITO-EJEMPLO.md` for more details

---

### Example 4: useEffect with cleanup - Interval

**File**: `Ejemplo4-Temporizador.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo4Temporizador() {
  const [segundos, setSegundos] = useState(0);
  const [activo, setActivo] = useState(false);

  useEffect(() => {
    // If it's not active, do nothing
    if (!activo) return;

    console.log('Iniciando temporizador...');

    // Create an interval that runs every 1000ms (1 second)
    const intervalo = setInterval(() => {
      setSegundos(s => s + 1);
      console.log('Tick!');
    }, 1000);

    // CLEANUP: function that runs on unmount or when activo changes
    return () => {
      console.log('Limpiando intervalo...');
      clearInterval(intervalo);
    };
  }, [activo]); // Runs when activo changes

  return (
    <div>
      <h2>Segundos: {segundos}</h2>
      <button onClick={() => setActivo(!activo)}>
        {activo ? 'Pausar' : 'Iniciar'}
      </button>
      <button onClick={() => setSegundos(0)}>Reiniciar</button>
      <p>Abre consola para ver los "Tick!" y "Limpiando..."</p>
    </div>
  );
}

export default Ejemplo4Temporizador;
```

**How it works**:
1. Click "Iniciar"
2. The counter starts rising (1 per second)
3. In the console you see "Tick!" every second
4. Click "Pausar"
5. In the console you see "Limpiando intervalo..."
6. The counter stops
7. If you click "Iniciar" again, it restarts

**Important - The Cleanup**:
```javascript
return () => {
  clearInterval(intervalo); // Clears the interval
};
```

Without the cleanup, every time you press "Iniciar" a new interval would be created without removing the previous one. Trouble!

---

### Example 5: useEffect that modifies the document

**File**: `Ejemplo5-CambiarTituloVentana.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo5CambiarTituloVentana() {
  const [seccion, setSeccion] = useState('Inicio');

  useEffect(() => {
    // Change the browser tab title
    document.title = `Mi App - ${seccion}`;
    console.log(`Página: ${seccion}`);
  }, [seccion]); // Runs when seccion changes

  return (
    <div>
      <h1>Sección actual: {seccion}</h1>
      <button onClick={() => setSeccion('Inicio')}>Inicio</button>
      <button onClick={() => setSeccion('Contacto')}>Contacto</button>
      <button onClick={() => setSeccion('Ayuda')}>Ayuda</button>
      <p>👆 Mira el título de la pestaña del navegador arriba</p>
    </div>
  );
}

export default Ejemplo5CambiarTituloVentana;
```

**How it works**:
1. Click "Contacto"
2. The tab title changes to "Mi App - Contacto"
3. Click "Ayuda"
4. The title changes to "Mi App - Ayuda"
5. Each click runs `useEffect` because `seccion` changed

---

### Example 6: Multiple dependencies

**File**: `Ejemplo6-MultiplesDependencias.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo6MultiplesDependencias() {
  const [nombre, setNombre] = useState('');
  const [edad, setEdad] = useState('');

  useEffect(() => {
    // Runs when NOMBRE OR EDAD change
    console.log(`Datos: ${nombre}, ${edad} años`);
    
    if (nombre && edad) {
      console.log('✅ Tienes nombre y edad');
    }
  }, [nombre, edad]); // Two dependencies

  return (
    <div>
      <input
        type="text"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        placeholder="Tu nombre"
      />
      <input
        type="number"
        value={edad}
        onChange={(e) => setEdad(e.target.value)}
        placeholder="Tu edad"
      />
      <p>Abre consola para ver los cambios</p>
    </div>
  );
}

export default Ejemplo6MultiplesDependencias;
```

**How it works**:
1. Type a name → `useEffect` runs
2. Type an age → `useEffect` runs again
3. Either variable triggers it
4. If both have a value, you see "✅ Tienes nombre y edad"

---

## Summary Table: When it runs

```javascript
// Version A: No dependencies
useEffect(() => {
  console.log('A');
});
// ❌ Runs ALWAYS (dangerous with state)

// Version B: Empty array
useEffect(() => {
  console.log('B');
}, []);
// ✅ Runs ONLY ONCE on mount

// Version C: One dependency
useEffect(() => {
  console.log('C');
}, [nombre]);
// ✅ Runs when nombre changes

// Version D: Multiple dependencies
useEffect(() => {
  console.log('D');
}, [nombre, edad]);
// ✅ Runs when nombre OR edad changes
```

---

## Golden Rule 🏆

**If you use a variable inside useEffect, it must be in the dependency array**

```javascript
const [nombre, setNombre] = useState('');

// ❌ BAD - uses nombre but it's not in dependencies
useEffect(() => {
  console.log(nombre); // Why not in dependencies?
}, []);

// ✅ GOOD - nombre is in dependencies
useEffect(() => {
  console.log(nombre);
}, [nombre]);
```

---

## Key Points ✨

1. **useEffect runs AFTER rendering** - Not during
2. **The dependency array controls WHEN** - It's the trigger
3. **Cleanup matters** - Especially with intervals, listeners, etc.
4. **No dependencies = danger** - Only safe if you don't use state
5. **Correct dependencies = safe** - React knows when to run

---

## Special File

There's a special file: `LOOP-INFINITO-EJEMPLO.md`

That file explains in detail:
- ❌ How to accidentally create an infinite loop
- ✅ How to fix it
- Concrete step-by-step examples

**Read that file if your code freezes or you see weird errors**

---

## Your Exercise 🎯

Create a file `MiEjercicio.jsx` that:

1. ✅ Has a state called `color` initialized to `'white'`
2. ✅ Uses `useEffect` to change the `<body>` background color when `color` changes
3. ✅ Has 3 buttons to switch between: red, blue, green
4. ✅ When the component unmounts, restores the color to white

**Basic structure**:
```javascript
import { useState, useEffect } from 'react';

function MiEjercicio() {
  const [color, setColor] = useState('white');

  // ❓ TODO: Use useEffect to change document.body.style.backgroundColor

  return (
    <div>
      <button onClick={() => setColor('red')}>Rojo</button>
      <button onClick={() => setColor('blue')}>Azul</button>
      <button onClick={() => setColor('green')}>Verde</button>
    </div>
  );
}

export default MiEjercicio;
```

**Hints**:
- Use `document.body.style.backgroundColor = color` to change the color
- The cleanup should restore the color to white
- Think: when should it run? when what changes?

---

## Next Steps

Once you understand:

✅ What useEffect is  
✅ The dependency array  
✅ How to write cleanup  

You'll be ready for:
- **Step 2**: The complete component lifecycle
- **Step 3**: Combining useState + useEffect in real apps

---

## Resources

- [useEffect in React Docs](https://react.dev/reference/react/useEffect)
- [Rules of Hooks](https://react.dev/warnings/mismatching-children-hint)
- [Special file: Infinite Loop](./LOOP-INFINITO-EJEMPLO.md)

---

**💡 Tip**: Open the browser console (F12) for every example. Seeing what happens in the console is key to understanding useEffect.
