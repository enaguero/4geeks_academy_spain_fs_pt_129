# 📞 Step 10: Proyecto Contact List App

## 🎯 Objetivo

**¡TU PROYECTO!** Construir una aplicación completa de gestión de contactos aplicando **TODO** lo aprendido en los steps anteriores:

- ✅ React Router (navegación)
- ✅ Context API (estado global)
- ✅ useReducer (gestión CRUD)
- ✅ Formularios controlados
- ✅ Validaciones
- ✅ Navegación programática

---

## ⚠️ IMPORTANTE

**Este step NO incluye código resuelto.**

Solo encontrarás:
- Descripción del proyecto
- Requisitos funcionales
- Estructura sugerida
- Mockups/wireframes
- Referencias a documentación

**TÚ DEBES IMPLEMENTARLO** usando lo que aprendiste en los steps 1-9.

---

## 📋 Descripción del Proyecto

Crearás una **aplicación de gestión de contactos** donde podrás:
- Ver lista de todos los contactos
- Añadir nuevo contacto
- Ver detalle de un contacto
- Editar contacto existente
- Eliminar contacto (con confirmación)

Todos los contactos se gestionarán con **estado global** (Context + useReducer) y estarán accesibles desde cualquier página.

---

## 🎯 Funcionalidades Requeridas

### 1. Lista de Contactos (`/`)
- Mostrar todos los contactos en una lista o tarjetas
- Cada contacto muestra: nombre, teléfono, email
- Botones: "Ver detalle", "Editar", "Eliminar"
- Si no hay contactos, mostrar mensaje "No hay contactos"
- Botón "Agregar contacto" que navega a `/add`

### 2. Agregar Contacto (`/add`)
- Formulario con campos:
  - Nombre (requerido)
  - Teléfono (requerido)
  - Email (requerido, validar formato)
  - Dirección (opcional)
- Validaciones:
  - No dejar campos requeridos vacíos
  - Email válido
  - Teléfono solo números
- Al enviar:
  - Agregar contacto al estado global
  - Navegar a `/` (lista)
  - Mostrar mensaje de éxito
- Botón "Cancelar" que vuelve a `/`

### 3. Ver Detalle (`/contact/:id`)
- Mostrar toda la información del contacto
- Botones: "Editar", "Eliminar", "Volver a lista"
- Si el ID no existe, mostrar "Contacto no encontrado" y link a home

### 4. Editar Contacto (`/edit/:id`)
- Formulario pre-llenado con datos actuales
- Mismas validaciones que agregar
- Al enviar:
  - Actualizar contacto en estado global
  - Navegar a detalle del contacto
  - Mostrar mensaje de éxito
- Botón "Cancelar" que vuelve a detalle

### 5. Eliminar Contacto
- Mostrar confirmación: "¿Estás seguro?"
- Si confirma:
  - Eliminar del estado global
  - Navegar a `/` (lista)
  - Mostrar mensaje "Contacto eliminado"
- Si cancela, no hacer nada

### 6. Navbar
- Link a "Inicio" (lista de contactos)
- Contador: "X contactos"
- Link "Agregar contacto"

### 7. Página 404
- Para rutas que no existen
- Mensaje amigable
- Link para volver al inicio

---

## 🎨 Estructura Sugerida del Proyecto

```
contact-list-app/
├── src/
│   ├── context/
│   │   ├── ContactContext.js      # Context Provider + useReducer
│   │   └── contactReducer.js      # Reducer con acciones CRUD
│   ├── pages/
│   │   ├── Home.js                # Lista de contactos
│   │   ├── AddContact.js          # Formulario agregar
│   │   ├── EditContact.js         # Formulario editar
│   │   ├── ContactDetail.js       # Ver detalle
│   │   └── NotFound.js            # Página 404
│   ├── components/
│   │   ├── Navbar.js              # Navegación
│   │   ├── ContactCard.js         # Tarjeta de contacto
│   │   ├── ContactForm.js         # Formulario reutilizable
│   │   └── ConfirmModal.js        # Modal de confirmación
│   ├── App.js                     # Router y Providers
│   └── main.jsx                   # Entry point
```

