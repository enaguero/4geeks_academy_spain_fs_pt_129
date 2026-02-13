# 🧭 Día 20: React Router + Gestión de Estado Global

## 🎯 Objetivos de Aprendizaje

Hoy aprenderás a crear **aplicaciones React completas y profesionales** con navegación y gestión de estado global. Los conceptos clave son:

### Parte 1: Navegación (React Router)
- **SPA (Single Page Application)**: Entender qué es y cómo funciona
- **React Router**: La librería estándar para navegación en React
- **Rutas**: Definir diferentes "páginas" en tu aplicación
- **Parámetros dinámicos**: URLs con variables (ej: `/user/123`)

### Parte 2: Estado Complejo (useReducer)
- **useReducer Hook**: Alternativa a useState para estado complejo
- **Reducers y Actions**: Patrón predecible para manejar estado
- **Cuándo usar useReducer**: vs useState

### Parte 3: Estado Global (Context API)
- **Context API**: Compartir estado entre componentes sin prop drilling
- **Provider y Consumer**: Patrón de contexto en React
- **useContext Hook**: Acceder al contexto fácilmente

### Parte 4: Integración
- **Store Pattern**: Combinar useReducer + Context para estado global
- **Router + Context**: Integrar navegación con estado compartido
- **Proyecto Real**: Contact List App con CRUD completo

## 📚 Estructura del Día

Este día tiene **10 pasos progresivos**, cada uno construyendo sobre el anterior:

---

## 👉 PARTE 1: React Router (Steps 1-4)

### Step 1: ¿Qué es una SPA? 📖
**Carpeta**: `step1-que-es-spa/`

Entender el concepto de Single Page Application sin escribir código todavía.

**Conceptos**:
- Web tradicional vs SPA
- Ventajas y desventajas
- Por qué React necesita un router
- Analogía del edificio de oficinas

---

### Step 2: Primera Ruta Básica 🚀
**Carpeta**: `step2-primera-ruta/`

Crear tu primera aplicación con React Router - lo más simple posible.

**Conceptos**:
- Instalación de react-router-dom
- BrowserRouter (el contenedor principal)
- Configurar una ruta básica
- Tu primera "página" en React

---

### Step 3: Múltiples Rutas y Navegación 🔗
**Carpeta**: `step3-multiples-rutas/`

Añadir varias páginas y navegar entre ellas.

**Conceptos**:
- Routes y Route
- Componente Link
- Crear Navbar/menú de navegación
- Páginas: Home, About, Contact

---

### Step 4: Parámetros en URLs 🔢
**Carpeta**: `step4-parametros-url/`

Crear rutas dinámicas con parámetros variables.

**Conceptos**:
- Rutas con parámetros: `/user/:id`
- Hook useParams
- Páginas de detalle (producto, usuario, post)
- Query strings básicos

---

## 👉 PARTE 2: useState vs useReducer (Steps 5-6)

### Step 5: Introducción a useReducer 🧠
**Carpeta**: `step5-intro-usereducer/`

¿Qué es useReducer? ¿Cuándo usarlo en lugar de useState?

**Conceptos**:
- Qué es useReducer
- Diferencia con useState
- Cuándo usar cada uno
- Ejemplo: contador con useReducer
- Acciones (actions) y reducer function
- Patrón: `dispatch({ type: 'ACTION', payload: data })`

---

### Step 6: useReducer para Estado Complejo 📦
**Carpeta**: `step6-usereducer-complejo/`

Usar useReducer para manejar estado complejo con múltiples acciones.

**Conceptos**:
- Todo list con useReducer
- Múltiples tipos de acciones (ADD, DELETE, TOGGLE, EDIT)
- Switch statement en reducer
- Ventajas sobre múltiples useState
- Código más predecible y testeable

---

## 👉 PARTE 3: Context API (Step 7)

### Step 7: Context API - Estado Global 🌐
**Carpeta**: `step7-context-api/`

Resolver el problema del "prop drilling" con Context API.

**Conceptos**:
- ¿Qué es prop drilling y por qué es un problema?
- createContext
- Context.Provider
- useContext hook
- Compartir estado entre componentes lejanos
- Ejemplo: tema dark/light mode global

---

## 👉 PARTE 4: Integración (Steps 8-10)

### Step 8: useReducer + Context = Store 🏪
**Carpeta**: `step8-usereducer-context-store/`

Combinar useReducer con Context para crear un "store" global (patrón similar a Redux).

