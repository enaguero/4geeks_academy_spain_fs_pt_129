[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 📡 Day 19: TodoList with React and Fetch

## 🎯 Learning Objectives

Today you'll learn how to connect your React application with real APIs using Fetch. The key concepts are:

- **API and JSON**: What they are and why they exist
- **HTTP**: Communication protocol and methods (GET, POST, PUT, DELETE)
- **REST**: Architecture for designing APIs
- **Synchronous vs Asynchronous**: Fundamental concepts of asynchronous programming
- **setTimeout**: First async tool in JavaScript
- **Callbacks**: Functions that run after something
- **Callback Hell**: The problem that Promises solve
- **Promises**: Understanding promises in JavaScript
- **Async/Await**: Modern syntax for asynchronous code
- **Fetch API**: Making HTTP requests from React
- **REST APIs**: Concepts and how to consume them
- **Integration**: Combining Fetch with useState and useEffect
- **Real Project**: TodoList that persists data on a server

---

## 🔗 How Does It All Connect?

This is the complete picture of what you'll learn today:

```
┌─────────────────────────────────────────────┐
│ 1. API (Application Programming Interface) │
│    └─> Contract between applications       │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. REST (Representational State Transfer)  │
│    └─> Architectural style for APIs        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. HTTP (Communication protocol)           │
│    └─> GET, POST, PUT, DELETE              │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. JSON (Data format)                      │
│    └─> Common language between client/srv  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. Fetch API (JavaScript tool)             │
│    └─> Consumes everything above           │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 6. React + Hooks                            │
│    └─> Integrates Fetch into your UI       │
└─────────────────────────────────────────────┘
```

**In short:** You'll use **Fetch** (JavaScript) to send **HTTP** requests (GET/POST/PUT/DELETE) to a **REST API**, exchanging data in **JSON** format.

## 📚 Structure of the Day

This day has **10 progressive steps**, each one building on the previous. Following the order is essential.

### Step 0: Fundamental Concepts 🌐
**Folder**: `step0-conceptos-fundamentales/`

**START HERE!** Before touching any code, understand what an API, JSON, HTTP and REST are.

**Concepts**:
- What an API is
- What JSON is and how it works
- HTTP: Protocol and methods (GET, POST, PUT, DELETE)
- REST: API architecture
- How everything connects

---

### Step 1: Synchronous vs Asynchronous 🔄
**Folder**: `step1-sync-async/`

Understand the fundamental concepts of synchronous and asynchronous code.

**Concepts**:
- What synchronous (blocking) code is
- What asynchronous (non-blocking) code is
- Real-life examples
- Why JavaScript needs asynchrony

---

### Step 2: setTimeout - Your First Async Tool ⏱️
**Folder**: `step2-settimeout/`

Learn how to use setTimeout and setInterval.

**Concepts**:
- setTimeout and setInterval
- clearTimeout and clearInterval
- Basic Event Loop
- Call Stack and Task Queue

---

### Step 3: Callbacks and "Callback Hell" 🔥
**Folder**: `step3-callbacks-hell/`

Understand what callbacks are and the problem they cause.

**Concepts**:
- What a callback is
- Nested callbacks
- The "Callback Hell" problem
- Why we need Promises

---

### Step 4: Promises - The Solution 🤝
**Folder**: `step4-promises/`

Learn how Promises solve Callback Hell.

**Concepts**:
- What a Promise is
- States: pending, resolved, rejected
- then(), catch(), finally()
- Promise chaining

---

### Step 5: Async/Await ⏳
**Folder**: `step5-async-await/`

Modern, more readable syntax on top of Promises.

**Concepts**:
- async function
- await keyword
- Try/catch for errors
- Advantages over .then()

---

### Step 6: Fetch API 🌐
**Folder**: `step6-fetch-api/`

Make HTTP requests using Fetch.

**Concepts**:
- fetch() syntax
- GET vs POST vs PUT vs DELETE
- Headers and body
- Response and .json()

---

### Step 7: REST APIs 🏭️
**Folder**: `step7-rest-apis/`

Understand what REST APIs are and how they work.

**Concepts**:
- What REST is
- HTTP methods
- Status codes
- Resources and endpoints

---

### Step 8: Fetch with React 🚀
**Folder**: `step8-fetch-react/`

Integrate Fetch with React hooks.

**Concepts**:
- Fetch inside useEffect
- Handling states: loading, data, error
- Avoiding race conditions
- Cleanup in fetch

---

### Step 9: TodoList with API 💾
**Folder**: `step9-todolist-api/`

Build a complete TodoList that consumes an API.

**Concepts**:
- CRUD operations with Fetch
- Syncing state with the server
- Error handling
- Full project

---

## 🚀 How to Use This Material

### 1. Follow the order
Each step depends on the previous one. Don't skip steps.

### 2. Practice with real APIs
We'll use public APIs to learn without needing your own server.

### 3. Experiment
Modify examples, try different endpoints, break things on purpose and fix them.

### 4. Understand, don't memorize
Aim to understand *why* it works, not just *how*.

## 🔗 Recommended APIs to Practice With

- **JSONPlaceholder**: https://jsonplaceholder.typicode.com/ (Free fake API)
- **OpenWeather**: Weather API (requires free key)
- **GitHub API**: https://api.github.com
- **PokéAPI**: https://pokeapi.co/

## 📖 Recommended Reading

### From 4Geeks Academy
- [Creating asynchronous algorithms](https://4geeks.com/syllabus/spain-fs-pt-129/read/asynchronous-algorithms-async-await)
- [The Fetch API](https://4geeks.com/syllabus/spain-fs-pt-129/read/the-fetch-javascript-api)
- [Understanding REST APIs](https://4geeks.com/syllabus/spain-fs-pt-129/read/understanding-rest-apis)

### MDN
- [Promises](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Async/Await](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/async_function)
- [Fetch API](https://developer.mozilla.org/es/docs/Web/API/Fetch_API)

## 🎓 Final Project

**TodoList Application with API**

You'll build a TodoList that:

✅ Loads tasks from a server  
✅ Adds new tasks to the API  
✅ Updates existing tasks  
✅ Deletes tasks from the server  
✅ Shows loading state  
✅ Handles errors properly  
✅ Syncs with localStorage as a fallback  

## 💡 Important Tips

### For Beginners

1. **Follow the order**: The 10 steps are designed for incremental learning
2. **Understand the basics first**: Synchronous vs Asynchronous before Promises
3. **Practice with the examples**: Copy and run the code in your browser
4. **Use Dev Tools**: Open the console and Network tab to see the requests
5. **Handle errors**: Always include try/catch or .catch()
6. **UI states**: Loading, success, error are essential
7. **Inspect APIs**: Use tools like Postman or the browser

### Critical Concepts

- **Synchronous vs Asynchronous**: The foundation of everything else
- **Event Loop**: How JavaScript handles async operations
- **Callback Hell**: Why Promises exist
- **Asynchrony**: Code keeps running while waiting for the response
- **States**: Your component can be in loading, success or error
- **CORS**: Some problems come from origin policies
- **Timeouts**: Requests can fail or take time

## ⚠️ Common Mistakes

### Mistake 1: Not handling errors
```javascript
// ❌ BAD
fetch(url).then(r => r.json()).then(data => setData(data));

// ✅ GOOD
try {
  const res = await fetch(url);
  const data = await res.json();
  setData(data);
} catch (error) {
  setError(error);
}
```

### Mistake 2: Fetching on every render
```javascript
// ❌ BAD
function Component() {
  const data = fetch(url); // Runs on every render
}

// ✅ GOOD
useEffect(() => {
  fetch(url).then(...);
}, []); // Runs only once
```

### Mistake 3: Not cleaning up on unmount
```javascript
// ❌ BAD
useEffect(() => {
  fetch(url); // If the component unmounts, you get an error
});

// ✅ GOOD
useEffect(() => {
  let isMounted = true;
  fetch(url).then(data => {
    if (isMounted) setData(data);
  });
  return () => { isMounted = false; };
}, []);
```

## 🆘 Need Help?

1. Read the tutorial step by step
2. Open the browser console (F12)
3. Check the Network tab to see the requests
4. Search for the specific error on Google
5. Ask in the Slack channel

## 📊 Progress

Check off each step as you complete it:

- [ ] Step 0: Fundamental Concepts (API, JSON, HTTP, REST)
- [ ] Step 1: Synchronous vs Asynchronous
- [ ] Step 2: setTimeout and setInterval
- [ ] Step 3: Callbacks and Callback Hell
- [ ] Step 4: Promises
- [ ] Step 5: Async/Await
- [ ] Step 6: Fetch API
- [ ] Step 7: REST APIs
- [ ] Step 8: Fetch with React
- [ ] Step 9: TodoList with API
- [ ] Final Project: Complete TodoList

---

**Let's connect with the world! 🌍**

Today we cross the line between local apps and real applications that talk to servers. It's an exciting moment — you're building professional applications.
