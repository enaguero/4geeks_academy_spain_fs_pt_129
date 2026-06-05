[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🌐 Step 7: Context API — Global State

## 🎯 Goal

Learn to use the **Context API** to share state between components without "prop drilling" (passing props through multiple levels).

---

## 🤔 The Problem: Prop Drilling

Imagine you have this structure:

```
App
 ├─ Header (needs user and theme)
 ├─ Main
 │   ├─ Sidebar (needs theme)
 │   └─ Content
 │       └─ Article (needs user)
 └─ Footer (needs theme)
```

**Without Context** (prop drilling):

```jsx
function App() {
  const [user, setUser] = useState({ name: 'Juan' });
  const [theme, setTheme] = useState('light');

  return (
    <>
      <Header user={user} theme={theme} /> {/* Passes props */}
      <Main theme={theme} user={user}> {/* Passes props */}
        <Sidebar theme={theme} /> {/* Passes props */}
        <Content user={user}> {/* Passes props */}
          <Article user={user} /> {/* Finally used */}
        </Content>
      </Main>
      <Footer theme={theme} /> {/* Passes props */}
    </>
  );
}
```

You're passing `theme` and `user` through components that **don't need them**, just so they reach child components.

**❌ Problems**:
- Many intermediate components "only pass" props through
- Hard to maintain
- If you add a new value, you must update ALL components

---

## ✅ The Solution: Context API

Context lets you "teleport" values from a parent component to any child, without going through intermediaries.

### Analogy: WiFi 📡

- **Without Context (cables)**: Each device needs a physically connected cable
- **With Context (WiFi)**: Devices connect directly to the WiFi signal, with no cables in between

---

## 🔧 How the Context API Works

### Three Steps:

1. **Create the Context**: `createContext()`
2. **Provide values**: Use the `Provider`
3. **Consume values**: Use `useContext()`

---

## 💡 Complete Example: Dark/Light Theme

### 1. Create the Context

```jsx
// ThemeContext.js
import { createContext } from 'react';

// Create context with an initial value
export const ThemeContext = createContext('light');
```

### 2. Provide the Value (in a parent component)

```jsx
// App.js
import { useState } from 'react';
import { ThemeContext } from './ThemeContext';
import Header from './Header';
import Content from './Content';

function App() {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    // We provide the context using .Provider
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div className={`app ${theme}`}>
        <Header />
        <Content />
      </div>
    </ThemeContext.Provider>
  );
}

export default App;
```

### 3. Consume the Value (in any child)

```jsx
// Header.js
import { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

function Header() {
  // Access the context with useContext
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <header>
      <h1>My App</h1>
      <button onClick={toggleTheme}>
        Switch to {theme === 'light' ? 'Dark' : 'Light'}
      </button>
      <p>Current theme: {theme}</p>
    </header>
  );
}

export default Header;
```

```jsx
// Content.js
import { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

function Content() {
  const { theme } = useContext(ThemeContext);

  return (
    <main className={theme}>
      <p>Content with {theme} theme</p>
    </main>
  );
}

export default Content;
```

**✅ Result**: Both `Header` and `Content` access the theme WITHOUT receiving it via props.

---

## 🎨 Pattern: Custom Context Provider

For better organization, create a custom Provider component:

```jsx
// ThemeContext.js
import { createContext, useState, useContext } from 'react';

const ThemeContext = createContext();

// Custom Provider Component
export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
  };

  const value = {
    theme,
    toggleTheme
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

// Custom hook to use the context
export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used inside ThemeProvider');
  }
  return context;
}
```

### Simplified Usage:

```jsx
// App.js
import { ThemeProvider } from './ThemeContext';
import Header from './Header';
import Content from './Content';

function App() {
  return (
    <ThemeProvider>
      <Header />
      <Content />
    </ThemeProvider>
  );
}

export default App;
```

```jsx
// Header.js
import { useTheme } from './ThemeContext';

function Header() {
  const { theme, toggleTheme } = useTheme();

  return (
    <header>
      <button onClick={toggleTheme}>Toggle Theme</button>
      <p>Current: {theme}</p>
    </header>
  );
}

export default Header;
```

---

## 💡 Example 2: User Context

```jsx
// UserContext.js
import { createContext, useState, useContext } from 'react';

const UserContext = createContext();

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (userData) => {
    setUser(userData);
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <UserContext.Provider value={{ user, login, logout }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  return useContext(UserContext);
}
```

```jsx
// Navbar.js
import { useUser } from './UserContext';

function Navbar() {
  const { user, logout } = useUser();

  return (
    <nav>
      {user ? (
        <>
          <p>Hi, {user.name}</p>
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <p>You're not signed in</p>
      )}
    </nav>
  );
}
```

---

## 🎯 Multiple Providers

You can have multiple contexts:

```jsx
// App.js
import { ThemeProvider } from './ThemeContext';
import { UserProvider } from './UserContext';
import { LanguageProvider } from './LanguageContext';

function App() {
  return (
    <ThemeProvider>
      <UserProvider>
        <LanguageProvider>
          <MainApp />
        </LanguageProvider>
      </UserProvider>
    </ThemeProvider>
  );
}
```

---

## ⚠️ When NOT to Use Context

### ❌ DON'T use Context for:
- State that changes very frequently (every second)
- State only used by 1-2 nearby components
- Simple props that don't travel through many levels

### ✅ DO use Context for:
- Themes (dark/light)
- Authenticated user
- Language/localization
- Global configuration
- State that MANY components need

---

## ⚠️ Common Mistakes

### 1. Forgetting the Provider

```jsx
// ❌ BAD: No Provider
function App() {
  return <Header />; // useContext will return undefined
}

// ✅ GOOD: With Provider
function App() {
  return (
    <ThemeProvider>
      <Header />
    </ThemeProvider>
  );
}
```

### 2. Using Context outside the Provider

```jsx
// ❌ BAD
const { theme } = useContext(ThemeContext); // Error if not inside the Provider
```

### 3. Unnecessary re-renders

If the Provider's value changes, ALL consumers re-render.

**Fix**: Split contexts when some values change more often than others.

---

## 📝 Practice Exercise

Create a **LanguageContext** that lets you switch between Spanish and English.

### Requirements:
- State: `language` ('es' or 'en')
- Function: `setLanguage(lang)`
- Custom hook: `useLanguage()`
- Components that display translated text

### Usage example:

```jsx
const { language, setLanguage } = useLanguage();

const translations = {
  es: { welcome: 'Bienvenido', goodbye: 'Adiós' },
  en: { welcome: 'Welcome', goodbye: 'Goodbye' }
};

return (
  <div>
    <h1>{translations[language].welcome}</h1>
    <button onClick={() => setLanguage('es')}>Español</button>
    <button onClick={() => setLanguage('en')}>English</button>
  </div>
);
```

---

## 🔗 Resources

### Official Documentation
- [Context - React Docs](https://react.dev/learn/passing-data-deeply-with-context)
- [useContext - React Docs](https://react.dev/reference/react/useContext)

### 4Geeks Academy
- [Global state with the Context API](https://4geeks.com/lesson/context-api)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ The Context API prevents prop drilling
- ✅ `createContext()` creates the context
- ✅ `<Context.Provider value={...}>` provides the values
- ✅ `useContext(Context)` consumes the values
- ✅ The Custom Provider + Custom Hook pattern is better
- ✅ Don't overuse Context (only for global state)

### Next Step

In **Step 8** you'll combine **useReducer + Context** to create a global "store" (a pattern similar to Redux but simpler).

---

**Practice creating your own Contexts! 🚀**
