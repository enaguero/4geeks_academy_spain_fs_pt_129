[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧠 Step 5: Introduction to useReducer

## 🎯 Goal

Understand **what useReducer is**, when to use it instead of `useState`, and how the **actions** and **reducers** pattern works.

---

## 📖 What is useReducer?

`useReducer` is a React Hook that lets you manage complex state in a more **predictable and organized** way.

### Restaurant Analogy 🍽️

Imagine you're at a restaurant:

**With useState** (the server does everything):
- You tell the server: "I want this cooked, no salt, extra cheese"
- The server has to remember EVERYTHING and execute it
- If there are many requests, it gets complicated

**With useReducer** (the server hands your order to the kitchen):
- You: "Order #5 with modification A"
- The server just carries the message
- The kitchen has a **system** (reducer) that knows what to do with each order
- More organized and predictable

---

## 🆚 useState vs useReducer

### Use `useState` when:
- ✅ State is simple (a string, a number, a boolean)
- ✅ There are only 1-2 ways to update state
- ✅ The update logic is trivial

**Example**:
```jsx
const [count, setCount] = useState(0);
const [isOpen, setIsOpen] = useState(false);
const [name, setName] = useState('');
```

### Use `useReducer` when:
- ✅ State is complex (objects with multiple properties)
- ✅ There are MANY ways to update state
- ✅ The next update depends on the previous state
- ✅ You want to centralize the update logic

**Example**: Todo list, shopping cart, complex form, game

---

## 🔧 Basic Syntax

```jsx
import { useReducer } from 'react';

// 1. Define the reducer (the "kitchen")
function reducer(state, action) {
  switch (action.type) {
    case 'ACTION_TYPE':
      return { ...state, /* changes */ };
    default:
      return state;
  }
}

// 2. Use it in your component
function MyComponent() {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  // 3. Dispatch actions
  dispatch({ type: 'ACTION_TYPE', payload: data });
}
```

### Key Concepts

1. **`reducer`**: Function that receives `(state, action)` and returns the new state
2. **`state`**: The current state (just like with useState)
3. **`dispatch`**: Function to send actions (replaces `setState`)
4. **`action`**: Object that describes WHAT happened (must have `type`)
5. **`payload`**: Additional data in the action (optional)

---

## 💡 Example 1: Simple Counter

Let's compare the same counter using both approaches:

### With useState
```jsx
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(count - 1)}>-1</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

### With useReducer
```jsx
// Reducer function
function counterReducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    case 'RESET':
      return { count: 0 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+1</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-1</button>
      <button onClick={() => dispatch({ type: 'RESET' })}>Reset</button>
    </div>
  );
}
```

**Which is better here?** For a simple counter, **useState is better** (simpler).

But notice how useReducer centralizes ALL the logic in a single place (the reducer).

---

## 💡 Example 2: Counter with More Actions

Now let's add more functionality:

```jsx
function counterReducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    case 'INCREMENT_BY':
      // Notice the use of payload for extra data
      return { count: state.count + action.payload };
    case 'DECREMENT_BY':
      return { count: state.count - action.payload };
    case 'MULTIPLY':
      return { count: state.count * action.payload };
    case 'RESET':
      return { count: 0 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+1</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-1</button>
      <button onClick={() => dispatch({ type: 'INCREMENT_BY', payload: 5 })}>+5</button>
      <button onClick={() => dispatch({ type: 'DECREMENT_BY', payload: 10 })}>-10</button>
      <button onClick={() => dispatch({ type: 'MULTIPLY', payload: 2 })}>x2</button>
      <button onClick={() => dispatch({ type: 'RESET' })}>Reset</button>
    </div>
  );
}
```

Now it starts to make more sense: all the logic is centralized and easier to read.

---

## 🎨 Action Pattern

### Convention: Actions as Objects

```javascript
// ✅ GOOD: Action with type
{ type: 'INCREMENT' }

// ✅ GOOD: Action with type and payload
{ type: 'ADD_TODO', payload: 'Buy milk' }

