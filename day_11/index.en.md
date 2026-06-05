[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 11: The DOM and Events in JavaScript

## What Is the DOM?

Imagine your web page is a house. The **DOM** (Document Object Model) is like a detailed blueprint of that house that JavaScript can read and modify.

**DOM = Document Object Model**

It's a **tree-shaped** representation of your HTML document that JavaScript can manipulate.

### Analogy: The DOM as a Family Tree

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My Page</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <p>This is a paragraph</p>
    </body>
</html>
```

The browser turns this into a tree:

```
document
  └── html
      ├── head
      │   └── title
      │       └── "My Page"
      └── body
          ├── h1
          │   └── "Welcome"
          └── p
              └── "This is a paragraph"
```

### Why Is the DOM Important?

| Without DOM | With DOM |
|-------------|----------|
| Static pages | Dynamic pages |
| No interaction | Reacts to user actions |
| Fixed content | Content that changes |
| Boring 😴 | Interactive 🎮 |

**The DOM lets you:**
- ✅ Change the page content
- ✅ Change CSS styles
- ✅ Add or remove elements
- ✅ Respond to user actions (clicks, keystrokes, etc.)
- ✅ Build interactive web applications

---

## DOM Structure: The Nodes

The DOM is made up of **nodes**. There are several types:

### Types of Nodes

```html
<div id="container" class="box">
    Hello world
    <span>Text inside span</span>
</div>
```

| Type | Example | Description |
|------|---------|-------------|
| **Element Node** | `<div>`, `<span>` | HTML tags |
| **Text Node** | `"Hello world"` | Text inside elements |
| **Attribute Node** | `id="container"` | Element attributes |
| **Document Node** | `document` | Root of the tree |

### Relationships in the DOM: Node Family

```html
<div id="parent">
    <h1 id="sibling1">Title</h1>
    <p id="sibling2">Paragraph</p>
</div>
```

```
     #parent (parent)
        |
    ----+----
    |       |
#sibling1  #sibling2
(sibling)  (sibling)
(child)    (child)
```

- **Parent**: `<div>` is the parent of `<h1>` and `<p>`
- **Children**: `<h1>` and `<p>` are children of `<div>`
- **Siblings**: `<h1>` and `<p>` are siblings of each other

---

## Accessing DOM Elements

JavaScript offers several methods to "find" elements in the DOM.

### 1. `getElementById()` — By ID (Unique)

```html
<h1 id="title">Hello World</h1>
<p id="description">This is a paragraph</p>
```

```javascript
// Get element by its ID
const title = document.getElementById('title');
console.log(title);  // <h1 id="title">Hello World</h1>

const description = document.getElementById('description');
console.log(description.textContent);  // "This is a paragraph"
```

**Advantages:**
- ✅ Very fast
- ✅ Returns ONE element
- ✅ Easy to use

**Limitation:**
- ⚠️ Only works with IDs (which must be unique)

### 2. `getElementsByClassName()` — By Class

```html
<p class="featured">Paragraph 1</p>
<p class="featured">Paragraph 2</p>
<p class="normal">Paragraph 3</p>
```

```javascript
// Get ALL elements with that class
const featured = document.getElementsByClassName('featured');

console.log(featured.length);  // 2

// It's a collection (like an array)
console.log(featured[0].textContent);  // "Paragraph 1"
console.log(featured[1].textContent);  // "Paragraph 2"

// Loop through all elements
for (let i = 0; i < featured.length; i++) {
    console.log(featured[i].textContent);
}
```

**Advantages:**
- ✅ Finds multiple elements at once
- ✅ Useful for elements with the same class

**Note:**
- ⚠️ Returns an **HTMLCollection** (similar to an array, but not a real array)

### 3. `getElementsByTagName()` — By Tag

```html
<p>Paragraph 1</p>
<p>Paragraph 2</p>
<div>A div</div>
```

```javascript
// Get ALL <p> elements
const paragraphs = document.getElementsByTagName('p');

console.log(paragraphs.length);  // 2

for (let i = 0; i < paragraphs.length; i++) {
    console.log(paragraphs[i].textContent);
}

// Get ALL divs
const divs = document.getElementsByTagName('div');
console.log(divs.length);  // 1
```

### 4. `querySelector()` — CSS Selector (Modern) ✨

```html
<div class="container">
    <h1 id="title">My Title</h1>
    <p class="text">First paragraph</p>
    <p class="text important">Second paragraph</p>
</div>
```

```javascript
// Using CSS selectors (returns THE FIRST one found)
const title = document.querySelector('#title');  // By ID
const firstText = document.querySelector('.text');  // By class
const firstParagraph = document.querySelector('p');  // By tag

// More complex selectors
const importantText = document.querySelector('.text.important');
const paragraphInContainer = document.querySelector('.container p');
```

**Advantages:**
- ✅ CSS syntax (very familiar)
- ✅ Very flexible and powerful
- ✅ Returns ONE element (the first)

### 5. `querySelectorAll()` — All Elements (Modern) ✨

```html
<p class="item">Item 1</p>
<p class="item">Item 2</p>
<p class="item">Item 3</p>
```

```javascript
// Get ALL elements that match
const items = document.querySelectorAll('.item');

console.log(items.length);  // 3

// Returns a NodeList (you can use forEach)
items.forEach(function(item, index) {
    console.log(`Item ${index}: ${item.textContent}`);
});

// Also with arrow function
items.forEach((item, index) => {
    console.log(`Item ${index}: ${item.textContent}`);
});
```

**Advantages:**
- ✅ CSS syntax
- ✅ Returns ALL elements
- ✅ You can use `.forEach()`

### Method Comparison Table

| Method | Returns | Syntax | Speed | Recommendation |
|--------|---------|--------|-------|----------------|
| `getElementById()` | 1 element | `getElementById('id')` | Very fast | ✅ When you have ID |
| `getElementsByClassName()` | Collection | `getElementsByClassName('class')` | Fast | ⚠️ Better to use querySelector |
| `getElementsByTagName()` | Collection | `getElementsByTagName('tag')` | Fast | ⚠️ Better to use querySelector |
| `querySelector()` | 1 element | `querySelector('selector')` | Normal | ✅✅ **Recommended** |
| `querySelectorAll()` | NodeList | `querySelectorAll('selector')` | Normal | ✅✅ **Recommended** |

### Practical Selector Examples

```javascript
// By ID
document.querySelector('#myId')

// By class
document.querySelector('.myClass')

// By tag
document.querySelector('p')

// Combinations
document.querySelector('div.container')  // div WITH class container
document.querySelector('.container p')   // p INSIDE .container
document.querySelector('p.featured')     // p WITH class featured

// Pseudo-classes
document.querySelector('p:first-child')  // First p
document.querySelector('li:nth-child(2)') // Second li

// Attributes
document.querySelector('[type="text"]')  // Elements with type="text"
document.querySelector('input[name="email"]')  // Input with name="email"
```

---

## Manipulating Content: innerHTML vs textContent

Once you have an element, you can change its content.

### `textContent` — Text Only

```html
<p id="paragraph">Original text</p>
```

```javascript
const paragraph = document.getElementById('paragraph');

// Read the text
console.log(paragraph.textContent);  // "Original text"

// Change the text
paragraph.textContent = "New text";
// Result: <p id="paragraph">New text</p>

// If you try HTML, it's shown as text
paragraph.textContent = "<strong>Bold</strong>";
// Result: <p id="paragraph">&lt;strong&gt;Bold&lt;/strong&gt;</p>
```

### `innerHTML` — Full HTML

```html
<div id="container">Original content</div>
```

```javascript
const container = document.getElementById('container');

// Read the HTML
console.log(container.innerHTML);  // "Original content"

// Change with HTML
container.innerHTML = "<strong>Bold text</strong>";
// Result: <div id="container"><strong>Bold text</strong></div>

// Add complex elements
container.innerHTML = `
    <h2>New Title</h2>
    <p>Paragraph with <em>emphasis</em></p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
`;
```

### Template Strings with innerHTML

**Template strings** (using backticks \`) are perfect for creating dynamic HTML:

```javascript
const name = "Ana";
const age = 25;
const city = "Madrid";

const container = document.getElementById('profile');

// ✅ Using template strings
container.innerHTML = `
    <div class="card">
        <h2>${name}'s Profile</h2>
        <p>Age: ${age} years old</p>
        <p>City: ${city}</p>
        <button>Contact</button>
    </div>
`;
```

### Practical Example: Product List

```html
<div id="products"></div>
```

```javascript
const products = [
    { name: "Laptop", price: 999 },
    { name: "Mouse", price: 25 },
    { name: "Keyboard", price: 75 }
];

const container = document.getElementById('products');

// Build HTML dynamically
let html = '<ul class="product-list">';

products.forEach(product => {
    html += `
        <li class="product">
            <span class="name">${product.name}</span>
            <span class="price">$${product.price}</span>
        </li>
    `;
});

html += '</ul>';

container.innerHTML = html;
```

**Result:**
```html
<div id="products">
    <ul class="product-list">
        <li class="product">
            <span class="name">Laptop</span>
            <span class="price">$999</span>
        </li>
        <li class="product">
            <span class="name">Mouse</span>
            <span class="price">$25</span>
        </li>
        <li class="product">
            <span class="name">Keyboard</span>
            <span class="price">$75</span>
        </li>
    </ul>
</div>
```

### Comparison: textContent vs innerHTML

| Aspect | `textContent` | `innerHTML` |
|--------|---------------|-------------|
| **Content** | Plain text only | Full HTML |
| **HTML tags** | Shown as text | Interpreted as HTML |
| **Security** | ✅ Safe | ⚠️ XSS risk with user data |
| **Speed** | Faster | Slower (parses HTML) |
| **Typical use** | Change simple text | Build HTML structures |

### ⚠️ Security Warning

```javascript
// ❌ DANGEROUS: Don't do this with user data
const userInput = "<script>alert('Hacked!')</script>";
container.innerHTML = userInput;  // Executes the script!

// ✅ SAFE: Use textContent for user data
container.textContent = userInput;  // Shows it as text
```

---

## What Is an Event?

An **event** is something that happens on your web page. It's like ringing a doorbell — someone responds.

### Common Event Examples

| Event | When It Happens | Example |
|-------|----------------|---------|
| **click** | User clicks | Button pressed |
| **change** | Input value changes | Selecting an option in a select |
| **input** | User types in an input | Each keystroke |
| **submit** | Form is submitted | Clicking "Submit" |
| **load** | Page/image finishes loading | Page ready |
| **keydown** | User presses a key | Typing in input |
| **mouseover** | Mouse enters an element | Hover over button |
| **mouseout** | Mouse leaves an element | Stop hovering |

### Anatomy of an Event

```javascript
element.addEventListener('event-type', function() {
    // Code that runs when the event happens
});
```

**Parts:**
1. **Element**: The HTML element that listens for the event
2. **Event type**: Which event to wait for (click, change, etc.)
3. **Function**: What to do when the event happens (also called "event handler")

---

## The `load` Event — Wait for the Page to Load

### Why Is It Important?

If JavaScript runs BEFORE the HTML is ready, it won't find the elements:

```html
<head>
    <script>
        // ❌ BAD: This code runs BEFORE the button exists
        const button = document.getElementById('myButton');
        console.log(button);  // null — doesn't exist yet!
    </script>
</head>
<body>
    <button id="myButton">Click here</button>
</body>
```

### Solution 1: `window.onload`

```html
<head>
    <script>
        // ✅ GOOD: Wait for EVERYTHING to load
        window.onload = function() {
            const button = document.getElementById('myButton');
            console.log(button);  // <button id="myButton">Click here</button>
        };
    </script>
</head>
<body>
    <button id="myButton">Click here</button>
</body>
```

### Solution 2: `DOMContentLoaded` (Faster)

```html
<head>
    <script>
        // ✅ BETTER: Wait only for the DOM to load (not images)
        document.addEventListener('DOMContentLoaded', function() {
            const button = document.getElementById('myButton');
            console.log(button);  // Works!
        });
    </script>
</head>
<body>
    <button id="myButton">Click here</button>
</body>
```

### Solution 3: Script at the End of Body (Simplest)

```html
<head>
    <!-- No JavaScript here -->
</head>
<body>
    <button id="myButton">Click here</button>

    <!-- ✅ SIMPLE: Script at the end -->
    <script>
        const button = document.getElementById('myButton');
        console.log(button);  // Works because the button already exists
    </script>
</body>
```

### Solution 4: Using `defer` (Modern) ✨

```html
<head>
    <!-- ✅ MODERN: defer waits automatically -->
    <script src="app.js" defer></script>
</head>
<body>
    <button id="myButton">Click here</button>
</body>
```

```javascript
// app.js — You don't need window.onload
const button = document.getElementById('myButton');
console.log(button);  // Works!
```

### Method Comparison

| Method | When to Use | Advantage | Drawback |
|--------|-------------|-----------|----------|
| `window.onload` | You need images to load | Waits for EVERYTHING | Slower |
| `DOMContentLoaded` | You only need the HTML | Faster than onload | A bit more code |
| Script at the end | Simple projects | Very simple | HTML and JS separated |
| `defer` | Modern projects | Clean and standard | Requires external file |

---

## `onclick` Event — The Mouse Click

### Way 1: In HTML (Inline) ❌

```html
<!-- ❌ NOT RECOMMENDED: Mixes HTML with JavaScript -->
<button onclick="greet()">Greet</button>

<script>
function greet() {
    alert('Hello!');
}
</script>
```

**Drawbacks:**
- Mixes HTML with JavaScript
- Hard to maintain
- Not good practice

### Way 2: With `onclick` in JavaScript

```html
<button id="myButton">Greet</button>

<script>
const button = document.getElementById('myButton');

// Assign function to the event
button.onclick = function() {
    alert('Hello!');
};
</script>
```

**Problem:**
- You can only assign ONE function per event

### Way 3: With `addEventListener()` (Recommended) ✅

```html
<button id="myButton">Greet</button>

<script>
const button = document.getElementById('myButton');

// ✅ BETTER: addEventListener
button.addEventListener('click', function() {
    alert('Hello!');
});

// You can add multiple listeners
button.addEventListener('click', function() {
    console.log('Click registered');
});
</script>
```

**Advantages:**
- You can assign multiple functions to the same event
- It's the modern standard
- More flexible

### Complete Example: Click Counter

```html
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
</head>
<body>
    <h1>Click Counter</h1>
    <p>You have clicked <span id="counter">0</span> times</p>
    <button id="btnCount">Click Me</button>
    <button id="btnReset">Reset</button>

    <script>
        let clicks = 0;

        const counterElement = document.getElementById('counter');
        const btnCount = document.getElementById('btnCount');
        const btnReset = document.getElementById('btnReset');

        // Increment counter
        btnCount.addEventListener('click', function() {
            clicks++;
            counterElement.textContent = clicks;
        });

        // Reset counter
        btnReset.addEventListener('click', function() {
            clicks = 0;
            counterElement.textContent = clicks;
        });
    </script>
</body>
</html>
```

### Accessing Event Information

```html
<button id="myButton">Click here</button>

<script>
const button = document.getElementById('myButton');

button.addEventListener('click', function(event) {
    console.log('Clicked element:', event.target);
    console.log('Event type:', event.type);
    console.log('X coordinates:', event.clientX);
    console.log('Y coordinates:', event.clientY);
});
</script>
```

---

## `onchange` Event — Detect Changes

The `change` event fires when an input's value changes and the user **leaves the field** (blur).

### With Text Input

```html
<label>Name:</label>
<input type="text" id="name">
<p id="greeting"></p>

<script>
const nameInput = document.getElementById('name');
const greeting = document.getElementById('greeting');

nameInput.addEventListener('change', function() {
    const value = nameInput.value;
    greeting.textContent = `Hello, ${value}!`;
});
</script>
```

### With Select (Dropdown)

```html
<label>Choose your city:</label>
<select id="city">
    <option value="">Select...</option>
    <option value="madrid">Madrid</option>
    <option value="barcelona">Barcelona</option>
    <option value="valencia">Valencia</option>
</select>
<p id="result"></p>

<script>
const citySelect = document.getElementById('city');
const result = document.getElementById('result');

citySelect.addEventListener('change', function() {
    const selectedCity = citySelect.value;

    if (selectedCity) {
        result.textContent = `You selected: ${selectedCity}`;
    } else {
        result.textContent = '';
    }
});
</script>
```

### With Checkbox

```html
<label>
    <input type="checkbox" id="accept">
    I accept the terms and conditions
</label>
<button id="submit" disabled>Submit</button>

<script>
const checkbox = document.getElementById('accept');
const submitButton = document.getElementById('submit');

checkbox.addEventListener('change', function() {
    // checkbox.checked is true or false
    if (checkbox.checked) {
        submitButton.disabled = false;
        submitButton.textContent = 'Submit ✅';
    } else {
        submitButton.disabled = true;
        submitButton.textContent = 'Submit';
    }
});
</script>
```

### With Radio Buttons

```html
<p>Select your plan:</p>
<label>
    <input type="radio" name="plan" value="basic"> Basic ($10/month)
</label>
<label>
    <input type="radio" name="plan" value="premium"> Premium ($20/month)
</label>
<label>
    <input type="radio" name="plan" value="enterprise"> Enterprise ($50/month)
</label>
<p id="selectedPlan"></p>

<script>
const radios = document.querySelectorAll('input[name="plan"]');
const selectedPlan = document.getElementById('selectedPlan');

radios.forEach(radio => {
    radio.addEventListener('change', function() {
        const plan = radio.value;

        let price;
        if (plan === 'basic') price = 10;
        else if (plan === 'premium') price = 20;
        else price = 50;

        selectedPlan.innerHTML = `
            <strong>Selected plan:</strong> ${plan.toUpperCase()}<br>
            <strong>Price:</strong> $${price}/month
        `;
    });
});
</script>
```

---

## `input` Event — Detect Every Keystroke

Unlike `change`, `input` fires **on every change** (every key pressed).

```html
<label>Search:</label>
<input type="text" id="search" placeholder="Type to search...">
<p id="result"></p>

<script>
const searchInput = document.getElementById('search');
const result = document.getElementById('result');

searchInput.addEventListener('input', function() {
    const text = searchInput.value;
    result.textContent = `Searching: "${text}" (${text.length} characters)`;
});
</script>
```

### Example: Real-Time Validation

```html
<label>Password:</label>
<input type="password" id="password">
<div id="validation"></div>

<script>
const passwordInput = document.getElementById('password');
const validation = document.getElementById('validation');

passwordInput.addEventListener('input', function() {
    const password = passwordInput.value;
    const length = password.length;

    let message = '';
    let color = '';

    if (length === 0) {
        message = '';
    } else if (length < 6) {
        message = '❌ Too short (minimum 6 characters)';
        color = 'red';
    } else if (length < 10) {
        message = '⚠️ Acceptable';
        color = 'orange';
    } else {
        message = '✅ Strong';
        color = 'green';
    }

    validation.textContent = message;
    validation.style.color = color;
});
</script>
```

---

## `submit` Event — Submitting Forms

```html
<form id="myForm">
    <label>Name:</label>
    <input type="text" id="name" required>

    <label>Email:</label>
    <input type="email" id="email" required>

    <button type="submit">Submit</button>
</form>

<div id="message"></div>

<script>
const form = document.getElementById('myForm');
const message = document.getElementById('message');

form.addEventListener('submit', function(event) {
    // IMPORTANT! Prevent the default submission
    event.preventDefault();

    // Get values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // Show message
    message.innerHTML = `
        <h3>Form submitted:</h3>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
    `;

    // Clear form
    form.reset();
});
</script>
```

**⚠️ Important:** `event.preventDefault()` prevents the form from submitting and reloading the page.

---

## Mouse Events

### `mouseover` and `mouseout` — Hover

```html
<div id="box" style="width: 200px; height: 200px; background: blue;">
    Hover the mouse here
</div>

<script>
const box = document.getElementById('box');

box.addEventListener('mouseover', function() {
    box.style.background = 'red';
    box.textContent = 'Mouse over!';
});

box.addEventListener('mouseout', function() {
    box.style.background = 'blue';
    box.textContent = 'Hover the mouse here';
});
</script>
```

### `mouseenter` and `mouseleave` (Similar but different)

```html
<div id="container" style="padding: 20px; background: lightgray;">
    <p>Outer container</p>
    <div id="inner" style="padding: 20px; background: white;">
        <p>Inner container</p>
    </div>
</div>

<script>
const container = document.getElementById('container');

// mouseenter does NOT fire on child elements
container.addEventListener('mouseenter', function() {
    console.log('Entered the container');
});

container.addEventListener('mouseleave', function() {
    console.log('Left the container');
});
</script>
```

### `mousemove` — Follow the Mouse

```html
<div id="area" style="width: 400px; height: 300px; background: lightblue; position: relative;">
    Move the mouse
</div>
<p id="coordinates"></p>

<script>
const area = document.getElementById('area');
const coordinates = document.getElementById('coordinates');

area.addEventListener('mousemove', function(event) {
    const x = event.offsetX;
    const y = event.offsetY;
    coordinates.textContent = `X: ${x}px, Y: ${y}px`;
});
</script>
```

---

## Keyboard Events

### `keydown` — When You Press a Key

```html
<input type="text" id="keyboard" placeholder="Press keys...">
<p id="info"></p>

<script>
const input = document.getElementById('keyboard');
const info = document.getElementById('info');

input.addEventListener('keydown', function(event) {
    info.innerHTML = `
        <strong>Key:</strong> ${event.key}<br>
        <strong>Code:</strong> ${event.code}<br>
        <strong>Ctrl:</strong> ${event.ctrlKey}<br>
        <strong>Shift:</strong> ${event.shiftKey}
    `;
});
</script>
```

### Detecting Special Keys

```html
<input type="text" id="field">
<p id="message"></p>

<script>
const field = document.getElementById('field');
const message = document.getElementById('message');

field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        message.textContent = 'You pressed Enter!';
    } else if (event.key === 'Escape') {
        field.value = '';
        message.textContent = 'Field cleared with Escape';
    } else if (event.ctrlKey && event.key === 's') {
        event.preventDefault();  // Prevent saving the page
        message.textContent = 'Ctrl+S shortcut detected!';
    }
});
</script>
```

---

## Practical Project: Interactive To-Do List

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
        }

        .task {
            padding: 10px;
            margin: 10px 0;
            background: #f0f0f0;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .task.completed {
            text-decoration: line-through;
            opacity: 0.6;
        }

        button {
            padding: 10px 20px;
            cursor: pointer;
        }

        .btn-delete {
            background: #ff4444;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>📝 My To-Do List</h1>

    <div>
        <input type="text" id="newTask" placeholder="Type a new task...">
        <button id="btnAdd">Add</button>
    </div>

    <div id="taskList"></div>

    <script>
        const newTaskInput = document.getElementById('newTask');
        const btnAdd = document.getElementById('btnAdd');
        const taskList = document.getElementById('taskList');

        let tasks = [];

        // Add task
        btnAdd.addEventListener('click', addTask);

        // Also add with Enter
        newTaskInput.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                addTask();
            }
        });

        function addTask() {
            const text = newTaskInput.value.trim();

            if (text === '') {
                alert('Please type a task');
                return;
            }

            // Create task object
            const task = {
                id: Date.now(),
                text: text,
                completed: false
            };

            // Add to array
            tasks.push(task);

            // Clear input
            newTaskInput.value = '';

            // Render list
            renderTasks();
        }

        function renderTasks() {
            // Build HTML with template strings
            let html = '';

            tasks.forEach(task => {
                html += `
                    <div class="task ${task.completed ? 'completed' : ''}" data-id="${task.id}">
                        <span>${task.text}</span>
                        <div>
                            <button onclick="toggleCompleted(${task.id})">
                                ${task.completed ? '↩️ Undo' : '✅ Complete'}
                            </button>
                            <button class="btn-delete" onclick="deleteTask(${task.id})">
                                🗑️ Delete
                            </button>
                        </div>
                    </div>
                `;
            });

            taskList.innerHTML = html;
        }

        function toggleCompleted(id) {
            const task = tasks.find(t => t.id === id);
            if (task) {
                task.completed = !task.completed;
                renderTasks();
            }
        }

        function deleteTask(id) {
            tasks = tasks.filter(t => t.id !== id);
            renderTasks();
        }
    </script>
</body>
</html>
```

