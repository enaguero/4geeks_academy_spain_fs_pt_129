🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🔢 Step 4: Parámetros en URLs

## 🎯 Objetivo

Aprender a crear **rutas dinámicas** con parámetros variables en la URL, como `/product/123` o `/user/juan`, y acceder a esos parámetros con el hook `useParams`.

---

## 🤔 ¿Qué Son los Parámetros de URL?

En lugar de crear una ruta para cada producto o usuario:
```
/product/1
/product/2
/product/3
... (¡tedioso!)
```

Creas UNA ruta dinámica:
```
/product/:id
```

El `:id` es un **parámetro** que puede cambiar.

---

## 💡 Ejemplo Real: Blog

Imagina un blog con posts. En lugar de:
```jsx
<Route path="/post1" element={<Post1 />} />
<Route path="/post2" element={<Post2 />} />
<Route path="/post3" element={<Post3 />} />
```

Usas UNA ruta:
```jsx
<Route path="/post/:id" element={<PostDetail />} />
```

Y el componente `PostDetail` lee el `id` para mostrar el post correcto.

---

## 🔧 Paso 1: Crear Datos de Ejemplo

Primero necesitamos datos con los que trabajar:

### data/posts.js

```javascript
export const posts = [
  {
    id: 1,
    title: 'Introducción a React Router',
    content: 'React Router es la librería estándar para navegación en React...',
    author: 'Juan Pérez',
    date: '2024-01-15'
  },
  {
    id: 2,
    title: 'useReducer vs useState',
    content: 'Ambos hooks manejan estado, pero useReducer es mejor cuando...',
    author: 'María García',
    date: '2024-01-20'
  },
  {
    id: 3,
    title: 'Context API Explicado',
    content: 'Context API resuelve el problema del prop drilling permitiendo...',
    author: 'Pedro López',
    date: '2024-01-25'
  }
];
```

---

## 🔧 Paso 2: Lista de Posts (sin parámetros)

### pages/Blog.jsx

```jsx
import { Link } from 'react-router-dom';
import { posts } from '../data/posts';

function Blog() {
  return (
    <div>
      <h1>📝 Blog</h1>
      <div>
        {posts.map(post => (
          <div key={post.id} style={{ 
            border: '1px solid #ddd',
            padding: '1rem',
            marginBottom: '1rem',
            borderRadius: '4px'
          }}>
            <h2>{post.title}</h2>
            <p style={{ color: '#666' }}>
              Por {post.author} • {post.date}
            </p>
            <p>{post.content.substring(0, 100)}...</p>
            
            {/* Link con parámetro dinámico */}
            <Link to={`/post/${post.id}`}>
              Leer más →
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Blog;
```

**Nota**: `to={`/post/${post.id}`}` crea URLs como `/post/1`, `/post/2`, etc.

---

## 🔧 Paso 3: Página de Detalle con useParams

### pages/PostDetail.jsx

```jsx
import { useParams, Link } from 'react-router-dom';
import { posts } from '../data/posts';

function PostDetail() {
  // useParams extrae los parámetros de la URL
  const { id } = useParams();
  
  // Buscar el post que coincide con el ID
  const post = posts.find(p => p.id === parseInt(id));

  // Si no existe el post
  if (!post) {
    return (
      <div>
        <h1>❌ Post no encontrado</h1>
        <p>El post con ID {id} no existe.</p>
        <Link to="/blog">← Volver al blog</Link>
      </div>
    );
  }

  // Mostrar el post completo
  return (
    <div>
      <Link to="/blog">← Volver al blog</Link>
      
      <article style={{ marginTop: '2rem' }}>
        <h1>{post.title}</h1>
        <p style={{ color: '#666' }}>
          Por {post.author} • {post.date}
        </p>
        <hr />
        <p style={{ 
          fontSize: '1.1rem',
          lineHeight: '1.6'
        }}>
          {post.content}
        </p>
      </article>
    </div>
  );
}

export default PostDetail;
```

### Conceptos Clave:

1. **`useParams()`**: Hook que retorna un objeto con todos los parámetros
2. **`const { id } = useParams()`**: Extrae el parámetro `id`
3. **`parseInt(id)`**: Convierte el string a número (URLs siempre son strings)
4. **Validación**: Verificar si el post existe antes de mostrarlo

---

