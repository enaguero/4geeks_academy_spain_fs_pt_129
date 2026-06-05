[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🚀 Step 2: First Basic Route with React Router

## 🎯 Goal

Build your **first application** with React Router in the simplest way possible.

By the end of this step you'll know how to:
- ✅ Install react-router-dom
- ✅ Configure BrowserRouter
- ✅ Create your first route
- ✅ Understand how `<Route>` works

---

## 📦 Step 1: Installation

First, you need to install React Router in your React project.

### Option A: New project with Vite (recommended)

```bash
# Create React project
npm create vite@latest mi-primera-spa -- --template react

# Enter the project
cd mi-primera-spa

# Install dependencies
npm install

# Install React Router
npm install react-router-dom

# Start the dev server
npm run dev
```

### Option B: Existing React project

If you already have a React project:

```bash
npm install react-router-dom
```

### ⚠️ Important

Make sure you install **`react-router-dom`** (NOT just `react-router`).

```bash
# ✅ CORRECT
npm install react-router-dom

# ❌ INCORRECT
npm install react-router
```

---

## 🏗️ Step 2: File Structure

Let's create a simple structure:

```
src/
├── App.jsx          ← Where we configure the router
├── main.jsx         ← Entry point (DON'T touch it)
└── pages/           ← New folder for our "pages"
    └── Home.jsx     ← Our first page
```

---

## 📄 Step 3: Create the First Page

Create a `pages` folder inside `src` and a `Home.jsx` file:

```jsx
// src/pages/Home.jsx
function Home() {
  return (
    <div>
      <h1>🏠 Welcome to My First SPA</h1>
      <p>This is the home page.</p>
      <p>If you see this, React Router works! 🎉</p>
    </div>
  );
}

export default Home;
```

**Explanation:**
- It's just a normal React component
- There's NOTHING special about it
- React Router will render it when we visit the `/` URL

---

## 🧭 Step 4: Configure React Router in App.jsx

Now the magic happens. Edit your `App.jsx`:

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

## 🔍 Understanding the Code Step by Step

### 1. Imports

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
```

- **`BrowserRouter`**: The main container — the whole router lives inside it
- **`Routes`**: Container for all individual routes
- **`Route`**: Defines ONE specific route

### 2. BrowserRouter

```jsx
<BrowserRouter>
  {/* Your entire routing system goes here */}
</BrowserRouter>
```

**Analogy:** It's the entire "building" from Step 1.

- Without it, nothing works
- You only use ONE per application
- It must wrap everything

### 3. Routes

```jsx
<Routes>
  {/* Individual routes go here */}
</Routes>
```

**Analogy:** It's the building "directory" listing every floor.

- Groups all the individual `<Route>` components
- React Router finds which one matches the current URL

### 4. Route

```jsx
<Route path="/" element={<Home />} />
```

**Analogy:** It's a specific "office" in the building.

- **`path="/"`**: The URL that activates this route
- **`element={<Home />}`**: The component that renders

---

## 🎯 How It Works

When you visit `http://localhost:5173/`:

```
1. React Router sees the current URL: "/"
   ↓
2. Looks inside <Routes> for a route with path="/"
   ↓
3. Finds: <Route path="/" element={<Home />} />
   ↓
4. Renders the <Home /> component
   ↓
5. You see on screen: "🏠 Welcome to My First SPA"
```

---

## 🧪 Step 5: Test Your Application

1. **Start the dev server:**
   ```bash
   npm run dev
   ```

2. **Open the browser:**
   ```
   http://localhost:5173/
   ```

3. **You should see:**
   ```
   🏠 Welcome to My First SPA
   This is the home page.
   If you see this, React Router works! 🎉
   ```

---

## 🎨 Adding a Bit of Polish

Let's add some basic styling to `Home.jsx`:

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
      <h2>Welcome to My First SPA</h2>
      <p>This is the home page.</p>
      <p style={{ 
        backgroundColor: '#4CAF50', 
        color: 'white', 
        padding: '10px',
        borderRadius: '5px',
        display: 'inline-block'
      }}>
        ✅ React Router is working correctly
      </p>
    </div>
  );
}