---

## Summary of the Most Common Events

### Mouse Events

| Event | When It Happens | Common Use |
|-------|----------------|------------|
| `click` | Mouse click | Buttons, links |
| `dblclick` | Double click | Open elements |
| `mouseover` | Mouse enters element | Tooltips, hover |
| `mouseout` | Mouse leaves element | Remove hover |
| `mouseenter` | Mouse enters (no bubbling) | Dropdown menus |
| `mouseleave` | Mouse leaves (no bubbling) | Dropdown menus |
| `mousemove` | Mouse moves over element | Follow cursor |
| `mousedown` | Mouse button pressed | Drag and drop |
| `mouseup` | Mouse button released | Drag and drop |

### Keyboard Events

| Event | When It Happens | Common Use |
|-------|----------------|------------|
| `keydown` | Key pressed | Detect special keys |
| `keyup` | Key released | Run after typing |
| `keypress` | Character key pressed | ⚠️ Deprecated, use keydown |

### Form Events

| Event | When It Happens | Common Use |
|-------|----------------|------------|
| `submit` | Form submitted | Validate before sending |
| `change` | Value changes and loses focus | Select, checkbox, radio |
| `input` | Value changes (every key) | Real-time validation |
| `focus` | Element receives focus | Highlight active field |
| `blur` | Element loses focus | Validate on leaving field |

