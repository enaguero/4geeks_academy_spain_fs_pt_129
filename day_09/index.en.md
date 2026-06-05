[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 9: Arrays in JavaScript

## Why Do Arrays Deserve Their Own Lesson?

Imagine you need to store the names of all your students. You could do this:

```javascript
const student1 = "Ana";
const student2 = "Carlos";
const student3 = "María";
const student4 = "Juan";
const student5 = "Laura";
// ... and so on with 50 students? 😱
```

**There's a much better way!** **Arrays** (also called lists) let you store multiple values in a single variable:

```javascript
const students = ["Ana", "Carlos", "María", "Juan", "Laura"];
```

### Why Are They So Important?

1. **Organization**: Group related data in a single place
2. **Efficiency**: Easily handle hundreds or thousands of elements
3. **Iteration**: You can loop through every element automatically
4. **Manipulation**: Adding, removing, or modifying elements is simple
5. **Ubiquity**: Arrays are everywhere in programming

**Arrays are fundamental** because:
- Your to-do list: array
- Posts on social media: array
- Products in a shopping cart: array
- Search results: array
- Comments on a post: array

---

## How to Declare an Array?

There are two ways to create arrays in JavaScript:

### Way 1: Array Literal (Recommended) ✅

```javascript
const fruits = ["apple", "banana", "orange"];
const numbers = [1, 2, 3, 4, 5];
const mixed = ["text", 42, true, null];
const empty = [];
```

### Way 2: Array Constructor (Less common)

```javascript
const colors = new Array("red", "blue", "green");
const emptyNumbers = new Array(5);  // Creates array with 5 empty slots
```

**Recommendation**: Always use the literal form `[]` — it's shorter, clearer, and faster.

### Data Types in Arrays

Arrays can contain any data type, even **mixed**:

```javascript
const mixedArray = [
    "text",            // String
    42,                // Number
    true,              // Boolean
    null,              // Null
    undefined,         // Undefined
    [1, 2, 3],         // Array inside array
    { name: "Ana" }    // Object
];
```

---

## Indexes: The Key to Understanding Arrays

### What Is an Index?

An **index** is the **position** of an element within the array. **IMPORTANT!** Indexes start at **0**, not 1.

```javascript
const fruits = ["apple", "banana", "orange", "grape"];
//              ↓         ↓         ↓         ↓
//           index 0   index 1   index 2   index 3
```

### Full Visualization

```
┌───────────┬──────────┬──────────┬──────────┬──────────┐
│ Element   │  apple   │  banana  │  orange  │  grape   │
├───────────┼──────────┼──────────┼──────────┼──────────┤
│ Index     │    0     │    1     │    2     │    3     │
├───────────┼──────────┼──────────┼──────────┼──────────┤
│ Position  │ 1st      │ 2nd      │ 3rd      │ 4th      │
└───────────┴──────────┴──────────┴──────────┴──────────┘
```

### ⚠️ KEY Difference: Index vs Position

```javascript
const letters = ["A", "B", "C", "D"];
```

| Concept | "A" | "B" | "C" | "D" |
|---------|-----|-----|-----|-----|
| **Index** (programming) | 0 | 1 | 2 | 3 |
| **Position** (humans) | 1st | 2nd | 3rd | 4th |

**Remember**:
- **Index 0** = First element
- **Index 1** = Second element
- **Index 2** = Third element
- And so on...

### Practical Examples

```javascript
const days = ["monday", "tuesday", "wednesday", "thursday", "friday"];

console.log("Index 0:", days[0]);       // "monday" - first day
console.log("Index 2:", days[2]);       // "wednesday" - third day
console.log("Index 4:", days[4]);       // "friday" - fifth day

// Position is NOT the same as index
console.log("The 1st day is at index:", 0);
console.log("The 3rd day is at index:", 2);
```

---

## Accessing Array Elements

To get a specific element, we use **brackets `[]`** with the index:

```javascript
const colors = ["red", "blue", "green", "yellow"];

// Access by index
console.log(colors[0]);  // "red"    (first element)
console.log(colors[1]);  // "blue"   (second element)
console.log(colors[2]);  // "green"  (third element)
console.log(colors[3]);  // "yellow" (fourth element)

// What happens if we access an index that doesn't exist?
console.log(colors[10]); // undefined (no element at that index)
```

### Accessing the First Element

```javascript
const animals = ["dog", "cat", "parrot", "fish"];

const firstAnimal = animals[0];
console.log(firstAnimal);  // "dog"
```

### Accessing the Last Element

There are **two ways** to get the last element:

#### Option 1: Using `length - 1`

```javascript
const numbers = [10, 20, 30, 40, 50];

const lastNumber = numbers[numbers.length - 1];
console.log(lastNumber);  // 50
```

**Why `length - 1`?**
- `numbers.length` = 5 (total number of elements)
- Indexes go from 0 to 4
- The last index is: 5 - 1 = 4
- `numbers[4]` = 50

#### Option 2: Using `at(-1)` (Modern) ✨

```javascript
const numbers = [10, 20, 30, 40, 50];

const lastNumber = numbers.at(-1);
console.log(lastNumber);  // 50

// You can also access from the end
console.log(numbers.at(-2));  // 40 (second to last)
console.log(numbers.at(-3));  // 30 (third to last)
```

### Visual Comparison

```javascript
const letters = ["A", "B", "C", "D", "E"];
//               ↑               ↑         ↑
//            index 0        index 2   index 4 (last)

// First element
console.log(letters[0]);              // "A"
console.log(letters.at(0));           // "A"

// Last element
console.log(letters[letters.length - 1]);  // "E"
console.log(letters.at(-1));               // "E" ✅ Simpler!
```

### Summary Table: Accessing Elements

| What you want | Syntax | Example |
|---------------|--------|---------|
| **First element** | `array[0]` | `fruits[0]` |
| **Second element** | `array[1]` | `fruits[1]` |
| **Specific element** | `array[index]` | `fruits[3]` |
| **Last element** | `array[array.length - 1]` | `fruits[fruits.length - 1]` |
| **Last element (modern)** | `array.at(-1)` | `fruits.at(-1)` ✅ |
| **Second to last element** | `array.at(-2)` | `fruits.at(-2)` |

---

## Updating Array Elements

You can **modify** existing elements by assigning them a new value:

```javascript
const fruits = ["apple", "banana", "orange"];

console.log(fruits);  // ["apple", "banana", "orange"]

// Change the second element (index 1)
fruits[1] = "strawberry";

console.log(fruits);  // ["apple", "strawberry", "orange"]
```

### Practical Example: Updating Grades

```javascript
const grades = [85, 90, 78, 92];

console.log("Before:", grades);  // [85, 90, 78, 92]

// The teacher corrected the third grade (index 2)
grades[2] = 88;

console.log("After:", grades);  // [85, 90, 88, 92]
```

### ⚠️ Arrays with `const`

Even though you declare an array with `const`, **you can modify its elements**:

```javascript
const numbers = [1, 2, 3];

numbers[0] = 100;  // ✅ Works
console.log(numbers);  // [100, 2, 3]

numbers = [4, 5, 6];  // ❌ Error: cannot reassign the whole array
```

**Why?**
- `const` protects the array's **reference** (you can't assign a new array to it)
- It does NOT protect the array's **contents** (you can change its elements)

