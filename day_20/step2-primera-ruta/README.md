# 🚀 Step 2: Primera Ruta Básica con React Router

## 🎯 Objetivo

Crear tu **primera aplicación** con React Router de la forma más simple posible.

Al finalizar este step sabrás:
- ✅ Instalar react-router-dom
- ✅ Configurar BrowserRouter
- ✅ Crear tu primera ruta
- ✅ Entender cómo funciona `<Route>`

---

## 📦 Paso 1: Instalación

Primero necesitas instalar React Router en tu proyecto React.

### Opción A: Proyecto nuevo con Vite (recomendado)

```bash
# Crear proyecto React
npm create vite@latest mi-primera-spa -- --template react

# Entrar al proyecto
cd mi-primera-spa

# Instalar dependencias
npm install

# Instalar React Router
npm install react-router-dom

# Iniciar servidor
npm run dev
```

### Opción B: Proyecto React existente

Si ya tienes un proyecto React:

```bash
npm install react-router-dom
```

### ⚠️ Importante

Asegúrate de instalar **`react-router-dom`** (NO solo `react-router`).

```bash
# ✅ CORRECTO
npm install react-router-dom

# ❌ INCORRECTO
npm install react-router
```

---

## 🏗️ Paso 2: Estructura de Archivos

Vamos a crear una estructura simple:

```
src/
├── App.jsx          ← Aquí configuramos el router
├── main.jsx         ← Punto de entrada (NO lo tocamos)
└── pages/           ← Carpeta nueva para nuestras "páginas"
    └── Home.jsx     ← Nuestra primera página
```

---

## 📄 Paso 3: Crear la Primera Página

Crea una carpeta `pages` dentro de `src` y un archivo `Home.jsx`:

```jsx
// src/pages/Home.jsx
function Home() {
  return (
    <div>
      <h1>🏠 Bienvenido a Mi Primera SPA</h1>
      <p>Esta es la página de inicio.</p>
      <p>Si ves esto, ¡React Router funciona! 🎉</p>
    </div>
  );
}

export default Home;
```

**Explicación:**
- Es solo un componente normal de React
- NO tiene nada especial
- React Router lo mostrará cuando visitemos la URL `/`

---

## 🧭 Paso 4: Configurar React Router en App.jsx

Ahora viene la magia. Edita tu `App.jsx`:

```jsx
// src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

---

## 🔍 Entendiendo el Código Paso a Paso

### 1. Importaciones

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
```

- **`BrowserRouter`**: El contenedor principal - todo el router vive aquí
- **`Routes`**: Contenedor de todas las rutas individuales
- **`Route`**: Define UNA ruta específica

### 2. BrowserRouter

```jsx
<BrowserRouter>
  {/* Todo tu sistema de rutas va aquí */}
</BrowserRouter>
```

**Analogía:** Es el "edificio" completo del Step 1.

- Sin esto, nada funciona
- Solo usas UNO por aplicación
- Debe envolver todo

### 3. Routes

```jsx
<Routes>
  {/* Aquí van las rutas individuales */}
</Routes>
```

**Analogía:** Es el "directorio" del edificio que lista todos los pisos.

- Agrupa todas las `<Route>` individuales
- React Router busca cuál ruta coincide con la URL actual

### 4. Route

```jsx
<Route path="/" element={<Home />} />
```

**Analogía:** Es una "oficina" específica en el edificio.

- **`path="/"`**: La URL que activa esta ruta
- **`element={<Home />}`**: El componente que se muestra

---

## 🎯 ¿Cómo Funciona?

Cuando visitas `http://localhost:5173/`:

```
1. React Router ve la URL actual: "/"
   ↓
2. Busca en <Routes> una ruta con path="/"
   ↓
3. Encuentra: <Route path="/" element={<Home />} />
   ↓
4. Renderiza el componente <Home />
   ↓
5. Ves en pantalla: "🏠 Bienvenido a Mi Primera SPA"
```

---

## 🧪 Paso 5: Probar Tu Aplicación

1. **Inicia el servidor:**
   ```bash
   npm run dev
   ```

2. **Abre el navegador:**
   ```
   http://localhost:5173/
   ```

3. **Deberías ver:**
   ```
   🏠 Bienvenido a Mi Primera SPA
   Esta es la página de inicio.
   Si ves esto, ¡React Router funciona! 🎉
   ```

---

## 🎨 Mejorando un Poco

Vamos a añadir algo de estilo básico a `Home.jsx`:

```jsx
// src/pages/Home.jsx
function Home() {
  return (
    <div style={{ 
      textAlign: 'center', 
      padding: '50px',
      backgroundColor: '#f0f0f0',
      minHeight: '100vh'
    }}>
      <h1 style={{ fontSize: '3em' }}>🏠</h1>
      <h2>Bienvenido a Mi Primera SPA</h2>
      <p>Esta es la página de inicio.</p>
      <p style={{ 
        backgroundColor: '#4CAF50', 
        color: 'white', 
        padding: '10px',
        borderRadius: '5px',
        display: 'inline-block'
      }}>
        ✅ React Router funciona correctamente
      </p>
    </div>
  );
}

export default Home;
```