### Page Events

| Event | When It Happens | Common Use |
|-------|----------------|------------|
| `load` | Page/element loaded | Initialize app |
| `DOMContentLoaded` | DOM ready (no images) | Initialize faster |
| `resize` | Window resized | Responsive JavaScript |
| `scroll` | User scrolls | Infinite scroll, animations |

---

## Good Practices with Events

### ✅ DO

```javascript
// ✅ Use addEventListener
element.addEventListener('click', myFunction);

// ✅ Prevent default behavior when needed
form.addEventListener('submit', function(event) {
    event.preventDefault();
    // Your code...
});

// ✅ Use event delegation for dynamic elements
document.addEventListener('click', function(event) {
    if (event.target.matches('.dynamic-button')) {
        // Handle click
    }
});

// ✅ Clean up event listeners when you no longer need them
element.removeEventListener('click', myFunction);
```

### ❌ DON'T

```javascript
// ❌ Avoid inline event handlers in HTML
<button onclick="alert('No!')">Bad</button>

// ❌ Don't use onclick directly (only allows one function)
element.onclick = function() { };

// ❌ Don't create heavy functions in events that fire often
window.addEventListener('scroll', function() {
    // ❌ Heavy calculations on every scroll
    doSomethingVeryHeavy();
});
```

---

