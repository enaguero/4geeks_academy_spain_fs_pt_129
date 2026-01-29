# Tutorial: Estado de Componentes en React con useState 🎣

## 📺 Videos de Referencia

- [React Hooks - useState](https://www.youtube.com/watch?v=O6P86uwfdR0)
- [Estado en React explicado](https://www.youtube.com/watch?v=4pO-HcG2igk)
- [Props vs State](https://www.youtube.com/watch?v=IYvD9oBCuJI)

---

## 🎯 ¿Qué vamos a aprender hoy?

En este tutorial aprenderás los conceptos fundamentales del **estado (state)** en React:

1. ✅ ¿Qué es el **estado** y por qué lo necesitamos?
2. ✅ Diferencia entre **props** y **state**
3. ✅ Cómo usar el Hook **useState**
4. ✅ Cómo **actualizar el estado** correctamente
5. ✅ Patrones comunes con useState
6. ✅ Ejercicios prácticos incrementales

---

## 🤔 Parte 1: ¿Qué es el Estado (State)?

### El problema que resuelve el estado

En el Día 16, aprendimos a crear componentes que reciben **props** y se renderizan cada segundo con `setInterval`. Pero hay un problema:

```jsx
// Día 16 - Sin estado local
let contador = 0; // ❌ Variable FUERA del componente

setInterval(() => {
    contador++;
    root.render(<Contador value={contador} />); // ❌ Re-renderizar TODO manualmente
}, 1000);
```

**Problemas:**
- ❌ La variable está fuera del componente (no es "suya")
- ❌ Tienes que llamar a `root.render()` manualmente cada vez
- ❌ No es escalable (imagina 10 contadores diferentes)

### La solución: Estado local del componente

El **estado** es **memoria propia** que cada componente puede tener y controlar.

```jsx
// Día 17 - Con estado local
function Contador() {
    const [contador, setContador] = useState(0); // ✅ Estado DENTRO del componente
    
    // ✅ React re-renderiza automáticamente cuando cambia el estado
    return <h1>{contador}</h1>;
}
```

---

## 🧠 Parte 2: Props vs State

### Diferencias clave

| Característica | Props | State |
|----------------|-------|-------|
| **¿Quién lo controla?** | El componente padre | El propio componente |
| **¿Puede cambiar?** | ❌ No (solo lectura) | ✅ Sí (mediante setState) |
| **¿Dónde se define?** | Fuera del componente | Dentro del componente |
| **¿Se pasa a otros?** | ✅ Sí (de padre a hijo) | ❌ No (es privado) |

### Analogía del mundo real

#### Props = Ingredientes que recibes

Imagina que eres un **chef**:
- Tu jefe te da ingredientes (props): tomates, queso, pasta
- **No puedes cambiar** los ingredientes que te dieron
- Solo puedes **usarlos** para cocinar

```jsx
function Chef(props) {
    // props.ingredientes = ["tomate", "queso", "pasta"]
    // No puedo hacer: props.ingredientes = ["chocolate"] ❌
    return <h1>Cocinando con {props.ingredientes}</h1>;
}
```

#### State = Tu receta/proceso de cocina

- **Tú controlas** cuánto tiempo cocinas (state)
- **Tú decides** cuándo agregar sal (state)
- **Tú puedes cambiar** la temperatura (state)

```jsx
function Chef() {
    const [temperatura, setTemperatura] = useState(100); // ✅ Puedo cambiarla
    const [tiempo, setTiempo] = useState(0); // ✅ Puedo cambiarla
    
    return <h1>Cocinando a {temperatura}° por {tiempo} minutos</h1>;
}
```

### Ejemplo visual

```jsx
// Componente padre (App)
function App() {
    return <Tarjeta nombre="Ana" edad={25} />; // Pasa PROPS
}

// Componente hijo (Tarjeta)
function Tarjeta(props) {
    const [megusta, setMegusta] = useState(0); // STATE local
    
    return (
        <div>
            <h1>{props.nombre}</h1> {/* Props (del padre) */}
            <p>Edad: {props.edad}</p> {/* Props (del padre) */}
            <p>❤️ Me gusta: {megusta}</p> {/* State (propio) */}
            <button onClick={() => setMegusta(megusta + 1)}>
                Dar like
            </button>
        </div>
    );
}
```

**Resultado:**
- `nombre` y `edad` vienen del componente padre → **props**
- `megusta` es controlado por el propio componente → **state**

---

## 🎣 Parte 3: El Hook useState - Conceptos Básicos

### ¿Qué es useState?

`useState` es un **Hook** (gancho) que le da **memoria** a tu componente.

### Sintaxis

```jsx
import { useState } from 'react';

function MiComponente() {
    const [variable, setVariable] = useState(valorInicial);
    
    return <div>{variable}</div>;
}
```

### Desglosando la sintaxis

```jsx
const [contador, setContador] = useState(0);
      ↑         ↑                   ↑
      │         │                   │
      │         │                   └─ Valor inicial (0)
      │         └───────────────────── Función para cambiar el estado
      └─────────────────────────────── Variable que guarda el estado actual
```

**Importante:** Los nombres son libres, pero la convención es:
- Variable: `nombre` descriptivo
- Función: `setNombre` (set + nombre capitalizado)

### Ejemplos de nombres correctos

```jsx
const [contador, setContador] = useState(0);
const [nombre, setNombre] = useState("");
const [activo, setActivo] = useState(false);
const [color, setColor] = useState("rojo");
const [usuarios, setUsuarios] = useState([]);
```

---

## 🚀 Parte 4: Tu Primer Estado - Contador Simple

### Paso 1: Estado básico sin interacción

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

**Resultado en pantalla:**
```
Contador: 0
```

### Paso 2: Añadir botón que cambia el estado

```jsx
import { useState } from 'react';

function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementar = () => {
        setNumero(numero + 1); // Cambia el estado
    };
    
    return (
        <div>
            <h1>Contador: {numero}</h1>
            <button onClick={incrementar}>Incrementar</button>
        </div>
    );
}
```

### ¿Qué pasa cuando haces click?

```
1. Usuario hace click en el botón
   ↓
2. Se ejecuta la función incrementar()
   ↓
3. Se llama a setNumero(numero + 1)
   ↓
4. React detecta que el estado cambió
   ↓
5. React re-renderiza el componente AUTOMÁTICAMENTE
   ↓
6. El número nuevo aparece en la pantalla ✨
```

### Paso 3: Múltiples botones

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

**⚠️ Nota:** Puedes usar funciones inline con `onClick={() => ...}` para casos simples.

### ✏️ Ejercicio 1: Tu primer contador

Crea un componente `ContadorPersonal` que:
1. Empiece en 10
2. Tenga un botón "Sumar 5" que aumente de 5 en 5
3. Tenga un botón "Restar 5" que disminuya de 5 en 5
4. Tenga un botón "Reset" que vuelva a 10

<details>
<summary>💡 Ver solución</summary>

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

## 💡 Parte 5: Tipos de Estado

### Estado con Números

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

### Estado con Strings (texto)

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

**¿Qué es `e.target.value`?**
- `e` = evento del input
- `e.target` = el elemento input
- `e.target.value` = el texto que escribiste

### Estado con Booleanos (true/false)

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

**Explicación del `!`:**
- `!` invierte el valor booleano
- Si `encendido = true` → `!encendido = false`
- Si `encendido = false` → `!encendido = true`

### Estado con Arrays (listas)

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

**¿Qué es `...tareas`?**
- Se llama "spread operator" (operador de propagación)
- Copia todos los elementos del array anterior
- Ejemplo: `[...tareas, "Nueva"]` = copia todas las tareas + añade una nueva

### Estado con Objetos

```jsx
function PerfilUsuario() {
    const [usuario, setUsuario] = useState({
        nombre: "Ana",
        edad: 25,
        ciudad: "Madrid"
    });
    
    const cumplirAños = () => {
        setUsuario({
            ...usuario,       // Copia todo lo anterior
            edad: usuario.edad + 1  // Pero cambia solo la edad
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

## ⚠️ Parte 6: Reglas Importantes del Estado

### Regla 1: NUNCA modifiques el estado directamente

```jsx
// ❌ MAL - No funciona
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementar = () => {
        numero = numero + 1;  // ❌ Error: no puedes cambiar numero directamente
    };
    
    return <button onClick={incrementar}>+1</button>;
}

// ✅ BIEN - Usa setNumero
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementar = () => {
        setNumero(numero + 1);  // ✅ Correcto
    };
    
    return <button onClick={incrementar}>+1</button>;
}
```

### Regla 2: El estado es asíncrono

```jsx
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementarDosVeces = () => {
        setNumero(numero + 1);
        setNumero(numero + 1); // ❌ No suma 2, ¡solo suma 1!
        
        console.log(numero); // ❌ Todavía muestra el valor ANTERIOR
    };
    
    return <button onClick={incrementarDosVeces}>+2</button>;
}
```

**¿Por qué?**
- React **agrupa** las actualizaciones de estado
- No se actualiza inmediatamente

**Solución: Usa la forma funcional**

```jsx
function Contador() {
    const [numero, setNumero] = useState(0);
    
    const incrementarDosVeces = () => {
        setNumero(prev => prev + 1); // ✅ Correcto
        setNumero(prev => prev + 1); // ✅ Correcto
    };
    
    return <button onClick={incrementarDosVeces}>+2</button>;
}
```

**Explicación de `prev`:**
- `prev` = valor anterior del estado
- React garantiza que siempre es el valor más reciente

### Regla 3: No mutaciones con arrays y objetos

```jsx
// ❌ MAL - Mutación directa
const agregarTarea = () => {
    tareas.push("Nueva tarea");  // ❌ Modifica el array original
    setTareas(tareas);  // ❌ React no detecta el cambio
};

