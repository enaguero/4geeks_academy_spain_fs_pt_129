[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🔗🌐 Step 9: Router + Context Together

## 🎯 Goal

Integrate **React Router** with **Context API** + **useReducer** to build complete applications with navigation AND global state shared across pages.

---

## 🤔 Why Do You Need Both?

### React Router
- ✅ Navigation between pages
- ✅ Dynamic URLs
- ✅ Route parameters

### Context + useReducer
- ✅ Global state
- ✅ Share data between components
- ✅ Centralized management

### Together = Complete Application 💪
- ✅ Multiple pages that share state
- ✅ Programmatic navigation based on state
- ✅ Data that persists when changing pages

---

## 💡 Complete Example: App with Authentication

Let's build an app with:
- Login/Logout
- Protected routes (only accessible when authenticated)
- User state shared across pages

### 1. Create the Auth Context

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
    throw new Error('useAuth must be used inside AuthProvider');
  }
  return context;
}
```

### 2. App Structure with Router

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
          
          {/* Protected routes */}
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

### 3. Protected Route Component

```jsx
// ProtectedRoute.js
import { Navigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

function ProtectedRoute({ children }) {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    // Redirect to login if not authenticated
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default ProtectedRoute;
```

### 4. Navbar (reads global state)

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
          <span>Hi, {user.name}</span>
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

### 5. Login Page (with programmatic navigation)

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
    
    // We simulate authentication
    if (username && password) {
      login({ name: username, email: `${username}@example.com` });
      
      // Programmatic navigation after login
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
        <button type="submit">Sign In</button>
      </form>
    </div>
  );
}

export default Login;
```

### 6. Protected Pages (read the user)

```jsx
// Dashboard.js
import { useAuth } from '../AuthContext';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {user.name}!</p>
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
    navigate('/'); // Navigate to home after logout
  };

  return (
    <div>
      <h1>My Profile</h1>
      <p>Name: {user.name}</p>
      <p>Email: {user.email}</p>
      <button onClick={handleLogout}>Sign Out</button>
    </div>
  );
}

export default Profile;
```

---

## 🎯 Application Flow

1. User visits `/dashboard` without being authenticated
2. `ProtectedRoute` detects `isAuthenticated = false`
3. Redirects to `/login`
4. User enters credentials and submits
5. `login()` updates the global state
6. `navigate('/dashboard')` programmatically navigates
7. Now `isAuthenticated = true`, they can access it
8. The Navbar shows authenticated-user options
9. On logout, redirects to home

---

## 💡 Pattern: Persistence with localStorage

```jsx
// AuthContext.js
export function AuthProvider({ children }) {
  // Read initial state from localStorage
  const [state, dispatch] = useReducer(authReducer, initialState, (initial) => {
    const stored = localStorage.getItem('auth');
    return stored ? JSON.parse(stored) : initial;
  });

  // Save to localStorage whenever it changes
  useEffect(() => {
    localStorage.setItem('auth', JSON.stringify(state));
  }, [state]);

  // ... rest of the code
}
```

Now, if you refresh the page, the user stays authenticated.

---

## 🎯 Programmatic Navigation from Context

You can pass `navigate` to the Context to use it inside functions:

```jsx
// AuthContext.js (advanced)
export function AuthProvider({ children }) {
  const navigate = useNavigate(); // Only works inside BrowserRouter
  const [state, dispatch] = useReducer(authReducer, initialState);

  const login = (userData) => {
    dispatch({ type: 'LOGIN', payload: userData });
    navigate('/dashboard'); // Navigates automatically
  };

  const logout = () => {
    dispatch({ type: 'LOGOUT' });
    navigate('/'); // Navigates automatically
  };

  // ...
}
```

---

## ⚠️ Provider Order Matters

```jsx
// ❌ BAD: useNavigate won't work in AuthProvider
function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>...</Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

// ✅ GOOD: BrowserRouter wraps AuthProvider
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

## 📝 Practice Exercise

Extend the app with these features:

### Requirements:
1. **Register page** (`/register`)
   - Form to create an account
   - After registering, log in automatically

2. **Settings page** (`/settings`) — protected
   - Allow changing the username
   - Update the global state

3. **404 page**
   - For routes that don't exist
   - Link back to home

4. **Smart redirect**
   - If you try to visit `/login` while already authenticated, redirect to `/dashboard`

---

## 🔗 Resources

### Official Documentation
- [React Router v6](https://reactrouter.com/en/main)
- [useReducer + Context](https://react.dev/learn/scaling-up-with-reducer-and-context)

### 4Geeks Academy
- [Routing our Views with React Router](https://4geeks.com/lesson/routing-our-views-with-react-router)
- [Global state with the Context API](https://4geeks.com/lesson/context-api)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ Router + Context complement each other perfectly
- ✅ Context shares state between pages/routes
- ✅ useNavigate enables programmatic navigation from code
- ✅ Protected routes check state before rendering
- ✅ The Provider must be INSIDE BrowserRouter
- ✅ localStorage lets you persist state between sessions

### Next Step

In **Step 10** you'll apply EVERYTHING you've learned in a full project: a **Contact List App** with Router, Context, useReducer, and complete CRUD.

---

**You now have all the tools to build professional apps! 🚀**
