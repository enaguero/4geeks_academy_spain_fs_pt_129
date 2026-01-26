# Tutorial: React Componentes, Props, setInterval y Ciclo de Vida

## 📺 Videos de Referencia

- [¿Qué es React?](https://www.youtube.com/watch?v=MPLN1ahXgcs)
- [Componentes y Props en React](https://www.youtube.com/watch?v=Y2hgEGPzTZY)
- [Ciclo de vida en React](https://www.youtube.com/watch?v=qnN_FuFNq2g)

---

## 🎯 ¿Qué vamos a aprender hoy?

En este tutorial aprenderás los conceptos fundamentales para crear un **contador de segundos** en React:

1. ✅ Qué son los **componentes** y cómo crear componentes reutilizables
2. ✅ Qué son las **props** y cómo pasar información entre componentes
3. ✅ Cómo usar **setInterval** para ejecutar código repetidamente
4. ✅ El **ciclo de vida** de un componente React
5. ✅ Cómo aplicar todo esto para crear un contador visual

---

## 🧩 Parte 1: Componentes en React

### ¿Qué es un componente?

Un **componente** es como un **bloque de LEGO** que puedes usar y reutilizar en diferentes partes de tu aplicación web. Es una pieza independiente de tu interfaz que tiene su propia apariencia y comportamiento.

### Analogía del mundo real

Imagina que estás construyendo una casa con LEGO:
- 🧱 Una **ventana** es un componente (siempre tiene el mismo diseño)
- 🚪 Una **puerta** es otro componente
- 🏠 La **casa completa** está hecha de muchos componentes juntos

En React funciona igual: tu página web está hecha de muchos componentes pequeños que se combinan.

### Tu primer componente: Un saludo simple

```jsx
function Saludo() {
    return <h1>¡Hola Mundo!</h1>;
}
```

**¿Qué está pasando aquí?**
- `function Saludo()` → Defines un componente (es solo una función de JavaScript)
- `return` → Devuelve lo que el componente debe mostrar
- `<h1>¡Hola Mundo!</h1>` → Esto es JSX (HTML dentro de JavaScript)

### Usar tu componente

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

function Saludo() {
    return <h1>¡Hola Mundo!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Saludo />);
```

**Resultado en el navegador:**
```
¡Hola Mundo!
```

### ✏️ Ejercicio 1: Tu primer componente

Crea un componente llamado `MiPresentacion` que muestre:
- Tu nombre en un `<h1>`
- Tu edad en un `<p>`
- Tu ciudad en un `<p>`

<details>
<summary>💡 Ver solución</summary>

```jsx
function MiPresentacion() {
    return (
        <div>
            <h1>Ana García</h1>
            <p>Edad: 25 años</p>
            <p>Ciudad: Madrid</p>
        </div>
    );
}
```
</details>

---

## 📦 Parte 2: Props - Pasando Información a los Componentes

### ¿Qué son las props?

Las **props** (propiedades) son como los **argumentos de una función**, pero para componentes. Te permiten pasar información de un componente padre a un componente hijo.

### Analogía

Imagina que tienes una **máquina de hacer tarjetas de cumpleaños**:
- La máquina es el **componente**
- Le pasas el **nombre** y la **edad** como **props**
- La máquina produce una tarjeta personalizada con esos datos

### Ejemplo básico de props

```jsx
// Componente que RECIBE props
function Saludo(props) {
    return <h1>¡Hola, {props.nombre}!</h1>;
}

// Uso del componente - ENVIANDO props
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Saludo nombre="Carlos" />);
```

**Resultado:**
```
¡Hola, Carlos!
```

### ¿Cómo funciona?

1. Cuando escribes `<Saludo nombre="Carlos" />`, estás pasando la prop `nombre` con el valor `"Carlos"`
2. Dentro del componente, accedes a ese valor con `props.nombre`
3. Las llaves `{}` te permiten insertar JavaScript dentro del JSX

### Múltiples props

```jsx
function TarjetaUsuario(props) {
    return (
        <div className="tarjeta">
            <h2>{props.nombre}</h2>
            <p>Edad: {props.edad} años</p>
            <p>Ciudad: {props.ciudad}</p>
            <p>Profesión: {props.profesion}</p>
        </div>
    );
}

// Uso
<TarjetaUsuario 
    nombre="María López" 
    edad={28} 
    ciudad="Barcelona" 
    profesion="Desarrolladora"
/>
```

**⚠️ Importante:**
- Texto va entre comillas: `nombre="María"`
- Números y JavaScript van entre llaves: `edad={28}`

### Reutilización de componentes con diferentes props

```jsx
function Tarjeta(props) {
    return (
        <div className="tarjeta">
            <h3>{props.titulo}</h3>
            <p>{props.descripcion}</p>
        </div>
    );
}

// ¡Puedes usar el mismo componente muchas veces con diferentes datos!
<div>
    <Tarjeta titulo="React" descripcion="Librería de JavaScript" />
    <Tarjeta titulo="Python" descripcion="Lenguaje de programación" />
    <Tarjeta titulo="HTML" descripcion="Lenguaje de marcado" />
</div>
```

### ✏️ Ejercicio 2: Componente con props

Crea un componente `ProductoCard` que reciba estas props:
- `nombre` (nombre del producto)
- `precio` (precio en euros)
- `stock` (cantidad disponible)

Y muestre esta información en un formato bonito.

<details>
<summary>💡 Ver solución</summary>

```jsx
function ProductoCard(props) {
    return (
        <div className="producto">
            <h3>{props.nombre}</h3>
            <p className="precio">{props.precio}€</p>
            <p className="stock">Disponibles: {props.stock} unidades</p>
        </div>
    );
}

// Uso
<ProductoCard nombre="Teclado mecánico" precio={89} stock={15} />
```
</details>

---

## ⏱️ Parte 3: La Función setInterval

### ¿Qué es setInterval?

`setInterval` es una función de JavaScript que **ejecuta código repetidamente** cada cierto intervalo de tiempo.

### Sintaxis básica

```javascript
setInterval(función, tiempoEnMilisegundos)
```

- **función**: Lo que quieres ejecutar repetidamente
- **tiempoEnMilisegundos**: Cada cuánto tiempo (1000 ms = 1 segundo)

### Ejemplo 1: Contador en la consola

```javascript
let contador = 0;

setInterval(() => {
    contador = contador + 1;
    console.log("Han pasado " + contador + " segundos");
}, 1000);
```

**Lo que pasa:**
- Cada 1 segundo (1000 ms) se ejecuta la función
- El contador aumenta de 1 en 1
- Se imprime en la consola

**Salida en la consola:**
```
Han pasado 1 segundos
Han pasado 2 segundos
Han pasado 3 segundos
Han pasado 4 segundos
...
```

### Ejemplo 2: Mostrar en el HTML (sin React todavía)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Contador: <span id="contador">0</span></h1>
    
    <script>
        let segundos = 0;
        
        setInterval(() => {
            segundos = segundos + 1;
            document.getElementById('contador').textContent = segundos;
        }, 1000);
    </script>
</body>
</html>
```

### Ejemplo 3: setInterval con diferentes velocidades

```javascript
// Cada medio segundo (rápido)
setInterval(() => {
    console.log("¡Rápido!");
}, 500);

// Cada 2 segundos (lento)
setInterval(() => {
    console.log("Lento...");
}, 2000);

// Cada 5 segundos (muy lento)
setInterval(() => {
    console.log("Muy lento......");
}, 5000);
```

### Detener un intervalo: clearInterval

A veces necesitas **detener** un `setInterval`. Para eso usas `clearInterval`.

```javascript
let contador = 0;

// Guardar el ID del intervalo
const miIntervalo = setInterval(() => {
    contador = contador + 1;
    console.log(contador);
    
    // Detener cuando llegue a 10
    if (contador === 10) {
        clearInterval(miIntervalo);
        console.log("¡Contador detenido!");
    }
}, 1000);
```

**Lo que pasa:**
- El contador cuenta hasta 10
- Cuando llega a 10, se detiene automáticamente

### Ejemplo 4: Reloj digital simple

```javascript
setInterval(() => {
    const ahora = new Date();
    const horas = ahora.getHours();
    const minutos = ahora.getMinutes();
    const segundos = ahora.getSeconds();
    
    console.log(`${horas}:${minutos}:${segundos}`);
}, 1000);
```

### ✏️ Ejercicio 3: Practica setInterval

Crea un contador que:
1. Empiece en 0
2. Aumente de 1 en 1 cada segundo
3. Se detenga cuando llegue a 5
4. Muestre "¡Terminado!" cuando se detenga

<details>
<summary>💡 Ver solución</summary>

```javascript
let numero = 0;

const intervalo = setInterval(() => {
    console.log(numero);
    numero = numero + 1;
    
    if (numero > 5) {
        clearInterval(intervalo);
        console.log("¡Terminado!");
    }
}, 1000);
```
</details>

---

## 🔄 Parte 4: setInterval + React

### Concepto básico

Ahora vamos a combinar `setInterval` con React para crear un contador visual.

### Ejemplo simple: Contador que se actualiza cada segundo

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

// Componente que muestra el número de segundos
function ContadorSimple(props) {
    return (
        <div>
            <h1>Segundos transcurridos: {props.segundos}</h1>
        </div>
    );
}

// Obtener el elemento root
const root = ReactDOM.createRoot(document.getElementById('root'));

// Variable que cuenta los segundos
let segundosTranscurridos = 0;

// setInterval re-renderiza el componente cada segundo
setInterval(() => {
    segundosTranscurridos = segundosTranscurridos + 1;
    
    // Re-renderizar con el nuevo valor
    root.render(<ContadorSimple segundos={segundosTranscurridos} />);
}, 1000);
```

**¿Qué está pasando?**
1. Creamos un componente `ContadorSimple` que recibe `segundos` como prop
2. Cada segundo, `setInterval` ejecuta su función
3. Incrementamos `segundosTranscurridos`
4. Llamamos a `root.render()` de nuevo con el nuevo valor
5. React actualiza solo lo que cambió en la pantalla (eficiente ✨)

### Ejemplo con formato más bonito

```jsx
function ContadorBonito(props) {
    return (
        <div className="contador-container">
            <h1>⏱️ Contador de Segundos</h1>
            <div className="numero-grande">
                {props.segundos}
            </div>
            <p>segundos transcurridos</p>
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
let tiempo = 0;

setInterval(() => {
    tiempo++;
    root.render(<ContadorBonito segundos={tiempo} />);
}, 1000);
```

### ¿Por qué re-renderizar en lugar de usar estado?

En este momento estamos aprendiendo conceptos básicos. En el proyecto Simple Counter, esta es la forma **correcta** de hacerlo según las instrucciones:

> "The component does not need a local state, you can pass the number of seconds as props"

Más adelante aprenderás sobre `useState` y `useEffect`, que son formas más avanzadas de manejar esto.

---

## 🔄 Parte 5: Ciclo de Vida de un Componente

### ¿Qué es el ciclo de vida?

Cada componente de React pasa por diferentes **fases** desde que se crea hasta que se elimina. A esto le llamamos el **ciclo de vida del componente**.

### Las 3 fases principales

```
  MONTAJE       →       ACTUALIZACIÓN      →      DESMONTAJE
(Mount/Mounting)      (Update/Updating)         (Unmount)
     ↓                       ↓                        ↓
 Se crea y se           Se actualiza             Se elimina
 añade al DOM          (props o estado            del DOM
                          cambian)
```

### Analogía de la vida real

Piensa en un **actor en una obra de teatro**:

1. **MONTAJE**: El actor **entra al escenario** 🎭
   - Se prepara, se coloca en su posición
   
2. **ACTUALIZACIÓN**: El actor **cambia durante la obra** 🎬
   - Dice diferentes líneas
   - Cambia de vestuario
   - Se mueve por el escenario

3. **DESMONTAJE**: El actor **sale del escenario** 🚪
   - Se retira
   - Limpia su espacio

### Fase 1: Montaje (Mount)

El componente se **crea** y se **añade al DOM** por primera vez.

```jsx
function MiComponente() {
    console.log("Estoy renderizando por primera vez");
    return <h1>¡Hola!</h1>;
}

// Cuando haces esto, el componente se MONTA:
root.render(<MiComponente />);
```

### Fase 2: Actualización (Update)

El componente se **vuelve a renderizar** porque:
- Cambiaron sus props
- Cambió su estado interno

```jsx
function Contador(props) {
    console.log("Me estoy actualizando, ahora seconds = " + props.seconds);
    return <h1>Segundos: {props.seconds}</h1>;
}

// Primera vez (MONTAJE):
root.render(<Contador seconds={0} />);

// Un segundo después (ACTUALIZACIÓN):
root.render(<Contador seconds={1} />);

// Dos segundos después (ACTUALIZACIÓN):
root.render(<Contador seconds={2} />);
```

### Fase 3: Desmontaje (Unmount)

El componente se **elimina** del DOM.

```jsx
// El componente está en el DOM
root.render(<MiComponente />);

// Ahora lo quitamos (DESMONTAJE)
root.render(null);

// O renderizamos otro componente diferente
root.render(<OtroComponente />);
```

### Visualización completa del ciclo

```
Tiempo 0s: root.render(<Contador seconds={0} />)
           ↓
        MONTAJE - El componente aparece por primera vez
           
Tiempo 1s: root.render(<Contador seconds={1} />)
           ↓
        ACTUALIZACIÓN - Props cambiaron (0 → 1)
           
Tiempo 2s: root.render(<Contador seconds={2} />)
           ↓
        ACTUALIZACIÓN - Props cambiaron (1 → 2)
           
Tiempo 3s: root.render(null)
           ↓
        DESMONTAJE - El componente se elimina
```

---

## 🎣 Parte 6: Hooks y useEffect (Concepto avanzado)

### ¿Qué es un Hook?

Los **Hooks** son funciones especiales de React que te permiten "engancharte" (hook into) al ciclo de vida y otras características de React.

### El Hook más importante para el ciclo de vida: useEffect

`useEffect` te permite ejecutar código en diferentes momentos del ciclo de vida.

### Sintaxis básica

```jsx
import { useEffect } from 'react';

function MiComponente() {
    useEffect(() => {
        // Código que se ejecuta
    }, [dependencias]);
    
    return <h1>Componente</h1>;
}
```

### Caso 1: Ejecutar solo al MONTAR (una vez)

```jsx
import { useEffect } from 'react';

function MiComponente() {
    useEffect(() => {
        console.log("¡El componente se montó!");
        console.log("Esto solo se ejecuta UNA VEZ");
    }, []); // Array vacío [] = solo al montar
    
    return <h1>¡Hola Mundo!</h1>;
}
```

**Explicación del `[]`:**
- El array vacío `[]` le dice a React: "ejecuta esto solo una vez, cuando el componente se monte"

### Caso 2: Ejecutar en cada ACTUALIZACIÓN

```jsx
import { useEffect } from 'react';

function Contador(props) {
    useEffect(() => {
        console.log("El componente se actualizó");
        console.log("Nuevo valor de segundos:", props.segundos);
    }); // Sin array = se ejecuta en cada renderizado
    
    return <h1>Segundos: {props.segundos}</h1>;
}
```

### Caso 3: Ejecutar solo cuando cambia una prop específica

```jsx
import { useEffect } from 'react';

function Usuario(props) {
    useEffect(() => {
        console.log("El nombre cambió a:", props.nombre);
    }, [props.nombre]); // Solo cuando props.nombre cambia
    
    return (
        <div>
            <h1>{props.nombre}</h1>
            <p>Edad: {props.edad}</p>
        </div>
    );
}
```

**Explicación:**
- `[props.nombre]` = "ejecuta esto solo cuando `props.nombre` cambie"
- Si cambia `props.edad`, este `useEffect` NO se ejecuta

### Caso 4: Limpiar al DESMONTAR (cleanup)

Este es **súper importante** para `setInterval`.

```jsx
import { useEffect } from 'react';

function ContadorConLimpieza() {
    useEffect(() => {
        console.log("Iniciando intervalo...");
        
        const intervalo = setInterval(() => {
            console.log("Tick");
        }, 1000);
        
        // Función de limpieza (cleanup function)
        return () => {
            console.log("Deteniendo intervalo...");
            clearInterval(intervalo);
        };
    }, []);
    
    return <h1>Contador activo</h1>;
}
```

**¿Por qué es importante la limpieza?**

Sin limpieza:
```jsx
// ❌ PROBLEMA
useEffect(() => {
    setInterval(() => {
        console.log("Esto nunca se detiene!");
    }, 1000);
}, []);
// Si el componente se desmonta, el intervalo sigue ejecutándose
// Esto causa "memory leaks" (fugas de memoria)
```

Con limpieza:
```jsx
// ✅ CORRECTO
useEffect(() => {
    const intervalo = setInterval(() => {
        console.log("Esto se detendrá");
    }, 1000);
    
    return () => {
        clearInterval(intervalo);
    };
}, []);
// Cuando el componente se desmonta, se detiene el intervalo
```

### Resumen visual de useEffect

```jsx
useEffect(() => {
    // Código que se ejecuta
    
    return () => {
        // Código de limpieza (opcional)
    };
}, []);
   ↑
   Dependencias:
   - [] = solo al montar
   - [variable] = cuando variable cambia
   - sin array = en cada renderizado
```

---

## 🎯 Parte 7: Aplicando Todo al Proyecto Simple Counter

### Concepto del proyecto

Vas a crear un **contador visual de segundos** que muestre cada dígito en una caja separada, como un reloj digital.

```
┌─────┬─────┬─────┬─────┬─────┬─────┐
│  ⏱  │  0  │  0  │  0  │  1  │  2  │
└─────┴─────┴─────┴─────┴─────┴─────┘
```

### Estructura conceptual

```jsx
// 1. Componente que muestra el contador
function SecondsCounter(props) {
    // Recibe props.seconds (ejemplo: 123)
    // Debe separar 123 en [1, 2, 3]
    // Mostrar cada dígito en una caja
    
    return (
        <div>
            {/* Tu diseño aquí */}
        </div>
    );
}

// 2. En tu archivo principal (index.js)
const root = ReactDOM.createRoot(document.getElementById('root'));

let segundos = 0;

setInterval(() => {
    segundos = segundos + 1;
    root.render(<SecondsCounter seconds={segundos} />);
}, 1000);
```

### Desafío 1: Separar un número en dígitos

Si tienes `seconds = 1234`, necesitas obtener: `[1, 2, 3, 4]`

**Método 1: Convertir a string**
```javascript
let numero = 1234;
let digitos = numero.toString().split('');
// Resultado: ['1', '2', '3', '4']
```

**Método 2: Matemáticas**
```javascript
let numero = 1234;

let unidades = numero % 10;                           // 4
let decenas = Math.floor(numero / 10) % 10;          // 3
let centenas = Math.floor(numero / 100) % 10;        // 2
let miles = Math.floor(numero / 1000) % 10;          // 1
```

### Desafío 2: Mostrar 6 dígitos siempre

El contador debe mostrar siempre 6 dígitos, rellenando con ceros a la izquierda:

```
seconds = 5     →  000005
seconds = 42    →  000042
seconds = 1234  →  001234
```

**Pista:** Usa `padStart()`
```javascript
let numero = 5;
let conCeros = numero.toString().padStart(6, '0');
// Resultado: "000005"
```

### Desafío 3: Renderizar múltiples cajas

Necesitas crear una caja por cada dígito:

```jsx
function SecondsCounter(props) {
    // Separar en dígitos
    const digitosArray = props.seconds.toString().padStart(6, '0').split('');
    
    return (
        <div className="contador-container">
            <div className="digito">⏱️</div>
            
            {digitosArray.map((digito, index) => (
                <div key={index} className="digito">
                    {digito}
                </div>
            ))}
        </div>
    );
}
```

**¿Qué hace `.map()`?**
- Recorre cada elemento del array
- Crea un elemento JSX por cada uno
- `key={index}` es necesario para que React identifique cada elemento

### Ejemplo de CSS (para que se vea bonito)

```css
.contador-container {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 50px;
}

.digito {
    background-color: #282c34;
    color: white;
    font-size: 48px;
    font-family: 'Courier New', monospace;
    width: 60px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

---

## 📚 Parte 8: Conceptos Adicionales

### Font Awesome (para el ícono del reloj)

Para añadir el ícono del reloj ⏱️, necesitas Font Awesome:

**Opción 1: CDN en tu HTML**
```html
<head>
    <link rel="stylesheet" 
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
```

**Opción 2: NPM**
```bash
npm install @fortawesome/fontawesome-free
```

```jsx
import '@fortawesome/fontawesome-free/css/all.min.css';

function SecondsCounter(props) {
    return (
        <div>
            <div className="digito">
                <i className="far fa-clock"></i>
            </div>
            {/* resto del código */}
        </div>
    );
}
```

### Bonus: Parar, reiniciar y reanudar

Para los bonus del proyecto, necesitarás:

**1. Variable para guardar el intervalo**
```javascript
let intervaloActual = null;

function iniciarContador() {
    intervaloActual = setInterval(() => {
        segundos++;
        root.render(<SecondsCounter seconds={segundos} />);
    }, 1000);
}

function pararContador() {
    clearInterval(intervaloActual);
}

function reiniciarContador() {
    pararContador();
    segundos = 0;
    root.render(<SecondsCounter seconds={segundos} />);
}
```

**2. Botones en tu componente**
```jsx
function SecondsCounter(props) {
    return (
        <div>
            {/* Contador visual */}
            <div className="controles">
                <button onClick={props.onPausar}>Pausar</button>
                <button onClick={props.onReanudar}>Reanudar</button>
                <button onClick={props.onReiniciar}>Reiniciar</button>
            </div>
        </div>
    );
}
```

---

## 🎓 Resumen de Conceptos

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **Componente** | Bloque reutilizable de UI | `function Card() { return <div>...</div> }` |
| **Props** | Datos que pasas al componente | `<Card nombre="Ana" edad={25} />` |
| **setInterval** | Ejecuta código repetidamente | `setInterval(() => {...}, 1000)` |
| **clearInterval** | Detiene un intervalo | `clearInterval(miIntervalo)` |
| **Ciclo de vida** | Fases: Montaje → Actualización → Desmontaje | Ver sección 5 |
| **useEffect** | Hook para ejecutar código en el ciclo de vida | `useEffect(() => {...}, [])` |
| **JSX** | HTML dentro de JavaScript | `<h1>{variable}</h1>` |
| **map()** | Renderiza arrays en JSX | `array.map(item => <div>{item}</div>)` |

---

## ✅ Checklist del Proyecto

Antes de empezar, asegúrate de entender:

- [ ] Cómo crear un componente función en React
- [ ] Cómo pasar y recibir props
- [ ] Cómo funciona setInterval y clearInterval
- [ ] Qué es el ciclo de vida de un componente
- [ ] Cómo separar un número en dígitos individuales
- [ ] Cómo usar .map() para renderizar arrays
- [ ] Cómo usar ReactDOM.createRoot y root.render

---

## 🔗 Recursos Adicionales

### Documentación oficial
- [React Docs - Componentes y Props](https://react.dev/learn/passing-props-to-a-component)
- [MDN - setInterval](https://developer.mozilla.org/es/docs/Web/API/setInterval)
- [React Docs - useEffect](https://react.dev/reference/react/useEffect)

### Tutoriales recomendados
- [Tutorial interactivo de React](https://react.dev/learn/tutorial-tic-tac-toe)
- [JavaScript.info - setInterval y setTimeout](https://javascript.info/settimeout-setinterval)

---

## 💡 Consejos Finales

1. **Empieza simple**: Primero haz que el contador funcione con un solo número
2. **Luego mejora**: Añade la separación de dígitos
3. **Después estiliza**: Haz que se vea bonito con CSS
4. **Por último bonus**: Añade las funcionalidades extra

**¡Buena suerte con tu proyecto! 🚀**

---

## ❓ Preguntas Frecuentes

### ¿Por qué uso root.render() en lugar de useState?

En este proyecto específico, las instrucciones dicen que **no uses estado local**. Esto es para aprender los conceptos básicos primero. Más adelante usarás `useState` y `useEffect` para esto.

### ¿Cada cuánto se ejecuta setInterval?

El segundo parámetro está en milisegundos:
- 1000 ms = 1 segundo
- 500 ms = 0.5 segundos
- 2000 ms = 2 segundos

### ¿Qué pasa si no uso clearInterval?

Si no detienes un intervalo cuando el componente se desmonta, seguirá ejecutándose en segundo plano, causando problemas de rendimiento (memory leak).

### ¿Puedo usar let/const dentro de setInterval?

Sí, pero ten cuidado con el scope:

```javascript
// ❌ No funciona
setInterval(() => {
    let contador = 0;  // Se reinicia a 0 cada vez
    contador++;
}, 1000);

// ✅ Funciona
let contador = 0;  // Fuera del setInterval
setInterval(() => {
    contador++;
}, 1000);
```

---

**Creado con ❤️ para 4Geeks Academy - Cohort España FS PT 129**
