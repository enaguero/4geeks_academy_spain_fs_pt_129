# 🔗 Step 3: Múltiples Rutas y Navegación

## 🎯 Objetivo

Crear una aplicación con **múltiples páginas** y aprender a navegar entre ellas usando `Link` sin recargar el navegador.

---

## 🤔 ¿Qué Aprenderás?

En el Step 2 creaste UNA ruta. Ahora crearás VARIAS rutas y navegarás entre ellas:
- Múltiples componentes de página (Home, About, Contact)
- Navegación con `<Link>`
- Crear un Navbar/menú de navegación
- Ruta activa (highlighting)

---

## 📁 Estructura del Proyecto

```
src/
├── App.jsx
├── main.jsx
└── pages/
    ├── Home.jsx
    ├── About.jsx
    └── Contact.jsx
```

---

## 🔧 Paso 1: Crear los Componentes de Página

### pages/Home.jsx

```jsx
function Home() {
  return (
    <div>
      <h1>🏠 Home</h1>
      <p>Bienvenido a la página principal</p>
    </div>
  );
}

export default Home;
```

### pages/About.jsx

```jsx
function About() {
  return (
    <div>
      <h1>ℹ️ About</h1>
      <p>Esta es la página sobre nosotros</p>
      <h2>Nuestra Misión</h2>
      <p>Enseñar React Router de forma incremental y práctica</p>
    </div>
  );
}

export default About;
```

### pages/Contact.jsx

```jsx
function Contact() {
  return (
    <div>
      <h1>📧 Contact</h1>
      <p>¿Tienes preguntas? Contáctanos:</p>
      <ul>
        <li>Email: hello@example.com</li>
        <li>Teléfono: 555-0123</li>
        <li>Dirección: Calle Principal 123</li>
      </ul>
    </div>
  );
}

export default Contact;
```

---

## 🔧 Paso 2: Configurar las Rutas en App.jsx

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Probando las Rutas

Ahora puedes visitar manualmente:
- `http://localhost:5173/` → Home
- `http://localhost:5173/about` → About
- `http://localhost:5173/contact` → Contact

**Problema**: ¡Tienes que escribir la URL manualmente! Necesitas un menú de navegación.

---

## 🔧 Paso 3: Crear Navbar con Links

### ⚠️ Diferencia Importante

```jsx
// ❌ MAL: Recarga toda la página
<a href="/about">About</a>

// ✅ BIEN: Navegación sin recarga (SPA)
<Link to="/about">About</Link>
```

### components/Navbar.jsx

```jsx
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ 
      padding: '1rem',
      backgroundColor: '#333',
      color: 'white'
    }}>
      <ul style={{ 
        display: 'flex',
        gap: '1rem',
        listStyle: 'none',
        margin: 0,
        padding: 0
      }}>
        <li><Link to="/" style={{ color: 'white' }}>Home</Link></li>
        <li><Link to="/about" style={{ color: 'white' }}>About</Link></li>
        <li><Link to="/contact" style={{ color: 'white' }}>Contact</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

---

## 🔧 Paso 4: Agregar Navbar a la App

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <BrowserRouter>
      {/* Navbar FUERA de Routes para que aparezca en todas las páginas */}
      <Navbar />
      
      <div style={{ padding: '2rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
```

**Importante**: El Navbar está FUERA de `<Routes>`, así aparece en todas las páginas.

---

## 🎨 Resaltar Link Activo con NavLink

`NavLink` es como `Link` pero con superpoderes: puede aplicar estilos cuando está activo.

### components/Navbar.jsx (mejorado)

```jsx
import { NavLink } from 'react-router-dom';

function Navbar() {
  // Función para determinar estilos según si está activo
  const getNavLinkStyle = ({ isActive }) => ({
    color: isActive ? 'yellow' : 'white',
    fontWeight: isActive ? 'bold' : 'normal',
    textDecoration: 'none'
  });

  return (
    <nav style={{ 
      padding: '1rem',
      backgroundColor: '#333',
      color: 'white'
    }}>
      <ul style={{ 
        display: 'flex',
        gap: '1rem',
        listStyle: 'none',
        margin: 0,
        padding: 0
      }}>
        <li>
          <NavLink to="/" style={getNavLinkStyle}>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/about" style={getNavLinkStyle}>
            About
          </NavLink>
        </li>
        <li>
          <NavLink to="/contact" style={getNavLinkStyle}>
            Contact
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

Ahora el link de la página actual se resalta en amarillo y negrita.

---

## 💡 Links Dentro de las Páginas

Puedes poner `<Link>` en cualquier parte, no solo en el Navbar:

### pages/Home.jsx (mejorado)

```jsx
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>🏠 Home</h1>
      <p>Bienvenido a la página principal</p>
      
      <div style={{ marginTop: '2rem' }}>
        <h2>Explora:</h2>
        <ul>
          <li><Link to="/about">Conoce más sobre nosotros</Link></li>
          <li><Link to="/contact">Ponte en contacto</Link></li>
        </ul>
      </div>
    </div>
  );
}

