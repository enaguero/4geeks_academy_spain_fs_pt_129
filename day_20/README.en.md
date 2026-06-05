[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧭 Day 20: React Router + Global State Management

## 🎯 Learning Objectives

Today you'll learn how to build **complete, professional React applications** with navigation and global state management. The key concepts are:

### Part 1: Navigation (React Router)
- **SPA (Single Page Application)**: Understand what it is and how it works
- **React Router**: The standard library for navigation in React
- **Routes**: Define different "pages" in your application
- **Dynamic parameters**: URLs with variables (e.g., `/user/123`)

### Part 2: Complex State (useReducer)
- **useReducer Hook**: An alternative to useState for complex state
- **Reducers and Actions**: A predictable pattern for managing state
- **When to use useReducer**: vs useState

### Part 3: Global State (Context API)
- **Context API**: Share state between components without prop drilling
- **Provider and Consumer**: The context pattern in React
- **useContext Hook**: Easily access the context

### Part 4: Integration
- **Store Pattern**: Combine useReducer + Context for global state
- **Router + Context**: Integrate navigation with shared state
- **Real Project**: Contact List App with full CRUD

## 📚 Day Structure

This day has **10 progressive steps**, each building on the previous one:

---

## 👉 PART 1: React Router (Steps 1-4)

### Step 1: What is a SPA? 📖
**Folder**: `step1-que-es-spa/`

Understand the Single Page Application concept without writing code yet.

**Concepts**:
- Traditional web vs SPA
- Pros and cons
- Why React needs a router
- The office building analogy

---

### Step 2: First Basic Route 🚀
**Folder**: `step2-primera-ruta/`

Build your first app with React Router — as simple as possible.

**Concepts**:
- Installing react-router-dom
- BrowserRouter (the main container)
- Configuring a basic route
- Your first "page" in React

---

### Step 3: Multiple Routes and Navigation 🔗
**Folder**: `step3-multiples-rutas/`

Add several pages and navigate between them.

**Concepts**:
- Routes and Route
- The Link component
- Creating a Navbar/navigation menu
- Pages: Home, About, Contact

---

### Step 4: URL Parameters 🔢
**Folder**: `step4-parametros-url/`

Create dynamic routes with variable parameters.

**Concepts**:
- Routes with parameters: `/user/:id`
- The useParams hook
- Detail pages (product, user, post)
- Basic query strings

---

## 👉 PART 2: useState vs useReducer (Steps 5-6)

### Step 5: Introduction to useReducer 🧠
**Folder**: `step5-intro-usereducer/`

What is useReducer? When should you use it instead of useState?

**Concepts**:
- What useReducer is
- Differences from useState
- When to use each
- Example: a counter with useReducer
- Actions and the reducer function
- Pattern: `dispatch({ type: 'ACTION', payload: data })`

---

### Step 6: useReducer for Complex State 📦
**Folder**: `step6-usereducer-complejo/`

Use useReducer to handle complex state with multiple actions.

**Concepts**:
- Todo list with useReducer
- Multiple action types (ADD, DELETE, TOGGLE, EDIT)
- Switch statements in reducers
- Advantages over multiple useState calls
- More predictable and testable code

---

## 👉 PART 3: Context API (Step 7)

### Step 7: Context API — Global State 🌐
**Folder**: `step7-context-api/`

Solve the "prop drilling" problem with the Context API.

**Concepts**:
- What prop drilling is and why it's a problem
- createContext
- Context.Provider
- The useContext hook
- Sharing state between distant components
- Example: global dark/light theme

---

## 👉 PART 4: Integration (Steps 8-10)

### Step 8: useReducer + Context = Store 🏪
**Folder**: `step8-usereducer-context-store/`

Combine useReducer with Context to create a global "store" (a pattern similar to Redux).

**Concepts**:
- Combining useReducer + Context
- Creating a global store
- A Provider with dispatch available globally
- Example: a global shopping cart
- Centralized actions
- State accessible from any component

---

### Step 9: Router + Context Together 🔗🌐
**Folder**: `step9-router-context-integracion/`

Integrate navigation (Router) with global state (Context).

**Concepts**:
- Sharing state between different pages/routes
- useNavigate with Context
- Programmatic navigation from actions
- Example: app with simulated authentication
- Login, logout, protected routes

---

### Step 10: Contact List App Project 📞
**Folder**: `step10-proyecto-contact-list/`

YOUR PROJECT! A complete app using EVERYTHING you've learned.

**⚠️ IMPORTANT**: This step does NOT include a solved version. It only has:
- Project description
- Functional requirements
- Suggested structure
- Documentation references
- Mockup/wireframe

**You have to build it** applying:
- ✅ React Router (multiple pages)
- ✅ Context API (global state)
- ✅ useReducer (contact management)
- ✅ Full CRUD (Create, Read, Update, Delete)
- ✅ Forms
- ✅ Validations
- ✅ Programmatic navigation

---

## 🚀 How to Use This Material

### 1. Follow STRICT order
This day is **very progressive**. Each step builds on the previous one:
- Steps 1-4: Learn Router
- Steps 5-6: Learn useReducer
- Step 7: Learn Context
- Steps 8-9: Integrate everything
- Step 10: Final project (you build it)

### 2. Don't skip the theory
Steps 1, 5, and 7 are more theoretical but **essential** for understanding the rest.

### 3. Experiment and break things
- Open DevTools (F12) while navigating
- Modify the example code
- Try things you think won't work
- Read the errors in the console

### 4. Don't move on if you don't understand
If something doesn't make sense in a step, **stop**. Review, ask, experiment. Don't continue without understanding it.

## 🔗 Before You Start: Prerequisites

You should be comfortable with:
- ✅ React components
- ✅ Props
- ✅ useState
- ✅ React project structure

If you don't have a solid grasp of these concepts, **review days 15-17 first**.

## 📖 Recommended Reading

### From 4Geeks Academy
- [React Router Tutorial](https://4geeks.com/lesson/routing-our-views-with-react-router)
- [What is a Single Page Application](https://4geeks.com/lesson/what-is-a-single-page-application-spa)

### Official Documentation
- [React Router v6 - Getting Started](https://reactrouter.com/en/main/start/tutorial)
- [React Router v6 - Overview](https://reactrouter.com/en/main/start/overview)

### Recommended Videos
- [React Router in 100 Seconds](https://www.youtube.com/watch?v=Ul3y1LXxzdU)
- [React Router v6 Tutorial](https://www.youtube.com/watch?v=59IXY5IDrBA)

## 🎯 Final Project: Contact List App

You'll build a complete contact management app with:

### Required Features
✅ **Contact list** — view all contacts  
✅ **Add contact** — a form to create new contacts  
✅ **View detail** — an individual page for each contact  
✅ **Edit contact** — modify existing information  
✅ **Delete contact** — with confirmation  
✅ **Navigation** — between all views with no reloads  
✅ **Global state** — contacts accessible from any component  
✅ **Validations** — forms with validation  

### Technologies You'll Use
- 🔗 **React Router** — navigation between views
- 🌐 **Context API** — share state
- 🧠 **useReducer** — manage CRUD operations
- 📝 **Forms** — controlled inputs
- 🎨 **CSS** — professional design

Step 10 will give you all the info you need, but **you have to implement it**.

## 💡 Key Concepts to Understand

### Critical Difference
```
Traditional website:
- Click on link → Browser downloads new HTML → Page reloads
- Each page = a different HTML file

React Router (SPA):
- Click on link → JavaScript swaps the component → NO reload
- All "pages" = JavaScript components in a single HTML file
```

### Main React Router Components

| Component | Purpose | Analogy |
|------------|-----------|----------|
| `BrowserRouter` | Overall container | The entire building |
| `Routes` | Route container | The building directory |
| `Route` | A specific route | An office in the building |
| `Link` | Navigation link | Elevator between floors |
| `useParams` | Read URL parameters | Read the office number |
| `useNavigate` | Navigate programmatically | A GPS that takes you there automatically |

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

// ✅ GOOD
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

### Mistake 2: Using <a> instead of <Link>
```jsx
// ❌ BAD — reloads the page
<a href="/about">About</a>

// ✅ GOOD — navigation without reload
<Link to="/about">About</Link>
```

### Mistake 3: Not using element={} on Route
```jsx
// ❌ BAD (old React Router v5 syntax)
<Route path="/about" component={About} />

// ✅ GOOD (React Router v6)
<Route path="/about" element={<About />} />
```

### Mistake 4: Routes outside <Routes>
```jsx
// ❌ BAD
<BrowserRouter>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
</BrowserRouter>

// ✅ GOOD
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
  </Routes>
</BrowserRouter>
```

## 🆘 Need Help?

1. Read the tutorial step by step (really, read it!)
2. Open DevTools (F12) to see what's going on
3. Verify you installed `react-router-dom` correctly
4. Make sure you're using React Router v6
5. Ask in the Slack channel

## 📊 Progress

Check off each step as you complete it:

### Part 1: React Router
- [ ] Step 1: What is a SPA?
- [ ] Step 2: First Basic Route
- [ ] Step 3: Multiple Routes and Navigation
- [ ] Step 4: URL Parameters

### Part 2: useReducer
- [ ] Step 5: Introduction to useReducer
- [ ] Step 6: useReducer for Complex State

### Part 3: Context API
- [ ] Step 7: Context API — Global State

### Part 4: Integration
- [ ] Step 8: useReducer + Context (Store)
- [ ] Step 9: Router + Context Together
- [ ] Step 10: Contact List App Project (build it yourself)

---

## 🎯 Why Is This Day Important?

### React Router
Without a Router your React app is a single page. With Router you can build apps with multiple views, shareable URLs, and professional navigation.

### useReducer
For simple state use `useState`. But once your state gets complex (many actions, complicated logic), `useReducer` keeps your code cleaner and more maintainable.

### Context API
Avoid "prop drilling" (passing props through 5 levels of components). Context lets you share state globally in an elegant way.

### Why combine useReducer + Context?
It's the most common pattern in professional React for global state. Similar to Redux but simpler and without external libraries.

**After this day you'll be able to build complete, professional React applications.**

## 💼 Professional Use Cases

Real-world apps that need React Router:
- 🛒 E-commerce: Home, Products, Product detail, Cart, Checkout
- 📱 Social networks: Feed, Profile, Settings, Messages
- 📰 Blog: Post list, Post detail, Categories, Author
- 🏢 Dashboard: Overview, Stats, Settings, Users
- 🎓 Learning platform: Courses, Lessons, Profile, Progress

## 📝 Important Notes

### React Router Version
This tutorial uses **React Router v6** (the current, most modern version).

If you find older tutorials with different syntax (v5 or v4), **ignore them**.

### Installation
```bash
npm install react-router-dom
```

**Do NOT** install `react-router` alone (it's different).

### BrowserRouter vs HashRouter
We'll use `BrowserRouter` (the standard).

`HashRouter` uses URLs with `#` and is only for special cases.

---

**Let's navigate! 🚀**

React Router is one of the most important skills in professional React development. After this day, your applications will feel like real websites with multiple pages.

**Take your time, read everything, experiment, and have fun building.**

---

**Made with ❤️ for 4Geeks Academy - Cohort España FS PT 129**