// ✅ BIEN - Crear nuevo array
const agregarTarea = () => {
    setTareas([...tareas, "Nueva tarea"]);  // ✅ Nuevo array
};
```

---

## 🎮 Parte 7: Ejercicios Prácticos Incrementales

### Ejercicio 2: Campo de nombre

Crea un componente que:
- Tenga un input para escribir tu nombre
- Muestre "Hola, [nombre]!" debajo
- El saludo debe actualizarse mientras escribes

<details>
<summary>💡 Ver solución</summary>

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

### Ejercicio 3: Botón de Like

Crea un componente que:
- Muestre un botón con "❤️ Like (0)"
- Cada click incrementa el número de likes
- Cuando llegue a 10, muestre "¡Popular!" debajo

<details>
<summary>💡 Ver solución</summary>

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

### Ejercicio 4: Cambio de color

Crea un componente que:
- Muestre un cuadrado con color de fondo
- Tenga botones: "Rojo", "Azul", "Verde"
- Al hacer click, cambie el color del cuadrado

<details>
<summary>💡 Ver solución</summary>

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

### Ejercicio 5: Mostrar/Ocultar contenido

Crea un componente que:
- Tenga un botón "Mostrar/Ocultar"
- Al hacer click, muestre u oculte un párrafo de texto

<details>
<summary>💡 Ver solución</summary>

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

### Ejercicio 6: Formulario de registro simple

Crea un componente con:
- Input para nombre
- Input para email
- Botón "Registrar"
- Al hacer click en "Registrar", muestra los datos debajo

<details>
<summary>💡 Ver solución</summary>

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

## 🎯 Parte 8: Proyecto - Sistema de Semáforo Interactivo

### Concepto del proyecto

Vas a crear un **semáforo** que cambie de color con botones o automáticamente.

```
     ┌───────┐
     │       │
     │  🔴   │  ← Rojo (por defecto)
     │       │
     ├───────┤
     │       │
     │  🟡   │  ← Amarillo
     │       │
     ├───────┤
     │       │
     │  🟢   │  ← Verde
     │       │
     └───────┘