// ✅ GOOD: Payload can be anything
{ type: 'UPDATE_USER', payload: { name: 'Juan', age: 25 } }

// ❌ BAD: No type
{ value: 5 }
```

### Convention: TYPES in UPPERCASE

```javascript
// ✅ GOOD
case 'ADD_TODO':
case 'DELETE_TODO':
case 'TOGGLE_TODO':

// ❌ BAD (works, but not conventional)
case 'addTodo':
case 'deleteTodo':
```

### Tip: Constants for Types

To avoid typos:

```javascript
// Define constants
const ACTIONS = {
  INCREMENT: 'INCREMENT',
  DECREMENT: 'DECREMENT',
  RESET: 'RESET'
};

// Use in reducer
function counterReducer(state, action) {
  switch (action.type) {
    case ACTIONS.INCREMENT:
      return { count: state.count + 1 };
    case ACTIONS.DECREMENT:
      return { count: state.count - 1 };
    case ACTIONS.RESET:
      return { count: 0 };
    default:
      return state;
  }
}

// Use when dispatching
dispatch({ type: ACTIONS.INCREMENT });
```

---

## ⚠️ Important Reducer Rules

### 1. It must be a PURE function
- ✅ Returns new state based on inputs
- ❌ Don't mutate the state directly
- ❌ Don't make async calls (fetch, setTimeout)
- ❌ Don't generate random values

```javascript
// ❌ BAD: Mutates state directly
function badReducer(state, action) {
  state.count++; // NO!
  return state;
}

// ✅ GOOD: Returns a new object
function goodReducer(state, action) {
  return { ...state, count: state.count + 1 };
}
```

### 2. Always return a state

```javascript
// ✅ GOOD: There's always a return
function reducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    default:
      return state; // Important
  }
}

// ❌ BAD: Forgot the default
function badReducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    // What if action.type is not 'INCREMENT'? undefined!
  }
}
```

### 3. Use the spread operator for immutability

```javascript
// ✅ GOOD
return { ...state, count: state.count + 1 };

// ❌ BAD
state.count = state.count + 1;
return state;
```

---

## 🤔 When to Use Each?

### Use `useState` for:
- ✅ Simple state
- ✅ Small components
- ✅ Few updates

### Use `useReducer` for:
- ✅ Complex state (objects/arrays)
- ✅ Many ways to update state
- ✅ Complex update logic
- ✅ When you want to test the logic easily

---

## 📝 Practice Exercise

Build a component that manages a traffic light's state:

### Requirements:
- State: `{ light: 'red' }` (can be 'red', 'yellow', 'green')
- Actions:
  - `NEXT`: Move to the next color (red → yellow → green → red)
  - `RESET`: Go back to red
  - `SET_COLOR`: Set a specific color (use payload)

### Structure:

```jsx
// 1. Define the reducer
function trafficLightReducer(state, action) {
  // Your code here
}

// 2. Create the component
function TrafficLight() {
  const [state, dispatch] = useReducer(trafficLightReducer, { light: 'red' });

  return (
    <div>
      {/* Show the traffic light */}
      {/* Buttons to change the state */}
    </div>
  );
}
```

---

## 🔗 Resources

### Official Documentation
- [useReducer - React Docs](https://react.dev/reference/react/useReducer)

### 4Geeks Academy
- [What is and How to Use The useReducer Hook](https://4geeks.com/lesson/what-is-usereducer-react)

### Videos
- [useReducer in 100 seconds](https://www.youtube.com/watch?v=kK_Wqx3RnHk)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ useReducer is for complex state
- ✅ A reducer is a pure function: `(state, action) => newState`
- ✅ dispatch sends actions: `dispatch({ type: 'ACTION' })`
- ✅ Actions describe WHAT happened, not HOW to update it
- ✅ The reducer decides HOW to update the state
- ✅ Always return a new state (immutability)

### Next Step

In **Step 6** you'll see how to use useReducer to manage REALLY complex state (a todo list with multiple actions).

---

**Practice and experiment! 🚀**

If useReducer still doesn't click, that's normal. It makes more sense once you see real use cases (next step).