---

## Adding Elements: The `push()` Function

The `push()` function **adds one or more elements to the end** of the array.

### Syntax

```javascript
array.push(element1, element2, ...);
```

### Basic Example

```javascript
const tasks = ["study", "exercise"];

console.log(tasks);  // ["study", "exercise"]

// Add a task
tasks.push("read book");

console.log(tasks);  // ["study", "exercise", "read book"]
```

### Adding Multiple Elements

```javascript
const numbers = [1, 2, 3];

numbers.push(4, 5, 6);

console.log(numbers);  // [1, 2, 3, 4, 5, 6]
```

### Return Value

`push()` returns the **new length** of the array:

```javascript
const fruits = ["apple"];

const newLength = fruits.push("banana", "orange");

console.log(newLength);  // 3
console.log(fruits);     // ["apple", "banana", "orange"]
```

### Practical Example: Shopping Cart

```javascript
const cart = [];

console.log("Empty cart:", cart);  // []

cart.push("Laptop");
console.log("Cart:", cart);  // ["Laptop"]

cart.push("Mouse", "Keyboard");
console.log("Cart:", cart);  // ["Laptop", "Mouse", "Keyboard"]

cart.push("Monitor");
console.log("Final cart:", cart);  // ["Laptop", "Mouse", "Keyboard", "Monitor"]
```