## Practical Exercises

### Exercise 1: Change Background Color

Create a button that changes the page background color every time it's clicked.

```html
<button id="btnColor">Change Color</button>
```

<details>
<summary>See solution</summary>

```javascript
const btnColor = document.getElementById('btnColor');
const colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink'];
let index = 0;

btnColor.addEventListener('click', function() {
    document.body.style.backgroundColor = colors[index];
    index = (index + 1) % colors.length;
});
```
</details>

### Exercise 2: Character Counter

Create a textarea that shows how many characters the user has typed in real time.

```html
<textarea id="text" rows="5" cols="50"></textarea>
<p>Characters: <span id="counter">0</span></p>
```

<details>
<summary>See solution</summary>

```javascript
const text = document.getElementById('text');
const counter = document.getElementById('counter');

text.addEventListener('input', function() {
    counter.textContent = text.value.length;
});
```
</details>

### Exercise 3: Show/Hide Content

Create a button that shows or hides a div.

```html
<button id="btnToggle">Show/Hide</button>
<div id="content" style="display: none;">
    <p>This content can be shown or hidden</p>
</div>
```

<details>
<summary>See solution</summary>

```javascript
const btnToggle = document.getElementById('btnToggle');
const content = document.getElementById('content');

btnToggle.addEventListener('click', function() {
    if (content.style.display === 'none') {
        content.style.display = 'block';
        btnToggle.textContent = 'Hide';
    } else {
        content.style.display = 'none';
        btnToggle.textContent = 'Show';
    }
});
```
</details>

