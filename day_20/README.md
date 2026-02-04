# 🧭 Día 20: React Router - Navegación en Aplicaciones React

## 🎯 Objetivos de Aprendizaje

Hoy aprenderás a crear **aplicaciones de múltiples páginas** en React usando React Router. Los conceptos clave son:

- **SPA (Single Page Application)**: Entender qué es y cómo funciona
- **React Router**: La librería estándar para navegación en React
- **Rutas**: Definir diferentes "páginas" en tu aplicación
- **Navegación**: Moverse entre páginas sin recargar el navegador
- **Parámetros dinámicos**: URLs con variables (ej: `/user/123`)
- **Navegación programática**: Redireccionar desde código JavaScript
- **Proyecto Real**: Blog o Portfolio con múltiples páginas

## 📚 Estructura del Día

Este día tiene 6 pasos progresivos, cada uno construyendo sobre el anterior:

### Step 1: ¿Qué es una SPA? 📖
**Archivo**: `step1-que-es-spa/`

Entender el concepto de Single Page Application sin escribir código todavía.

**Conceptos**:
- Web tradicional vs SPA
- Ventajas y desventajas
- Por qué React necesita un router
- Analogía del edificio de oficinas

---

### Step 2: Primera Ruta Básica 🚀
**Archivo**: `step2-primera-ruta/`

Crear tu primera aplicación con React Router - lo más simple posible.

**Conceptos**:
- Instalación de react-router-dom
- BrowserRouter (el contenedor principal)
- Configurar una ruta básica
- Tu primera "página" en React

---

### Step 3: Múltiples Rutas y Navegación 🔗
**Archivo**: `step3-multiples-rutas/`

Añadir varias páginas y navegar entre ellas.

**Conceptos**:
- Routes y Route
- Componente Link
- Crear Navbar/menú de navegación
- Páginas: Home, About, Contact

---

### Step 4: Parámetros en URLs 🔢
**Archivo**: `step4-parametros-url/`

Crear rutas dinámicas con parámetros variables.

**Conceptos**:
- Rutas con parámetros: `/user/:id`
- Hook useParams
- Páginas de detalle (producto, usuario, post)
- Query strings básicos

---

### Step 5: Navegación Programática 🎮
**Archivo**: `step5-navegacion-programatica/`

Navegar desde código JavaScript (no solo con clicks en links).

**Conceptos**:
- Hook useNavigate
- Redireccionar después de acciones
- Navegar hacia atrás/adelante
- Casos de uso: login, formularios, etc.

---

### Step 6: Proyecto Blog Completo 📝
**Archivo**: `step6-proyecto-blog/`

Aplicación completa con todas las características aprendidas.

**Conceptos**:
- Estructura profesional
- Layout compartido
- Navbar persistente
- Lista de posts + detalle de post
- Página 404
- Proyecto completo funcional

---

## 🚀 Cómo Usar Este Material

### 1. Seguir en orden ESTRICTO
Este día es **especialmente progresivo**. Cada paso es esencial para entender el siguiente.

### 2. No saltarse el Step 1
Aunque no tiene código, entender QUÉ es una SPA es crítico.

### 3. Experimentar navegando
Abre las DevTools (F12) y observa qué pasa cuando navegas (Network, Elements).

### 4. Probar rompiendo intencionalmente
- ¿Qué pasa si escribes mal una ruta?
- ¿Qué pasa si visitas `/ruta-que-no-existe`?
- ¿Cómo se ve la URL al navegar?

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

## 🎓 Proyecto Final

**Portfolio Personal o Blog**

Crearás una aplicación profesional con:

✅ Página de inicio (Home)  
✅ Sobre mí / About  
✅ Lista de proyectos o posts  
✅ Página de detalle para cada proyecto/post  
✅ Página de contacto  
✅ Navbar en todas las páginas  
✅ Página 404 para rutas inexistentes  
✅ Navegación fluida sin recarga  

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

- [ ] Step 1: ¿Qué es una SPA?
- [ ] Step 2: Primera Ruta Básica
- [ ] Step 3: Múltiples Rutas
- [ ] Step 4: Parámetros en URLs
- [ ] Step 5: Navegación Programática
- [ ] Step 6: Proyecto Blog Completo
- [ ] Proyecto Final: Portfolio Personal

---

## 🎯 ¿Por Qué Es Importante React Router?

### Sin React Router
```
Tu app: solo una "página" 
URL: siempre http://localhost:3000/
Problema: No puedes compartir link a secciones específicas
Problema: No puedes usar botones atrás/adelante del navegador
```

### Con React Router
```
Tu app: múltiples "páginas" virtuales
URLs: http://localhost:3000/about, /contact, /products/123
✅ Puedes compartir links
✅ Botones del navegador funcionan
✅ Comportamiento como sitio web tradicional
✅ Pero sin recargas (más rápido)
```

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