---

## Removing Elements: The `pop()` Function

The `pop()` function **removes and returns the last element** of the array.

### Syntax

```javascript
const removedElement = array.pop();
```

### Basic Example

```javascript
const fruits = ["apple", "banana", "orange"];

console.log("Before:", fruits);  // ["apple", "banana", "orange"]

const removedFruit = fruits.pop();

console.log("Removed:", removedFruit);  // "orange"
console.log("After:", fruits);          // ["apple", "banana"]
```

### Pop on an Empty Array

```javascript
const empty = [];
const result = empty.pop();

console.log(result);  // undefined
console.log(empty);   // []
```

### Practical Example: Stack of Books

```javascript
const bookStack = ["Book 1", "Book 2", "Book 3", "Book 4"];

console.log("Stack:", bookStack);  // ["Book 1", "Book 2", "Book 3", "Book 4"]

// Take the top book
const book = bookStack.pop();
console.log("Took:", book);        // "Book 4"
console.log("Stack:", bookStack);  // ["Book 1", "Book 2", "Book 3"]

// Take another book
const anotherBook = bookStack.pop();
console.log("Took:", anotherBook);  // "Book 3"
console.log("Stack:", bookStack);   // ["Book 1", "Book 2"]
```

---

## Adding/Removing from the Beginning

### `unshift()`: Add to the Beginning

Adds one or more elements to the **beginning** of the array:

```javascript
const numbers = [2, 3, 4];

console.log("Before:", numbers);  // [2, 3, 4]

numbers.unshift(1);

console.log("After:", numbers);  // [1, 2, 3, 4]
```

### Adding Multiple Elements to the Beginning

```javascript
const letters = ["C", "D"];

letters.unshift("A", "B");

console.log(letters);  // ["A", "B", "C", "D"]
```

### `shift()`: Remove from the Beginning

Removes and returns the **first element** of the array:

```javascript
const tasks = ["wash dishes", "study", "exercise"];

console.log("Before:", tasks);  // ["wash dishes", "study", "exercise"]

const completedTask = tasks.shift();

console.log("Completed:", completedTask);  // "wash dishes"
console.log("After:", tasks);              // ["study", "exercise"]
```

### Visual Comparison: push vs unshift / pop vs shift

```javascript
const array = [2, 3, 4];

// ADD
array.push(5);     // [2, 3, 4, 5]    → Adds to the END
array.unshift(1);  // [1, 2, 3, 4, 5] → Adds to the BEGINNING

// REMOVE
array.pop();       // [1, 2, 3, 4]    → Removes from the END
array.shift();     // [2, 3, 4]       → Removes from the BEGINNING
```

### Summary Table: Modification Methods

| Method | What it does | Where it acts | Returns | Example |
|--------|--------------|---------------|---------|---------|
| **push()** | Adds element(s) | End | New length | `arr.push(5)` |
| **pop()** | Removes element | End | Removed element | `arr.pop()` |
| **unshift()** | Adds element(s) | Beginning | New length | `arr.unshift(1)` |
| **shift()** | Removes element | Beginning | Removed element | `arr.shift()` |

---

## Looping Through an Array

There are several ways to iterate through all the elements of an array.

### Method 1: Traditional `for`

```javascript
const fruits = ["apple", "banana", "orange"];

for (let i = 0; i < fruits.length; i++) {
    console.log(`Index ${i}: ${fruits[i]}`);
}

// Output:
// Index 0: apple
// Index 1: banana
// Index 2: orange
```

**Advantages**: You have explicit access to the index.

### Method 2: `for...of` (Recommended for Arrays) ✅

