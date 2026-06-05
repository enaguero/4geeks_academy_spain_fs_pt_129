🇪🇸 **Español** | [🇬🇧 English](LOOP-INFINITO-EJEMPLO.en.md)

# ⚠️ Loop Infinito con useEffect - Ejemplo Concreto

## El Problema

Cuando usas `useEffect` **sin array de dependencias** y **modificas el estado**, creas un loop infinito.

## Ejemplo que GENERA Loop Infinito ❌

```javascript
import { useState, useEffect } from 'react';

function LoopInfinitoMALO() {
  const [contador, setContador] = useState(0);

  // ❌ MALO - SIN array de dependencias
  useEffect(() => {
    console.log('useEffect ejecutado, contador es:', contador);
    setContador(contador + 1); // Esto causa un nuevo render
  }); // Falta el array de dependencias []

  return <div>Contador: {contador}</div>;
}

export default LoopInfinitoMALO;
```

## ¿Qué sucede paso a paso?

```
1. El componente se renderiza por primera vez
   contador = 0

2. useEffect se ejecuta (porque no tiene array de dependencias)
   console.log('useEffect ejecutado, contador es: 0')
   setContador(0 + 1) → contador ahora es 1

3. Como el estado cambió, React re-renderiza el componente
   contador = 1

4. useEffect se ejecuta NUEVAMENTE (porque no tiene array de dependencias)
   console.log('useEffect ejecutado, contador es: 1')
   setContador(1 + 1) → contador ahora es 2

5. Como el estado cambió, React re-renderiza el componente
   contador = 2

6. useEffect se ejecuta NUEVAMENTE
   console.log('useEffect ejecutado, contador es: 2')
   setContador(2 + 1) → contador ahora es 3

7. ... esto continúa INFINITAMENTE ...
```

## Síntomas: Cómo saber que tienes un loop infinito

1. **En la consola**: Los mensajes aparecen sin parar (a velocidad de rayo)
2. **La página se congela o va muy lenta**
3. **El navegador puede crashear** por el uso de memoria

## Abre la consola del navegador y verás:

```
useEffect ejecutado, contador es: 0
useEffect ejecutado, contador es: 1
useEffect ejecutado, contador es: 2
useEffect ejecutado, contador es: 3
useEffect ejecutado, contador es: 4
useEffect ejecutado, contador es: 5
... miles de veces ...
```

---

## La Solución: Array de Dependencias ✅

### Solución 1: Si quieres que se ejecute UNA SOLA VEZ

```javascript
import { useState, useEffect } from 'react';

function LoopInfinitoFIJO1() {
  const [contador, setContador] = useState(0);

  // ✅ BIEN - CON array vacío []
  useEffect(() => {
    console.log('useEffect ejecutado una sola vez, contador es:', contador);
    setContador(1); // Se ejecuta UNA SOLA VEZ
  }, []); // Array vacío = solo al cargar

  return <div>Contador: {contador}</div>;
}

export default LoopInfinitoFIJO1;
```

**Paso a paso**:
```
1. El componente se renderiza por primera vez
   contador = 0

2. useEffect se ejecuta (es la primera vez y tiene [])
   console.log('useEffect ejecutado una sola vez, contador es: 0')
   setContador(1) → contador ahora es 1

3. Como el estado cambió, React re-renderiza el componente
   contador = 1

4. useEffect NO se ejecuta nuevamente (porque tiene [] vacío)
   Fin. Sin loop infinito.
```

---

### Solución 2: Si quieres ejecutar solo cuando contador cambia

```javascript
import { useState, useEffect } from 'react';

function LoopInfinitoFIJO2() {
  const [contador, setContador] = useState(0);

  // ✅ BIEN - CON contador en dependencias
  useEffect(() => {
    console.log('El contador cambió a:', contador);
    // Aquí NO modificas el contador
    // Solo haces algo basado en su valor
  }, [contador]); // Contador en dependencias

  return (
    <div>
      <p>Contador: {contador}</p>
      <button onClick={() => setContador(contador + 1)}>
        Aumentar
      </button>
    </div>
  );
}

export default LoopInfinitoFIJO2;
```

