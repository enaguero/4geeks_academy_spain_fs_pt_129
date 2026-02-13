# 🏪 Step 8: useReducer + Context = Store Global

## 🎯 Objetivo

Combinar **useReducer** y **Context API** para crear un "store" global que cualquier componente pueda usar. Este es el patrón más común en React profesional (similar a Redux pero más simple).

---

## 🤔 ¿Por Qué Combinarlos?

### useReducer solo
- ✅ Maneja estado complejo con acciones
- ❌ Solo disponible en un componente y sus hijos (via props)

### Context solo
- ✅ Comparte valores globalmente
- ❌ No tiene patrón claro para actualizar estado complejo

### useReducer + Context = 💪
- ✅ Estado complejo centralizado (reducer)
- ✅ Accesible desde cualquier componente (context)
- ✅ Dispatch global (cualquier componente puede despachar acciones)

---

## 💡 Ejemplo Completo: Carrito de Compras Global

### 1. Definir Actions y Reducer

```jsx
// cartReducer.js

// Action Types
export const CART_ACTIONS = {
  ADD_ITEM: 'ADD_ITEM',
  REMOVE_ITEM: 'REMOVE_ITEM',
  UPDATE_QUANTITY: 'UPDATE_QUANTITY',
  CLEAR_CART: 'CLEAR_CART'
};

// Initial State
export const initialCartState = {
  items: [],
  total: 0
};

// Reducer
export function cartReducer(state, action) {
  switch (action.type) {
    case CART_ACTIONS.ADD_ITEM: {
      const existingItem = state.items.find(item => item.id === action.payload.id);
      
      if (existingItem) {
        // Si ya existe, incrementa cantidad
        return {
          ...state,
          items: state.items.map(item =>
            item.id === action.payload.id
              ? { ...item, quantity: item.quantity + 1 }
              : item
          )
        };
      } else {
        // Si no existe, agrégalo
        return {
          ...state,
          items: [...state.items, { ...action.payload, quantity: 1 }]
        };
      }
    }

    case CART_ACTIONS.REMOVE_ITEM:
      return {
        ...state,
        items: state.items.filter(item => item.id !== action.payload)
      };

    case CART_ACTIONS.UPDATE_QUANTITY:
      return {
        ...state,
        items: state.items.map(item =>
          item.id === action.payload.id
            ? { ...item, quantity: action.payload.quantity }
            : item
        )
      };

    case CART_ACTIONS.CLEAR_CART:
      return initialCartState;

    default:
      return state;
  }
}
```

### 2. Crear el Context con Provider

```jsx
// CartContext.js
import { createContext, useReducer, useContext } from 'react';
import { cartReducer, initialCartState, CART_ACTIONS } from './cartReducer';

// Crear el Context
const CartContext = createContext();

// Provider Component
export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, initialCartState);

  // Calcular total
  const total = state.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  // Funciones helper (opcional pero recomendado)
  const addItem = (product) => {
    dispatch({ type: CART_ACTIONS.ADD_ITEM, payload: product });
  };

  const removeItem = (productId) => {
    dispatch({ type: CART_ACTIONS.REMOVE_ITEM, payload: productId });
  };

  const updateQuantity = (productId, quantity) => {
    dispatch({ 
      type: CART_ACTIONS.UPDATE_QUANTITY,
      payload: { id: productId, quantity }
    });
  };

  const clearCart = () => {
    dispatch({ type: CART_ACTIONS.CLEAR_CART });
  };

  // Value que se compartirá
  const value = {
    // Estado
    items: state.items,
    total,
    itemCount: state.items.length,
    // Acciones
    addItem,
    removeItem,
    updateQuantity,
    clearCart,
    // Dispatch directo (por si necesitas acciones personalizadas)
    dispatch
  };

  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}

// Custom Hook
export function useCart() {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart debe usarse dentro de CartProvider');
  }
  return context;
}
```

### 3. Envolver la App con el Provider

```jsx
// App.js
import { CartProvider } from './CartContext';
import ProductList from './ProductList';
import Cart from './Cart';
import Navbar from './Navbar';

function App() {
  return (
    <CartProvider>
      <Navbar />
      <ProductList />
      <Cart />
    </CartProvider>
  );
}

export default App;
```

### 4. Usar el Store en Componentes

```jsx
// Navbar.js
import { useCart } from './CartContext';

function Navbar() {
  const { itemCount, total } = useCart();

  return (
    <nav>
      <h1>Mi Tienda</h1>
      <div>
        🛒 {itemCount} items - ${total.toFixed(2)}
      </div>
    </nav>
  );
}

export default Navbar;
```

