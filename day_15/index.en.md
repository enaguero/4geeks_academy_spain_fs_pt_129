[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 15: JavaScript Modules and React ⚛️

## Introduction

Today we'll take two important steps on your path as a developer:
1. **JavaScript Modules**: You'll learn how to organize your code in separate files
2. **React**: You'll meet the most popular library for building modern web interfaces

---

## Part 1: What Are Modules?

### The Problem: Everything in a Single File 😰

Imagine you're building a large application:

```javascript
// app.js - ALL THE CODE HERE (5000 lines!)

function sum(a, b) { return a + b; }
function subtract(a, b) { return a - b; }
function multiply(a, b) { return a * b; }
function getUserData() { /* ... */ }
function processPayment() { /* ... */ }
function sendEmail() { /* ... */ }
// ... 200 more functions ...
```

**Problems**:
- ❌ Impossible to navigate
- ❌ Hard to maintain
- ❌ You can't reuse code in other projects
- ❌ Multiple developers can't work at the same time

### The Solution: Modules 🎯

**Modules** let you split your code into separate files, each with its own responsibility.

```
project/
├── calculator.js      ← Math functions
├── user.js           ← User management
├── payment.js        ← Payment processing
└── app.js            ← Main file
```

### What Is a Module?

**Module** = A JavaScript file that **exports** functions, variables, or objects so other files can **import them**.

---

## Part 2: Export — Share Your Code

### Basic Export (Named Export)

**File: `math.js`**
```javascript
// Export individual functions
export function sum(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export const PI = 3.14159;
```

### 🔍 Explanation

```javascript
export function sum(a, b) { ... }
```

The `export` keyword says: **"This function can be used by other files"**.

### Export at the End of the File

You can also export everything at the end:

**File: `math.js`**
```javascript
function sum(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

const PI = 3.14159;

// Export everything at the end
export { sum, subtract, PI };
```

### 📊 Comparison

| Method | When to use |
|--------|-------------|
| `export function sum()` | When you export a few things |
| `export { sum, subtract }` | When you export many things at the end |

---

## Part 3: Import — Use Code from Other Files

### Basic Import

**File: `app.js`**
```javascript
// Import specific functions
import { sum, subtract, PI } from './math.js';

console.log(sum(5, 3));       // 8
console.log(subtract(10, 4)); // 6
console.log(PI);              // 3.14159
```

### 🔍 Explanation

```javascript
import { sum, subtract } from './math.js';
```

- **`import`**: Keyword to import
- **`{ sum, subtract }`**: What you want to import (in braces)
- **`from './math.js'`**: Where to import from

### Paths in Import

```javascript
// Same directory
import { sum } from './math.js';

// Subdirectory
import { getUserData } from './utils/user.js';

// Parent directory
import { config } from '../config.js';
```

---

## Part 4: Export Default — The Main Export

### What Is Export Default?

When a file has **one main thing** to export, you use `export default`.

**File: `calculator.js`**
```javascript
// One main class
class Calculator {
    sum(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }
}

export default Calculator;
```

**File: `app.js`**
```javascript
// No braces when importing!
import Calculator from './calculator.js';

const calc = new Calculator();
console.log(calc.sum(5, 3)); // 8
```

### 🔍 Key Difference

| Export Type | Export Syntax | Import Syntax |
|-------------|---------------|---------------|
| **Named** | `export function sum()` | `import { sum } from './file.js'` |
| **Default** | `export default Calculator` | `import Calculator from './file.js'` |

### Golden Rule

- **Named exports**: Multiple things with **specific names** (you need braces `{}`)
- **Default export**: **One main thing** per file (no braces)

---

## Part 5: Complete Example — User System

### Project Structure

```
user-system/
├── user.js           ← User class
├── userService.js    ← User services
├── validator.js      ← Validations
└── app.js            ← Main file
```

### File 1: `user.js`

```javascript
// Default export: the main class
class User {
    constructor(name, email, age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }

    greet() {
        return `Hello, I'm ${this.name}`;
    }
}

export default User;
```

### File 2: `validator.js`

```javascript
// Named exports: multiple validation functions
export function isValidEmail(email) {
    return email.includes('@');
}

export function isValidAge(age) {
    return age >= 18 && age <= 120;
}

export function isValidName(name) {
    return name.length >= 2;
}
```

### File 3: `userService.js`

```javascript
// Mixing imports
import User from './user.js';  // Default import
import { isValidEmail, isValidAge, isValidName } from './validator.js';  // Named imports

