# 📡 Día 19: TodoList con React y Fetch

## 🎯 Objetivos de Aprendizaje

Hoy aprenderás a conectar tu aplicación React con APIs reales usando Fetch. Los conceptos clave son:

- **API y JSON**: Qué son y por qué existen
- **HTTP**: Protocolo de comunicación y métodos (GET, POST, PUT, DELETE)
- **REST**: Arquitectura para diseñar APIs
- **Síncrono vs Asíncrono**: Conceptos fundamentales de programación asíncrona
- **setTimeout**: Primera herramienta asíncrona en JavaScript
- **Callbacks**: Funciones que se ejecutan después de algo
- **Callback Hell**: El problema que solucionan las Promises
- **Promises**: Entender promesas en JavaScript
- **Async/Await**: Sintaxis moderna para código asincrónico
- **Fetch API**: Hacer peticiones HTTP desde React
- **REST APIs**: Conceptos y cómo consumirlas
- **Integración**: Combinar Fetch con useState y useEffect
- **Proyecto Real**: TodoList que persiste datos en un servidor

---

## 🔗 ¿Cómo se Relaciona Todo?

Este es el panorama completo de lo que aprenderás hoy:

```
┌─────────────────────────────────────────────┐
│ 1. API (Application Programming Interface) │
│    └─> Contrato entre aplicaciones         │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. REST (Representational State Transfer)  │
│    └─> Estilo arquitectónico para APIs     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. HTTP (Protocolo de comunicación)        │
│    └─> GET, POST, PUT, DELETE              │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. JSON (Formato de datos)                 │
│    └─> Lenguaje común entre cliente/server │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. Fetch API (Herramienta JavaScript)      │
│    └─> Consume todo lo anterior            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 6. React + Hooks                            │
│    └─> Integra Fetch en tu UI              │
└─────────────────────────────────────────────┘
```

**En resumen:** Usarás **Fetch** (JavaScript) para hacer peticiones **HTTP** (GET/POST/PUT/DELETE) a una **REST API**, intercambiando datos en formato **JSON**.

## 📚 Estructura del Día

Este día tiene **10 pasos progresivos**, cada uno construyendo sobre el anterior. Es fundamental seguir el orden.

### Step 0: Conceptos Fundamentales 🌐
**Archivo**: `step0-conceptos-fundamentales/`

**¡COMIENZA AQUÍ!** Antes de tocar código, entiende qué es una API, JSON, HTTP y REST.

**Conceptos**:
- Qué es una API
- Qué es JSON y cómo funciona
- HTTP: Protocolo y métodos (GET, POST, PUT, DELETE)
- REST: Arquitectura para APIs
- Cómo se relaciona todo

---

### Step 1: Síncrono vs Asíncrono 🔄
**Archivo**: `step1-sync-async/`

Entiende los conceptos fundamentales de código síncrono y asíncrono.

**Conceptos**:
- Qué es código síncrono (bloqueante)
- Qué es código asíncrono (no bloqueante)
- Ejemplos de vida real
- Por qué JavaScript necesita asincronía

---

### Step 2: setTimeout - Tu Primera Herramienta Asíncrona ⏱️
**Archivo**: `step2-settimeout/`

Aprende a usar setTimeout y setInterval.

**Conceptos**:
- setTimeout y setInterval
- clearTimeout y clearInterval
- Event Loop básico
- Call Stack y Task Queue

---

### Step 3: Callbacks y el "Callback Hell" 🔥
**Archivo**: `step3-callbacks-hell/`

Entiende qué son los callbacks y el problema que generan.

**Conceptos**:
- Qué es un callback
- Callbacks anidados
- El problema del "Callback Hell"
- Por qué necesitamos Promises

---

### Step 4: Promises - La Solución 🤝
**Archivo**: `step4-promises/`

Aprende cómo las Promises solucionan el Callback Hell.

**Conceptos**:
- Qué es una Promise
- Estados: pending, resolved, rejected
- then(), catch(), finally()
- Promise chaining

---

### Step 5: Async/Await ⏳
**Archivo**: `step5-async-await/`

Sintaxis moderna y más legible sobre Promises.

**Conceptos**:
- async function
- await keyword
- Try/catch para errores
- Ventajas sobre .then()

---

### Step 6: Fetch API 🌐
**Archivo**: `step6-fetch-api/`

Haz peticiones HTTP usando Fetch.

**Conceptos**:
- Sintaxis de fetch()
- GET vs POST vs PUT vs DELETE
- Headers y body
- Response y .json()

---

### Step 7: REST APIs 🏭️
**Archivo**: `step7-rest-apis/`

Entiende qué son REST APIs y cómo funcionan.

**Conceptos**:
- Qué es REST
- Métodos HTTP
- Status codes
- Recursos y endpoints

---

### Step 8: Fetch con React 🚀
**Archivo**: `step8-fetch-react/`

Integra Fetch con React hooks.

**Conceptos**:
- Fetch en useEffect
- Manejo de estados: loading, data, error
- Evitar race conditions
- Cleanup en fetch

---

### Step 9: TodoList con API 💾
**Archivo**: `step9-todolist-api/`

