[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 8: Fetch with React 🚀

## 🔗 All Together: React + Fetch + REST + JSON

Now you'll integrate everything you've learned into React components:

```javascript
// React (UI) + useEffect (lifecycle) + Fetch (request) + 
// HTTP (method) + REST API (server) + JSON (data)

import { useState, useEffect } from 'react';

function Usuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function cargarUsuarios() {
      try {
        // 1. Fetch makes an HTTP GET request to a REST API
        const response = await fetch('https://api.ejemplo.com/usuarios');
        
        // 2. Verify the response
        if (!response.ok) {
          throw new Error(`HTTP Error: ${response.status}`);
        }
        
        // 3. Parse JSON into a JavaScript object
        const data = await response.json();
        
        // 4. Update React state
        setUsuarios(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    cargarUsuarios();
  }, []);

  if (loading) return <p>Loading users...</p>;
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

### What's Happening?

1. **React** mounts the component
2. **useEffect** runs (once, because of the empty `[]` array)
3. **Fetch** makes an **HTTP GET** request to the **REST API**
4. **Server** processes and returns **JSON**
5. **response.json()** parses the JSON into a JavaScript object
6. **setState** updates React state
7. **React** re-renders showing the users

### Each Piece Has a Role:

- **React**: Renders the UI
- **useState**: Stores the data (users, loading, error)
- **useEffect**: Runs code when the component mounts
- **Fetch**: Makes the HTTP request
- **REST API**: Returns the data
- **JSON**: Format of the data
- **async/await**: Handles the asynchrony

---

## Integrating Fetch into Components

The correct pattern is to use `useEffect` to make requests:

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
  }, []); // Run only once on mount

  if (cargando) return <p>Loading...</p>;
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

## Example: Get a List

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

  if (cargando) return <p>Loading users...</p>;

  return (
    <ul>
      {usuarios.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## Example: POST - Create Data

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
        placeholder="New task"
      />
      <button disabled={creando}>
        {creando ? 'Creating...' : 'Create'}
      </button>
    </form>
  );
}
```

## Example: Data with Parameters

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
  }, [userId]); // Runs whenever userId changes

  return (
    <div>
      <input
        type="number"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        min="1"
        max="10"
      />
      
      {cargando && <p>Loading...</p>}
      
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}
```

## Pattern: Race Condition

```javascript
// ❌ BAD - If userId changes quickly, there can be a conflict
useEffect(() => {
  fetch(`/api/usuario/${userId}`)
    .then(r => r.json())
    .then(data => setDatos(data)); // Could be stale data
}, [userId]);

// ✅ GOOD - Verify the data matches the current userId
useEffect(() => {
  let isMounted = true;

  fetch(`/api/usuario/${userId}`)
    .then(r => r.json())
    .then(data => {
      if (isMounted) {
        setDatos(data); // Only if still mounted
      }
    });

  return () => {
    isMounted = false; // Cleanup
  };
}, [userId]);
```

## Example: Load on Click

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
        {cargando ? 'Loading...' : 'Load User'}
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

## Common Mistakes

### Mistake 1: Fetch without useEffect
```javascript
// ❌ BAD - Runs on every render
function Componente() {
  const [datos, setDatos] = useState(null);
  
  fetch(url).then(r => r.json()).then(setDatos);
  return <div>{datos}</div>;
}

// ✅ GOOD
function Componente() {
  const [datos, setDatos] = useState(null);
  
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setDatos);
  }, []);
  
  return <div>{datos}</div>;
}
```

### Mistake 2: Not showing a loading state
```javascript
// ❌ BAD - Empty UI while loading
return <ul>{items.map(...)}</ul>;

// ✅ GOOD
if (cargando) return <p>Loading...</p>;
if (error) return <p>Error: {error}</p>;
return <ul>{items.map(...)}</ul>;
```

## Key Points ✨

1. **useEffect** to make requests
2. **Three states**: loading, data, error
3. **Render UI** based on the state
4. **Cleanup** to avoid memory leaks
5. **Dependency array** to control when to refresh

## Your Exercise 🎯

Build a component that:
1. ✅ Loads users on mount
2. ✅ Shows a loading state
3. ✅ Handles errors
4. ✅ Allows searching by name (refetch)

---

**💡 Tip**: Always show loading, error and success states.
