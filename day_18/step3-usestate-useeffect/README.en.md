[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 3: Combining useState + useEffect 🔗

## Why combine them?

- **useState**: Manages state (data that changes)
- **useEffect**: Runs code when state changes

Together they create dynamic, powerful components.

## The Main Pattern

```javascript
import { useState, useEffect } from 'react';

function MiComponente() {
  // 1. Create state
  const [variable, setVariable] = useState(valorInicial);

  // 2. Run code when state changes
  useEffect(() => {
    // Do something here
  }, [variable]); // Dependency

  // 3. Update the state
  return (
    <button onClick={() => setVariable(nuevoValor)}>
      Click
    </button>
  );
}
```

---

## Example 1: Real-time search

**File**: `Ejemplo1-Busqueda.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo1Busqueda() {
  // State for what the user is searching
  const [busqueda, setBusqueda] = useState('');
  
  // State for the results
  const [resultados, setResultados] = useState([]);
  
  // State holding the people list (simulates API data)
  const [personas, setPersonas] = useState([
    'Juan',
    'María',
    'Carlos',
    'Ana',
    'Juan Carlos'
  ]);

  // When the user searches, filter results
  useEffect(() => {
    if (busqueda === '') {
      setResultados([]);
      return;
    }

    // Filter people matching the search
    const filtrados = personas.filter(p =>
      p.toLowerCase().includes(busqueda.toLowerCase())
    );

    setResultados(filtrados);
    console.log(`Buscando: "${busqueda}" - Encontrados: ${filtrados.length}`);
  }, [busqueda, personas]); // Runs when busqueda OR personas change

  return (
    <div>
      <h2>Buscar personas:</h2>
      <input
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
        placeholder="Buscar personas..."
      />
      
      {resultados.length > 0 && (
        <ul>
          {resultados.map((persona, i) => (
            <li key={i}>{persona}</li>
          ))}
        </ul>
      )}
      
      {busqueda !== '' && resultados.length === 0 && (
        <p>❌ No se encontraron resultados</p>
      )}

      <p>Abre consola para ver los logs</p>
    </div>
  );
}

export default Ejemplo1Busqueda;
```

**Flow step by step**:
1. User types "Juan" in the input → `setBusqueda('Juan')`
2. `busqueda` changes from `''` to `'Juan'` → React re-renders
3. `useEffect` runs because `busqueda` changed
4. People are filtered: `['Juan', 'Juan Carlos']`
5. `setResultados(...)` runs → React re-renders
6. The UI shows the 2 results

**Try it**: Type and open the console to see the messages

---

## Example 2: Shopping cart - Add items and compute total

**File**: `Ejemplo2-CarritoCompras.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo2CarritoCompras() {
  // Cart state (list of items)
  const [carrito, setCarrito] = useState([
    { id: 1, nombre: 'Laptop', precio: 500 },
    { id: 2, nombre: 'Mouse', precio: 20 }
  ]);

  // State for the total
  const [total, setTotal] = useState(0);

  // When the cart changes, recompute the total
  useEffect(() => {
    const sumaTotal = carrito.reduce((suma, item) => suma + item.precio, 0);
    setTotal(sumaTotal);
    
    console.log(`Items en carrito: ${carrito.length}`);
    console.log(`Total: $${sumaTotal}`);
  }, [carrito]); // Runs when carrito changes

  // Function to add a new item
  const agregarItem = () => {
    const nuevoItem = {
      id: carrito.length + 1,
      nombre: 'Teclado',
      precio: 80
    };
    
    // Create a new array with all items + the new one
    setCarrito([...carrito, nuevoItem]);
  };

  // Function to remove an item
  const eliminarItem = (id) => {
    const carritoActualizado = carrito.filter(item => item.id !== id);
    setCarrito(carritoActualizado);
  };

  return (
    <div>
      <h2>Mi Carrito</h2>
      
      <ul>
        {carrito.map(item => (
          <li key={item.id}>
            {item.nombre} - ${item.precio}
            <button onClick={() => eliminarItem(item.id)}>Eliminar</button>
          </li>
        ))}
      </ul>

      <h3>Total: ${total}</h3>
      <button onClick={agregarItem}>Añadir Teclado</button>

      <p>Abre consola para ver cuándo se recalcula el total</p>
    </div>
  );
}

export default Ejemplo2CarritoCompras;
```

**Flow**:
1. User clicks → `setCarrito` runs with the new item
2. `carrito` changes → `useEffect` runs
3. The total is computed → `setTotal` runs
4. The UI updates with the new total

**Important**: Use `[...carrito]` to create a new array. React needs to see that state changed.

---

## Example 3: Real-time validation

**File**: `Ejemplo3-Validacion.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo3Validacion() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  // Validation states
  const [emailValido, setEmailValido] = useState(false);
  const [passwordValido, setPasswordValido] = useState(false);
  const [puedeEnviar, setPuedeEnviar] = useState(false);

  // Validate email when it changes
  useEffect(() => {
    const valido = email.includes('@') && email.includes('.');
    setEmailValido(valido);
    
    console.log(`Email: "${email}" - Válido: ${valido}`);
  }, [email]);

  // Validate password when it changes
  useEffect(() => {
    const valido = password.length >= 6;
    setPasswordValido(valido);
    
    console.log(`Password: ${password.length} caracteres - Válido: ${valido}`);
  }, [password]);

  // If both are valid, allow submit
  useEffect(() => {
    const puede = emailValido && passwordValido;
    setPuedeEnviar(puede);
    
    console.log(`¿Puede enviar? ${puede}`);
  }, [emailValido, passwordValido]);

  return (
    <div>
      <h2>Registro</h2>
      
      <div>
        <label>Email:</label>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="tu@email.com"
        />
        <span>{emailValido ? '✅' : '❌'}</span>
      </div>

      <div>
        <label>Contraseña:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Al menos 6 caracteres"
        />
        <span>{passwordValido ? '✅' : '❌'}</span>
      </div>

      <button disabled={!puedeEnviar}>
        {puedeEnviar ? 'Enviar' : 'Llena el formulario'}
      </button>

      <p>Abre consola para ver validaciones en tiempo real</p>
    </div>
  );
}

export default Ejemplo3Validacion;
```

**Flow**: 
1. User types email → `setEmail` runs
2. `email` changes → `useEffect` validates → `setEmailValido` runs
3. User types password → `setPassword` runs
4. `password` changes → `useEffect` validates → `setPasswordValido` runs
5. `emailValido` or `passwordValido` change → `useEffect` checks if it can submit
6. The button enables when both are valid

---

## Example 4: Load data based on filter

**File**: `Ejemplo4-CargarDatos.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo4CargarDatos() {
  // State for the filter the user chooses
  const [categoria, setCategoria] = useState('frutas');
  
  // State for items to display
  const [items, setItems] = useState([]);
  
  // State to indicate loading
  const [cargando, setCargando] = useState(false);

  // When the category changes, load new data
  useEffect(() => {
    setCargando(true);
    console.log(`Cargando ${categoria}...`);

    // Simulate an API call with setTimeout
    const timeout = setTimeout(() => {
      // Simulated API data
      const datos = {
        frutas: ['Manzana', 'Banana', 'Naranja'],
        verduras: ['Lechuga', 'Tomate', 'Zanahoria'],
        carnes: ['Pollo', 'Res', 'Pescado']
      };

      setItems(datos[categoria] || []);
      setCargando(false);
      console.log('✅ Items cargados');
    }, 1500); // Simulate API latency

    // Cleanup: if the category changes before it finishes, cancel
    return () => {
      clearTimeout(timeout);
      console.log('Carga cancelada');
    };
  }, [categoria]); // Runs when categoria changes

  return (
    <div>
      <h2>Elige una categoría:</h2>
      
      <div>
        <button 
          onClick={() => setCategoria('frutas')}
          style={{ fontWeight: categoria === 'frutas' ? 'bold' : 'normal' }}
        >
          Frutas
        </button>
        <button 
          onClick={() => setCategoria('verduras')}
          style={{ fontWeight: categoria === 'verduras' ? 'bold' : 'normal' }}
        >
          Verduras
        </button>
        <button 
          onClick={() => setCategoria('carnes')}
          style={{ fontWeight: categoria === 'carnes' ? 'bold' : 'normal' }}
        >
          Carnes
        </button>
      </div>

      {cargando && <p>⏳ Cargando {categoria}...</p>}

      {!cargando && items.length > 0 && (
        <ul>
          {items.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      )}

      <p>Abre consola para ver cuándo se carga</p>
    </div>
  );
}

export default Ejemplo4CargarDatos;
```

**Flow**:
1. User clicks "Verduras" → `setCategoria('verduras')`
2. `categoria` changes → `useEffect` runs
3. Shows "⏳ Cargando..." → `setCargando(true)`
4. Waits 1.5 seconds (simulating API)
5. Loads the data → `setItems([...])`
6. Hides loading → `setCargando(false)`
7. The UI shows the items

**With cleanup**: If you change category before it finishes, the previous one is canceled

---

## Summary Table: useState + useEffect flow

| Step | What happens |
|------|--------------|
| 1 | User does something (types, clicks, etc.) |
| 2 | `setState(...)` runs |
| 3 | State changes |
| 4 | React re-renders the component |
| 5 | `useEffect` detects that its dependencies changed |
| 6 | `useEffect` runs |
| 7 | It may run more `setState(...)` calls |
| 8 | React updates the UI |

---

## Key Points ✨

1. **The flow**: User acts → State changes → useEffect runs
2. **Dependencies are critical**: React watches which variables you use
3. **One setState can trigger multiple useEffects**: If several depend on that variable
4. **Cleanup matters**: To cancel pending operations
5. **Array state needs new arrays**: Use `[...array]` or `array.filter(...)`, etc.

---

## Your Exercise 🎯

Create a `MiEjercicio.jsx` that:

1. ✅ Has a `productos` state with 3 initial products (id, nombre, precio)
2. ✅ Has a `cantidad` state starting at 0
3. ✅ When you select a product (with buttons), increases the quantity
4. ✅ Uses `useEffect` to print to the console: "Producto: Laptop, Cantidad: 2"
5. ✅ Displays which product is selected and the quantity on screen

**Basic structure**:
```javascript
const [productos, setProductos] = useState([
  { id: 1, nombre: 'Laptop', precio: 500 },
  { id: 2, nombre: 'Mouse', precio: 20 },
  { id: 3, nombre: 'Teclado', precio: 80 }
]);

const [productoSeleccionado, setProductoSeleccionado] = useState(null);
const [cantidad, setCantidad] = useState(0);

// ❓ TODO: Use useEffect to do something when cantidad changes
```

**Hint**: 
- When you switch products, reset the quantity to 0
- The `useEffect` should log information to the console
- What is the dependency?

---

## Next Steps

Once you understand how to combine hooks:

✅ useState handles multiple states  
✅ useEffect reacts to multiple changes  
✅ You can build complex interactions  

You'll be ready for:
- **Step 4**: Building controlled forms
- **Step 5**: Input validation

---

**💡 Tip**: Draw a diagram. Write each `useState` as a box and each `useEffect` as an arrow watching that box. When the box changes, the arrow fires.