export function createUser(name, email, age) {
    // Validate data
    if (!isValidName(name)) {
        throw new Error('Invalid name');
    }

    if (!isValidEmail(email)) {
        throw new Error('Invalid email');
    }

    if (!isValidAge(age)) {
        throw new Error('Invalid age');
    }

    // Create and return user
    return new User(name, email, age);
}

export function getUserInfo(user) {
    return {
        name: user.name,
        email: user.email,
        age: user.age,
        canVote: user.age >= 18
    };
}
```

### File 4: `app.js`

```javascript
import { createUser, getUserInfo } from './userService.js';

// Create users
try {
    const user1 = createUser('Ana García', 'ana@example.com', 25);
    const user2 = createUser('Pedro López', 'pedro@example.com', 17);

    console.log(user1.greet());  // Hello, I'm Ana García
    console.log(getUserInfo(user1));

} catch (error) {
    console.error('Error:', error.message);
}
```

---

## Part 6: Import * (Import Everything)

### Syntax

```javascript
import * as MathUtils from './math.js';

console.log(MathUtils.sum(2, 3));      // 5
console.log(MathUtils.subtract(10, 4)); // 6
console.log(MathUtils.PI);              // 3.14159
```

### When to Use

✅ **Use** `import *` when the module has many related functions
❌ **Don't use** it if you only need 1-2 functions (import them specifically)

---

## 📝 Exercise 1: String Library

Create a modular system to manipulate strings.

**File: `stringHelpers.js`**
```javascript
export function toUpperCase(str) {
    return str.toUpperCase();
}

export function toLowerCase(str) {
    return str.toLowerCase();
}

export function reverse(str) {
    return str.split('').reverse().join('');
}

export function countVowels(str) {
    const vowels = str.match(/[aeiouAEIOU]/g);
    return vowels ? vowels.length : 0;
}
```

**File: `app.js`**
```javascript
// TODO: Import the functions and use them
```

<details>
<summary>Solution</summary>

```javascript
import { toUpperCase, toLowerCase, reverse, countVowels } from './stringHelpers.js';

const text = 'Hello World';

console.log(toUpperCase(text));  // HELLO WORLD
console.log(toLowerCase(text));  // hello world
console.log(reverse(text));      // dlroW olleH
console.log(countVowels(text));  // 3
```
</details>

---

## Part 7: Introduction to React ⚛️

### What Is React?

**React** is a **JavaScript library** created by Facebook for efficiently building user interfaces (UI).

### The Problem React Solves

#### Before React (Vanilla JS)

```javascript
// Tedious code that's hard to maintain
document.querySelector('#app').innerHTML =
    '<div class="card">' +
    '  <h2>' + user.name + '</h2>' +
    '  <p>' + user.email + '</p>' +
    '</div>';

// Repeat this for every DOM element! 😰
```

#### With React

```javascript
// Clean code that's easy to maintain
function UserCard() {
    return (
        <div className="card">
            <h2>{user.name}</h2>
            <p>{user.email}</p>
        </div>
    );
}
```

### Why Is React Popular?

| Benefit | Explanation |
|---------|-------------|
| 🧩 **Components** | Splits the UI into reusable pieces |
| ⚡ **Fast** | Only updates what changes in the DOM |
| 📝 **JSX** | Write HTML inside JavaScript |
| 🔄 **Reactive** | Changes are reflected automatically |
| 🌐 **Popular** | Used by Facebook, Instagram, Netflix, Airbnb |

---

## Part 8: Components — The Building Blocks of React

### What Is a Component?

A **component** is a reusable piece of the interface. It's like LEGO: you put many small components together to build something big.

### Analogy: A House 🏠

```
House
├── Navbar (navigation)
├── Header
├── Main (main content)
│   ├── Card
│   ├── Card
│   └── Card
└── Footer
```

Each part is an independent component you can reuse.

### Your First Component

```javascript
function Welcome() {
    return <h1>Hello World!</h1>;
}
```

### 🔍 Anatomy of a Component

```javascript
function Welcome() {        // 1. Name in PascalCase
    return (                // 2. return returns JSX
        <h1>Hello!</h1>    // 3. JSX (looks like HTML)
    );
}
```

**Rules**:
1. Name in **PascalCase** (`Welcome`, not `welcome`)
2. Must **return** JSX
3. A single root element

---

## Part 9: JSX — HTML Inside JavaScript

### What Is JSX?

**JSX** = JavaScript + XML. It lets you write HTML inside JavaScript.

```javascript
// JSX (what you write)
const element = <h1>Hello, {name}</h1>;

