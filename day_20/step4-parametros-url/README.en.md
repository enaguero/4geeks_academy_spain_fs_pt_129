[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🔢 Step 4: URL Parameters

## 🎯 Goal

Learn to create **dynamic routes** with variable parameters in the URL, like `/product/123` or `/user/juan`, and access those parameters with the `useParams` hook.

---

## 🤔 What Are URL Parameters?

Instead of creating a route per product or user:
```
/product/1
/product/2
/product/3
... (tedious!)
```

You create ONE dynamic route:
```
/product/:id
```

The `:id` is a **parameter** that can change.

---

## 💡 Real-World Example: Blog

Imagine a blog with posts. Instead of:
```jsx
<Route path="/post1" element={<Post1 />} />
<Route path="/post2" element={<Post2 />} />
<Route path="/post3" element={<Post3 />} />
```

You use ONE route:
```jsx
<Route path="/post/:id" element={<PostDetail />} />
```

And the `PostDetail` component reads the `id` to display the correct post.

---

## 🔧 Step 1: Create Sample Data

First we need some data to work with:

### data/posts.js

```javascript
export const posts = [
  {
    id: 1,
    title: 'Introduction to React Router',
    content: 'React Router is the standard library for navigation in React...',
    author: 'Juan Pérez',
    date: '2024-01-15'
  },
  {
    id: 2,
    title: 'useReducer vs useState',
    content: 'Both hooks manage state, but useReducer is better when...',
    author: 'María García',
    date: '2024-01-20'
  },
  {
    id: 3,
    title: 'Context API Explained',
    content: 'Context API solves the prop drilling problem by letting you...',
    author: 'Pedro López',
    date: '2024-01-25'
  }
];
```

---

## 🔧 Step 2: Post List (no parameters)

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
              By {post.author} • {post.date}
            </p>
            <p>{post.content.substring(0, 100)}...</p>
            
            {/* Link with dynamic parameter */}
            <Link to={`/post/${post.id}`}>
              Read more →
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Blog;
```

**Note**: `to={`/post/${post.id}`}` produces URLs like `/post/1`, `/post/2`, etc.

---

## 🔧 Step 3: Detail Page with useParams

### pages/PostDetail.jsx

```jsx
import { useParams, Link } from 'react-router-dom';
import { posts } from '../data/posts';

function PostDetail() {
  // useParams reads the URL parameters
  const { id } = useParams();
  
  // Find the post matching the ID
  const post = posts.find(p => p.id === parseInt(id));

  // If the post doesn't exist
  if (!post) {
    return (
      <div>
        <h1>❌ Post not found</h1>
        <p>The post with ID {id} does not exist.</p>
        <Link to="/blog">← Back to blog</Link>
      </div>
    );
  }

  // Display the full post
  return (
    <div>
      <Link to="/blog">← Back to blog</Link>
      
      <article style={{ marginTop: '2rem' }}>
        <h1>{post.title}</h1>
        <p style={{ color: '#666' }}>
          By {post.author} • {post.date}
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

### Key Concepts:

1. **`useParams()`**: Hook that returns an object with all the parameters
2. **`const { id } = useParams()`**: Destructure the `id` parameter
3. **`parseInt(id)`**: Convert the string to a number (URLs are always strings)
4. **Validation**: Verify the post exists before rendering it

---

## 🔧 Step 4: Configure the Route in App.jsx

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
          {/* Route with parameter */}
          <Route path="/post/:id" element={<PostDetail />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
```

**Important**: `:id` can be anything: `:userId`, `:productId`, `:slug`, etc.

---

## 💡 Multiple Parameters

You can have multiple parameters in a URL:

```jsx
// Route
<Route path="/category/:categoryId/post/:postId" element={<Post />} />

// Component
function Post() {
  const { categoryId, postId } = useParams();
  
  return (
    <div>
      <p>Category: {categoryId}</p>
      <p>Post: {postId}</p>
    </div>
  );
}

// Usage
<Link to="/category/tech/post/123">View post</Link>
// URL: /category/tech/post/123
```

---

## 💡 Optional Parameters

For optional parameters, create separate routes:

```jsx
<Routes>
  {/* No parameter: show all */}
  <Route path="/products" element={<Products />} />
  
  {/* With parameter: filter by category */}
  <Route path="/products/:category" element={<Products />} />
</Routes>
```

In the component:

```jsx
function Products() {
  const { category } = useParams();
  
  // category can be undefined when you're on /products
  const filteredProducts = category 
    ? products.filter(p => p.category === category)
    : products;

  return (
    <div>
      <h1>Products {category && `- ${category}`}</h1>
      {/* ... */}
    </div>
  );
}
```

---

## 💡 Query Strings (Search)

For search or filters, use query strings: `/search?q=react`

```jsx
import { useSearchParams } from 'react-router-dom';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('q');

  return (
    <div>
      <h1>Searching: {query}</h1>
      {/* Search your data using query */}
    </div>
  );
}
```

Link with query string:
```jsx
<Link to="/search?q=react">Search "react"</Link>
```

---

## 📝 Practice Exercise: Product Store

Build a simple store with dynamic routes:

### Requirements:

1. **Data** (`data/products.js`):
```javascript
export const products = [
  { id: 1, name: 'Laptop', price: 999, category: 'tech' },
  { id: 2, name: 'Mouse', price: 29, category: 'tech' },
  { id: 3, name: 'Chair', price: 199, category: 'furniture' },
  { id: 4, name: 'Table', price: 299, category: 'furniture' }
];
```

2. **"Products" page** (`/products`):
   - List every product
   - Each product links to `/product/:id`

3. **"ProductDetail" page** (`/product/:id`):
   - Show name, price, category
   - "Back to products" button
   - Handle product-not-found

4. **Bonus**: Category page (`/category/:categoryName`)
   - Filter products by category
   - Example: `/category/tech` shows only tech products

---

## ⚠️ Common Mistakes

### 1. Forgetting parseInt when comparing with numbers

```javascript
// ❌ BAD: '1' !== 1
const post = posts.find(p => p.id === id);

// ✅ GOOD: Convert to number
const post = posts.find(p => p.id === parseInt(id));
```

### 2. Not validating that the resource exists

```jsx
// ❌ BAD: If it doesn't exist, the app crashes
return <h1>{post.title}</h1>;

// ✅ GOOD: Validate first
if (!post) {
  return <p>Not found</p>;
}
return <h1>{post.title}</h1>;
```

### 3. Mixing up parameters and query strings

```jsx
// Parameter: /post/123
<Route path="/post/:id" />
const { id } = useParams();

// Query string: /search?q=react
<Route path="/search" />
const [searchParams] = useSearchParams();
const query = searchParams.get('q');
```

### 4. Using template literals incorrectly

```jsx
// ❌ BAD
<Link to="/post/" + post.id>View</Link>

// ✅ GOOD
<Link to={`/post/${post.id}`}>View</Link>
```

---

## 🎯 Real-World Use Cases

### E-commerce
```
/product/:productId
/category/:categoryName
/category/:categoryName/product/:productId
```

### Social Network
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

## 🔗 Resources

### Official Documentation
- [useParams - React Router](https://reactrouter.com/en/main/hooks/use-params)
- [useSearchParams - React Router](https://reactrouter.com/en/main/hooks/use-search-params)

### 4Geeks Academy
- [Routing our Views with React Router](https://4geeks.com/lesson/routing-our-views-with-react-router)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ `:parameter` in a route creates a dynamic parameter
- ✅ `useParams()` reads parameters from the URL
- ✅ Parameters are always strings (use parseInt if you need numbers)
- ✅ Always validate that the resource exists
- ✅ Query strings (`?q=value`) are different from parameters
- ✅ You can have multiple parameters in one route

### Next Step

In **Step 5** you'll learn about **useReducer**, an alternative to `useState` for handling complex state.

---

**Practice with dynamic routes! 🚀**
