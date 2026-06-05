[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🔗 Step 3: Multiple Routes and Navigation

## 🎯 Goal

Build an application with **multiple pages** and learn how to navigate between them using `Link` without reloading the browser.

---

## 🤔 What Will You Learn?

In Step 2 you created ONE route. Now you'll create SEVERAL routes and navigate between them:
- Multiple page components (Home, About, Contact)
- Navigation with `<Link>`
- Creating a Navbar/navigation menu
- Active route (highlighting)

---

## 📁 Project Structure

```
src/
├── App.jsx
├── main.jsx
└── pages/
    ├── Home.jsx
    ├── About.jsx
    └── Contact.jsx
```

---

## 🔧 Step 1: Create the Page Components

### pages/Home.jsx

```jsx
function Home() {
  return (
    <div>
      <h1>🏠 Home</h1>
      <p>Welcome to the main page</p>
    </div>
  );
}

export default Home;
```

### pages/About.jsx

```jsx
function About() {
  return (
    <div>
      <h1>ℹ️ About</h1>
      <p>This is the about us page</p>
      <h2>Our Mission</h2>
      <p>Teach React Router incrementally and in a practical way</p>
    </div>
  );
}

export default About;
```

### pages/Contact.jsx

```jsx
function Contact() {
  return (
    <div>
      <h1>📧 Contact</h1>
      <p>Got questions? Reach out:</p>
      <ul>
        <li>Email: hello@example.com</li>
        <li>Phone: 555-0123</li>
        <li>Address: 123 Main Street</li>
      </ul>
    </div>
  );
}

export default Contact;
```

---

## 🔧 Step 2: Configure the Routes in App.jsx

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Testing the Routes

Now you can manually visit:
- `http://localhost:5173/` → Home
- `http://localhost:5173/about` → About
- `http://localhost:5173/contact` → Contact

**Problem**: You have to type the URL manually! You need a navigation menu.

---

## 🔧 Step 3: Build a Navbar with Links

### ⚠️ Important Difference

```jsx
// ❌ BAD: Reloads the whole page
<a href="/about">About</a>

// ✅ GOOD: Navigation without reload (SPA)
<Link to="/about">About</Link>
```

### components/Navbar.jsx

```jsx
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ 
      padding: '1rem',
      backgroundColor: '#333',
      color: 'white'
    }}>
      <ul style={{ 
        display: 'flex',
        gap: '1rem',
        listStyle: 'none',
        margin: 0,
        padding: 0
      }}>
        <li><Link to="/" style={{ color: 'white' }}>Home</Link></li>
        <li><Link to="/about" style={{ color: 'white' }}>About</Link></li>
        <li><Link to="/contact" style={{ color: 'white' }}>Contact</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

---

## 🔧 Step 4: Add the Navbar to the App

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <BrowserRouter>
      {/* Navbar OUTSIDE Routes so it shows on every page */}
      <Navbar />
      
      <div style={{ padding: '2rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
```

**Important**: The Navbar lives OUTSIDE `<Routes>`, so it shows on every page.

---

## 🎨 Highlight the Active Link with NavLink

`NavLink` is like `Link` but with superpowers: it can apply styles when active.

### components/Navbar.jsx (improved)

```jsx
import { NavLink } from 'react-router-dom';

function Navbar() {
  // Function to compute styles based on active state
  const getNavLinkStyle = ({ isActive }) => ({
    color: isActive ? 'yellow' : 'white',
    fontWeight: isActive ? 'bold' : 'normal',
    textDecoration: 'none'
  });

  return (
    <nav style={{ 
      padding: '1rem',
      backgroundColor: '#333',
      color: 'white'
    }}>
      <ul style={{ 
        display: 'flex',
        gap: '1rem',
        listStyle: 'none',
        margin: 0,
        padding: 0
      }}>
        <li>
          <NavLink to="/" style={getNavLinkStyle}>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/about" style={getNavLinkStyle}>
            About
          </NavLink>
        </li>
        <li>
          <NavLink to="/contact" style={getNavLinkStyle}>
            Contact
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

Now the link for the current page shows in yellow and bold.

---

## 💡 Links Inside Pages

You can place `<Link>` anywhere, not only in the Navbar:

### pages/Home.jsx (improved)

```jsx
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>🏠 Home</h1>
      <p>Welcome to the main page</p>
      
      <div style={{ marginTop: '2rem' }}>
        <h2>Explore:</h2>
        <ul>
          <li><Link to="/about">Learn more about us</Link></li>
          <li><Link to="/contact">Get in touch</Link></li>
        </ul>
      </div>
    </div>
  );
}