// Pure JavaScript (what React generates)
const element = React.createElement('h1', null, 'Hello, ', name);
```

### JSX Rules

#### 1. **A single root element**

```javascript
// ❌ INCORRECT: Two root elements
function App() {
    return (
        <h1>Title</h1>
        <p>Paragraph</p>
    );
}

// ✅ CORRECT: Wrapped in a div
function App() {
    return (
        <div>
            <h1>Title</h1>
            <p>Paragraph</p>
        </div>
    );
}

// ✅ CORRECT: Using a Fragment (<>)
function App() {
    return (
        <>
            <h1>Title</h1>
            <p>Paragraph</p>
        </>
    );
}
```

#### 2. **Close all tags**

```javascript
// ❌ INCORRECT in JSX
<img src="photo.jpg">
<br>

// ✅ CORRECT in JSX
<img src="photo.jpg" />
<br />
```

#### 3. **className instead of class**

```javascript
// ❌ INCORRECT
<div class="card">Content</div>

// ✅ CORRECT
<div className="card">Content</div>
```

**Reason**: `class` is a reserved word in JavaScript.

#### 4. **JavaScript expressions with {}**

```javascript
function Greeting() {
    const name = "Ana";
    const age = 25;

    return (
        <div>
            <h1>Hello, {name}</h1>
            <p>You are {age} years old</p>
            <p>Can you vote? {age >= 18 ? 'Yes' : 'No'}</p>
        </div>
    );
}
```

---

## Part 10: Components with Props

### What Are Props?

**Props** (properties) are **parameters** you pass to a component to customize it.

### Example Without Props (Repetitive Code)

```javascript
function UserCard1() {
    return <h2>Ana García</h2>;
}

function UserCard2() {
    return <h2>Pedro López</h2>;
}

function UserCard3() {
    return <h2>María Rodríguez</h2>;
}

// You'd have to create 100 components for 100 users! 😱
```

### Example With Props (Reusable)

```javascript
function UserCard(props) {
    return <h2>{props.name}</h2>;
}

// Use the component with different props
<UserCard name="Ana García" />
<UserCard name="Pedro López" />
<UserCard name="María Rodríguez" />
```

### Props with Multiple Values

```javascript
function UserCard(props) {
    return (
        <div className="card">
            <h2>{props.name}</h2>
            <p>Email: {props.email}</p>
            <p>Age: {props.age}</p>
        </div>
    );
}

// Usage
<UserCard
    name="Ana García"
    email="ana@example.com"
    age={25}
/>
```

### 🔍 Types of Props

```javascript
<UserCard
    name="Ana"           // String (in quotes)
    age={25}            // Number (in braces)
    isActive={true}     // Boolean (in braces)
    hobbies={['read', 'run']}  // Array (in braces)
/>
```

---

## Part 11: Destructuring Props

### Without Destructuring

```javascript
function UserCard(props) {
    return (
        <div>
            <h2>{props.name}</h2>
            <p>{props.email}</p>
            <p>{props.age}</p>
        </div>
    );
}
```

### With Destructuring (Cleaner)

```javascript
function UserCard({ name, email, age }) {
    return (
        <div>
            <h2>{name}</h2>
            <p>{email}</p>
            <p>{age}</p>
        </div>
    );
}
```

**Advantage**: You write less and the code is more readable.

---

## Part 12: Complete Component — Product Card

```javascript
function ProductCard({ name, price, image, inStock }) {
    return (
        <div className="product-card">
            <img src={image} alt={name} />
            <h3>{name}</h3>
            <p className="price">${price}</p>
            {inStock ? (
                <button>Buy</button>
            ) : (
                <p className="out-of-stock">Out of stock</p>
            )}
        </div>
    );
}

// Usage
function App() {
    return (
        <div>
            <ProductCard
                name="Laptop"
                price={999}
                image="laptop.jpg"
                inStock={true}
            />
            <ProductCard
                name="Mouse"
                price={25}
                image="mouse.jpg"
                inStock={false}
            />
        </div>
    );
}
```

---

## 📝 Exercise 2: Profile Card

Create a `ProfileCard` component that displays:
- Profile photo
- Name
- Profession
- "Follow" button if you don't follow, "Following" if you already follow

```javascript
function ProfileCard({ name, profession, photo, isFollowing }) {
    // TODO: Implement the component
}

// Should be used like this:
<ProfileCard
    name="Ana García"
    profession="Frontend Developer"
    photo="ana.jpg"
    isFollowing={false}