---

## Conclusion

You have learned:

✅ **DOM**: What it is and how it's structured
✅ **Selecting elements**: getElementById, querySelector, querySelectorAll
✅ **Manipulating content**: innerHTML, textContent, template strings
✅ **Events**: What they are and how they work
✅ **Event listeners**: addEventListener for handling events
✅ **Common events**: click, change, input, submit, load
✅ **Mouse events**: mouseover, mouseout, mousemove
✅ **Keyboard events**: keydown, keyup
✅ **Practical project**: Complete to-do list

### Next Steps

1. Practice with the exercises
2. Build your own interactive project
3. Experiment with different events
4. Combine events with DOM manipulation
5. Learn about event propagation (bubbling and capturing)

**Now you can create fully interactive web pages! 🚀**

---

## Additional Resources

- **MDN - DOM**: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
- **MDN - Events**: https://developer.mozilla.org/en-US/docs/Web/Events
- **JavaScript.info - DOM**: https://javascript.info/document
- **W3Schools - DOM Tutorial**: https://www.w3schools.com/js/js_htmldom.asp

---

## Cheat Sheet: DOM and Events

```javascript
// SELECT ELEMENTS
document.getElementById('id')
document.querySelector('.class')
document.querySelectorAll('p')

// MANIPULATE CONTENT
element.textContent = 'text'
element.innerHTML = '<strong>HTML</strong>'
element.innerHTML = `<p>${variable}</p>`

// BASIC EVENTS
element.addEventListener('click', function() { })
element.addEventListener('change', function() { })
element.addEventListener('input', function() { })

// WAIT FOR LOADING
window.onload = function() { }
document.addEventListener('DOMContentLoaded', function() { })

// PREVENT DEFAULT BEHAVIOR
event.preventDefault()

// GET VALUES
input.value
checkbox.checked
select.value

// MODIFY STYLES
element.style.color = 'red'
element.style.display = 'none'
```
