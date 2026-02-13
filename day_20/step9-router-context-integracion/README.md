# 🔗🌐 Step 9: Router + Context Juntos

## 🎯 Objetivo

Integrar **React Router** con **Context API** + **useReducer** para crear aplicaciones completas con navegación Y estado global compartido entre páginas.

---

## 🤔 ¿Por Qué Necesitas Ambos?

### React Router
- ✅ Navegación entre páginas
- ✅ URLs dinámicas
- ✅ Parámetros en rutas

### Context + useReducer
- ✅ Estado global
- ✅ Compartir datos entre componentes
- ✅ Gestión centralizada

### Juntos = Aplicación Completa 💪
- ✅ Múltiples páginas que comparten estado
- ✅ Navegación programática basada en estado
- ✅ Datos persistentes al cambiar de página

---

## 💡 Ejemplo Completo: App con Autenticación

Vamos a crear una app con:
- Login/Logout
- Rutas protegidas (solo accesibles si estás autenticado)
- Estado de usuario compartido entre páginas

### 1. Crear Auth Context

```jsx
// AuthContext.js
import { createContext, useReducer, useContext } from 'react';

const AuthContext = createContext();

// Action Types
const AUTH_ACTIONS = {
  LOGIN: 'LOGIN',
  LOGOUT: 'LOGOUT'
};

// Reducer
function authReducer(state, action) {
  switch (action.type) {
    case AUTH_ACTIONS.LOGIN:
      return {
        user: action.payload,
        isAuthenticated: true
      };
    case AUTH_ACTIONS.LOGOUT:
      return {
        user: null,
        isAuthenticated: false
      };
    default:
      return state;
  }
}

// Initial State
const initialState = {
  user: null,
  isAuthenticated: false
};

// Provider
export function AuthProvider({ children }) {
  const [state, dispatch] = useReducer(authReducer, initialState);

  const login = (userData) => {
    dispatch({ type: AUTH_ACTIONS.LOGIN, payload: userData });
  };

  const logout = () => {
    dispatch({ type: AUTH_ACTIONS.LOGOUT });
  };

  return (
    <AuthContext.Provider value={{ ...state, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// Custom Hook
export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth debe usarse dentro de AuthProvider');
  }
  return context;
}
```

### 2. Estructura de la App con Router

```jsx
// App.js
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './AuthContext';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Profile from './pages/Profile';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          
          {/* Rutas protegidas */}
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/profile"
            element={
              <ProtectedRoute>
                <Profile />
              </ProtectedRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
```

### 3. Componente de Ruta Protegida

```jsx
// ProtectedRoute.js
import { Navigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

function ProtectedRoute({ children }) {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    // Redirigir a login si no está autenticado
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default ProtectedRoute;
```

### 4. Navbar (accede al estado global)

```jsx
// Navbar.js
import { Link } from 'react-router-dom';
import { useAuth } from '../AuthContext';

function Navbar() {
  const { user, isAuthenticated, logout } = useAuth();

  return (
    <nav>
      <Link to="/">Home</Link>
      
      {isAuthenticated ? (
        <>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/profile">Profile</Link>
          <span>Hola, {user.name}</span>
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <Link to="/login">Login</Link>
      )}
    </nav>
  );
}

export default Navbar;
```

### 5. Página de Login (con navegación programática)

```jsx
// Login.js
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Simulamos autenticación
    if (username && password) {
      login({ name: username, email: `${username}@example.com` });
      
      // Navegación programática después del login
      navigate('/dashboard');
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Iniciar Sesión</button>
      </form>
    </div>
  );
}

export default Login;
```

### 6. Páginas Protegidas (acceden al usuario)

```jsx
// Dashboard.js
import { useAuth } from '../AuthContext';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Bienvenido, {user.name}!</p>
      <p>Email: {user.email}</p>
    </div>
  );
}

export default Dashboard;
```