```javascript
const fruits = ["apple", "banana", "orange"];

for (const fruit of fruits) {
    console.log(fruit);
}

// Output:
// apple
// banana
// orange
```

**Advantages**: Simpler and clearer syntax.

### Method 3: `forEach()` (Modern)

```javascript
const fruits = ["apple", "banana", "orange"];

fruits.forEach(function(fruit, index) {
    console.log(`${index}: ${fruit}`);
});

// Output:
// 0: apple
// 1: banana
// 2: orange
```

**With arrow function** (more modern):

```javascript
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```

### Practical Example: Sum All Numbers

```javascript
const numbers = [10, 20, 30, 40, 50];
let sum = 0;

for (const number of numbers) {
    sum += number;
}

console.log("Total sum:", sum);  // 150
```

### Practical Example: Filter Elements

```javascript
const grades = [85, 92, 78, 95, 88, 76];

console.log("Passing grades (>= 80):");

for (const grade of grades) {
    if (grade >= 80) {
        console.log(grade);
    }
}

// Output:
// 85
// 92
// 95
// 88
```

---

## `for...in` vs `for...of`

### ⚠️ IMPORTANT Difference

```javascript
const colors = ["red", "blue", "green"];

// for...in → Iterates over INDEXES (not recommended for arrays)
for (const index in colors) {
    console.log(index);  // "0", "1", "2" (strings!)
}

// for...of → Iterates over VALUES ✅ (recommended)
for (const color of colors) {
    console.log(color);  // "red", "blue", "green"
}
```

### When to Use Each One

| Loop | For | Iterates over | Example |
|------|-----|---------------|---------|
| **for...of** | Arrays | Values | `for (const item of array)` ✅ |
| **for...in** | Objects | Properties (keys) | `for (const key in object)` ✅ |

**Recommendation**: For arrays, use **`for...of`**, NOT `for...in`.

### Example with an Object (for...in)

```javascript
const person = {
    name: "Ana",
    age: 25,
    city: "Madrid"
};

for (const property in person) {
    console.log(`${property}: ${person[property]}`);
}

// Output:
// name: Ana
// age: 25
// city: Madrid
```

---

## Removing Specific Elements

### Method 1: `splice()` (Modifies the original array)

`splice()` can **add, remove, or replace** elements at any position.

#### Syntax

```javascript
array.splice(start, deleteCount, newElement1, newElement2, ...);
```

#### Removing Elements

```javascript
const fruits = ["apple", "banana", "orange", "grape", "watermelon"];
//              ↓        ↓         ↓         ↓        ↓
//           index 0  index 1   index 2   index 3  index 4

// Remove "orange" (index 2) - remove 1 element
fruits.splice(2, 1);

console.log(fruits);  // ["apple", "banana", "grape", "watermelon"]
```

#### Removing Multiple Elements

```javascript
const numbers = [1, 2, 3, 4, 5, 6];

// Starting from index 2, remove 3 elements
numbers.splice(2, 3);

console.log(numbers);  // [1, 2, 6]
```

#### Replacing Elements

```javascript
const days = ["monday", "tuesday", "wednesday", "thursday"];

// Starting from index 1, remove 2 elements and add "TUESDAY", "WEDNESDAY"
days.splice(1, 2, "TUESDAY", "WEDNESDAY");

console.log(days);  // ["monday", "TUESDAY", "WEDNESDAY", "thursday"]
```

#### Adding Without Removing

```javascript
const letters = ["A", "B", "D"];

// At index 2, remove 0 elements and add "C"
letters.splice(2, 0, "C");

console.log(letters);  // ["A", "B", "C", "D"]
```

### Method 2: `slice()` (Does NOT modify the original array)

`slice()` **creates a copy** of a portion of the array.

#### Syntax

```javascript
const newArray = array.slice(start, end);
```

- `start`: Index to start from (included)
- `end`: Index to end at (**NOT included**)

#### Examples

```javascript
const fruits = ["apple", "banana", "orange", "grape", "watermelon"];
//              ↓        ↓         ↓         ↓        ↓
//           index 0  index 1   index 2   index 3  index 4

// From index 1 to 3 (does NOT include 3)
const someFruits = fruits.slice(1, 3);

console.log(someFruits);  // ["banana", "orange"]
console.log(fruits);      // ["apple", "banana", "orange", "grape", "watermelon"] (unchanged)
```

