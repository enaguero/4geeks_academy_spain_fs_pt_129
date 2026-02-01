# Step 1: useEffect Básico ⚙️

## ¿Qué es useEffect?

`useEffect` es un hook de React que te permite ejecutar código **después** de que el componente se renderiza en la pantalla.

### Analogía simple

Piensa en un cocinero:
- **El renderizado**: El cocinero prepara el plato y lo pone en la mesa
- **useEffect**: Después de ponerlo en la mesa, hace algo más (añade salsa, pone decoración, etc.)

### Sintaxis básica

```javascript
import { useEffect } from 'react';

function MiComponente() {
  useEffect(() => {
    // Este código se ejecuta DESPUÉS de que el componente se renderiza
    console.log('El componente se acaba de dibujar en pantalla!');
  }, []); // El array de dependencias controla CUÁNDO

  return <div>Hola</div>;
}
```

---

## El Array de Dependencias 🔑

El **segundo parámetro** de `useEffect` es el array de dependencias. Controla **CUÁNDO** se ejecuta:

| Array | Se ejecuta | Cuándo |
|-------|-----------|--------|
| (sin incluir) | Después de CADA render | ⚠️ Peligroso si modificas estado |
| `[]` | UNA SOLA VEZ | Al cargar el componente |
| `[variable]` | Cuando variable cambia | Cada vez que esa variable cambia |
| `[var1, var2]` | Cuando var1 O var2 cambian | Cada vez que cualquiera cambia |

---

## Ejemplos Concretos y Completos

### Ejemplo 1: useEffect básico sin estado

**Archivo**: `Ejemplo1-BienvenidaConsola.jsx`

```javascript
import { useEffect } from 'react';

function Ejemplo1BienvenidaConsola() {
  useEffect(() => {
    // Se ejecuta UNA SOLA VEZ cuando el componente se carga
    console.log('¡Bienvenido! El componente se cargó');
    alert('Componente cargado correctamente');
  }, []); // Array vacío = ejecutar solo 1 vez

  return (
    <div>
      <h1>Abre la consola (F12) para ver el mensaje</h1>
    </div>
  );
}

export default Ejemplo1BienvenidaConsola;
```

**Cómo funciona**:
1. El componente se renderiza por primera vez
2. El `alert` aparece una sola vez
3. El `console.log` se ejecuta una sola vez
4. Si recargais la página, se ejecuta nuevamente (es una nueva carga)

**Prueba**: Recarga la página y verás que solo aparece una vez

---

### Ejemplo 2: useEffect con estado - Detectar cambios

**Archivo**: `Ejemplo2-DetectarCambios.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo2DetectarCambios() {
  const [nombre, setNombre] = useState('');

  // Se ejecuta cuando el valor de "nombre" cambia
  useEffect(() => {
    console.log(`El usuario escribió: "${nombre}"`);
    console.log(`Número de caracteres: ${nombre.length}`);
  }, [nombre]); // Dependencia: nombre

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

**Cómo funciona**:
1. Abre la consola (F12)
2. Escribe en el input
3. Cada letra que escribes ejecuta el `useEffect` porque `nombre` cambió
4. En la consola ves el nombre y cuántas letras tiene
5. Cuando dejas de escribir, el `useEffect` deja de ejecutarse

**Prueba**: Abre consola, escribe 5 letras y verás 5 mensajes diferentes

---

### Ejemplo 3: useEffect sin dependencias - PELIGRO ⚠️

**Archivo**: `Ejemplo3-PeligroLoopInfinito.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo3PeligroLoopInfinito() {
  const [contador, setContador] = useState(0);

  // ❌ ESTO CAUSA LOOP INFINITO
  useEffect(() => {
    console.log(`Contador: ${contador}`);
    setContador(contador + 1); // Modifica el estado
  }); // SIN array de dependencias - ¡PROBLEMA!

  return (
    <div>
      <h1>Contador: {contador}</h1>
      <p>Abre consola - ¡Los números no paran!</p>
    </div>
  );
}

