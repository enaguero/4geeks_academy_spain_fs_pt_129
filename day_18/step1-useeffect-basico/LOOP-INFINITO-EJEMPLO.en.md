[🇪🇸 Español](LOOP-INFINITO-EJEMPLO.md) | 🇬🇧 **English**

# ⚠️ Infinite Loop with useEffect - Concrete Example

## The Problem

When you use `useEffect` **without a dependency array** and **modify state inside it**, you create an infinite loop.

## Example that CAUSES an Infinite Loop ❌

```javascript
import { useState, useEffect } from 'react';

function LoopInfinitoMALO() {
  const [contador, setContador] = useState(0);

  // ❌ BAD - NO dependency array
  useEffect(() => {
    console.log('useEffect ejecutado, contador es:', contador);
    setContador(contador + 1); // This triggers a new render
  }); // Missing dependency array []

  return <div>Contador: {contador}</div>;
}

export default LoopInfinitoMALO;
```

## What happens, step by step?

```
1. The component renders for the first time
   contador = 0

2. useEffect runs (because it has no dependency array)
   console.log('useEffect ejecutado, contador es: 0')
   setContador(0 + 1) → contador is now 1

3. Because state changed, React re-renders the component
   contador = 1

4. useEffect runs AGAIN (because it has no dependency array)
   console.log('useEffect ejecutado, contador es: 1')
   setContador(1 + 1) → contador is now 2

5. Because state changed, React re-renders the component
   contador = 2

6. useEffect runs AGAIN
   console.log('useEffect ejecutado, contador es: 2')
   setContador(2 + 1) → contador is now 3

7. ... this continues FOREVER ...
```

## Symptoms: How to tell you have an infinite loop

1. **In the console**: Messages keep appearing nonstop (lightning fast)
2. **The page freezes or gets very slow**
3. **The browser may crash** due to memory usage

## Open the browser console and you will see:

```
useEffect ejecutado, contador es: 0
useEffect ejecutado, contador es: 1
useEffect ejecutado, contador es: 2
useEffect ejecutado, contador es: 3
useEffect ejecutado, contador es: 4
useEffect ejecutado, contador es: 5
... thousands of times ...
```

---

## The Fix: Dependency Array ✅

### Fix 1: If you want it to run ONLY ONCE

```javascript
import { useState, useEffect } from 'react';

function LoopInfinitoFIJO1() {
  const [contador, setContador] = useState(0);

  // ✅ GOOD - WITH an empty array []
  useEffect(() => {
    console.log('useEffect ejecutado una sola vez, contador es:', contador);
    setContador(1); // Runs only ONCE
  }, []); // Empty array = only on mount

  return <div>Contador: {contador}</div>;
}

export default LoopInfinitoFIJO1;
```

**Step by step**:
```
1. The component renders for the first time
   contador = 0

2. useEffect runs (it's the first time and the array is [])
   console.log('useEffect ejecutado una sola vez, contador es: 0')
   setContador(1) → contador is now 1

3. Because state changed, React re-renders the component
   contador = 1

4. useEffect does NOT run again (because the array is empty [])
   Done. No infinite loop.
```

---

### Fix 2: If you want to run only when contador changes

```javascript
import { useState, useEffect } from 'react';

function LoopInfinitoFIJO2() {
  const [contador, setContador] = useState(0);

  // ✅ GOOD - WITH contador in the dependencies
  useEffect(() => {
    console.log('El contador cambió a:', contador);
    // Here you do NOT modify contador
    // You just do something based on its value
  }, [contador]); // contador in the dependencies

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

**Step by step**:
```
1. The component renders for the first time
   contador = 0

2. useEffect runs (first time)
   console.log('El contador cambió a: 0')
   We don't modify contador

3. The user clicks the button
   setContador(1) → contador is now 1

4. React re-renders the component
   contador = 1

5. useEffect runs (because contador CHANGED)
   console.log('El contador cambió a: 1')
   We don't modify contador

6. The user clicks again
   setContador(2) → contador is now 2

7. React re-renders the component
   contador = 2

8. useEffect runs (because contador CHANGED)
   console.log('El contador cambió a: 2')
   We don't modify contador

9. No infinite loop. It only runs when the user changes contador.
```

---

## Visual Comparison

### ❌ BAD - Infinite Loop (no array)
```javascript
const [count, setCount] = useState(0);

useEffect(() => {
  setCount(count + 1); // Modifies state with NO dependency array
});
// RESULT: Infinite loop ↔️↔️↔️
```

### ✅ GOOD - Only once (empty array)
```javascript
const [count, setCount] = useState(0);

useEffect(() => {
  setCount(1); // Runs only ONCE
}, []);
// RESULT: Runs 1 time, done
```

### ✅ GOOD - When the dependency changes (array with variable)
```javascript
const [count, setCount] = useState(0);

useEffect(() => {
  console.log('Count es:', count);
  // You do NOT modify count here
}, [count]);
// RESULT: Runs only when count changes (the user does something)
```

---

## The Golden Rule 🏆

**If you modify state inside useEffect, you must use a dependency array that prevents the loop**

| Situation | Code | Result |
|-----------|------|--------|
| No array, modifies state | `setCount(count + 1)` with no array | ❌ Infinite loop |
| Empty array, modifies state | `setCount(1)` with `[]` | ✅ Runs once |
| Array with dependency, reads state | `console.log(count)` with `[count]` | ✅ Runs when it changes |
| Array with dependency, modifies state | `setCount(count + 1)` with `[count]` | ❌ Infinite loop |

---

## Exercise: Spot the Problem 🎯

Which of these has an infinite loop?

### Option A:
```javascript
const [name, setName] = useState('');

useEffect(() => {
  console.log('Hola ' + name);
}, [name]);
```

### Option B:
```javascript
const [name, setName] = useState('');

useEffect(() => {
  setName('Juan');
});
```

### Option C:
```javascript
const [name, setName] = useState('');

useEffect(() => {
  console.log('Hola ' + name);
}, []);
```

---

## Exercise Answers

**Option A: ✅ GOOD**
- Runs when `name` changes
- Only logs, doesn't modify state
- No infinite loop

**Option B: ❌ BAD - Infinite Loop**
- No dependency array
- Modifies `name` on every render
- That triggers a new render → which runs useEffect → which modifies name → infinite cycle

**Option C: ✅ GOOD**
- Runs ONLY ONCE
- Empty array `[]` prevents re-runs
- No infinite loop

---

## Summary

| Concept | Explanation |
|---------|-------------|
| **No array** | Runs after EVERY render (dangerous if you modify state) |
| **Empty array []** | Runs ONLY ONCE on mount (safe for initialization) |
| **Array with dependencies** | Runs when dependencies change (best option) |
| **Infinite loop** | Happens when you modify state without an appropriate dependency array |

---

## How to Fix It if It Happens to You

If your page freezes due to an infinite loop:

1. **Ctrl+Shift+J** (or F12) to open the console
2. You'll see messages repeating infinitely
3. Find the `useEffect` causing the problem
4. Add a dependency array `[]` or `[variable]`
5. Make sure you do NOT modify the state listed in the dependencies