#### Copy the Entire Array

```javascript
const original = [1, 2, 3];
const copy = original.slice();

console.log(copy);  // [1, 2, 3]

copy.push(4);
console.log(original);  // [1, 2, 3] (original unchanged)
console.log(copy);      // [1, 2, 3, 4]
```

#### From an Index to the End

```javascript
const numbers = [10, 20, 30, 40, 50];

const last = numbers.slice(2);  // From index 2 to the end

console.log(last);  // [30, 40, 50]
```

#### With Negative Indexes

```javascript
const letters = ["A", "B", "C", "D", "E"];

const lastTwo = letters.slice(-2);  // Last 2 elements

console.log(lastTwo);  // ["D", "E"]
```

### Comparison Table: `splice()` vs `slice()`

| Aspect | `splice()` | `slice()` |
|--------|------------|-----------|
| **Modifies original** | ✅ Yes | ❌ No |
| **Returns** | Removed elements | New copy |
| **For** | Modifying array | Copying portion |
| **Can add** | ✅ Yes | ❌ No |
| **Syntax** | `splice(start, count, ...elements)` | `slice(start, end)` |

### Complete Example

```javascript
const tasks = ["sleep", "study", "eat", "exercise", "read"];

console.log("Original:", tasks);

// slice: copy elements 1 to 3 (does NOT modify original)
const some = tasks.slice(1, 3);
console.log("Copy (slice):", some);  // ["study", "eat"]
console.log("Original:", tasks);     // Unchanged

// splice: remove "eat" (index 2)
tasks.splice(2, 1);
console.log("After splice:", tasks);  // ["sleep", "study", "exercise", "read"]

// splice: add "work" at index 2
tasks.splice(2, 0, "work");
console.log("After adding:", tasks);  // ["sleep", "study", "work", "exercise", "read"]
```

---

## Sorting Arrays: `sort()`

The `sort()` method sorts the elements of an array **alphabetically** by default.

### Sorting Strings

```javascript
const fruits = ["orange", "apple", "grape", "banana"];

fruits.sort();

console.log(fruits);  // ["apple", "banana", "grape", "orange"]
```

### ⚠️ Problem with Numbers

```javascript
const numbers = [10, 5, 40, 25, 1000, 1];

numbers.sort();

console.log(numbers);  // [1, 10, 1000, 25, 40, 5] ❌ Incorrect!
```

**Why?** `sort()` converts numbers to strings and sorts them alphabetically: "1", "10", "1000", "25", etc.

### Solution: Comparison Function

To sort numbers correctly, use a **comparison function**:

```javascript
const numbers = [10, 5, 40, 25, 1000, 1];

// Ascending order (smallest to largest)
numbers.sort(function(a, b) {
    return a - b;
});

console.log(numbers);  // [1, 5, 10, 25, 40, 1000] ✅
```

**With arrow function** (shorter):

```javascript
numbers.sort((a, b) => a - b);  // Ascending
```

### Descending Order

```javascript
const numbers = [10, 5, 40, 25, 1000, 1];

// Descending order (largest to smallest)
numbers.sort((a, b) => b - a);

console.log(numbers);  // [1000, 40, 25, 10, 5, 1]
```

### How the Comparison Function Works

```javascript
function compare(a, b) {
    // If it returns negative: a goes before b
    // If it returns positive: b goes before a
    // If it returns 0: order doesn't change
    return a - b;
}
```

### Sorting Objects by Property

```javascript
const students = [
    { name: "Ana", age: 22 },
    { name: "Carlos", age: 19 },
    { name: "María", age: 25 }
];

// Sort by age
students.sort((a, b) => a.age - b.age);

console.log(students);
// [
//   { name: "Carlos", age: 19 },
//   { name: "Ana", age: 22 },
//   { name: "María", age: 25 }
// ]
```

### Reverse Alphabetical Order