export default Ejemplo3PeligroLoopInfinito;
```

**⚠️ ADVERTENCIA**: 
- Abre la consola y verás números infinitos
- El contador sube sin parar
- La página se congela
- **NO USES ESTE CÓDIGO EN PRODUCCIÓN**

**Por qué pasa**:
1. Componente se renderiza → contador = 0
2. `useEffect` se ejecuta → `setContador(1)`
3. Estado cambió → nuevo render
4. `useEffect` se ejecuta OTRA VEZ → `setContador(2)`
5. Estado cambió → nuevo render
6. ... INFINITAMENTE ...

Ver archivo: `LOOP-INFINITO-EJEMPLO.md` para más detalles

---

### Ejemplo 4: useEffect con cleanup - Interval

**Archivo**: `Ejemplo4-Temporizador.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo4Temporizador() {
  const [segundos, setSegundos] = useState(0);
  const [activo, setActivo] = useState(false);

  useEffect(() => {
    // Si no está activo, no hacer nada
    if (!activo) return;

    console.log('Iniciando temporizador...');

    // Crear un interval que se ejecuta cada 1000ms (1 segundo)
    const intervalo = setInterval(() => {
      setSegundos(s => s + 1);
      console.log('Tick!');
    }, 1000);

    // CLEANUP: función que se ejecuta cuando se desmonta o cuando activo cambia
    return () => {
      console.log('Limpiando intervalo...');
      clearInterval(intervalo);
    };
  }, [activo]); // Se ejecuta cuando activo cambia

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

**Cómo funciona**:
1. Haz click en "Iniciar"
2. El contador empieza a subir (cada segundo aumenta 1)
3. En consola ves "Tick!" cada segundo
4. Haz click en "Pausar"
5. En consola ves "Limpiando intervalo..."
6. El contador se detiene
7. Si vuelves a hacer click en "Iniciar", comienza de nuevo

**Importante - El Cleanup**:
```javascript
return () => {
  clearInterval(intervalo); // Limpia el interval
};
```

Sin el cleanup, cada vez que presionarías "Iniciar", se crearía un nuevo interval sin eliminar el anterior. ¡Problemas!

---

### Ejemplo 5: useEffect que modifica el documento

**Archivo**: `Ejemplo5-CambiarTituloVentana.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo5CambiarTituloVentana() {
  const [seccion, setSeccion] = useState('Inicio');

  useEffect(() => {
    // Cambiar el título de la pestaña del navegador
    document.title = `Mi App - ${seccion}`;
    console.log(`Página: ${seccion}`);
  }, [seccion]); // Se ejecuta cuando seccion cambia

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

**Cómo funciona**:
1. Haz click en "Contacto"
2. El título de la pestaña cambió a "Mi App - Contacto"
3. Haz click en "Ayuda"
4. El título cambió a "Mi App - Ayuda"
5. Cada click ejecuta el `useEffect` porque `seccion` cambió

---

### Ejemplo 6: Múltiples dependencias

**Archivo**: `Ejemplo6-MultiplesDependencias.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo6MultiplesDependencias() {
  const [nombre, setNombre] = useState('');
  const [edad, setEdad] = useState('');

  useEffect(() => {
    // Se ejecuta cuando NOMBRE O EDAD cambian
    console.log(`Datos: ${nombre}, ${edad} años`);
    
    if (nombre && edad) {
      console.log('✅ Tienes nombre y edad');
    }
  }, [nombre, edad]); // Dos dependencias

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

**Cómo funciona**:
1. Escribe un nombre → `useEffect` se ejecuta
2. Escribe una edad → `useEffect` se ejecuta nuevamente
3. Cualquiera de las dos variables causa la ejecución
4. Si ambas tienen valor, ves el mensaje "✅ Tienes nombre y edad"

---

## Tabla Resumen: Cuándo se ejecuta

```javascript
// Versión A: Sin dependencias
useEffect(() => {
  console.log('A');
});
// ❌ Se ejecuta SIEMPRE (peligroso con estado)

// Versión B: Array vacío
useEffect(() => {
  console.log('B');
}, []);
// ✅ Se ejecuta UNA SOLA VEZ al cargar

// Versión C: Una dependencia
useEffect(() => {
  console.log('C');
}, [nombre]);
// ✅ Se ejecuta cuando nombre cambia

// Versión D: Múltiples dependencias
useEffect(() => {
  console.log('D');
}, [nombre, edad]);
// ✅ Se ejecuta cuando nombre O edad cambian
```

---

## Regla de Oro 🏆

**Si usas una variable en useEffect, debe estar en el array de dependencias**

```javascript
const [nombre, setNombre] = useState('');

// ❌ MALO - Usa nombre pero no está en dependencias
useEffect(() => {
  console.log(nombre); // ¿Por qué no en dependencias?
}, []);

// ✅ BIEN - nombre está en dependencias
useEffect(() => {
  console.log(nombre);
}, [nombre]);
```

---

## Puntos Clave ✨

1. **useEffect se ejecuta DESPUÉS del renderizado** - No durante
2. **El array de dependencias controla CUÁNDO** - Es el gatillo
3. **Cleanup es importante** - Especialmente con intervals, listeners, etc.
4. **Sin dependencias = peligro** - Solo si no usas estado
5. **Con dependencias correctas = seguro** - React sabe cuándo ejecutar

---

## Archivo Especial

Hay un archivo especial: `LOOP-INFINITO-EJEMPLO.md`

Este archivo explica en detalle:
- ❌ Cómo crear accidentalmente un loop infinito
- ✅ Cómo arreglarlo
- Ejemplos concretos paso a paso

**Lee este archivo si tu código se congela o ves errores raros**

---

## Tu Ejercicio 🎯

Crea un archivo `MiEjercicio.jsx` que:

1. ✅ Tenga un estado llamado `color` con valor inicial `'white'`
2. ✅ Usa `useEffect` para cambiar el color de fondo del `<body>` cuando `color` cambia
3. ✅ Tenga 3 botones para cambiar entre: rojo, azul, verde
4. ✅ Cuando el componente se desmonta, restaure el color blanco

**Estructura básica**:
```javascript
import { useState, useEffect } from 'react';

function MiEjercicio() {
  const [color, setColor] = useState('white');

  // ❓ TODO: Usa useEffect para cambiar document.body.style.backgroundColor

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

**Pistas**:
- Usa `document.body.style.backgroundColor = color` para cambiar el color
- El cleanup debería restaurar el color a blanco
- Piensa: ¿cuándo debería ejecutarse? ¿cuando qué cambia?

---

## Próximos Pasos

Una vez entiendas:

✅ Qué es useEffect  
✅ El array de dependencias  
✅ Cómo escribir cleanup  

Estarás listo para:
- **Step 2**: Ciclo de vida completo del componente
- **Step 3**: Combinar useState + useEffect en aplicaciones reales

---

## Recursos

- [useEffect en React Docs](https://react.dev/reference/react/useEffect)
- [Rules of Hooks](https://react.dev/warnings/mismatching-children-hint)
- [Archivo especial: Loop Infinito](./LOOP-INFINITO-EJEMPLO.md)

---

**💡 Consejo**: Abre la consola del navegador (F12) con cada ejemplo. Ver lo que sucede en consola es clave para entender useEffect.