```

### Nivel 1: Semáforo básico con botones

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

### Nivel 2: Ciclo automático

Añade un botón "Auto" que cambie el color automáticamente cada 2 segundos.

**Pista:** Usa `useEffect` con `setInterval`

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
            {/* ... mismo HTML del semáforo ... */}
            
            <button onClick={() => setAuto(!auto)}>
                {auto ? "Detener" : "Automático"}
            </button>
        </div>
    );
}
```

---

## 📚 Parte 9: Patrones Comunes

### Patrón 1: Toggle (Alternar)

```jsx
const [activo, setActivo] = useState(false);

// Alternar entre true y false
<button onClick={() => setActivo(!activo)}>
    {activo ? "Activado" : "Desactivado"}
</button>
```

### Patrón 2: Contador con límites

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

### Patrón 3: Input controlado

```jsx
const [texto, setTexto] = useState("");

<input 
    value={texto}
    onChange={(e) => setTexto(e.target.value)}
/>
```

### Patrón 4: Estado derivado (calculado)

```jsx
const [precio, setPrecio] = useState(100);
const [cantidad, setCantidad] = useState(1);

// No necesitas estado para esto:
const total = precio * cantidad;

return <p>Total: {total}€</p>;
```

### Patrón 5: Resetear múltiples estados

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