```javascript
const names = ["Carlos", "Ana", "María", "Beatriz"];

names.sort();  // Normal alphabetical order
console.log(names);  // ["Ana", "Beatriz", "Carlos", "María"]

names.reverse();  // Reverse the order
console.log(names);  // ["María", "Carlos", "Beatriz", "Ana"]
```

### Summary Table: `sort()`

| Data type | Syntax | Order |
|-----------|--------|-------|
| **Strings** | `array.sort()` | Alphabetical A-Z |
| **Strings reversed** | `array.sort().reverse()` | Alphabetical Z-A |
| **Numbers ascending** | `array.sort((a, b) => a - b)` | Smallest to largest |
| **Numbers descending** | `array.sort((a, b) => b - a)` | Largest to smallest |
| **Objects by property** | `array.sort((a, b) => a.prop - b.prop)` | By property |

---

## Useful Array Methods

### `length`: Get Length

```javascript
const fruits = ["apple", "banana", "orange"];

console.log(fruits.length);  // 3
```

### `includes()`: Check if It Exists

```javascript
const numbers = [1, 2, 3, 4, 5];

console.log(numbers.includes(3));   // true
console.log(numbers.includes(10));  // false
```

### `indexOf()`: Find Index

```javascript
const colors = ["red", "blue", "green", "yellow"];

console.log(colors.indexOf("green"));   // 2
console.log(colors.indexOf("orange"));  // -1 (doesn't exist)
```

### `join()`: Convert to String

```javascript
const words = ["Hello", "world", "from", "JavaScript"];

const phrase = words.join(" ");
console.log(phrase);  // "Hello world from JavaScript"

const withCommas = words.join(", ");
console.log(withCommas);  // "Hello, world, from, JavaScript"
```

### `concat()`: Join Arrays

```javascript
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const array3 = [7, 8, 9];

const combined = array1.concat(array2, array3);
console.log(combined);  // [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### `reverse()`: Reverse Order

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.reverse();
console.log(numbers);  // [5, 4, 3, 2, 1]
```

### `find()`: Find First Element That Meets a Condition

```javascript
const numbers = [5, 12, 8, 130, 44];

const found = numbers.find(num => num > 10);
console.log(found);  // 12 (first number greater than 10)
```

### `filter()`: Filter Elements

```javascript
const numbers = [5, 12, 8, 130, 44];

const greaterThan10 = numbers.filter(num => num > 10);
console.log(greaterThan10);  // [12, 130, 44]
```

### `map()`: Transform Elements

```javascript
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(num => num * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]
```

### `reduce()`: Reduce to a Single Value

```javascript
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((accumulator, num) => accumulator + num, 0);
console.log(sum);  // 15
```

---

## Summary Table: Array Methods

| Method | What it does | Modifies original | Example |
|--------|--------------|-------------------|---------|
| **push()** | Adds to end | ✅ Yes | `arr.push(5)` |
| **pop()** | Removes from end | ✅ Yes | `arr.pop()` |
| **unshift()** | Adds to beginning | ✅ Yes | `arr.unshift(1)` |
| **shift()** | Removes from beginning | ✅ Yes | `arr.shift()` |
| **splice()** | Adds/removes/replaces | ✅ Yes | `arr.splice(2, 1)` |
| **slice()** | Copies portion | ❌ No | `arr.slice(1, 3)` |
| **sort()** | Sorts elements | ✅ Yes | `arr.sort((a,b) => a-b)` |
| **reverse()** | Reverses order | ✅ Yes | `arr.reverse()` |
| **concat()** | Joins arrays | ❌ No | `arr1.concat(arr2)` |
| **join()** | Converts to string | ❌ No | `arr.join(", ")` |
| **includes()** | Checks if exists | ❌ No | `arr.includes(3)` |
| **indexOf()** | Finds index | ❌ No | `arr.indexOf("red")` |
| **find()** | First element matching | ❌ No | `arr.find(x => x > 10)` |
| **filter()** | Filters elements | ❌ No | `arr.filter(x => x > 10)` |
| **map()** | Transforms elements | ❌ No | `arr.map(x => x * 2)` |
| **forEach()** | Iterates elements | ❌ No | `arr.forEach(x => {...})` |

