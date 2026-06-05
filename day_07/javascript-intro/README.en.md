[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Intro to JavaScript - Day 7

Incremental learning module covering the fundamentals of JavaScript for beginners.

## 📚 Module Structure

This module is organized into **5 progressive steps**, each focused on specific JavaScript concepts:

### Step 1: Variables and Data Types
- Variable declaration (`const`, `let`, `var`)
- Primitive data types (String, Number, Boolean)
- Basic arrays and objects
- Math operations and concatenation

### Step 2: Functions
- Function declarations
- Functions with parameters
- Functions that return values
- Function scope
- Anonymous functions
- Arrow functions
- Nested functions

### Step 3: Conditionals
- `if/else` statements
- Comparison operators (`===`, `!==`, `>`, `<`)
- Logical operators (`&&`, `||`, `!`)
- Switch statement
- Ternary operator
- Conditional rendering

### Step 4: Loops
- `for` loop
- `while` loop
- `for...of` (for arrays)
- `for...in` (for objects)
- `break` and `continue`
- Nested loops

### Step 5: Final Project - Interactive Calculator
A capstone project that combines **everything you've learned**:
- Global and local variables
- Functions with different purposes
- Conditionals for validation
- Switch for math operations
- Arrays for history
- Loops for rendering
- DOM manipulation

### Step 6: HTML + JavaScript Integration
How HTML, CSS, and JavaScript work together:
- Browser processing order
- Loading strategies: `defer`, `async`, `type="module"`
- Real-time DOM manipulation
- Events and binding functions
- Interactive demos of every concept

## 🚀 How to Use This Module

### 1. Start the Server

```bash
# Make sure you have Flask installed
pip3 install flask

# Start the server
python3 server.py
```

The server will be available at `http://localhost:3000`

### 2. Navigate the Exercises

1. Open your browser at `http://localhost:3000`
2. You'll see a home page with links to the 5 steps
3. Click each step to go to the matching exercise
4. **Important**: Open the browser console (F12) to see the results

### 3. Complete the Exercises

Each HTML file contains:
- **Demo examples**: Code that runs automatically
- **Hands-on exercises**: Sections marked with `// TODO:` that you need to complete
- **Bonus challenges**: More advanced exercises to practice

## 📖 Learning Methodology

### Incremental Approach
Each step builds on the previous one:
- **Step 1** → Variables (the foundation)
- **Step 2** → Functions (reusing code)
- **Step 3** → Conditionals (making decisions)
- **Step 4** → Loops (repeating tasks)
- **Step 5** → Project (putting it all together)

### Learn by Doing
1. **Read** the example code
2. **Observe** the results in the console
3. **Modify** values to experiment
4. **Complete** the TODO exercises
5. **Break** the code on purpose and learn from the errors

## 💡 Tips for Students

### Using the Browser Console
```javascript
// The console is your best friend
console.log("Hello World");

// Use console.log to debug
const number = 42;
console.log("The number is:", number);
```

### Common Mistakes
1. **Forgetting parentheses when calling functions**
   ```javascript
   greet    // ❌ Doesn't call the function
   greet()  // ✅ Correct
   ```

2. **Using `==` instead of `===`**
   ```javascript
   5 == "5"   // ❌ Avoid this
   5 === "5"  // ✅ Use this
   ```

3. **Confusing variable scope**
   ```javascript
   if (true) {
     let x = 5;
   }
   console.log(x);  // ❌ Error: x is not defined
   ```

### Experimentation
- Change values and see what happens
- Comment and uncomment lines of code
- Add your own `console.log()` calls to understand the flow
- Don't be afraid to break things — **you'll learn more from mistakes**

## 🎯 Learning Objectives

By the end of this module, you'll be able to:
- ✅ Declare and use variables correctly
- ✅ Create reusable functions
- ✅ Implement conditional logic
- ✅ Iterate over arrays and objects
- ✅ Combine every concept into a working project
- ✅ Debug code using the console

## 📝 Additional Resources

### Official Documentation
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [JavaScript.info](https://javascript.info/)

### Extra Practice
- [FreeCodeCamp - JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- [Exercism - JavaScript Track](https://exercism.org/tracks/javascript)

### Main Tutorial Concepts
For more in-depth theory, check the `../index.md` file in the `day_07` folder.

## 🔧 Troubleshooting

### The server won't start
```bash
# Make sure Flask is installed
pip3 install flask

# If you're on Python 2
pip install flask
```

### The page doesn't load
- Make sure you're in the right folder: `day_07/javascript-intro`
- Check that port 3000 isn't already in use
- Check the server console for errors

### Changes don't show up
- Reload the page with `Ctrl + Shift + R` (hard reload, no cache)
- The server disables caching automatically

## 🎓 For the Instructor

### Recommended Teaching Order
1. Live-demo each step
2. Explain concepts with visual examples
3. Give students time to experiment
4. Address specific questions
5. Review exercise solutions as a group

### Estimated Time
- Step 1: 30 minutes
- Step 2: 45 minutes
- Step 3: 45 minutes
- Step 4: 45 minutes
- Step 5: 60 minutes (project)
- **Total**: ~3.5 hours

### Key Concepts to Emphasize
- **const vs let**: Always default to `const`
- **=== vs ==**: Always use strict equality
- **Scope**: Difference between global and local
- **Functions**: The importance of reusing code
- **Debugging**: Use `console.log()` constantly

---

**Questions?** Check the main `day_07/index.md` file or ask in class.

Happy coding! 💻🚀