export default Home;
```

---

## 🎯 Experimento: Observa la Diferencia

### Prueba 1: Con <Link> (SPA)
1. Abre DevTools (F12) → pestaña Network
2. Haz click en "About" del navbar
3. **Observa**: ¡No se recarga la página! No hay nuevas peticiones HTTP

### Prueba 2: Con <a href> (tradicional)
1. Cambia temporalmente un `<Link>` por `<a href>`
2. Haz click
3. **Observa**: La página se recarga completamente, nuevas peticiones HTTP

Esto demuestra la **magia de React Router**: navegación instantánea sin recargas.

---

## 🎨 CSS Modular (Opcional pero Recomendado)

Crea un archivo CSS para el Navbar:

### Navbar.module.css

```css
.navbar {
  padding: 1rem;
  background-color: #333;
  color: white;
}

.navList {
  display: flex;
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navLink {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.navLink:hover {
  background-color: #555;
}

.navLinkActive {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}
```

### Navbar.jsx (usando CSS module)

```jsx
import { NavLink } from 'react-router-dom';
import styles from './Navbar.module.css';

function Navbar() {
  return (
    <nav className={styles.navbar}>
      <ul className={styles.navList}>
        <li>
          <NavLink 
            to="/" 
            className={({ isActive }) => 
              isActive ? `${styles.navLink} ${styles.navLinkActive}` : styles.navLink
            }
          >
            Home
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/about" 
            className={({ isActive }) => 
              isActive ? `${styles.navLink} ${styles.navLinkActive}` : styles.navLink
            }
          >
            About
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/contact" 
            className={({ isActive }) => 
              isActive ? `${styles.navLink} ${styles.navLinkActive}` : styles.navLink
            }
          >
            Contact
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

---

## 📝 Ejercicio Práctico

Agrega dos páginas más:

### 1. Página "Services" (`/services`)
- Lista 3-4 servicios que ofreces
- Cada servicio con título y descripción

### 2. Página "Blog" (`/blog`)
- Lista 2-3 posts de blog (título + resumen)
- Por ahora sin hacer clickeables (eso en el siguiente step)

### 3. Actualiza el Navbar
- Agrega links a las nuevas páginas
- Asegúrate que el resaltado funcione

---

## ⚠️ Errores Comunes

### 1. Usar <a> en lugar de <Link>

```jsx
// ❌ MAL: Recarga la página
<a href="/about">About</a>

// ✅ BIEN: Navegación SPA
<Link to="/about">About</Link>
```

### 2. Poner Navbar dentro de Routes

```jsx
// ❌ MAL: Navbar solo aparecerá en Home
<Routes>
  <Route path="/" element={<><Navbar /><Home /></>} />
</Routes>

// ✅ BIEN: Navbar fuera de Routes
<Navbar />
<Routes>
  <Route path="/" element={<Home />} />
</Routes>
```

### 3. Olvidar importar Link/NavLink

```jsx
// ❌ MAL: Error - Link is not defined
<Link to="/">Home</Link>

// ✅ BIEN
import { Link } from 'react-router-dom';
```

---

## 🔗 Recursos

### Documentación Oficial
- [Link - React Router](https://reactrouter.com/en/main/components/link)
- [NavLink - React Router](https://reactrouter.com/en/main/components/nav-link)

### 4Geeks Academy
- [Routing our Views with React Router](https://4geeks.com/lesson/routing-our-views-with-react-router)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ Puedes tener múltiples `<Route>` en `<Routes>`
- ✅ `<Link to="/path">` navega sin recargar
- ✅ `<NavLink>` permite resaltar el link activo
- ✅ Componentes fuera de `<Routes>` aparecen en todas las páginas
- ✅ La navegación es instantánea (no hay peticiones HTTP)

### Siguiente Paso

En el **Step 4** aprenderás a usar **parámetros dinámicos** en las URLs, como `/blog/123` o `/user/juan`.

---

**¡Practica navegando sin recargas! 🚀**