---

## 🧠 Estructura del Estado Global

### Estado Inicial

```javascript
const initialState = {
  contacts: [
    {
      id: 1,
      name: 'Juan Pérez',
      phone: '555-0101',
      email: 'juan@example.com',
      address: 'Calle Principal 123'
    },
    {
      id: 2,
      name: 'María García',
      phone: '555-0102',
      email: 'maria@example.com',
      address: 'Avenida Central 456'
    }
  ]
};
```

### Acciones Necesarias

```javascript
const CONTACT_ACTIONS = {
  ADD_CONTACT: 'ADD_CONTACT',
  UPDATE_CONTACT: 'UPDATE_CONTACT',
  DELETE_CONTACT: 'DELETE_CONTACT'
};
```

### Funciones Helper Sugeridas

```javascript
// En ContactContext.js
const addContact = (contactData) => { ... };
const updateContact = (id, contactData) => { ... };
const deleteContact = (id) => { ... };
const getContactById = (id) => { ... };
```

---

## 🎨 Mockup Visual

```
┌─────────────────────────────────────────┐
│  [Navbar]  Home | Agregar | 3 contactos │
├─────────────────────────────────────────┤
│                                         │
│  CONTACTOS                              │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Juan Pérez                        │ │
│  │ 📞 555-0101  ✉️ juan@example.com  │ │
│  │ [Ver] [Editar] [Eliminar]         │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ María García                      │ │
│  │ 📞 555-0102  ✉️ maria@example.com │ │
│  │ [Ver] [Editar] [Eliminar]         │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [+ Agregar Nuevo Contacto]            │
│                                         │
└─────────────────────────────────────────┘
```

---

## ✅ Checklist de Implementación

### Paso 1: Setup Inicial
- [ ] Crear proyecto con Vite
- [ ] Instalar react-router-dom
- [ ] Crear estructura de carpetas

### Paso 2: Context y Reducer
- [ ] Crear `contactReducer.js` con acciones CRUD
- [ ] Crear `ContactContext.js` con Provider
- [ ] Implementar custom hook `useContacts()`
- [ ] Agregar datos de prueba inicial

### Paso 3: Router
- [ ] Configurar BrowserRouter en App.js
- [ ] Definir todas las rutas
- [ ] Crear componentes de páginas básicos

### Paso 4: Lista de Contactos
- [ ] Mostrar lista desde Context
- [ ] Crear ContactCard component
- [ ] Implementar botón eliminar con confirmación
- [ ] Links a ver detalle y editar

### Paso 5: Agregar Contacto
- [ ] Crear formulario con validaciones
- [ ] Conectar con addContact del Context
- [ ] Navegación programática después de agregar
- [ ] Mensajes de éxito/error

### Paso 6: Ver Detalle
- [ ] Leer parámetro :id de la URL
- [ ] Buscar contacto por ID
- [ ] Mostrar toda la información
- [ ] Manejar contacto no encontrado

### Paso 7: Editar Contacto
- [ ] Pre-llenar formulario con datos actuales
- [ ] Conectar con updateContact del Context
- [ ] Navegación después de editar
- [ ] Mensajes de éxito

### Paso 8: Navbar y 404
- [ ] Navbar con links y contador
- [ ] Página 404 para rutas inexistentes

### Paso 9: Estilos
- [ ] CSS básico para que se vea profesional
- [ ] Responsive (opcional)

### Paso 10: Extras (Opcional)
- [ ] Persistencia con localStorage
- [ ] Búsqueda/filtro de contactos
- [ ] Ordenar alfabéticamente
- [ ] Validación de teléfonos duplicados

---

## 🎯 Criterios de Evaluación

Tu proyecto será evaluado en:

### Funcionalidad (40%)
- ✅ CRUD completo funciona correctamente
- ✅ Navegación entre páginas
- ✅ Formularios con validaciones
- ✅ Estado global compartido