```jsx
// Profile.js
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';

function Profile() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/'); // Navegar a home después de logout
  };

  return (
    <div>
      <h1>Mi Perfil</h1>
      <p>Nombre: {user.name}</p>
      <p>Email: {user.email}</p>
      <button onClick={handleLogout}>Cerrar Sesión</button>
    </div>
  );
}

export default Profile;
```

---

## 🎯 Flujo de la Aplicación

1. Usuario visita `/dashboard` sin estar autenticado
2. `ProtectedRoute` detecta que `isAuthenticated = false`
3. Redirige a `/login`
4. Usuario ingresa credenciales y hace submit
5. `login()` actualiza el estado global
6. `navigate('/dashboard')` navega programáticamente
7. Ahora `isAuthenticated = true`, puede acceder
8. Navbar muestra opciones de usuario autenticado
9. Al hacer logout, redirige a home

---

## 💡 Patrón: Persistencia con localStorage

```jsx
// AuthContext.js
export function AuthProvider({ children }) {
  // Leer estado inicial de localStorage
  const [state, dispatch] = useReducer(authReducer, initialState, (initial) => {
    const stored = localStorage.getItem('auth');
    return stored ? JSON.parse(stored) : initial;
  });

  // Guardar en localStorage cuando cambie
  useEffect(() => {
    localStorage.setItem('auth', JSON.stringify(state));
  }, [state]);

  // ... resto del código
}
```

Ahora si refrescas la página, el usuario sigue autenticado.

---

## 🎯 Navegación Programática desde Context

Puedes pasar `navigate` al Context para usarlo en funciones:

```jsx
// AuthContext.js (avanzado)
export function AuthProvider({ children }) {
  const navigate = useNavigate(); // Solo funciona dentro de BrowserRouter
  const [state, dispatch] = useReducer(authReducer, initialState);

  const login = (userData) => {
    dispatch({ type: 'LOGIN', payload: userData });
    navigate('/dashboard'); // Navega automáticamente
  };

  const logout = () => {
    dispatch({ type: 'LOGOUT' });
    navigate('/'); // Navega automáticamente
  };

  // ...
}
```

---

## ⚠️ Orden Importante de Providers

```jsx
// ❌ MAL: useNavigate no funcionará en AuthProvider
function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>...</Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

// ✅ BIEN: BrowserRouter envuelve AuthProvider
function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>...</Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
```

---

## 📝 Ejercicio Práctico

Extiende la app con estas funcionalidades:

### Requisitos:
1. **Página de Registro** (`/register`)
   - Formulario para crear cuenta
   - Después de registrarse, hacer login automáticamente

2. **Página de Settings** (`/settings`) - protegida
   - Permitir cambiar nombre de usuario
   - Actualizar el estado global

3. **Página 404**
   - Para rutas que no existen
   - Link para volver a home

4. **Redirección inteligente**
   - Si intentas ir a `/login` ya autenticado, redirigir a `/dashboard`

---

## 🔗 Recursos

### Documentación Oficial
- [React Router v6](https://reactrouter.com/en/main)
- [useReducer + Context](https://react.dev/learn/scaling-up-with-reducer-and-context)

### 4Geeks Academy
- [Routing our Views with React Router](https://4geeks.com/lesson/routing-our-views-with-react-router)
- [Global state with the Context API](https://4geeks.com/lesson/context-api)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ Router + Context se complementan perfectamente
- ✅ Context comparte estado entre páginas/rutas
- ✅ useNavigate permite navegación programática desde código
- ✅ Rutas protegidas verifican estado antes de renderizar
- ✅ El Provider debe estar DENTRO de BrowserRouter
- ✅ localStorage permite persistir estado entre sesiones

### Siguiente Paso

En el **Step 10** aplicarás TODO lo aprendido en un proyecto completo: **Contact List App** con Router, Context, useReducer y CRUD completo.

---

**¡Ya tienes todas las herramientas para construir apps profesionales! 🚀**
