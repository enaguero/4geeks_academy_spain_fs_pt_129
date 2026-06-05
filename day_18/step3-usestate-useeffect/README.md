🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# Step 3: Combinando useState + useEffect 🔗

## ¿Por qué combinar ambos?

- **useState**: Maneja el estado (datos que cambian)
- **useEffect**: Ejecuta código cuando el estado cambia

Juntos crean componentes dinámicos y poderosos.

## Patrón Principal

```javascript
import { useState, useEffect } from 'react';

function MiComponente() {
  // 1. Crea estado
  const [variable, setVariable] = useState(valorInicial);

  // 2. Ejecuta código cuando el estado cambia
  useEffect(() => {
    // Haz algo aquí
  }, [variable]); // Dependencia

  // 3. Actualiza el estado
  return (
    <button onClick={() => setVariable(nuevoValor)}>
      Click
    </button>
  );
}
```

---

## Ejemplo 1: Búsqueda en tiempo real

**Archivo**: `Ejemplo1-Busqueda.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo1Busqueda() {
  // Estado para lo que busca el usuario
  const [busqueda, setBusqueda] = useState('');
  
  // Estado para los resultados
  const [resultados, setResultados] = useState([]);
  
  // Estado con la lista de personas (simula datos de una API)
  const [personas, setPersonas] = useState([
    'Juan',
    'María',
    'Carlos',
    'Ana',
    'Juan Carlos'
  ]);

  // Cuando el usuario busca, filtrar resultados
  useEffect(() => {
    if (busqueda === '') {
      setResultados([]);
      return;
    }

    // Filtrar personas que coincidan con la búsqueda
    const filtrados = personas.filter(p =>
      p.toLowerCase().includes(busqueda.toLowerCase())
    );

    setResultados(filtrados);
    console.log(`Buscando: "${busqueda}" - Encontrados: ${filtrados.length}`);
  }, [busqueda, personas]); // Se ejecuta cuando busqueda O personas cambian

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

**Flujo paso a paso**:
1. Usuario escribe "Juan" en el input → `setBusqueda('Juan')`
2. `busqueda` cambia de `''` a `'Juan'` → React re-renderiza
3. `useEffect` se ejecuta porque `busqueda` cambió
4. Se filtran personas: `['Juan', 'Juan Carlos']`
5. Se ejecuta `setResultados(...)` → React re-renderiza
6. La UI muestra los 2 resultados

**Prueba**: Escribe y abre consola para ver los mensajes

---

## Ejemplo 2: Carrito de compras - Añadir y calcular total

**Archivo**: `Ejemplo2-CarritoCompras.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo2CarritoCompras() {
  // Estado del carrito (lista de items)
  const [carrito, setCarrito] = useState([
    { id: 1, nombre: 'Laptop', precio: 500 },
    { id: 2, nombre: 'Mouse', precio: 20 }
  ]);

  // Estado para el total
  const [total, setTotal] = useState(0);

  // Cuando el carrito cambia, recalcular el total
  useEffect(() => {
    const sumaTotal = carrito.reduce((suma, item) => suma + item.precio, 0);
    setTotal(sumaTotal);
    
    console.log(`Items en carrito: ${carrito.length}`);
    console.log(`Total: $${sumaTotal}`);
  }, [carrito]); // Se ejecuta cuando carrito cambia

  // Función para añadir un nuevo item
  const agregarItem = () => {
    const nuevoItem = {
      id: carrito.length + 1,
      nombre: 'Teclado',
      precio: 80
    };
    
    // Crea un nuevo array con todos los items + el nuevo
    setCarrito([...carrito, nuevoItem]);
  };

  // Función para eliminar un item
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

**Flujo**:
1. Usuario hace click → `setCarrito` se ejecuta con nuevo item
2. `carrito` cambia → `useEffect` se ejecuta
3. Se calcula el total → `setTotal` se ejecuta
4. La UI se actualiza con el nuevo total

**Importante**: Usa `[...carrito]` para crear un nuevo array. React necesita ver que el estado cambió.

---

## Ejemplo 3: Validación en tiempo real

**Archivo**: `Ejemplo3-Validacion.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo3Validacion() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  // Estados para validación
  const [emailValido, setEmailValido] = useState(false);
  const [passwordValido, setPasswordValido] = useState(false);
  const [puedeEnviar, setPuedeEnviar] = useState(false);

  // Validar email cuando cambia
  useEffect(() => {
    const valido = email.includes('@') && email.includes('.');
    setEmailValido(valido);
    
    console.log(`Email: "${email}" - Válido: ${valido}`);
  }, [email]);

  // Validar password cuando cambia
  useEffect(() => {
    const valido = password.length >= 6;
    setPasswordValido(valido);
    
    console.log(`Password: ${password.length} caracteres - Válido: ${valido}`);
  }, [password]);

  // Si ambos son válidos, permitir envío
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

**Flujo**: 
1. Usuario escribe email → `setEmail` ejecuta
2. `email` cambia → `useEffect` valida → `setEmailValido` ejecuta
3. Usuario escribe password → `setPassword` ejecuta
4. `password` cambia → `useEffect` valida → `setPasswordValido` ejecuta
5. `emailValido` o `passwordValido` cambian → `useEffect` verifica si puede enviar
6. El botón se activa cuando ambos son válidos

---

## Ejemplo 4: Cargar datos según filtro

**Archivo**: `Ejemplo4-CargarDatos.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo4CargarDatos() {
  // Estado del filtro que el usuario elige
  const [categoria, setCategoria] = useState('frutas');
  
  // Estado de los items a mostrar
  const [items, setItems] = useState([]);
  
  // Estado para mostrar carga
  const [cargando, setCargando] = useState(false);

  // Cuando la categoría cambia, cargar nuevos datos
  useEffect(() => {
    setCargando(true);
    console.log(`Cargando ${categoria}...`);

    // Simular API call con setTimeout
    const timeout = setTimeout(() => {
      // Simular datos de una API
      const datos = {
        frutas: ['Manzana', 'Banana', 'Naranja'],
        verduras: ['Lechuga', 'Tomate', 'Zanahoria'],
        carnes: ['Pollo', 'Res', 'Pescado']
      };

      setItems(datos[categoria] || []);
      setCargando(false);
      console.log('✅ Items cargados');
    }, 1500); // Simular latencia de la API

    // Cleanup: si cambian de categoría antes de terminar, cancelar
    return () => {
      clearTimeout(timeout);
      console.log('Carga cancelada');
    };
  }, [categoria]); // Se ejecuta cuando categoria cambia

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

**Flujo**:
1. Usuario hace click "Verduras" → `setCategoria('verduras')`
2. `categoria` cambia → `useEffect` se ejecuta
3. Muestra "⏳ Cargando..." → `setCargando(true)`
4. Espera 1.5 segundos (simular API)
5. Carga los datos → `setItems([...])`
6. Oculta cargando → `setCargando(false)`
7. La UI muestra los items

**Con cleanup**: Si cambias de categoría antes de que termine, se cancela el anterior

---

## Tabla Resumen: Flujo useState + useEffect

| Paso | Qué sucede |
|------|-----------|
| 1 | Usuario hace algo (escribe, click, etc.) |
| 2 | Se ejecuta `setState(...)` |
| 3 | El estado cambia |
| 4 | React re-renderiza el componente |
| 5 | `useEffect` detecta que sus dependencias cambiaron |
| 6 | `useEffect` se ejecuta |
| 7 | Puede ejecutar más `setState(...)` |
| 8 | React actualiza la UI |

---

## Puntos Clave ✨

1. **El flujo**: Usuario actúa → Estado cambia → useEffect se ejecuta
2. **Dependencias son críticas**: React observa qué variables usar
3. **Un setState puede disparar múltiples useEffects**: Si varias dependencias tienen esa variable
4. **Cleanup es importante**: Para cancelar operaciones pendientes
5. **Los estados con listas necesitan nuevos arrays**: Usa `[...array]` o `array.filter(...)` etc.

---

## Tu Ejercicio 🎯

Crea un `MiEjercicio.jsx` que:

1. ✅ Tenga un estado `productos` con 3 productos iniciales (id, nombre, precio)
2. ✅ Tenga un estado `cantidad` que empiece en 0
3. ✅ Cuando selecciones un producto (con botones), aumenta la cantidad
4. ✅ Usa `useEffect` para mostrar en consola: "Producto: Laptop, Cantidad: 2"
5. ✅ Muestra en pantalla qué producto está seleccionado y la cantidad

**Estructura básica**:
```javascript
const [productos, setProductos] = useState([
  { id: 1, nombre: 'Laptop', precio: 500 },
  { id: 2, nombre: 'Mouse', precio: 20 },
  { id: 3, nombre: 'Teclado', precio: 80 }
]);

const [productoSeleccionado, setProductoSeleccionado] = useState(null);
const [cantidad, setCantidad] = useState(0);

// ❓ TODO: Usa useEffect para hacer algo cuando cantidad cambia
```

**Pista**: 
- Cuando cambies de producto, reinicia la cantidad a 0
- El `useEffect` debería mostrar información en consola
- ¿Cuál es la dependencia?

---

## Próximos Pasos

Una vez entiendas cómo combinar hooks:

✅ useState maneja múltiples estados  
✅ useEffect responde a múltiples cambios  
✅ Puedes crear interacciones complejas  

Estarás listo para:
- **Step 4**: Crear formularios controlados
- **Step 5**: Validación de inputs

---

**💡 Consejo**: Dibuja un diagrama. Escribe cada `useState` como una caja y cada `useEffect` como una flecha que observa esa caja. Cuando la caja cambia, la flecha se ejecuta.