### Código (30%)
- ✅ Uso correcto de useReducer + Context
- ✅ Router configurado correctamente
- ✅ Componentes bien organizados
- ✅ Código limpio y comentado

### UX/UI (20%)
- ✅ Interfaz amigable e intuitiva
- ✅ Mensajes de éxito/error
- ✅ Confirmaciones antes de eliminar
- ✅ Validaciones claras

### Extras (10%)
- ✅ Persistencia con localStorage
- ✅ Diseño responsive
- ✅ Funcionalidades adicionales

---

## 🔗 Recursos y Referencias

### Documentación Oficial
- [React Router v6 - Tutorial](https://reactrouter.com/en/main/start/tutorial)
- [useReducer + Context](https://react.dev/learn/scaling-up-with-reducer-and-context)
- [Forms in React](https://react.dev/reference/react-dom/components/input)

### 4Geeks Academy - Proyecto Oficial
- [Contact List App Using React & Context](https://4geeks.com/project/contact-list-context)

### Repasa los Steps Anteriores
- **Step 1-4**: React Router
- **Step 5-6**: useReducer
- **Step 7**: Context API
- **Step 8**: useReducer + Context
- **Step 9**: Router + Context integración

---

## 💡 Consejos para Implementar

### 1. Empieza Simple
No intentes hacer todo a la vez. Construye paso a paso:
1. Setup básico
2. Context funcionando
3. Una ruta (lista)
4. Segunda ruta (agregar)
5. Y así sucesivamente

### 2. Testea Frecuentemente
Después de cada funcionalidad, prueba que funcione antes de continuar.

### 3. Usa console.log
Para debuggear el estado y las acciones que se despachan.

### 4. Validaciones Primero Simples
Empieza con validaciones básicas (campo no vacío), luego mejora.

### 5. Estilos al Final
Primero que funcione, luego que se vea bien.

---

## 🆘 ¿Necesitas Ayuda?

### Si Estás Atascado:
1. **Repasa los steps anteriores** - especialmente 7, 8 y 9
2. **Lee el error en consola** - te dice exactamente qué falta
3. **Divide el problema** - si algo no funciona, simplifícalo
4. **Pregunta en Slack** - comparte el error específico
5. **Revisa la documentación oficial** - React Router y React Docs

### Errores Comunes:
- ❌ Olvidar envolver con Providers
- ❌ Intentar usar useNavigate fuera de BrowserRouter
- ❌ Mutar el estado en el reducer
- ❌ No validar que el contacto existe antes de mostrarlo
- ❌ Olvidar el `replace` en Navigate

---

## 📦 Entrega

### ¿Qué Entregar?
- Repositorio de GitHub con el código
- README.md con instrucciones para correr el proyecto
- (Opcional) Deploy en Netlify/Vercel

### Instrucciones en el README:
```markdown
# Contact List App

Aplicación de gestión de contactos con React Router y Context API.

## Instalación
\`\`\`bash
npm install
\`\`\`

## Ejecutar
\`\`\`bash
npm run dev
\`\`\`

## Tecnologías
- React 18
- React Router v6
- Context API + useReducer
- Vite
```

---

## ✅ Resumen

### Has Aprendido:
- ✅ Navegación con React Router
- ✅ Estado complejo con useReducer
- ✅ Estado global con Context API
- ✅ Patrón Store (useReducer + Context)
- ✅ Integración Router + Context

### Ahora Puedes:
- ✅ Construir aplicaciones multi-página
- ✅ Gestionar estado complejo globalmente
- ✅ Crear CRUDs completos
- ✅ Aplicar patrones profesionales de React

---

**¡Manos a la obra! 🚀 Este proyecto demuestra que dominas React a nivel profesional.**

**Recuerda**: No hay código resuelto. **TÚ** eres quien construye este proyecto aplicando todo lo aprendido. ¡Confía en ti!

---

**Creado con ❤️ para 4Geeks Academy - Cohort España FS PT 129**