**Conceptos**:
- Combinar useReducer + Context
- Crear un store global
- Provider con dispatch disponible globalmente
- Ejemplo: carrito de compras global
- Actions centralizadas
- Estado accesible desde cualquier componente

---

### Step 9: Router + Context Juntos 🔗🌐
**Carpeta**: `step9-router-context-integracion/`

Integrar navegación (Router) con estado global (Context).

**Conceptos**:
- Compartir estado entre diferentes páginas/rutas
- useNavigate con Context
- Navegación programática desde acciones
- Ejemplo: app con autenticación simulada
- Login, logout, rutas protegidas

---

### Step 10: Proyecto Contact List App 📞
**Carpeta**: `step10-proyecto-contact-list/`

¡TU PROYECTO! Aplicación completa usando TODO lo aprendido.

**⚠️ IMPORTANTE**: Este step NO incluye código resuelto. Solo tiene:
- Descripción del proyecto
- Requisitos funcionales
- Estructura sugerida
- Referencias a documentación
- Mockup/wireframe

**Tú debes construirlo** aplicando:
- ✅ React Router (múltiples páginas)
- ✅ Context API (estado global)
- ✅ useReducer (gestión de contactos)
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Formularios
- ✅ Validaciones
- ✅ Navegación programática

---

## 🚀 Cómo Usar Este Material

### 1. Seguir en orden ESTRICTO
Este día es **MUY progresivo**. Cada paso construye sobre el anterior:
- Steps 1-4: Aprendes Router
- Steps 5-6: Aprendes useReducer
- Step 7: Aprendes Context
- Steps 8-9: Integras todo
- Step 10: Proyecto final (tú lo construyes)

### 2. No saltarse conceptos teóricos
Los steps 1, 5 y 7 son más teóricos pero **esenciales** para entender el resto.

### 3. Experimentar y romper cosas
- Abre las DevTools (F12) mientras navegas
- Modifica el código de los ejemplos
- Prueba cosas que crees que no funcionarán
- Lee los errores en la consola

### 4. No avanzar si no entiendes
Si algo no tiene sentido en un step, **para**. Revisa, pregunta, experimenta. No sigas adelante sin entenderlo.

## 🔗 Antes de Empezar: Requisitos Previos

Debes sentirte cómodo con:
- ✅ Componentes de React
- ✅ Props
- ✅ useState
- ✅ Estructura de un proyecto React

Si aún no dominas estos conceptos, **revisa los días 15-17 primero**.

## 📖 Lectura Recomendada