---

## Practical Exercises

### Exercise 1: Shopping List

Create an empty array `shoppingList` and:
1. Add "milk", "bread", and "eggs"
2. Add "apples" at the beginning
3. Remove the last element
4. Print the complete array

```javascript
const shoppingList = [];

// Your code here
```

<details>
<summary>See solution</summary>

```javascript
const shoppingList = [];

shoppingList.push("milk", "bread", "eggs");
console.log(shoppingList);  // ["milk", "bread", "eggs"]

shoppingList.unshift("apples");
console.log(shoppingList);  // ["apples", "milk", "bread", "eggs"]

shoppingList.pop();
console.log(shoppingList);  // ["apples", "milk", "bread"]
```
</details>

### Exercise 2: Grades

Given the array `grades = [78, 92, 85, 88, 95, 73]`:
1. Print the first grade
2. Print the last grade
3. Calculate the average
4. Find how many grades are greater than 80

```javascript
const grades = [78, 92, 85, 88, 95, 73];

// Your code here
```

<details>
<summary>See solution</summary>

```javascript
const grades = [78, 92, 85, 88, 95, 73];

// 1. First grade
console.log("First:", grades[0]);  // 78

// 2. Last grade
console.log("Last:", grades[grades.length - 1]);  // 73
// or using at():
console.log("Last:", grades.at(-1));  // 73

// 3. Average
let sum = 0;
for (const grade of grades) {
    sum += grade;
}
const average = sum / grades.length;
console.log("Average:", average);  // 85.16...

// 4. Greater than 80
const greaterThan80 = grades.filter(grade => grade > 80);
console.log("Greater than 80:", greaterThan80.length);  // 4
```
</details>

### Exercise 3: Names in Order

Given `names = ["Carlos", "Ana", "Beatriz", "David"]`:
1. Sort alphabetically
2. Print in reverse order
3. Find the index of "Beatriz"

```javascript
const names = ["Carlos", "Ana", "Beatriz", "David"];

// Your code here
```

<details>
<summary>See solution</summary>

```javascript
const names = ["Carlos", "Ana", "Beatriz", "David"];

// 1. Sort alphabetically
names.sort();
console.log("Sorted:", names);  // ["Ana", "Beatriz", "Carlos", "David"]

// 2. Reverse order
names.reverse();
console.log("Reversed:", names);  // ["David", "Carlos", "Beatriz", "Ana"]

// 3. Index of "Beatriz"
const index = names.indexOf("Beatriz");
console.log("Index of Beatriz:", index);  // 2
```
</details>

### Exercise 4: Filter Even Numbers

Given `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, create a new array with only even numbers.

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Your code here
```

<details>
<summary>See solution</summary>

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const evens = numbers.filter(num => num % 2 === 0);
console.log(evens);  // [2, 4, 6, 8, 10]

// Alternative with for...of
const evensAlt = [];
for (const num of numbers) {
    if (num % 2 === 0) {
        evensAlt.push(num);
    }
}
console.log(evensAlt);  // [2, 4, 6, 8, 10]
```
</details>

### Exercise 5: Double Values

Given `prices = [10, 20, 30, 40]`, create a new array with all the prices doubled.

```javascript
const prices = [10, 20, 30, 40];

// Your code here
```

<details>
<summary>See solution</summary>

```javascript
const prices = [10, 20, 30, 40];

const doubled = prices.map(price => price * 2);
console.log(doubled);  // [20, 40, 60, 80]
```
</details>

---

## Integration Project: Student Manager

Build a system to manage students with the following features:

```javascript
const students = [];

// Functions to implement:

function addStudent(name) {
    // Add student to the array
}

function removeStudent(name) {
    // Find and remove student
}

function findStudent(name) {
    // Check if student exists
}

function listStudents() {
    // Print all students
}

function sortedStudents() {
    // Return students in alphabetical order
}

// Tests
addStudent("Ana");
addStudent("Carlos");
addStudent("Beatriz");
listStudents();
console.log("Is Carlos there?", findStudent("Carlos"));
removeStudent("Carlos");
console.log("Sorted:", sortedStudents());
```

<details>
<summary>See full solution</summary>

```javascript
const students = [];

