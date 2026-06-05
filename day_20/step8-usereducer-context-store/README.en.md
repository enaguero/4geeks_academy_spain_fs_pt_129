[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🏪 Step 8: useReducer + Context = Global Store

## 🎯 Goal

Combine **useReducer** and **Context API** to create a global "store" that any component can use. This is the most common pattern in professional React (similar to Redux but simpler).

---

## 🤔 Why Combine Them?

### useReducer alone
- ✅ Handles complex state with actions
- ❌ Only available in one component and its children (via props)

### Context alone
- ✅ Shares values globally
- ❌ Has no clear pattern for updating complex state

### useReducer + Context = 💪
- ✅ Centralized complex state (reducer)
- ✅ Accessible from any component (context)
- ✅ Global dispatch (any component can dispatch actions)

---

## 💡 Complete Example: Global Shopping Cart

### 1. Define Actions and Reducer

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
        // If it already exists, increment quantity
        return {
          ...state,
          items: state.items.map(item =>
            item.id === action.payload.id
              ? { ...item, quantity: item.quantity + 1 }
              : item
          )
        };
      } else {
        // If it doesn't exist, add it
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

### 2. Create the Context with Provider

```jsx
// CartContext.js
import { createContext, useReducer, useContext } from 'react';
import { cartReducer, initialCartState, CART_ACTIONS } from './cartReducer';

// Create the Context
const CartContext = createContext();

// Provider Component
export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, initialCartState);

  // Compute total
  const total = state.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  // Helper functions (optional but recommended)
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

  // Value that will be shared
  const value = {
    // State
    items: state.items,
    total,
    itemCount: state.items.length,
    // Actions
    addItem,
    removeItem,
    updateQuantity,
    clearCart,
    // Direct dispatch (in case you need custom actions)
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
    throw new Error('useCart must be used inside CartProvider');
  }
  return context;
}
```

### 3. Wrap the App with the Provider

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

### 4. Use the Store in Components

```jsx
// Navbar.js
import { useCart } from './CartContext';

function Navbar() {
  const { itemCount, total } = useCart();

  return (
    <nav>
      <h1>My Store</h1>
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
  { id: 3, name: 'Keyboard', price: 79 }
];

function ProductList() {
  const { addItem } = useCart();

  return (
    <div>
      <h2>Products</h2>
      {products.map(product => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>${product.price}</p>
          <button onClick={() => addItem(product)}>
            Add to Cart
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
    return <div>The cart is empty</div>;
  }

  return (
    <div>
      <h2>Shopping Cart</h2>
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
          <button onClick={() => removeItem(item.id)}>Remove</button>
        </div>
      ))}
      <h3>Total: ${total.toFixed(2)}</h3>
      <button onClick={clearCart}>Empty Cart</button>
    </div>
  );
}

export default Cart;
```

---

## 🎯 Pattern Advantages

### ✅ Total Centralization
- State in one place
- Logic in the reducer
- Access from any component

### ✅ Predictable
- All updates flow through the reducer
- Easy to debug (you know which action caused which change)

### ✅ Testable
- You can test the reducer in isolation
- You don't need to render components to test the logic

### ✅ Scalable
- Adding new actions is easy
- Adding new components that use the store is trivial

---

## 🔧 Advanced Pattern: Multiple Stores

You can have multiple stores for different domains:

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

## 💡 Persistence with localStorage

You can save state to localStorage:

```jsx
export function CartProvider({ children }) {
  // Read initial state from localStorage
  const [state, dispatch] = useReducer(
    cartReducer,
    initialCartState,
    (initial) => {
      const stored = localStorage.getItem('cart');
      return stored ? JSON.parse(stored) : initial;
    }
  );

  // Save to localStorage whenever it changes
  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(state));
  }, [state]);

  // ... rest of the code
}
```

---

## ⚠️ Common Mistakes

### 1. Forgetting the Provider

```jsx
// ❌ BAD: useCart() will fail
function App() {
  return <ProductList />;
}

// ✅ GOOD
function App() {
  return (
    <CartProvider>
      <ProductList />
    </CartProvider>
  );
}
```

### 2. Mutating state in the reducer

```jsx
// ❌ BAD
case 'ADD_ITEM':
  state.items.push(action.payload);
  return state;

// ✅ GOOD
case 'ADD_ITEM':
  return {
    ...state,
    items: [...state.items, action.payload]
  };
```

### 3. Not using helper functions

```jsx
// ❌ Works but tedious
dispatch({ type: 'ADD_ITEM', payload: product });

// ✅ Better
addItem(product);
```

---

## 📝 Practice Exercise

Create a **TodoContext** combining useReducer + Context:

### Requirements:
- State: `{ todos: [], filter: 'all' }`
- Actions: ADD_TODO, TOGGLE_TODO, DELETE_TODO, SET_FILTER
- Functions: addTodo, toggleTodo, deleteTodo, setFilter
- Custom hook: useTodos()
- Components: TodoList, TodoForm, TodoFilters (all use the store)

---

## 🔗 Resources

### Official Documentation
- [useReducer + Context - React Docs](https://react.dev/learn/scaling-up-with-reducer-and-context)

### 4Geeks Academy
- [Global state with the Context API](https://4geeks.com/lesson/context-api)
- [What is useReducer](https://4geeks.com/lesson/what-is-usereducer-react)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ useReducer + Context = Global store
- ✅ The reducer handles the update logic
- ✅ Context shares state and dispatch globally
- ✅ Helper functions keep the code cleaner
- ✅ This pattern is similar to Redux but simpler
- ✅ Ideal for complex state that many components need

### Next Step

In **Step 9** you'll integrate this global store with **React Router** to build complete applications with both navigation AND shared state.

---

**Practice by building your own global store! 🚀**