**Paso a paso**:
```
1. El componente se renderiza por primera vez
   contador = 0

2. useEffect se ejecuta (es la primera vez)
   console.log('El contador cambió a: 0')
   No modificamos contador

3. El usuario hace click en el botón
   setContador(1) → contador ahora es 1

4. React re-renderiza el componente
   contador = 1

5. useEffect se ejecuta (porque contador CAMBIÓ)
   console.log('El contador cambió a: 1')
   No modificamos contador

6. El usuario hace click nuevamente
   setContador(2) → contador ahora es 2

7. React re-renderiza el componente
   contador = 2

8. useEffect se ejecuta (porque contador CAMBIÓ)
   console.log('El contador cambió a: 2')
   No modificamos contador

9. Sin loop infinito. Solo se ejecuta cuando el usuario cambia el contador.
```

---

## Comparación Visual

### ❌ MALO - Loop Infinito (sin array)
```javascript
const [count, setCount] = useState(0);

useEffect(() => {
  setCount(count + 1); // Modifica estado SIN array de dependencias
});
// RESULTADO: Loop infinito ↔️↔️↔️
```

### ✅ BIEN - Solo una vez (array vacío)
```javascript
const [count, setCount] = useState(0);

useEffect(() => {
  setCount(1); // Se ejecuta UNA SOLA VEZ
}, []);
// RESULTADO: Se ejecuta 1 vez, fin
```

### ✅ BIEN - Cuando cambia la dependencia (array con variable)
```javascript
const [count, setCount] = useState(0);

useEffect(() => {
  console.log('Count es:', count);
  // NO modificas count aquí
}, [count]);
// RESULTADO: Se ejecuta solo cuando count cambia (el usuario hace algo)
```

---

## La Regla de Oro 🏆

**Si modificas estado en useEffect, debes tener un array de dependencias que evite el loop**

| Situación | Código | Resultado |
|-----------|--------|-----------|
| Sin array, modifica estado | `setCount(count + 1)` con ningún array | ❌ Loop infinito |
| Array vacío, modifica estado | `setCount(1)` con `[]` | ✅ Una sola ejecución |
| Array con dependencia, Lee estado | `console.log(count)` con `[count]` | ✅ Se ejecuta cuando cambias |
| Array con dependencia, Modifica estado | `setCount(count + 1)` con `[count]` | ❌ Loop infinito |

---

## Ejercicio: Identifica el Problema 🎯

¿Cuál de estos tiene loop infinito?

### Opción A:
```javascript
const [name, setName] = useState('');

useEffect(() => {
  console.log('Hola ' + name);
}, [name]);
```

### Opción B:
```javascript
const [name, setName] = useState('');

useEffect(() => {
  setName('Juan');
});
```

### Opción C:
```javascript
const [name, setName] = useState('');

useEffect(() => {
  console.log('Hola ' + name);
}, []);
```

---

## Respuestas del Ejercicio

**Opción A: ✅ BIEN**
- Ejecuta cuando `name` cambia
- Solo imprime, no modifica estado
- Sin loop infinito

**Opción B: ❌ MALO - Loop Infinito**
- Sin array de dependencias
- Modifica `name` cada vez que se renderiza
- Eso causa un nuevo render → que ejecuta useEffect → que modifica name → ciclo infinito

**Opción C: ✅ BIEN**
- Ejecuta UNA SOLA VEZ
- Array vacío `[]` previene re-ejecuciones
- Sin loop infinito

---

## Resumen

| Concepto | Explicación |
|----------|-------------|
| **Sin array** | Se ejecuta después de CADA render (peligroso si modificas estado) |
| **Array vacío []** | Se ejecuta UNA SOLA VEZ al cargar (seguro para inicializar) |
| **Array con dependencias** | Se ejecuta cuando las dependencias cambian (mejor opción) |
| **Loop infinito** | Ocurre cuando modificas estado sin un array de dependencias apropiado |

---

## Cómo Arreglarlo si Te Pasa

Si tu página se congela por un loop infinito:

1. **Ctrl+Shift+J** (o F12) para abrir consola
2. Verás mensajes repetidos infinitamente
3. Busca el `useEffect` que está causando el problema
4. Añade un array de dependencias `[]` o `[variable]`
5. Asegúrate de NO modificar el estado que está en las dependencias
