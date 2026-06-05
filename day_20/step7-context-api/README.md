🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🌐 Step 7: Context API - Estado Global

## 🎯 Objetivo

Aprender a usar **Context API** para compartir estado entre componentes sin "prop drilling" (pasar props por múltiples niveles).

---

## 🤔 El Problema: Prop Drilling

Imagina que tienes esta estructura:

```
App
 ├─ Header (necesita usuario y tema)
 ├─ Main
 │   ├─ Sidebar (necesita tema)
 │   └─ Content
 │       └─ Article (necesita usuario)
 └─ Footer (necesita tema)
```

**Sin Context** (prop drilling):

```jsx
function App() {
  const [user, setUser] = useState({ name: 'Juan' });
  const [theme, setTheme] = useState('light');

  return (
    <>
      <Header user={user} theme={theme} /> {/* Pasa props */}
      <Main theme={theme} user={user}> {/* Pasa props */}
        <Sidebar theme={theme} /> {/* Pasa props */}
        <Content user={user}> {/* Pasa props */}
          <Article user={user} /> {/* Finalmente se usa */}
        </Content>
      </Main>
      <Footer theme={theme} /> {/* Pasa props */}
    </>
  );
}
```

Estás pasando `theme` y `user` por componentes que **no los necesitan**, solo para que lleguen a componentes hijos.

**❌ Problemas**:
- Muchos componentes intermedios "solo pasan" las props
- Difícil de mantener
- Si agregas un nuevo valor, debes actualizar TODOS los componentes

---

## ✅ La Solución: Context API

Context te permite "teleportar" valores desde un componente padre hasta cualquier hijo, sin pasar por los intermedios.

### Analogía: WiFi 📡

- **Sin Context (cables)**: Cada dispositivo necesita un cable conectado físicamente
- **Con Context (WiFi)**: Los dispositivos se conectan directamente a la señal WiFi, sin cables intermedios

---

## 🔧 Cómo Funciona Context API

### Tres Pasos:

1. **Crear el Context**: `createContext()`
2. **Proveer valores**: Usar el `Provider`
3. **Consumir valores**: Usar `useContext()`

---

## 💡 Ejemplo Completo: Tema Dark/Light

### 1. Crear el Context

```jsx
// ThemeContext.js
import { createContext } from 'react';

// Crear contexto con valor inicial
export const ThemeContext = createContext('light');
```

### 2. Proveer el Valor (en componente padre)

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
    // Proveemos el contexto con .Provider
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

### 3. Consumir el Valor (en cualquier hijo)

```jsx
// Header.js
import { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

function Header() {
  // Acceder al contexto con useContext
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <header>
      <h1>Mi App</h1>
      <button onClick={toggleTheme}>
        Cambiar a {theme === 'light' ? 'Dark' : 'Light'}
      </button>
      <p>Tema actual: {theme}</p>
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
      <p>Contenido con tema {theme}</p>
    </main>
  );
}

export default Content;
```

**✅ Resultado**: Tanto `Header` como `Content` acceden al tema SIN que se lo pases via props.

---

## 🎨 Patrón: Custom Context Provider

Para organizar mejor, crea un componente Provider personalizado:

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

// Custom Hook para usar el contexto
export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme debe usarse dentro de ThemeProvider');
  }
  return context;
}
```

### Uso Simplificado:

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

## 💡 Ejemplo 2: User Context

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
          <p>Hola, {user.name}</p>
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <p>No has iniciado sesión</p>
      )}
    </nav>
  );
}
```

---

## 🎯 Múltiples Providers

Puedes tener múltiples contextos:

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

## ⚠️ Cuándo NO Usar Context

### ❌ NO uses Context para:
- Estado que cambia muy frecuentemente (cada segundo)
- Estado que solo usan 1-2 componentes cercanos
- Props simples que no viajan muchos niveles

### ✅ USA Context para:
- Temas (dark/light)
- Usuario autenticado
- Idioma/localización
- Configuración global
- Estado que MUCHOS componentes necesitan

---

## ⚠️ Errores Comunes

### 1. Olvidar el Provider

```jsx
// ❌ MAL: Sin Provider
function App() {
  return <Header />; // useContext devolverá undefined
}

// ✅ BIEN: Con Provider
function App() {
  return (
    <ThemeProvider>
      <Header />
    </ThemeProvider>
  );
}
```

### 2. Usar Context fuera del Provider

```jsx
// ❌ MAL
const { theme } = useContext(ThemeContext); // Error si no está dentro del Provider
```

### 3. Re-renders innecesarios

Si el valor del Provider cambia, TODOS los consumidores se re-renderizan.

**Solución**: Separa contextos si algunos valores cambian más que otros.

---

## 📝 Ejercicio Práctico

Crea un **LanguageContext** que permita cambiar entre español e inglés.

### Requisitos:
- Estado: `language` ('es' o 'en')
- Función: `setLanguage(lang)`
- Custom hook: `useLanguage()`
- Componentes que muestren texto traducido

### Ejemplo de uso:

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

## 🔗 Recursos

### Documentación Oficial
- [Context - React Docs](https://react.dev/learn/passing-data-deeply-with-context)
- [useContext - React Docs](https://react.dev/reference/react/useContext)

### 4Geeks Academy
- [Global state with the Context API](https://4geeks.com/lesson/context-api)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ Context API evita prop drilling
- ✅ `createContext()` crea el contexto
- ✅ `<Context.Provider value={...}>` provee los valores
- ✅ `useContext(Context)` consume los valores
- ✅ Patrón Custom Provider + Custom Hook es mejor
- ✅ NO abuses de Context (solo para estado global)

### Siguiente Paso

En el **Step 8** combinarás **useReducer + Context** para crear un "store" global (patrón similar a Redux pero más simple).

---

**¡Practica creando tus propios Contexts! 🚀**