### De 4Geeks Academy
- [React Router Tutorial](https://4geeks.com/lesson/routing-our-views-with-react-router)
- [What is a Single Page Application](https://4geeks.com/lesson/what-is-a-single-page-application-spa)

### Documentación Oficial
- [React Router v6 - Getting Started](https://reactrouter.com/en/main/start/tutorial)
- [React Router v6 - Overview](https://reactrouter.com/en/main/start/overview)

### Videos Recomendados
- [React Router in 100 Seconds](https://www.youtube.com/watch?v=Ul3y1LXxzdU)
- [React Router v6 Tutorial](https://www.youtube.com/watch?v=59IXY5IDrBA)

## 🎯 Proyecto Final: Contact List App

Crearás una aplicación completa de gestión de contactos con:

### Funcionalidades Requeridas
✅ **Lista de contactos** - ver todos los contactos  
✅ **Añadir contacto** - formulario para crear nuevos contactos  
✅ **Ver detalle** - página individual de cada contacto  
✅ **Editar contacto** - modificar información existente  
✅ **Eliminar contacto** - con confirmación  
✅ **Navegación** - entre todas las vistas sin recarga  
✅ **Estado global** - contactos accesibles desde cualquier componente  
✅ **Validaciones** - formularios con validación  

### Tecnologías que Usarás
- 🔗 **React Router** - navegación entre vistas
- 🌐 **Context API** - compartir estado
- 🧠 **useReducer** - gestionar CRUD operations
- 📝 **Formularios** - inputs controlados
- 🎨 **CSS** - diseño profesional

El Step 10 te dará toda la información necesaria, pero **tú debes implementarlo**.

## 💡 Conceptos Clave a Entender

### Diferencia Crítica
```
Sitio web tradicional:
- Click en link → Navegador descarga HTML nuevo → Página se recarga
- Cada página = archivo HTML diferente

React Router (SPA):
- Click en link → JavaScript cambia componente → NO hay recarga
- Todas las "páginas" = componentes JavaScript en un solo HTML
```

### Componentes Principales de React Router

| Componente | Propósito | Analogía |
|------------|-----------|----------|
| `BrowserRouter` | Contenedor general | El edificio completo |
| `Routes` | Contenedor de rutas | El directorio del edificio |
| `Route` | Una ruta específica | Una oficina del edificio |
| `Link` | Enlace de navegación | Ascensor entre pisos |
| `useParams` | Leer parámetros URL | Leer número de oficina |
| `useNavigate` | Navegar programáticamente | GPS que te lleva automáticamente |

## ⚠️ Errores Comunes

### Error 1: Olvidar el BrowserRouter
```jsx
// ❌ MALO
function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}

// ✅ BIEN
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### Error 2: Usar <a> en lugar de <Link>
```jsx
// ❌ MALO - recarga la página
<a href="/about">About</a>

// ✅ BIEN - navegación sin recarga
<Link to="/about">About</Link>
```

### Error 3: No usar element={} en Route
```jsx
// ❌ MALO (sintaxis vieja de React Router v5)
<Route path="/about" component={About} />

// ✅ BIEN (React Router v6)
<Route path="/about" element={<About />} />
```

### Error 4: Rutas fuera de <Routes>
```jsx
// ❌ MALO
<BrowserRouter>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
</BrowserRouter>

// ✅ BIEN
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
  </Routes>
</BrowserRouter>
```

## 🆘 Necesitas Ayuda?

1. Lee el tutorial paso a paso (¡de verdad, léelo!)
2. Abre las DevTools (F12) para ver qué pasa
3. Verifica que instalaste `react-router-dom` correctamente
4. Asegúrate de estar usando la versión 6 de React Router
5. Pregunta en el canal de Slack

## 📊 Progreso

Marca cada paso cuando lo completes:

### Parte 1: React Router
- [ ] Step 1: ¿Qué es una SPA?
- [ ] Step 2: Primera Ruta Básica
- [ ] Step 3: Múltiples Rutas y Navegación
- [ ] Step 4: Parámetros en URLs

### Parte 2: useReducer
- [ ] Step 5: Introducción a useReducer
- [ ] Step 6: useReducer para Estado Complejo

### Parte 3: Context API
- [ ] Step 7: Context API - Estado Global

### Parte 4: Integración
- [ ] Step 8: useReducer + Context (Store)
- [ ] Step 9: Router + Context Juntos
- [ ] Step 10: Proyecto Contact List App (construirlo tú mismo)

---

## 🎯 ¿Por Qué Es Importante Este Día?

### React Router
Sin Router tu app React es una sola página. Con Router puedes crear aplicaciones con múltiples vistas, URLs compartibles y navegación profesional.

### useReducer
Para estado simple usa `useState`. Pero cuando tu estado se vuelve complejo (muchas acciones, lógica complicada), `useReducer` hace tu código más limpio y mantenible.

### Context API
Evita "prop drilling" (pasar props por 5 niveles de componentes). Context te permite compartir estado globalmente de forma elegante.

### ¿Por qué combinar useReducer + Context?
Es el patrón más común en React profesional para estado global. Similar a Redux pero más simple y sin librerías externas.

**Después de este día podrás construir aplicaciones React completas y profesionales.**

## 💼 Casos de Uso Profesionales

Aplicaciones reales que necesitan React Router:
- 🛒 E-commerce: Home, Productos, Detalle de producto, Carrito, Checkout
- 📱 Redes sociales: Feed, Perfil, Configuración, Mensajes
- 📰 Blog: Lista de posts, Detalle de post, Categorías, Autor
- 🏢 Dashboard: Overview, Estadísticas, Configuración, Usuarios
- 🎓 Plataforma educativa: Cursos, Lecciones, Perfil, Progreso

## 📝 Notas Importantes

### Versión de React Router
Este tutorial usa **React Router v6** (la versión actual y más moderna).

Si encuentras tutoriales antiguos con sintaxis diferente (v5 o v4), **ignóralos**.

### Instalación
```bash
npm install react-router-dom
```

**NO** instales `react-router` solo (es diferente).

### Navegador vs HashRouter
Usaremos `BrowserRouter` (el estándar).

`HashRouter` usa URLs con `#` y es solo para casos especiales.

---

**¡Vamos a navegar! 🚀**

React Router es una de las habilidades más importantes en desarrollo React profesional. Después de este día, tus aplicaciones se sentirán como sitios web reales con múltiples páginas.

**Tómate tu tiempo, lee todo, experimenta, y diviértete construyendo.**

---

**Creado con ❤️ para 4Geeks Academy - Cohort España FS PT 129**