export default Home;
```

---

## 🔍 Inspecting with DevTools

Open DevTools (F12) and check:

### 1. Elements tab

You'll see there's only ONE `div id="root"`:

```html
<div id="root">
  <div style="text-align: center...">
    <h1>🏠</h1>
    <h2>Welcome to My First SPA</h2>
    ...
  </div>
</div>
```

### 2. Network tab

- Reload the page (Ctrl+R / Cmd+R)
- You'll see it downloads `index.html` and JS files
- Now don't do anything else
- **Notice:** NO new HTTP requests

This confirms it's a SPA — everything is loaded.

### 3. URL in the browser bar

It should say:
```
http://localhost:5173/
```

The trailing `/` is the `path="/"` from your route.

---

## 🧩 Experiments to Build Intuition

### Experiment 1: What happens when you visit a route that doesn't exist?

In your browser, type:
```
http://localhost:5173/no-existe
```

**Result:** Blank page.

**Why?** There's no `<Route path="/no-existe">`, so React Router doesn't know what to render.

### Experiment 2: Change the path

Edit `App.jsx`:

```jsx
<Route path="/inicio" element={<Home />} />
```

Now visit:
- `http://localhost:5173/` → Blank page
- `http://localhost:5173/inicio` → Works!

**Takeaway:** `path` determines WHICH URL renders the component.

### Experiment 3: Multiple routes for the same component

```jsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/inicio" element={<Home />} />
  <Route path="/home" element={<Home />} />
</Routes>
```

Now ALL of these URLs render `<Home />`:
- `/`
- `/inicio`
- `/home`

---

## ⚠️ Common Mistakes

### Mistake 1: Forgetting BrowserRouter

```jsx
// ❌ BAD
function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}
```

**Console error:**
```
useRoutes() may be used only in the context of a <Router> component.
```

**Fix:** Always wrap in `<BrowserRouter>`.

### Mistake 2: Old syntax (React Router v5)

```jsx
// ❌ BAD (old syntax)
<Route path="/" component={Home} />

// ✅ GOOD (React Router v6)
<Route path="/" element={<Home />} />
```

### Mistake 3: Routes outside of `<Routes>`

```jsx
// ❌ BAD
<BrowserRouter>
  <Route path="/" element={<Home />} />
</BrowserRouter>

// ✅ GOOD
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
  </Routes>
</BrowserRouter>
```

---

## ✏️ Practice Exercise

### Exercise 1: Create a second page

1. Create `src/pages/About.jsx`:

```jsx
function About() {
  return (
    <div style={{ padding: '50px', backgroundColor: '#e3f2fd' }}>
      <h1>📖 About Us</h1>
      <p>This is the About page.</p>
    </div>
  );
}

export default About;
```

2. Add it to the router in `App.jsx`:

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

3. Visit manually in the browser:
   - `http://localhost:5173/` → Renders Home
   - `http://localhost:5173/about` → Renders About

**Congrats!** You have two "pages" working.

**But there's a problem:** How do you navigate between them without typing the URL?

**→ We'll cover that in Step 3 with `<Link>`.**

---

## 📝 Summary

| Concept | What it does |
|----------|----------|
| `BrowserRouter` | The router's main container |
| `Routes` | Groups all routes |
| `Route` | Defines an individual route |
| `path` | The URL that activates the route |
| `element` | The component that renders |

### Minimal React Router code:

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

<BrowserRouter>
  <Routes>
    <Route path="/" element={<MyComponent />} />
  </Routes>
</BrowserRouter>
```

---

## ✅ Checklist

Before moving on to Step 3:

- [ ] I installed `react-router-dom` correctly
- [ ] I have `BrowserRouter` wrapping everything
- [ ] I have `Routes` inside `BrowserRouter`
- [ ] I have at least one working `Route`
- [ ] I understand what `path` and `element` do
- [ ] I can create new pages and add them to the router

---

## 🚀 Next Step

You now know how to create routes, but **you can't navigate** between them easily.

**→ In Step 3 we'll learn to use `<Link>` to navigate via clicks.**

---

**Made with ❤️ for 4Geeks Academy - Cohort España FS PT 129**
