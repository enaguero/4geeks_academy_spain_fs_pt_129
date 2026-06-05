[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 13: Random Card Generator — Step-by-Step Project 🃏

## Introduction

Today we're going to build a **random card generator** from scratch, applying everything we've learned about the DOM, events, and JavaScript. We'll do it **incrementally**, building the project step by step.

### What Are We Going to Build?

A web application that:
- Displays a random poker card
- Lets you generate new cards by clicking
- Has an automatic mode that generates cards every 3 seconds
- Looks great with animations

---

## Step 1: Basic HTML Structure

Let's start with the simplest part: creating the HTML structure.

### 📝 Create the file `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Card Generator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🃏 Random Card Generator</h1>

        <div id="card" class="card">
            <div class="top-suit">♠</div>
            <div class="number">A</div>
            <div class="bottom-suit">♠</div>
        </div>

        <button id="btnGenerate">Generate New Card</button>
    </div>

    <script src="app.js"></script>
</body>
</html>
```

### 🔍 HTML Analysis

| Element | Purpose |
|---------|---------|
| `.container` | Main wrapper to center everything |
| `#card` | The card we'll modify dynamically |
| `.top-suit` | Suit in the top corner |
| `.number` | Card value (A, 2, 3… K) |
| `.bottom-suit` | Suit in the bottom corner (inverted) |
| `#btnGenerate` | Button to generate cards |

**💡 Important note**: The suits (♠ ♥ ♦ ♣) are Unicode characters you can copy directly.

---

## Step 2: Basic CSS Styles

Now let's style our card.

### 📝 Create the file `style.css`

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.container {
    text-align: center;
}

h1 {
    color: white;
    margin-bottom: 30px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

### ✅ Checkpoint 1

**Open `index.html` in your browser**. You should see:
- A purple gradient background
- The centered title
- A card (still unstyled)
- A button

---

## Step 3: Style the Card

Let's make the card look like a real poker card.

### 📝 Add this to `style.css`

```css
.card {
    width: 200px;
    height: 300px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    margin: 30px auto;
    padding: 20px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.top-suit {
    font-size: 50px;
    text-align: left;
}

.number {
    font-size: 80px;
    font-weight: bold;
    text-align: center;
}

.bottom-suit {
    font-size: 50px;
    text-align: right;
    transform: rotate(180deg);
}

.card.red {
    color: #e74c3c;
}

.card.black {
    color: #2c3e50;
}
```

### 🔍 Key CSS Concepts

```css
display: flex;
flex-direction: column;      /* Arranges items vertically */
justify-content: space-between; /* Separates the items */
```

This creates the card layout: suit on top, number in the middle, suit on the bottom.

```css
transform: rotate(180deg);  /* Flips the bottom suit */
```

### ✅ Checkpoint 2

Refresh the browser. Now you should see a nice card with:
- White background and rounded corners
- A shadow that makes it "float"
- Top suit, central number, bottom suit inverted

---

## Step 4: Style the Button

Let's make the button look professional.

### 📝 Add to `style.css`

```css
button {
    background: #3498db;
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 25px;
    cursor: pointer;
    margin: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
}

button:active {
    transform: translateY(0);
}
```

### 🔍 Interactive Effects

- **`:hover`** — When you hover over it, the button lifts a bit
- **`:active`** — When you click it, it returns to its position
- **`transition`** — Makes the changes smooth

### ✅ Checkpoint 3

Hover over the button and click it. You should see the animations.

---

## Step 5: JavaScript — Basic Structure

Now comes the exciting part: bringing the card to life!

### 📝 Create the file `app.js`

```javascript
// Step 1: Get DOM elements
const card = document.getElementById('card');
const btnGenerate = document.getElementById('btnGenerate');

// Step 2: Define the card data
const suits = [
    { symbol: '♠', name: 'spade', color: 'black' },
    { symbol: '♣', name: 'club', color: 'black' },
    { symbol: '♥', name: 'heart', color: 'red' },
    { symbol: '♦', name: 'diamond', color: 'red' }
];

const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

// Step 3: Test message
console.log('JavaScript loaded successfully');
console.log('Available suits:', suits.length);
console.log('Available values:', values.length);
```

### 🔍 Step-by-step explanation

#### 1. Get DOM elements

```javascript
const card = document.getElementById('card');
```

This stores a reference to the HTML element with `id="card"`. Now we can manipulate it from JavaScript.

#### 2. Data arrays

```javascript
const suits = [
    { symbol: '♠', name: 'spade', color: 'black' },
    ...
];
```

Each suit is an **object** with 3 properties:
- `symbol`: The visual character (♠)
- `name`: Name in English
- `color`: 'black' or 'red' (for applying CSS)

### ✅ Checkpoint 4

Open the **Browser Console** (F12 → Console). You should see:
```
JavaScript loaded successfully
Available suits: 4
Available values: 13
```

---

## Step 6: Generate Random Numbers

Before generating cards, we need to understand how random numbers work.

### 📝 Add to `app.js`

```javascript
// Helper function: generate random number
function getRandomNumber(max) {
    return Math.floor(Math.random() * max);
}

// Test in the console
console.log('Random number between 0-3:', getRandomNumber(4));
console.log('Random number between 0-12:', getRandomNumber(13));
```

### 🔍 How does it work?

```javascript
Math.random()              // Generates a number between 0 and 1
                          // Examples: 0.234, 0.891, 0.012

Math.random() * 4         // Multiplies by 4
                          // Examples: 0.936, 3.564, 0.048

Math.floor(Math.random() * 4)  // Rounds down
                                // Examples: 0, 3, 0
```

**Result**: Integers between 0 and 3 (perfect for array indexes)

### 📊 Examples table

| `Math.random()` | `* 4` | `Math.floor()` | Result |
|-----------------|-------|----------------|--------|
| 0.123 | 0.492 | 0.492 | **0** |
| 0.456 | 1.824 | 1.824 | **1** |
| 0.789 | 3.156 | 3.156 | **3** |
| 0.999 | 3.996 | 3.996 | **3** |

---

## Step 7: Generate a Random Card

Now, let's actually generate random cards.

### 📝 Add to `app.js`

```javascript
// Function to generate a random card
function generateRandomCard() {
    // 1. Pick random suit
    const randomSuitIndex = getRandomNumber(suits.length);
    const randomSuit = suits[randomSuitIndex];

    // 2. Pick random value
    const randomValueIndex = getRandomNumber(values.length);
    const randomValue = values[randomValueIndex];

    // 3. Log to console (for verification)
    console.log('Card generated:', randomValue + randomSuit.symbol);

    // 4. Update the card on screen
    renderCard(randomSuit, randomValue);
}

// Test the function
generateRandomCard();
```

### 🔍 Code breakdown

```javascript
const randomSuitIndex = getRandomNumber(suits.length);
```
- `suits.length` = 4
- `getRandomNumber(4)` returns 0, 1, 2, or 3
- It's a valid index for the `suits` array

```javascript
const randomSuit = suits[randomSuitIndex];
```
- Returns the full object: `{ symbol: '♠', name: 'spade', color: 'black' }`

### ✅ Checkpoint 5

Save the file and refresh the browser. In the console you should see something like:
```
Card generated: 7♥
```

(The value changes each time you refresh because it's random)

---

## Step 8: Render the Card

Now we're going to update the HTML to display the generated card.

### 📝 Add to `app.js`

```javascript
// Function to render the card in the DOM
function renderCard(suit, value) {
    // 1. Get the inner elements of the card
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');

    // 2. Update the content
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;

    // 3. Update the color (red or black)
    card.className = 'card';  // Reset classes
    card.classList.add(suit.color);  // Add 'red' or 'black'

    console.log('Card rendered:', value + suit.symbol, '(' + suit.color + ')');
}
```

### 🔍 DOM methods used

| Method | What it does |
|--------|--------------|
| `querySelector('.top-suit')` | Finds the element with class `.top-suit` inside `card` |
| `textContent = '♥'` | Changes the element's text |
| `className = 'card'` | Resets all classes to just 'card' |
| `classList.add('red')` | Adds the 'red' class (without removing 'card') |

### 📊 Visual example

**Before** (static HTML):
```html
<div id="card" class="card">
    <div class="top-suit">♠</div>
    <div class="number">A</div>
    <div class="bottom-suit">♠</div>
</div>
```

**After** (dynamic JavaScript with 7♥):
```html
<div id="card" class="card red">
    <div class="top-suit">♥</div>
    <div class="number">7</div>
    <div class="bottom-suit">♥</div>
</div>
```

### ✅ Checkpoint 6

Refresh the browser several times. Each time you should see a different card generated automatically.

---

## Step 9: Wire Up the Button

Let's make the button work with a click event.

### 📝 Add to `app.js`

```javascript
// Event Listener for the button
btnGenerate.addEventListener('click', function() {
    console.log('Button clicked!');
    generateRandomCard();
});

// Generate an initial card on load
generateRandomCard();
```

### 🔍 Event-Driven Programming

```javascript
btnGenerate.addEventListener('click', function() {
    // This code ONLY runs when you click
    generateRandomCard();
});
```

**Anatomy of the Event Listener:**
1. **Element**: `btnGenerate` (the button)
2. **Event**: `'click'` (when it's clicked)
3. **Handler**: `function() { ... }` (what to do when it happens)

### ✅ Checkpoint 7

Click the button several times. Each click should generate a new random card.

---

## Step 10: Add Animation

Let's make the card have a small animation when it changes.

### 📝 Modify the `renderCard` function in `app.js`

```javascript
function renderCard(suit, value) {
    // 1. Get the inner elements of the card
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');

    // 2. Update the content
    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;

    // 3. Update the color
    card.className = 'card';
    card.classList.add(suit.color);

    // 4. ⭐ NEW: Entry animation
    card.style.transform = 'scale(0.9)';
    setTimeout(function() {
        card.style.transform = 'scale(1)';
    }, 100);

    console.log('Card rendered:', value + suit.symbol);
}
```

### 🔍 How does the animation work?

```javascript
card.style.transform = 'scale(0.9)';  // Makes the card smaller (90%)
```

```javascript
setTimeout(function() {
    card.style.transform = 'scale(1)';  // Returns to normal size (100%)
}, 100);  // After 100 milliseconds
```

**Visual effect**: The card "shrinks" and then returns to its size, giving a feeling of movement.

### 📝 Add transition in `style.css`

```css
.card {
    /* ... existing styles ... */
    transition: transform 0.3s ease;  /* ⭐ NEW */
}
```

### ✅ Checkpoint 8

Click the button. You should now see a smooth animation when the card changes.

---

## Step 11: Automatic Mode (Advanced)

Let's add a mode that generates cards automatically every 3 seconds.

### 📝 Update the HTML

```html
<button id="btnGenerate">Generate New Card</button>
<button id="btnAuto">Auto-Generate (every 3s)</button>
<button id="btnStop">Stop</button>
```

### 📝 Add styles in `style.css`

```css
#btnAuto {
    background: #2ecc71;
    color: white;
}

#btnStop {
    background: #e74c3c;
    color: white;
}
```

### 📝 Add at the beginning of `app.js`

```javascript
const btnAuto = document.getElementById('btnAuto');
const btnStop = document.getElementById('btnStop');

// Variable to control the interval
let autoGenerateInterval = null;
```

### 📝 Add at the end of `app.js`

```javascript
// Auto-Generate button
btnAuto.addEventListener('click', function() {
    // If already running, show message
    if (autoGenerateInterval) {
        alert('Already in automatic mode');
        return;
    }

    // Generate every 3 seconds
    autoGenerateInterval = setInterval(function() {
        generateRandomCard();
    }, 3000);

    // Visual feedback
    btnAuto.textContent = '✓ Auto-Generating...';
    btnAuto.style.opacity = '0.5';

    console.log('Automatic mode activated');
});

// Stop button
btnStop.addEventListener('click', function() {
    // Stop the interval
    if (autoGenerateInterval) {
        clearInterval(autoGenerateInterval);
        autoGenerateInterval = null;

        // Restore button
        btnAuto.textContent = 'Auto-Generate (every 3s)';
        btnAuto.style.opacity = '1';

        console.log('Automatic mode stopped');
    }
});
```

### 🔍 Key concepts: Timers in JavaScript

#### `setInterval()` — Repeat something every X time

```javascript
let interval = setInterval(function() {
    console.log('Hello every 3 seconds!');
}, 3000);
```

#### `clearInterval()` — Stop the repetition

```javascript
clearInterval(interval);
```

### 📊 Automatic mode flow

```
User clicks "Auto-Generate"
    ↓
An interval is created that runs generateRandomCard() every 3000ms
    ↓
The card changes automatically every 3 seconds
    ↓
User clicks "Stop"
    ↓
The interval is stopped
```

### ✅ Checkpoint 9

1. Click "Auto-Generate (every 3s)"
2. Watch as the card changes automatically every 3 seconds
3. Click "Stop" to stop

---

## Step 12: Improve the Card with Hover

Let's add an effect when you hover over the card.

### 📝 Add to `style.css`

```css
.card:hover {
    transform: scale(1.05);
    cursor: pointer;
}
```

### ✅ Checkpoint 10

Hover the mouse over the card. It should grow slightly.

---

## 🎯 Complete Final Code

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Card Generator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🃏 Random Card Generator</h1>

        <div id="card" class="card">
            <div class="top-suit">♠</div>
            <div class="number">A</div>
            <div class="bottom-suit">♠</div>
        </div>

        <button id="btnGenerate">Generate New Card</button>
        <button id="btnAuto">Auto-Generate (every 3s)</button>
        <button id="btnStop">Stop</button>
    </div>

    <script src="app.js"></script>
</body>
</html>
```

### `style.css`

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.container {
    text-align: center;
}

h1 {
    color: white;
    margin-bottom: 30px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.card {
    width: 200px;
    height: 300px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    margin: 30px auto;
    padding: 20px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: scale(1.05);
    cursor: pointer;
}

.top-suit {
    font-size: 50px;
    text-align: left;
}

.number {
    font-size: 80px;
    font-weight: bold;
    text-align: center;
}

.bottom-suit {
    font-size: 50px;
    text-align: right;
    transform: rotate(180deg);
}

.card.red {
    color: #e74c3c;
}

.card.black {
    color: #2c3e50;
}

button {
    background: white;
    border: none;
    padding: 15px 30px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 25px;
    cursor: pointer;
    margin: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
}

button:active {
    transform: translateY(0);
}

#btnGenerate {
    background: #3498db;
    color: white;
}

#btnAuto {
    background: #2ecc71;
    color: white;
}

#btnStop {
    background: #e74c3c;
    color: white;
}
```

### `app.js`

```javascript
// Get DOM elements
const card = document.getElementById('card');
const btnGenerate = document.getElementById('btnGenerate');
const btnAuto = document.getElementById('btnAuto');
const btnStop = document.getElementById('btnStop');

// Arrays of suits and values
const suits = [
    { symbol: '♠', name: 'spade', color: 'black' },
    { symbol: '♣', name: 'club', color: 'black' },
    { symbol: '♥', name: 'heart', color: 'red' },
    { symbol: '♦', name: 'diamond', color: 'red' }
];

const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

// Variable to control the auto-generator
let autoGenerateInterval = null;

// Helper function: generate random number
function getRandomNumber(max) {
    return Math.floor(Math.random() * max);
}

// Function to generate a random card
function generateRandomCard() {
    const randomSuit = suits[getRandomNumber(suits.length)];
    const randomValue = values[getRandomNumber(values.length)];

    renderCard(randomSuit, randomValue);
}

// Function to render the card in the DOM
function renderCard(suit, value) {
    const topSuit = card.querySelector('.top-suit');
    const number = card.querySelector('.number');
    const bottomSuit = card.querySelector('.bottom-suit');

    topSuit.textContent = suit.symbol;
    number.textContent = value;
    bottomSuit.textContent = suit.symbol;

    card.className = 'card';
    card.classList.add(suit.color);

    // Animation
    card.style.transform = 'scale(0.9)';
    setTimeout(function() {
        card.style.transform = 'scale(1)';
    }, 100);
}

// Event Listeners
btnGenerate.addEventListener('click', function() {
    generateRandomCard();
});

btnAuto.addEventListener('click', function() {
    if (autoGenerateInterval) {
        alert('Already in automatic mode');
        return;
    }

    autoGenerateInterval = setInterval(function() {
        generateRandomCard();
    }, 3000);

    btnAuto.textContent = '✓ Auto-Generating...';
    btnAuto.style.opacity = '0.5';
});

btnStop.addEventListener('click', function() {
    if (autoGenerateInterval) {
        clearInterval(autoGenerateInterval);
        autoGenerateInterval = null;

        btnAuto.textContent = 'Auto-Generate (every 3s)';
        btnAuto.style.opacity = '1';
    }
});

// Generate an initial card
generateRandomCard();
```

---

## 🚀 Extension Exercises

### Exercise 1: Add a Counter ⭐

Add a counter that shows how many cards have been generated.

**Hint:**
```javascript
let cardsGenerated = 0;

function generateRandomCard() {
    // ... existing code ...
    cardsGenerated++;
    document.getElementById('counter').textContent =
        `Cards generated: ${cardsGenerated}`;
}
```

### Exercise 2: Reset Button ⭐⭐

Add a button that resets the counter and generates a new card.

### Exercise 3: Card History ⭐⭐⭐

Show the last 5 generated cards below the main card.

**Hint:**
```javascript
let history = [];

function generateRandomCard() {
    // ... existing code ...

    history.push(value + suit.symbol);
    if (history.length > 5) {
        history.shift(); // Remove the first one
    }

    showHistory();
}
```

### Exercise 4: Change Auto-Generator Speed ⭐⭐⭐

Add an input that lets the user choose how often to generate cards.

---

## 📚 Concepts Learned

### JavaScript
✅ `Math.random()` and `Math.floor()` for random numbers
✅ `querySelector()` to find elements within others
✅ `textContent` to change text
✅ `classList.add()` to manipulate CSS classes
✅ `addEventListener()` for events
✅ `setInterval()` and `clearInterval()` for timers
✅ `setTimeout()` for delays

### CSS
✅ Flexbox with `flex-direction: column`
✅ `transform: scale()` and `rotate()` for transformations
✅ `transition` for smooth animations
✅ Pseudo-classes `:hover` and `:active`
✅ `box-shadow` for shadows

### DOM
✅ Dynamic HTML manipulation
✅ Event-driven programming
✅ Separation of logic (reusable functions)

---

## 🎉 Congratulations!

You've built a complete interactive web application from scratch, step by step. You now understand:

- How to structure a web project
- How to make elements interactive
- How to generate random content
- How to use timers for automation
- How to create smooth animations

**Next challenge**: Customize the project with your own styles and features.

---

## 🔗 Additional Resources

- [MDN - Math.random()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
- [MDN - setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/setInterval)
- [CSS Tricks - Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [MDN - Transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)