## 🎓 Resumen de Conceptos

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **State** | Memoria propia del componente | `const [x, setX] = useState(0)` |
| **useState** | Hook para crear estado | `useState(valorInicial)` |
| **Props** | Datos del padre (solo lectura) | `<Card nombre="Ana" />` |
| **setState** | Función para cambiar estado | `setContador(5)` |
| **Forma funcional** | Usar valor anterior del estado | `setState(prev => prev + 1)` |
| **Toggle** | Alternar booleano | `setActivo(!activo)` |
| **Spread** | Copiar array/objeto | `[...array, nuevo]` |

---

## ✅ Checklist de Aprendizaje

Antes de continuar al siguiente día, asegúrate de:

- [ ] Entender qué es el estado y para qué sirve
- [ ] Saber la diferencia entre props y state
- [ ] Poder usar `useState` con diferentes tipos de datos
- [ ] Nunca modificar el estado directamente
- [ ] Saber usar la forma funcional `setState(prev => ...)`
- [ ] Poder crear componentes con múltiples estados
- [ ] Manejar eventos (onClick, onChange)
- [ ] Crear inputs controlados

---

## 🔗 Recursos Adicionales

### Documentación oficial
- [React Docs - useState](https://react.dev/reference/react/useState)
- [React Docs - State: A Component's Memory](https://react.dev/learn/state-a-components-memory)
- [React Docs - Render and Commit](https://react.dev/learn/render-and-commit)

### Tutoriales recomendados
- [useState en 100 Segundos](https://www.youtube.com/watch?v=O6P86uwfdR0)
- [Thinking in React](https://react.dev/learn/thinking-in-react)

---

## 💡 Consejos Finales

1. **Practica cada tipo de estado**: número, string, boolean, array, objeto
2. **No uses estado si no lo necesitas**: Si algo se puede calcular, no necesita estado
3. **Un estado por preocupación**: Es mejor tener varios estados simples que uno complejo
4. **Nombres descriptivos**: `[contador, setContador]` es mejor que `[c, setC]`

---

## ❓ Preguntas Frecuentes

### ¿Cuántos useState puedo tener en un componente?

Los que necesites. Puedes tener 1, 5, 10... React no tiene límite.

```jsx
function MiComponente() {
    const [nombre, setNombre] = useState("");
    const [edad, setEdad] = useState(0);
    const [activo, setActivo] = useState(false);
    const [colores, setColores] = useState([]);
    // ... etc
}
```

### ¿Por qué usar setEstado en lugar de cambiar la variable?

Porque React necesita **saber** que cambió algo para re-renderizar. Si cambias la variable directamente, React no lo detecta.

### ¿Puedo usar estado en cualquier componente?

Sí, pero **solo en componentes de función** con Hooks. Los componentes de clase usan `this.state`.

### ¿Cuándo usar props vs state?

- **Props**: Si el dato viene del padre
- **State**: Si el componente necesita recordar o cambiar el dato

---

## 🏆 Desafío Final

Crea una aplicación de **lista de compras** que permita:
1. Agregar items con un input y un botón
2. Mostrar todos los items en una lista
3. Marcar items como comprados (tachados)
4. Eliminar items
5. Mostrar el total de items pendientes

<details>
<summary>💡 Ver solución</summary>

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

**¡Felicidades! 🎉 Ahora entiendes el estado en React.**

En el próximo día, aprenderás sobre **useEffect** y cómo combinar estado con efectos secundarios.

---

**Creado con ❤️ para 4Geeks Academy - Cohort España FS PT 129**
