# 📡 Día 19: TodoList con React y Fetch

## 🎯 Objetivos de Aprendizaje

Hoy aprenderás a conectar tu aplicación React con APIs reales usando Fetch. Los conceptos clave son:

- **Promises**: Entender promesas en JavaScript
- **Async/Await**: Sintaxis moderna para código asincrónico
- **Fetch API**: Hacer peticiones HTTP desde React
- **REST APIs**: Conceptos y cómo consumirlas
- **Integración**: Combinar Fetch con useState y useEffect
- **Proyecto Real**: TodoList que persiste datos en un servidor

## 📚 Estructura del Día

Este día tiene 6 pasos progresivos, cada uno construyendo sobre el anterior:

### Step 1: Promises 🤝
**Archivo**: `step1-promises/`

Entiende cómo funcionan las promesas en JavaScript.

**Conceptos**:
- Qué es una Promise
- Estados: pending, resolved, rejected
- then(), catch(), finally()
- Promise chaining

---

### Step 2: Async/Await ⏳
**Archivo**: `step2-async-await/`

Aprende la sintaxis moderna para código asincrónico.

**Conceptos**:
- async function
- await keyword
- Try/catch para errores
- Ventajas sobre .then()

---

### Step 3: Fetch API 🌐
**Archivo**: `step3-fetch-api/`

Haz peticiones HTTP usando Fetch.

**Conceptos**:
- Sintaxis de fetch()
- GET vs POST vs PUT vs DELETE
- Headers y body
- Response y .json()

---

### Step 4: REST APIs 🏗️
**Archivo**: `step4-rest-apis/`

Entiende qué son REST APIs y cómo funcionan.

**Conceptos**:
- Qué es REST
- Métodos HTTP
- Status codes
- Recursos y endpoints

---

### Step 5: Fetch con React 🚀
**Archivo**: `step5-fetch-datos/`

Integra Fetch con React hooks.

**Conceptos**:
- Fetch en useEffect
- Manejo de estados: loading, data, error
- Evitar race conditions
- Cleanup en fetch

---

### Step 6: TodoList con API 💾
**Archivo**: `step6-todolist-api/`

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

1. **Entiende Promises primero**: No saltes a Async/Await sin entender Promises
2. **Usa el Dev Tools**: Abre la consola y Network para ver las peticiones
3. **Maneja errores**: Siempre incluye try/catch o .catch()
4. **Estados de UI**: Loading, success, error son fundamentales
5. **Inspecciona APIs**: Usa herramientas como Postman o el navegador

### Conceptos Críticos

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

- [ ] Step 1: Promises
- [ ] Step 2: Async/Await
- [ ] Step 3: Fetch API
- [ ] Step 4: REST APIs
- [ ] Step 5: Fetch con React
- [ ] Step 6: TodoList con API
- [ ] Proyecto Final: TodoList Completa

---

**¡Vamos a conectar con el mundo! 🌍**

Hoy cruzaremos la línea entre aplicaciones locales y aplicaciones reales que se conectan con servidores. Es un momento emocionante - estás construyendo aplicaciones profesionales.