Crea un TodoList completo que consume una API.

**Conceptos**:
- CRUD operations con Fetch
- Sincronizar estado con servidor
- Manejo de errores
- Proyecto completo

---

## 🚀 Cómo Usar Este Material

### 1. Seguir en orden
Cada paso depende del anterior. No saltes pasos.

### 2. Practicar con APIs reales
Usaremos APIs públicas para aprender sin necesidad de un servidor propio.

### 3. Experimentar
Modifica ejemplos, prueba diferentes endpoints, rompe intencionalmente y arregla.

### 4. Entender, no memorizar
Busca entender *por qué* funciona así, no solo *cómo*.

## 🔗 APIs Recomendadas para Practicar

- **JSONPlaceholder**: https://jsonplaceholder.typicode.com/ (Fake API gratis)
- **OpenWeather**: API de clima (requiere clave gratis)
- **GitHub API**: https://api.github.com
- **PokéAPI**: https://pokeapi.co/

## 📖 Lectura Recomendada

### De 4Geeks Academy
- [Creating asynchronous algorithms](https://4geeks.com/syllabus/spain-fs-pt-129/read/asynchronous-algorithms-async-await)
- [The Fetch API](https://4geeks.com/syllabus/spain-fs-pt-129/read/the-fetch-javascript-api)
- [Understanding REST APIs](https://4geeks.com/syllabus/spain-fs-pt-129/read/understanding-rest-apis)

### MDN
- [Promises](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Async/Await](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/async_function)
- [Fetch API](https://developer.mozilla.org/es/docs/Web/API/Fetch_API)

## 🎓 Proyecto Final

**TodoList Application con API**

Crearás un TodoList que:

✅ Carga tareas desde un servidor  
✅ Añade nuevas tareas a la API  
✅ Actualiza tareas existentes  
✅ Elimina tareas del servidor  
✅ Muestra estado de carga  
✅ Maneja errores apropiadamente  
✅ Sincroniza con localStorage como fallback  

## 💡 Consejos Importantes

### Para Principiantes

1. **Sigue el orden**: Los 10 steps están diseñados para aprendizaje incremental
2. **Entiende conceptos básicos primero**: Síncrono vs Asíncrono antes de Promises
3. **Practica con ejemplos**: Copia y ejecuta el código en tu navegador
4. **Usa el Dev Tools**: Abre la consola y Network para ver las peticiones
5. **Maneja errores**: Siempre incluye try/catch o .catch()
6. **Estados de UI**: Loading, success, error son fundamentales
7. **Inspecciona APIs**: Usa herramientas como Postman o el navegador

### Conceptos Críticos

- **Síncrono vs Asíncrono**: La base de todo lo demás
- **Event Loop**: Cómo JavaScript maneja operaciones asíncronas
- **Callback Hell**: Por qué existen las Promises
- **Asincronía**: El código continúa mientras espera la respuesta
- **Estados**: Tu componente puede estar en loading, success o error
- **CORS**: Algunos problemas vienen de políticas de origen
- **Timeouts**: Las peticiones pueden fallar o tardar

## ⚠️ Errores Comunes

### Error 1: No manejar errores
```javascript
// ❌ MALO
fetch(url).then(r => r.json()).then(data => setData(data));

// ✅ BIEN
try {
  const res = await fetch(url);
  const data = await res.json();
  setData(data);
} catch (error) {
  setError(error);
}
```

### Error 2: Fetch en cada render
```javascript
// ❌ MALO
function Component() {
  const data = fetch(url); // Se ejecuta cada render
}

// ✅ BIEN
useEffect(() => {
  fetch(url).then(...);
}, []); // Se ejecuta solo una vez
```

### Error 3: No limpiar en unmount
```javascript
// ❌ MALO
useEffect(() => {
  fetch(url); // Si el componente se desmonta, hay error
});

// ✅ BIEN
useEffect(() => {
  let isMounted = true;
  fetch(url).then(data => {
    if (isMounted) setData(data);
  });
  return () => { isMounted = false; };
}, []);
```

## 🆘 Necesitas Ayuda?

1. Lee el tutorial paso a paso
2. Abre la consola del navegador (F12)
3. Revisa la pestaña Network para ver las peticiones
4. Busca el error específico en Google
5. Pregunta en el canal de Slack

## 📊 Progreso

Marca cada paso cuando lo completes:

- [ ] Step 0: Conceptos Fundamentales (API, JSON, HTTP, REST)
- [ ] Step 1: Síncrono vs Asíncrono
- [ ] Step 2: setTimeout y setInterval
- [ ] Step 3: Callbacks y Callback Hell
- [ ] Step 4: Promises
- [ ] Step 5: Async/Await
- [ ] Step 6: Fetch API
- [ ] Step 7: REST APIs
- [ ] Step 8: Fetch con React
- [ ] Step 9: TodoList con API
- [ ] Proyecto Final: TodoList Completa

---

**¡Vamos a conectar con el mundo! 🌍**

Hoy cruzaremos la línea entre aplicaciones locales y aplicaciones reales que se conectan con servidores. Es un momento emocionante - estás construyendo aplicaciones profesionales.