function addStudent(name) {
    students.push(name);
    console.log(`✅ ${name} added`);
}

function removeStudent(name) {
    const index = students.indexOf(name);
    if (index !== -1) {
        students.splice(index, 1);
        console.log(`❌ ${name} removed`);
    } else {
        console.log(`⚠️ ${name} not found`);
    }
}

function findStudent(name) {
    return students.includes(name);
}

function listStudents() {
    console.log("\n📋 Student list:");
    students.forEach((student, index) => {
        console.log(`${index + 1}. ${student}`);
    });
}

function sortedStudents() {
    return [...students].sort();  // Copy to avoid modifying original
}

// Tests
addStudent("Ana");
addStudent("Carlos");
addStudent("Beatriz");
addStudent("David");

listStudents();
// 📋 Student list:
// 1. Ana
// 2. Carlos
// 3. Beatriz
// 4. David

console.log("Is Carlos there?", findStudent("Carlos"));  // true
console.log("Is María there?", findStudent("María"));    // false

removeStudent("Carlos");  // ❌ Carlos removed
removeStudent("Pedro");   // ⚠️ Pedro not found

console.log("Sorted:", sortedStudents());  // ["Ana", "Beatriz", "David"]

listStudents();
// 📋 Student list:
// 1. Ana
// 2. Beatriz
// 3. David
```
</details>

---

## Conclusion

**Arrays** are one of the most important data structures in JavaScript. Mastering them will let you:

✅ Manage data collections efficiently
✅ Build dynamic and interactive applications
✅ Manipulate lists (tasks, products, users, etc.)
✅ Process large amounts of information
✅ Get ready for more advanced concepts (objects, APIs, etc.)

### Key Points to Remember

1. **Indexes start at 0** — The first element is at `array[0]`
2. **Index ≠ Position** — Index 0 is position 1
3. **Last element**: `array[array.length - 1]` or `array.at(-1)`
4. **`push()` / `pop()`**: Add/remove from the end
5. **`unshift()` / `shift()`**: Add/remove from the beginning
6. **`splice()`**: Modifies the original
7. **`slice()`**: Creates a copy
8. **`for...of`**: The best way to iterate arrays
9. **`sort()`**: Use a comparison function for numbers
10. **Advanced methods**: `map()`, `filter()`, `reduce()`

### Next Steps

Now that you've mastered arrays:
1. Practice the exercises daily
2. Combine arrays with functions
3. Explore arrays of objects
4. Learn about multidimensional arrays
5. Get ready to work with APIs (which return arrays)

**Keep practicing! 🚀** Arrays are fundamental in modern web development.

---

## Additional Resources

- **MDN Web Docs - Arrays**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
- **JavaScript.info - Arrays**: https://javascript.info/array
- **Array methods visualizer**: https://arrayexplorer.netlify.app/

---

## Cheat Sheet: Arrays in JavaScript

```javascript
// CREATE
const array = [1, 2, 3];
const empty = [];

// ACCESS
array[0]              // First element
array[array.length-1] // Last element
array.at(-1)          // Last element (modern)

// MODIFY
array[0] = 100;       // Change element

// ADD
array.push(4);        // End: [1, 2, 3, 4]
array.unshift(0);     // Beginning: [0, 1, 2, 3, 4]

// REMOVE
array.pop();          // Removes from end
array.shift();        // Removes from beginning
array.splice(2, 1);   // Removes at specific index

// ITERATE
for (const item of array) { ... }
array.forEach(item => { ... })

// SORT
array.sort((a, b) => a - b);  // Numbers ascending
array.reverse();               // Reverse

// SEARCH
array.includes(3);    // Exists?
array.indexOf(3);     // At which index?
array.find(x => ...)  // First element matching

// FILTER/TRANSFORM
array.filter(x => x > 2);  // Filter
array.map(x => x * 2);     // Transform
array.slice(1, 3);         // Copy portion

// OTHERS
array.length          // Length
array.join(", ")      // Convert to string
arr1.concat(arr2)     // Join arrays
```
