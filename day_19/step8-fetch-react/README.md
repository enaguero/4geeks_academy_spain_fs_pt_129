🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# Step 8: Fetch con React 🚀

## 🔗 Todo Junto: React + Fetch + REST + JSON

Ahora vas a integrar todo lo aprendido en componentes React:

```javascript
// React (UI) + useEffect (ciclo de vida) + Fetch (petición) + 
// HTTP (método) + REST API (servidor) + JSON (datos)

import { useState, useEffect } from 'react';

function Usuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function cargarUsuarios() {
      try {
        // 1. Fetch hace petición HTTP GET a una REST API
        const response = await fetch('https://api.ejemplo.com/usuarios');
        
        // 2. Verificar respuesta
        if (!response.ok) {
          throw new Error(`HTTP Error: ${response.status}`);
        }
        
        // 3. Parse JSON a objeto JavaScript
        const data = await response.json();
        
        // 4. Actualizar estado de React
        setUsuarios(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    cargarUsuarios();
  }, []);

  if (loading) return <p>Cargando usuarios...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {usuarios.map(user => (
        <li key={user.id}>{user.nombre}</li>
      ))}
    </ul>
  );
}
```

### ¿Qué Está Pasando?

1. **React** monta el componente
2. **useEffect** se ejecuta (una vez, por el array vacío `[]`)
3. **Fetch** hace petición **HTTP GET** a la **REST API**
4. **Servidor** procesa y devuelve **JSON**
5. **response.json()** parsea el JSON a objeto JavaScript
6. **setState** actualiza el estado de React
7. **React** re-renderiza mostrando los usuarios

### Cada Pieza Tiene un Rol:

- **React**: Renderiza la UI
- **useState**: Guarda los datos (usuarios, loading, error)
- **useEffect**: Ejecuta código cuando el componente carga
- **Fetch**: Hace la petición HTTP
- **REST API**: Devuelve los datos
- **JSON**: Formato de los datos
- **async/await**: Maneja la asincronía

---

## Integrar Fetch en Componentes

El patrón correcto es usar `useEffect` para hacer peticiones:

```javascript
import { useState, useEffect } from 'react';

function MiComponente() {
  const [datos, setDatos] = useState(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function cargar() {
      try {
        const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
        if (!res.ok) throw new Error('Error en la petición');
        const data = await res.json();
        setDatos(data);
      } catch (err) {
        setError(err);
      } finally {
        setCargando(false);
      }
    }

    cargar();
  }, []); // Ejecutar solo una vez al montar

  if (cargando) return <p>Cargando...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h2>{datos.name}</h2>
      <p>{datos.email}</p>
    </div>
  );
}

export default MiComponente;
```

## Ejemplo: Obtener Lista

```javascript
function ListaUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(r => r.json())
      .then(data => {
        setUsuarios(data);
        setCargando(false);
      })
      .catch(err => console.log(err));
  }, []);

  if (cargando) return <p>Cargando usuarios...</p>;

  return (
    <ul>
      {usuarios.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## Ejemplo: POST - Crear Datos

```javascript
function CrearTarea() {
  const [titulo, setTitulo] = useState('');
  const [creando, setCreando] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setCreando(true);

    try {
      const res = await fetch('https://jsonplaceholder.typicode.com/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: titulo,
          completed: false,
          userId: 1
        })
      });

      if (!res.ok) throw new Error('Error al crear');
      
      const nuevaTarea = await res.json();
      console.log('Creada:', nuevaTarea);
      setTitulo('');
    } catch (error) {
      console.log('Error:', error);
    } finally {
      setCreando(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={titulo}
        onChange={(e) => setTitulo(e.target.value)}
        placeholder="Nueva tarea"
      />
      <button disabled={creando}>
        {creando ? 'Creando...' : 'Crear'}
      </button>
    </form>
  );
}
```

## Ejemplo: Datos con Parámetros

```javascript
function BuscadorPosts() {
  const [userId, setUserId] = useState(1);
  const [posts, setPosts] = useState([]);
  const [cargando, setCargando] = useState(false);

  useEffect(() => {
    setCargando(true);
    
    fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`)
      .then(r => r.json())
      .then(data => {
        setPosts(data);
        setCargando(false);
      });
  }, [userId]); // Se ejecuta cuando userId cambia

  return (
    <div>
      <input
        type="number"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        min="1"
        max="10"
      />
      
      {cargando && <p>Cargando...</p>}
      
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}
```

## Patrón: Race Condition

```javascript
// ❌ MALO - Si userId cambia rápidamente, puede haber conflicto
useEffect(() => {
  fetch(`/api/usuario/${userId}`)
    .then(r => r.json())
    .then(data => setDatos(data)); // Puede ser dato viejo
}, [userId]);

// ✅ BIEN - Verificar que el dato corresponde al userId actual
useEffect(() => {
  let isMounted = true;

  fetch(`/api/usuario/${userId}`)
    .then(r => r.json())
    .then(data => {
      if (isMounted) {
        setDatos(data); // Solo si aún está montado
      }
    });

  return () => {
    isMounted = false; // Cleanup
  };
}, [userId]);
```

## Ejemplo: Cargar al Hacer Click

```javascript
function CargarOnClick() {
  const [usuario, setUsuario] = useState(null);
  const [cargando, setCargando] = useState(false);

  const cargarUsuario = async () => {
    setCargando(true);
    try {
      const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
      const data = await res.json();
      setUsuario(data);
    } finally {
      setCargando(false);
    }
  };

  return (
    <div>
      <button onClick={cargarUsuario} disabled={cargando}>
        {cargando ? 'Cargando...' : 'Cargar Usuario'}
      </button>
      
      {usuario && (
        <div>
          <h2>{usuario.name}</h2>
          <p>{usuario.email}</p>
        </div>
      )}
    </div>
  );
}
```

## Errores Comunes

### Error 1: Fetch sin useEffect
```javascript
// ❌ MALO - Se ejecuta en cada render
function Componente() {
  const [datos, setDatos] = useState(null);
  
  fetch(url).then(r => r.json()).then(setDatos);
  return <div>{datos}</div>;
}

// ✅ BIEN
function Componente() {
  const [datos, setDatos] = useState(null);
  
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setDatos);
  }, []);
  
  return <div>{datos}</div>;
}
```

### Error 2: No mostrar estado de carga
```javascript
// ❌ MALO - UI vacío mientras carga
return <ul>{items.map(...)}</ul>;

// ✅ BIEN
if (cargando) return <p>Cargando...</p>;
if (error) return <p>Error: {error}</p>;
return <ul>{items.map(...)}</ul>;
```

## Puntos Clave ✨

1. **useEffect** para hacer peticiones
2. **Tres estados**: cargando, dato, error
3. **Mostrar UI** según el estado
4. **Cleanup** para evitar memory leaks
5. **Array de dependencias** para cuándo actualizar

## Tu Ejercicio 🎯

Crea un componente que:
1. ✅ Cargue usuarios al montar
2. ✅ Muestre estado de carga
3. ✅ Maneje errores
4. ✅ Permita buscar por nombre (refetch)

---

**💡 Consejo**: Siempre muestra loading, error y success states.