```jsx
// ProductList.js
import { useCart } from './CartContext';

const products = [
  { id: 1, name: 'Laptop', price: 999 },
  { id: 2, name: 'Mouse', price: 29 },
  { id: 3, name: 'Teclado', price: 79 }
];

function ProductList() {
  const { addItem } = useCart();

  return (
    <div>
      <h2>Productos</h2>
      {products.map(product => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>${product.price}</p>
          <button onClick={() => addItem(product)}>
            Agregar al Carrito
          </button>
        </div>
      ))}
    </div>
  );
}

export default ProductList;
```

```jsx
// Cart.js
import { useCart } from './CartContext';

function Cart() {
  const { items, total, removeItem, updateQuantity, clearCart } = useCart();

  if (items.length === 0) {
    return <div>El carrito está vacío</div>;
  }

  return (
    <div>
      <h2>Carrito de Compras</h2>
      {items.map(item => (
        <div key={item.id}>
          <h3>{item.name}</h3>
          <p>${item.price} x {item.quantity}</p>
          <input
            type="number"
            value={item.quantity}
            onChange={(e) => updateQuantity(item.id, Number(e.target.value))}
            min="1"
          />
          <button onClick={() => removeItem(item.id)}>Eliminar</button>
        </div>
      ))}
      <h3>Total: ${total.toFixed(2)}</h3>
      <button onClick={clearCart}>Vaciar Carrito</button>
    </div>
  );
}

export default Cart;
```

---

## 🎯 Ventajas del Patrón

### ✅ Centralización Total
- Estado en un solo lugar
- Lógica en el reducer
- Acceso desde cualquier componente

### ✅ Predecible
- Todas las actualizaciones pasan por el reducer
- Es fácil debuggear (sabes qué acción causó qué cambio)

### ✅ Testeable
- Puedes testear el reducer independientemente
- No necesitas renderizar componentes para testear lógica

### ✅ Escalable
- Agregar nuevas acciones es fácil
- Agregar nuevos componentes que usen el store es trivial

---

## 🔧 Patrón Avanzado: Múltiples Stores

Puedes tener múltiples stores para diferentes dominios:

```jsx
// App.js
import { CartProvider } from './CartContext';
import { UserProvider } from './UserContext';
import { ThemeProvider } from './ThemeContext';

function App() {
  return (
    <ThemeProvider>
      <UserProvider>
        <CartProvider>
          <MainApp />
        </CartProvider>
      </UserProvider>
    </ThemeProvider>
  );
}
```

---

## 💡 Persistencia con localStorage

Puedes guardar el estado en localStorage:

```jsx
export function CartProvider({ children }) {
  // Leer estado inicial de localStorage
  const [state, dispatch] = useReducer(
    cartReducer,
    initialCartState,
    (initial) => {
      const stored = localStorage.getItem('cart');
      return stored ? JSON.parse(stored) : initial;
    }
  );

  // Guardar en localStorage cuando cambie
  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(state));
  }, [state]);

  // ... resto del código
}
```

---

## ⚠️ Errores Comunes

### 1. Olvidar el Provider

```jsx
// ❌ MAL: useCart() fallará
function App() {
  return <ProductList />;
}

// ✅ BIEN
function App() {
  return (
    <CartProvider>
      <ProductList />
    </CartProvider>
  );
}
```

### 2. Mutar el estado en el reducer

```jsx
// ❌ MAL
case 'ADD_ITEM':
  state.items.push(action.payload);
  return state;

// ✅ BIEN
case 'ADD_ITEM':
  return {
    ...state,
    items: [...state.items, action.payload]
  };
```

### 3. No usar funciones helper

```jsx
// ❌ Funciona pero es tedioso
dispatch({ type: 'ADD_ITEM', payload: product });

// ✅ Mejor
addItem(product);
```

---

## 📝 Ejercicio Práctico

Crea un **TodoContext** combinando useReducer + Context:

### Requisitos:
- Estado: `{ todos: [], filter: 'all' }`
- Acciones: ADD_TODO, TOGGLE_TODO, DELETE_TODO, SET_FILTER
- Functions: addTodo, toggleTodo, deleteTodo, setFilter
- Custom hook: useTodos()
- Componentes: TodoList, TodoForm, TodoFilters (todos usan el store)

---

## 🔗 Recursos

### Documentación Oficial
- [useReducer + Context - React Docs](https://react.dev/learn/scaling-up-with-reducer-and-context)

### 4Geeks Academy
- [Global state with the Context API](https://4geeks.com/lesson/context-api)
- [What is useReducer](https://4geeks.com/lesson/what-is-usereducer-react)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ useReducer + Context = Store global
- ✅ El reducer maneja la lógica de actualización
- ✅ El Context comparte estado y dispatch globalmente
- ✅ Funciones helper hacen el código más limpio
- ✅ Este patrón es similar a Redux pero más simple
- ✅ Ideal para estado complejo que muchos componentes necesitan

### Siguiente Paso

En el **Step 9** integrarás este store global con **React Router** para crear aplicaciones completas con navegación Y estado compartido.

---

**¡Practica creando tu propio store global! 🚀**