/>
```

<details>
<summary>Solution</summary>

```javascript
function ProfileCard({ name, profession, photo, isFollowing }) {
    return (
        <div className="profile-card">
            <img src={photo} alt={name} className="profile-photo" />
            <h2>{name}</h2>
            <p className="profession">{profession}</p>
            {isFollowing ? (
                <button className="btn-following">Following</button>
            ) : (
                <button className="btn-follow">Follow</button>
            )}
        </div>
    );
}
```
</details>

---

## Part 13: Rendering Lists

### Problem: Many Elements

```javascript
function App() {
    return (
        <div>
            <UserCard name="Ana" />
            <UserCard name="Pedro" />
            <UserCard name="María" />
            // ... What if I have 1000 users?
        </div>
    );
}
```

### Solution: map()

```javascript
function App() {
    const users = [
        { id: 1, name: 'Ana García' },
        { id: 2, name: 'Pedro López' },
        { id: 3, name: 'María Rodríguez' }
    ];

    return (
        <div>
            {users.map(user => (
                <UserCard
                    key={user.id}
                    name={user.name}
                />
            ))}
        </div>
    );
}
```

### 🔍 The `key` Prop

```javascript
<UserCard key={user.id} name={user.name} />
```

**`key`** is special: React uses it to identify each element uniquely.

**Rule**: Always use a unique ID, never the array index.

---

## Part 14: Complete Example — Product List

```javascript
function ProductList() {
    const products = [
        { id: 1, name: 'Laptop', price: 999, image: 'laptop.jpg', inStock: true },
        { id: 2, name: 'Mouse', price: 25, image: 'mouse.jpg', inStock: true },
        { id: 3, name: 'Keyboard', price: 75, image: 'keyboard.jpg', inStock: false },
        { id: 4, name: 'Monitor', price: 299, image: 'monitor.jpg', inStock: true }
    ];

    return (
        <div className="container">
            <h1>Our Products</h1>
            <div className="product-grid">
                {products.map(product => (
                    <ProductCard
                        key={product.id}
                        name={product.name}
                        price={product.price}
                        image={product.image}
                        inStock={product.inStock}
                    />
                ))}
            </div>
        </div>
    );
}

function ProductCard({ name, price, image, inStock }) {
    return (
        <div className="product-card">
            <img src={image} alt={name} />
            <h3>{name}</h3>
            <p className="price">${price}</p>
            {inStock ? (
                <button className="btn-primary">Add to cart</button>
            ) : (
                <p className="out-of-stock">Out of stock</p>
            )}
        </div>
    );
}

export default ProductList;
```

---

## 📝 Exercise 3: To-Do List

Build a to-do list with React.

```javascript
function TodoList() {
    const todos = [
        { id: 1, text: 'Learn JavaScript', completed: true },
        { id: 2, text: 'Study React', completed: false },
        { id: 3, text: 'Do exercises', completed: false }
    ];

    // TODO: Render each task with a TodoItem component
}

function TodoItem({ text, completed }) {
    // TODO: Show the text
    // TODO: Show "✓" if completed, "○" if not
}
```

<details>
<summary>Solution</summary>

```javascript
function TodoList() {
    const todos = [
        { id: 1, text: 'Learn JavaScript', completed: true },
        { id: 2, text: 'Study React', completed: false },
        { id: 3, text: 'Do exercises', completed: false }
    ];

    return (
        <div className="todo-list">
            <h2>My Tasks</h2>
            <ul>
                {todos.map(todo => (
                    <TodoItem
                        key={todo.id}
                        text={todo.text}
                        completed={todo.completed}
                    />
                ))}
            </ul>
        </div>
    );
}

function TodoItem({ text, completed }) {
    return (
        <li className={completed ? 'completed' : ''}>
            <span>{completed ? '✓' : '○'}</span>
            <span>{text}</span>
        </li>
    );
}
```
</details>

---

## Summary: Key Concepts

### JavaScript Modules
✅ **Module** = File that exports code
✅ **`export`** = Share functions/variables
✅ **`import`** = Use code from other files
✅ **Named export** = `export function sum()` → `import { sum }`
✅ **Default export** = `export default` → `import Calculator`
✅ Organize code in separate files

### React
✅ **React** = Library for building UIs
✅ **Component** = Reusable piece of UI
✅ **JSX** = HTML inside JavaScript
✅ **Props** = Parameters to customize components
✅ **key** = Unique identifier in lists
✅ Everything is a component

### JSX
✅ A single root element
✅ Close all tags (`<br />`)
✅ `className` instead of `class`
✅ `{}` for JavaScript expressions

---

## Cheat Sheet

```javascript
// ============ MODULES ============