export default Home;
```

---

## 🎯 Experiment: Spot the Difference

### Test 1: With <Link> (SPA)
1. Open DevTools (F12) → Network tab
2. Click "About" in the navbar
3. **Notice**: The page doesn't reload! No new HTTP requests

### Test 2: With <a href> (traditional)
1. Temporarily swap a `<Link>` for an `<a href>`
2. Click it
3. **Notice**: The page reloads completely, new HTTP requests

This shows the **magic of React Router**: instant navigation without reloads.

---

## 🎨 Modular CSS (Optional but Recommended)

Create a CSS file for the Navbar:

### Navbar.module.css

```css
.navbar {
  padding: 1rem;
  background-color: #333;
  color: white;
}

.navList {
  display: flex;
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navLink {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.navLink:hover {
  background-color: #555;
}

.navLinkActive {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}
```

### Navbar.jsx (using the CSS module)

```jsx
import { NavLink } from 'react-router-dom';
import styles from './Navbar.module.css';

function Navbar() {
  return (
    <nav className={styles.navbar}>
      <ul className={styles.navList}>
        <li>
          <NavLink 
            to="/" 
            className={({ isActive }) => 
              isActive ? `${styles.navLink} ${styles.navLinkActive}` : styles.navLink
            }
          >
            Home
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/about" 
            className={({ isActive }) => 
              isActive ? `${styles.navLink} ${styles.navLinkActive}` : styles.navLink
            }
          >
            About
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/contact" 
            className={({ isActive }) => 
              isActive ? `${styles.navLink} ${styles.navLinkActive}` : styles.navLink
            }
          >
            Contact
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

---

## 📝 Practice Exercise

Add two more pages:

### 1. "Services" page (`/services`)
- List 3-4 services you offer
- Each service with title and description

### 2. "Blog" page (`/blog`)
- List 2-3 blog posts (title + summary)
- They don't need to be clickable yet (that's the next step)

### 3. Update the Navbar
- Add links to the new pages
- Make sure the active highlight works

---

## ⚠️ Common Mistakes

### 1. Using <a> instead of <Link>

```jsx
// ❌ BAD: Reloads the page
<a href="/about">About</a>

// ✅ GOOD: SPA navigation
<Link to="/about">About</Link>
```

### 2. Putting the Navbar inside Routes

```jsx
// ❌ BAD: Navbar only shows on Home
<Routes>
  <Route path="/" element={<><Navbar /><Home /></>} />
</Routes>

// ✅ GOOD: Navbar outside Routes
<Navbar />
<Routes>
  <Route path="/" element={<Home />} />
</Routes>
```

### 3. Forgetting to import Link/NavLink

```jsx
// ❌ BAD: Error — Link is not defined
<Link to="/">Home</Link>

// ✅ GOOD
import { Link } from 'react-router-dom';
```

---

## 🔗 Resources

### Official Documentation
- [Link - React Router](https://reactrouter.com/en/main/components/link)
- [NavLink - React Router](https://reactrouter.com/en/main/components/nav-link)

### 4Geeks Academy
- [Routing our Views with React Router](https://4geeks.com/lesson/routing-our-views-with-react-router)

---

## ✅ Summary

### Before moving on, you should understand:

- ✅ You can have multiple `<Route>` components inside `<Routes>`
- ✅ `<Link to="/path">` navigates without reload
- ✅ `<NavLink>` lets you highlight the active link
- ✅ Components outside `<Routes>` show on every page
- ✅ Navigation is instant (no HTTP requests)

### Next Step

In **Step 4** you'll learn to use **dynamic parameters** in URLs, like `/blog/123` or `/user/juan`.

---

**Practice navigating without reloads! 🚀**