## 🔧 Paso 4: Configurar la Ruta en App.jsx

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Blog from './pages/Blog';
import PostDetail from './pages/PostDetail';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div style={{ padding: '2rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/blog" element={<Blog />} />
          {/* Ruta con parámetro */}
          <Route path="/post/:id" element={<PostDetail />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
```

**Importante**: `:id` puede ser cualquier cosa: `:userId`, `:productId`, `:slug`, etc.

---

## 💡 Múltiples Parámetros

Puedes tener varios parámetros en una URL:

```jsx
// Ruta
<Route path="/category/:categoryId/post/:postId" element={<Post />} />

// Componente
function Post() {
  const { categoryId, postId } = useParams();
  
  return (
    <div>
      <p>Categoría: {categoryId}</p>
      <p>Post: {postId}</p>
    </div>
  );
}

// Uso
<Link to="/category/tech/post/123">Ver post</Link>
// URL: /category/tech/post/123
```

---

## 💡 Parámetros Opcionales

Para parámetros opcionales, crea rutas separadas:

```jsx
<Routes>
  {/* Sin parámetro: muestra todos */}
  <Route path="/products" element={<Products />} />
  
  {/* Con parámetro: filtra por categoría */}
  <Route path="/products/:category" element={<Products />} />
</Routes>
```

En el componente:

```jsx
function Products() {
  const { category } = useParams();
  
  // category puede ser undefined si estás en /products
  const filteredProducts = category 
    ? products.filter(p => p.category === category)
    : products;

  return (
    <div>
      <h1>Productos {category && `- ${category}`}</h1>
      {/* ... */}
    </div>
  );
}
```

---

## 💡 Query Strings (Búsqueda)

Para búsquedas o filtros, usa query strings: `/search?q=react`

```jsx
import { useSearchParams } from 'react-router-dom';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('q');

  return (
    <div>
      <h1>Buscando: {query}</h1>
      {/* Buscar en tus datos usando query */}
    </div>
  );
}
```

Link con query string:
```jsx
<Link to="/search?q=react">Buscar "react"</Link>
```

---

## 📝 Ejercicio Práctico: Tienda de Productos

Crea una tienda simple con rutas dinámicas:

### Requisitos:

1. **Datos** (`data/products.js`):
```javascript
export const products = [
  { id: 1, name: 'Laptop', price: 999, category: 'tech' },
  { id: 2, name: 'Mouse', price: 29, category: 'tech' },
  { id: 3, name: 'Silla', price: 199, category: 'furniture' },
  { id: 4, name: 'Mesa', price: 299, category: 'furniture' }
];
```

2. **Página "Products"** (`/products`):
   - Lista todos los productos
   - Cada producto con link a `/product/:id`

3. **Página "ProductDetail"** (`/product/:id`):
   - Mostrar nombre, precio, categoría
   - Botón "Volver a productos"
   - Manejar producto no encontrado

4. **Bonus**: Página de categoría (`/category/:categoryName`)
   - Filtrar productos por categoría
   - Ejemplo: `/category/tech` solo muestra productos tech

---

## ⚠️ Errores Comunes

### 1. Olvidar parseInt cuando comparas con números

```javascript
// ❌ MAL: '1' !== 1
const post = posts.find(p => p.id === id);

// ✅ BIEN: Convertir a número
const post = posts.find(p => p.id === parseInt(id));
```

### 2. No validar que el recurso existe

```jsx
// ❌ MAL: Si no existe, app crashea
return <h1>{post.title}</h1>;

// ✅ BIEN: Validar primero
if (!post) {
  return <p>No encontrado</p>;
}
return <h1>{post.title}</h1>;
```

### 3. Confundir parámetros con query strings

```jsx
// Parámetro: /post/123
<Route path="/post/:id" />
const { id } = useParams();

// Query string: /search?q=react
<Route path="/search" />
const [searchParams] = useSearchParams();
const query = searchParams.get('q');
```

### 4. No usar template literals correctamente

```jsx
// ❌ MAL
<Link to="/post/" + post.id>Ver</Link>

// ✅ BIEN
<Link to={`/post/${post.id}`}>Ver</Link>
```

---

## 🎯 Casos de Uso Reales

### E-commerce
```
/product/:productId
/category/:categoryName
/category/:categoryName/product/:productId
```

### Red Social
```
/user/:username
/user/:username/posts
/post/:postId
/post/:postId/comments
```

### Blog
```
/post/:slug
/category/:categoryName
/author/:authorName
/tag/:tagName
```

### Dashboard
```
/dashboard/user/:userId
/dashboard/analytics/:reportId
/settings/:section
```

---

## 🔗 Recursos

### Documentación Oficial
- [useParams - React Router](https://reactrouter.com/en/main/hooks/use-params)
- [useSearchParams - React Router](https://reactrouter.com/en/main/hooks/use-search-params)

### 4Geeks Academy
- [Routing our Views with React Router](https://4geeks.com/lesson/routing-our-views-with-react-router)

---

## ✅ Resumen

### Antes de continuar, debes entender:

- ✅ `:parametro` en una ruta crea un parámetro dinámico
- ✅ `useParams()` extrae parámetros de la URL
- ✅ Los parámetros siempre son strings (usa parseInt si necesitas números)
- ✅ Siempre valida que el recurso existe
- ✅ Query strings (`?q=valor`) son diferentes a parámetros
- ✅ Puedes tener múltiples parámetros en una ruta

### Siguiente Paso

En el **Step 5** aprenderás sobre **useReducer**, una alternativa a `useState` para manejar estado complejo.

---

**¡Practica con rutas dinámicas! 🚀**