---

## 🔍 Inspeccionando con DevTools

Abre las DevTools (F12) y observa:

### 1. Pestaña Elements

Verás que solo hay UN `div id="root"`:

```html
<div id="root">
  <div style="text-align: center...">
    <h1>🏠</h1>
    <h2>Bienvenido a Mi Primera SPA</h2>
    ...
  </div>
</div>
```

### 2. Pestaña Network

- Recarga la página (Ctrl+R / Cmd+R)
- Verás que descarga `index.html` y archivos JS
- Ahora NO hagas nada más
- **Observa:** NO hay nuevas peticiones HTTP

Esto confirma que es una SPA - todo está cargado.

### 3. URL en la Barra del Navegador

Debería decir:
```
http://localhost:5173/
```

El `/` al final es el `path="/"` de tu ruta.

---

## 🧩 Experimentos para Entender Mejor

### Experimento 1: ¿Qué pasa si visitas una ruta que no existe?

En el navegador, escribe:
```
http://localhost:5173/no-existe
```

**Resultado:** Página en blanco.

**¿Por qué?** No hay ninguna `<Route path="/no-existe">`, entonces React Router no sabe qué mostrar.

### Experimento 2: Cambiar el path

Edita `App.jsx`:

```jsx
<Route path="/inicio" element={<Home />} />
```

Ahora visita:
- `http://localhost:5173/` → Página en blanco
- `http://localhost:5173/inicio` → ¡Funciona!

**Conclusión:** El `path` determina QUÉ URL muestra el componente.

### Experimento 3: Múltiples rutas con el mismo componente

```jsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/inicio" element={<Home />} />
  <Route path="/home" element={<Home />} />
</Routes>
```

Ahora TODAS estas URLs muestran `<Home />`:
- `/`
- `/inicio`
- `/home`

---

## ⚠️ Errores Comunes

### Error 1: Olvidar BrowserRouter

```jsx
// ❌ MALO
function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}
```

**Error en consola:**
```
useRoutes() may be used only in the context of a <Router> component.
```

**Solución:** Siempre envuelve en `<BrowserRouter>`.

### Error 2: Sintaxis vieja (React Router v5)

```jsx
// ❌ MALO (sintaxis antigua)
<Route path="/" component={Home} />

// ✅ BIEN (React Router v6)
<Route path="/" element={<Home />} />
```

### Error 3: Rutas fuera de `<Routes>`

```jsx
// ❌ MALO
<BrowserRouter>
  <Route path="/" element={<Home />} />
</BrowserRouter>

// ✅ BIEN
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
  </Routes>
</BrowserRouter>
```

---

## ✏️ Ejercicio Práctico

### Ejercicio 1: Crear una segunda página

1. Crea `src/pages/About.jsx`:

```jsx
function About() {
  return (
    <div style={{ padding: '50px', backgroundColor: '#e3f2fd' }}>
      <h1>📖 Sobre Nosotros</h1>
      <p>Esta es la página About.</p>
    </div>
  );
}

export default About;
```

2. Añádela al router en `App.jsx`:

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

3. Visita manualmente en el navegador:
   - `http://localhost:5173/` → Muestra Home
   - `http://localhost:5173/about` → Muestra About

**¡Felicidades!** Tienes dos "páginas" funcionando.

**Pero hay un problema:** ¿Cómo navegar entre ellas sin escribir la URL?

**→ Eso lo veremos en el Step 3 con `<Link>`.**

---

## 📝 Resumen

| Concepto | Qué hace |
|----------|----------|
| `BrowserRouter` | Contenedor principal del router |
| `Routes` | Agrupa todas las rutas |
| `Route` | Define una ruta individual |
| `path` | La URL que activa la ruta |
| `element` | El componente que se muestra |

### Código mínimo para React Router:

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

<BrowserRouter>
  <Routes>
    <Route path="/" element={<MiComponente />} />
  </Routes>
</BrowserRouter>
```

---

## ✅ Checklist

Antes de continuar al Step 3:

- [ ] Instalé `react-router-dom` correctamente
- [ ] Tengo `BrowserRouter` envolviendo todo
- [ ] Tengo `Routes` dentro de `BrowserRouter`
- [ ] Tengo al menos una `Route` funcionando
- [ ] Entiendo qué hace `path` y `element`
- [ ] Puedo crear nuevas páginas y añadirlas al router

---

## 🚀 Siguiente Paso

Ahora sabes crear rutas, pero **no puedes navegar** entre ellas fácilmente.

**→ En el Step 3 aprenderemos a usar `<Link>` para crear navegación con clicks.**

---

**Creado con ❤️ para 4Geeks Academy - Cohort España FS PT 129**