// EXPORT (math.js)
export function sum(a, b) { return a + b; }
export const PI = 3.14;
export default class Calculator { }

// IMPORT (app.js)
import { sum, PI } from './math.js';
import Calculator from './calculator.js';
import * as Math from './math.js';

// ============ REACT ============

// BASIC COMPONENT
function Welcome() {
    return <h1>Hello!</h1>;
}

// COMPONENT WITH PROPS
function UserCard({ name, age }) {
    return (
        <div>
            <h2>{name}</h2>
            <p>{age} years old</p>
        </div>
    );
}

// USAGE
<UserCard name="Ana" age={25} />

// RENDER LIST
{users.map(user => (
    <UserCard key={user.id} name={user.name} />
))}

// CONDITIONAL IN JSX
{isLoggedIn ? <Dashboard /> : <Login />}

// JS EXPRESSIONS
<h1>Hello, {name}</h1>
<p>Total: ${price * quantity}</p>
```

---

## 🎯 Guided Project: Profile Gallery

Let's create a team profile gallery using everything we've learned.

### File Structure

```
team-gallery/
├── data.js          ← Team data
├── ProfileCard.js   ← Card component
├── App.js           ← Main component
└── index.html       ← Base HTML
```

### `data.js`

```javascript
const teamMembers = [
    {
        id: 1,
        name: 'Ana García',
        role: 'Frontend Developer',
        photo: 'https://i.pravatar.cc/150?img=1',
        skills: ['React', 'CSS', 'JavaScript']
    },
    {
        id: 2,
        name: 'Pedro López',
        role: 'Backend Developer',
        photo: 'https://i.pravatar.cc/150?img=2',
        skills: ['Node.js', 'Python', 'SQL']
    },
    {
        id: 3,
        name: 'María Rodríguez',
        role: 'UX Designer',
        photo: 'https://i.pravatar.cc/150?img=3',
        skills: ['Figma', 'Sketch', 'Photoshop']
    }
];

export default teamMembers;
```

### `ProfileCard.js`

```javascript
function ProfileCard({ name, role, photo, skills }) {
    return (
        <div className="profile-card">
            <img src={photo} alt={name} className="profile-photo" />
            <h2>{name}</h2>
            <p className="role">{role}</p>
            <div className="skills">
                {skills.map((skill, index) => (
                    <span key={index} className="skill-tag">
                        {skill}
                    </span>
                ))}
            </div>
            <button className="btn-contact">Contact</button>
        </div>
    );
}

export default ProfileCard;
```

### `App.js`

```javascript
import teamMembers from './data.js';
import ProfileCard from './ProfileCard.js';

function App() {
    return (
        <div className="container">
            <header>
                <h1>Our Team</h1>
                <p>Meet the people who make our project possible</p>
            </header>

            <div className="profile-grid">
                {teamMembers.map(member => (
                    <ProfileCard
                        key={member.id}
                        name={member.name}
                        role={member.role}
                        photo={member.photo}
                        skills={member.skills}
                    />
                ))}
            </div>
        </div>
    );
}

export default App;
```

---

## 🔗 Additional Resources

- **MDN - Modules**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
- **React Docs**: https://react.dev/learn
- **4Geeks - React Tutorial**: https://4geeks.com/lesson/learn-react-js-tutorial
- **4Geeks - Creating Components**: https://4geeks.com/lesson/making-react-components

---

## 🎉 Congratulations!

You now know:

- ✅ What modules are and why they matter
- ✅ How to use `export` and `import` to organize code
- ✅ The difference between named and default exports
- ✅ What React is and why it's popular
- ✅ How to create reusable components
- ✅ How to use JSX to write HTML in JavaScript
- ✅ How to pass data with props
- ✅ How to render lists with `map()`
- ✅ How to apply conditionals in JSX

**Next step**: In the upcoming classes you'll learn about **state** in React, which lets you build interactive components that respond to user actions.

---

## 💡 Final Thought

> "React is not just a library, it's a way of thinking about how to build interfaces"
> — Dan Abramov (co-creator of Redux and part of the React team)

Modules and React are fundamental in modern web development. Mastering them opens doors to:
- 🚀 Single Page Applications (SPA)
- 📱 Mobile apps with React Native
- 💼 Job opportunities at tech companies

**Keep practicing and building projects!**
