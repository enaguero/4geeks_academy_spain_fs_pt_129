[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 10: Good Practices and Code Standards

## Why Are Code Standards Important?

Imagine you walk into a kitchen where:

- The ingredients have no labels
- The knives are mixed in with the spoons
- There are no written recipes — everything is in the chef's memory
- Every cook organizes things differently

**Could you cook efficiently?** Probably not. The same goes for code.

### The Real Cost of Bad Practices

Bad practices don't just make code hard to read — they **cost real money** and can cause disasters:

#### Real Cases of Disasters Caused by Bad Code

**1. NASA Mars Climate Orbiter (1999) - $320 million lost** 💸

- **Problem**: One team used the metric system, another the imperial system
- **Result**: The space probe was lost on Mars
- **Root cause**: Lack of consistent standards in the code

**2. ESA's Ariane 5 Rocket (1996) - $370 million lost** 🚀

- **Problem**: Poorly written code, hard to read
- **Result**: The rocket exploded 40 seconds after launch
- **Root cause**: A data conversion error not caught due to illegible code

**3. U.S. Stock Market Flash Crash (2010)** 📉

- **Problem**: Complex code without good practices
- **Result**: Massive financial losses in minutes
- **Root cause**: Systems without proper error handling

### Data That Matters

Studies show that:

- ✅ Developers who use good practices are **40% more productive**
- ✅ Code with good practices is **50% cheaper to maintain**
- ❌ 70% of development time is spent **reading** code, not writing it

> "I'm not a great programmer; I'm just a good programmer with great habits." — Kent Beck

---

## 1. Global Variables: The Silent Enemy

### ❌ Bad Practice: Using Global Variables

**Global variables** are variables accessible from anywhere in the code.

```javascript
// ❌ BAD: Global variables
let userAge = 25;
let userName = 'Carlos';
let isLoggedIn = false;

function login(name) {
  userName = name;
  isLoggedIn = true;
  console.log(`${userName} has logged in`);
}

function updateAge(age) {
  userAge = age;
}

function displayUser() {
  console.log(`${userName}, ${userAge} years old`);
}

login('Ana');
updateAge(30);
displayUser();
```

### Why Is It Bad?

| Problem                       | Description                                  | Consequence                            |
| ----------------------------- | -------------------------------------------- | -------------------------------------- |
| **Hard-to-track bugs**        | Any function can modify the variable         | You don't know which function caused it |
| **Naming conflicts**          | Different parts of the code use the same name | Accidental overwrites                  |
| **Hard to test**              | Functions depend on global state             | You can't test functions in isolation  |
| **Side effects**              | Changing one variable affects the whole program | Unpredictable behavior              |
| **Not scalable**              | Hard to maintain on large projects           | Code becomes unmanageable              |

### Real Problem Example

```javascript
// ❌ DISASTER WAITING TO HAPPEN
let total = 0;

function calculateDiscount(price) {
  total = price * 0.9; // Modifies global variable
  return total;
}

function calculateTax(price) {
  total = price * 1.21; // Overwrites the previous total!
  return total;
}

// User wants discount + tax
const priceWithDiscount = calculateDiscount(100); // total = 90
const finalPrice = calculateTax(priceWithDiscount); // total = 108.9

console.log(total); // 108.9 — the discount was lost!
```

### ✅ Good Practice: Use Parameters and Return Values

```javascript
// ✅ GOOD: No global variables
function login(name) {
  return {
    userName: name,
    isLoggedIn: true,
    timestamp: Date.now(),
  };
}

function updateAge(user, age) {
  return {
    ...user,
    age: age,
  };
}

function displayUser(user) {
  console.log(`${user.userName}, ${user.age} years old`);
}

// Usage
let currentUser = login('Ana');
currentUser = updateAge(currentUser, 30);
displayUser(currentUser);
```

### Advantages of Avoiding Global Variables

✅ **Predictable**: Each function only modifies what it receives
✅ **Testable**: You can test functions independently
✅ **Maintainable**: Easy to find where each variable is used
✅ **No side effects**: One function doesn't affect others
✅ **Reusable**: Functions work in any context

### Corrected Example: Discount System

```javascript
// ✅ GOOD: Pure functions without global variables
function calculateDiscount(price, percentage) {
  return price * (1 - percentage / 100);
}

function calculateTax(price, taxRate) {
  return price * (1 + taxRate / 100);
}

function calculateFinalPrice(price, discount, tax) {
  const priceWithDiscount = calculateDiscount(price, discount);
  const priceWithTax = calculateTax(priceWithDiscount, tax);
  return priceWithTax;
}

// Clear, predictable usage
const finalPrice = calculateFinalPrice(100, 10, 21);
console.log(finalPrice); // 108.9 — correct!
```

---

## 2. Variable Names: Your Code Should Speak

### ❌ Bad Practice: Cryptic or Non-descriptive Names

```javascript
// ❌ BAD: Meaningless names
let x = 25;
let y = 'Juan';
let z = true;
let temp = 1000;
let data = [];
let n = 0;
let a, b, c;

function calc(p, q) {
  let r = p * q;
  return r;
}

// What does this do? 🤔
for (let i = 0; i < data.length; i++) {
  if (data[i] > temp) {
    n++;
  }
}
```

### Why Is It Bad?

| Problem                   | Example               | Impact                            |
| ------------------------- | --------------------- | --------------------------------- |
| **You don't know what it holds** | `let x = 25`          | Age? Price? Temperature?         |
| **Wasted time**           | `function calc(p, q)` | You have to read the whole function |
| **Hard to maintain**      | `let temp = 1000`     | Temporary? Temperature? Limit?    |
| **Errors when modifying** | `a, b, c`             | You easily mix up variables       |

### Real Example: Illegible Code

```javascript
// ❌ MAINTENANCE NIGHTMARE
function proc(u) {
  let t = 0;
  for (let i = 0; i < u.o.length; i++) {
    t += u.o[i].p * u.o[i].q;
  }
  if (u.m) {
    t *= 0.9;
  }
  return t;
}

const r = proc({
  n: 'Ana',
  m: true,
  o: [
    { p: 100, q: 2 },
    { p: 50, q: 1 },
  ],
});
```

**Can you understand what this function does in 5 seconds?** Probably not.

### ✅ Good Practice: Descriptive and Clear Names

```javascript
// ✅ GOOD: Names that explain their purpose
let customerAge = 25;
let customerName = 'Juan';
let isAuthenticated = true;
let maximumPrice = 1000;
let products = [];
let itemCount = 0;

function calculateTotalPrice(basePrice, quantity) {
  const totalPrice = basePrice * quantity;
  return totalPrice;
}

// Now it's obvious what this does
for (let i = 0; i < products.length; i++) {
  if (products[i].price > maximumPrice) {
    itemCount++;
  }
}
```

### Naming Conventions in JavaScript

#### 1. **Variables and Functions**: camelCase

```javascript
// ✅ Variables
let firstName = 'María';
let productPrice = 99.99;
let isAvailable = true;
let orderTotal = 0;

// ✅ Functions
function calculateDiscount() {}
function getUserById() {}
function processPayment() {}
```

#### 2. **Constants**: UPPER_SNAKE_CASE

```javascript
// ✅ Constants
const MAX_USERS = 100;
const API_KEY = 'abc123';
const TAX_RATE = 0.21;
const DATABASE_URL = 'https://api.example.com';
```

#### 3. **Classes**: PascalCase

```javascript
// ✅ Classes
class UserAccount {}
class ShoppingCart {}
class ProductCatalog {}
```

### Golden Rules for Variable Names

| Rule                      | ❌ Bad              | ✅ Good                         |
| ------------------------- | ------------------- | ------------------------------- |
| **Be descriptive**        | `let d = 10`        | `let daysUntilDelivery = 10`    |
| **Avoid abbreviations**   | `let usrNm = "Ana"` | `let userName = "Ana"`          |
| **Don't use single letters** | `let x, y, z`    | `let width, height, depth`      |
| **Indicate the type**     | `let data`          | `let userList` or `let userData` |
| **Use full names**        | `let prod`          | `let product`                   |
| **Avoid numbers**         | `let user1, user2`  | `let currentUser, previousUser` |

### Corrected Example: Readable Code

```javascript
// ✅ SELF-EXPLANATORY CODE
function calculateOrderTotal(customer) {
  let orderTotal = 0;

  for (let i = 0; i < customer.orders.length; i++) {
    const order = customer.orders[i];
    orderTotal += order.price * order.quantity;
  }

  if (customer.isMember) {
    orderTotal *= 0.9; // 10% discount for members
  }

  return orderTotal;
}

const totalPrice = calculateOrderTotal({
  name: 'Ana',
  isMember: true,
  orders: [
    { price: 100, quantity: 2 },
    { price: 50, quantity: 1 },
  ],
});

console.log(totalPrice); // 225
```

### Function Names: Should Describe the Action

```javascript
// ❌ BAD: Vague verbs or no verbs
function user(id) {}
function data() {}
function process(x) {}

// ✅ GOOD: Verb + noun
function getUser(id) {}
function fetchUserData() {}
function processPayment(transaction) {}
function validateEmail(email) {}
function calculateTotalPrice(items) {}
```

### Common Verbs Table

| Action        | Verb                   | Example                                |
| ------------- | ---------------------- | -------------------------------------- |
| Get data      | `get`, `fetch`         | `getUserById()`, `fetchProducts()`     |
| Create        | `create`, `add`        | `createAccount()`, `addToCart()`       |
| Update        | `update`, `set`        | `updateProfile()`, `setPrice()`        |
| Delete        | `delete`, `remove`     | `deleteUser()`, `removeItem()`         |
| Validate      | `validate`, `check`    | `validateForm()`, `checkPassword()`    |
| Calculate     | `calculate`, `compute` | `calculateTotal()`, `computeAverage()` |
| Display       | `show`, `display`      | `showModal()`, `displayResults()`      |

---

## 3. Indentation: The Visual Architecture of Code

### ❌ Bad Practice: Code Without Indentation

```javascript
// ❌ NIGHTMARE: No indentation
function processOrder(order) {
  if (order.items.length > 0) {
    let total = 0;
    for (let i = 0; i < order.items.length; i++) {
      if (order.items[i].price > 0) {
        total += order.items[i].price;
      }
    }
    if (order.customer.isMember) {
      total *= 0.9;
    }
    return total;
  }
  return 0;
}
```

**Can you tell where each block starts and ends?** It's almost impossible.

### ✅ Good Practice: Consistent Indentation

```javascript
// ✅ CLEAR: Proper indentation
function processOrder(order) {
  if (order.items.length > 0) {
    let total = 0;

    for (let i = 0; i < order.items.length; i++) {
      if (order.items[i].price > 0) {
        total += order.items[i].price;
      }
    }

    if (order.customer.isMember) {
      total *= 0.9;
    }

    return total;
  }

  return 0;
}
```

### Advantages of Good Indentation

✅ **Instant readability**: You see the code structure at a glance
✅ **Spot errors**: Improperly closed blocks become immediately visible
✅ **Quick navigation**: You find functions and blocks easily
✅ **Collaboration**: The whole team reads the code the same way
✅ **Professionalism**: Shows attention to detail

### Indentation Rules

| Language       | Recommended Spaces    | Standard           |
| -------------- | --------------------- | ------------------ |
| **JavaScript** | 2 or 4 spaces         | Airbnb: 2 spaces   |
| **Python**     | 4 spaces              | PEP 8: 4 spaces    |
| **HTML/CSS**   | 2 spaces              | Common: 2 spaces   |
| **Java**       | 4 spaces              | Oracle: 4 spaces   |

### Automatic Tools: Prettier

```javascript
// Before Prettier (messy code)
function example() {
  const x = 10;
  if (x > 5) {
    console.log('big');
  } else {
    console.log('small');
  }
}

// After Prettier (automatically formatted)
function example() {
  const x = 10;

  if (x > 5) {
    console.log('big');
  } else {
    console.log('small');
  }
}
```

**Prettier configuration** (`.prettierrc`):

```json
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "useTabs": false,
  "printWidth": 80
}
```

### Visual Example: Indentation Levels

```javascript
function calculateOrderDiscount(order) {
  // Level 0
  if (order.customer.isMember) {
    // Level 1
    if (order.total > 100) {
      // Level 2
      if (order.items.length > 5) {
        // Level 3
        return order.total * 0.8; // Level 4 ⚠️ Too deep
      }
    }
  }
  return order.total;
}

// ✅ BETTER: Reduce nesting levels
function calculateOrderDiscount(order) {
  // Level 0
  if (!order.customer.isMember) {
    // Level 1
    return order.total;
  }

  if (order.total <= 100) {
    // Level 1
    return order.total * 0.95;
  }

  if (order.items.length <= 5) {
    // Level 1
    return order.total * 0.9;
  }

  return order.total * 0.8; // Level 0
}
```

---

## 4. Error Handling: Don't Let Your Program Blow Up

### ❌ Bad Practice: Ignoring Errors

```javascript
// ❌ BAD: No error handling
function getUserData(userId) {
  const response = fetch(`/api/users/${userId}`);
  const data = response.json();
  return data;
}

function divideNumbers(a, b) {
  return a / b; // What if b = 0?
}

function parseUserInput(input) {
  const data = JSON.parse(input); // What if input isn't valid JSON?
  return data;
}
```

### Why Is It Bad?

| Problem                  | Consequence                | User Sees                     |
| ------------------------ | -------------------------- | ----------------------------- |
| **Unexpected crashes**   | The application freezes    | Blank screen                  |
| **Corrupted data**       | Invalid data gets saved    | Strange behavior              |
| **Cryptic messages**     | Non-descriptive error      | "Error undefined"             |
| **Hard to debug**        | You don't know where it failed | You can't reproduce the error |

### ✅ Good Practice: Proactive Error Handling

#### 1. Try-Catch in JavaScript

```javascript
// ✅ GOOD: Error handling with try-catch
async function getUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching user:', error);
    // Show friendly message to the user
    return null;
  }
}
```

#### 2. Input Validation

```javascript
// ✅ GOOD: Validate before operating
function divideNumbers(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Both arguments must be numbers');
  }

  if (b === 0) {
    throw new Error('Cannot divide by zero');
  }

  return a / b;
}

// Safe usage
try {
  const result = divideNumbers(10, 2);
  console.log(result); // 5
} catch (error) {
  console.error('Division error:', error.message);
}
```

#### 3. Catch on Promises

```javascript
// ✅ GOOD: Always include .catch()
fetch('/api/products')
  .then((response) => response.json())
  .then((data) => {
    console.log('Products:', data);
  })
  .catch((error) => {
    console.error('Error loading products:', error);
    // Show message to the user
    displayErrorMessage('Could not load products');
  });
```

#### 4. Handling Invalid JSON

```javascript
// ✅ GOOD: Validate JSON before parsing
function parseUserInput(input) {
  try {
    const data = JSON.parse(input);
    return { success: true, data: data };
  } catch (error) {
    console.error('Invalid JSON:', error);
    return { success: false, error: 'Invalid format' };
  }
}

// Usage
const result = parseUserInput('{"name": "Ana"}');
if (result.success) {
  console.log('Data:', result.data);
} else {
  console.log('Error:', result.error);
}
```

### Error Handling Best Practices

| Practice                    | ❌ Bad               | ✅ Good                                |
| --------------------------- | -------------------- | -------------------------------------- |
| **Log errors**              | Silencing errors     | `console.error()` or logging system    |
| **Descriptive messages**    | `"Error"`            | `"Error loading products: timeout"`    |
| **Graceful recovery**       | App freezes          | Show message and alternatives          |
| **Don't suppress exceptions** | Empty `catch {}`   | Log and handle the error               |
| **Validate inputs**         | Trust the user       | Validate before processing             |

### Complete Example: Form with Error Handling

```javascript
// ✅ GOOD: Robust error handling
async function submitContactForm(formData) {
  // 1. Validate data
  if (!formData.email || !formData.message) {
    return {
      success: false,
      error: 'Email and message are required',
    };
  }

  // 2. Validate email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(formData.email)) {
    return {
      success: false,
      error: 'Invalid email',
    };
  }

  // 3. Send data with error handling
  try {
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const result = await response.json();

    return {
      success: true,
      message: 'Message sent successfully',
    };
  } catch (error) {
    console.error('Error sending form:', error);

    return {
      success: false,
      error: 'Could not send the message. Please try again later.',
    };
  }
}

// Usage
const result = await submitContactForm({
  email: 'ana@example.com',
  message: 'Hello!',
});

if (result.success) {
  showSuccessMessage(result.message);
} else {
  showErrorMessage(result.error);
}
```

---

## 5. Readability: Code That Explains Itself

Readability is **the most important characteristic** of good code. Code is read 10 times more than it's written.

### Principles of Readability

#### 1. Small, Focused Functions

```javascript
// ❌ BAD: Giant function that does everything
function processUserOrder(userId, products, paymentInfo, shippingAddress) {
  // Validate user
  const user = database.getUser(userId);
  if (!user) return null;
  if (!user.isActive) return null;

  // Calculate total
  let total = 0;
  for (let i = 0; i < products.length; i++) {
    total += products[i].price * products[i].quantity;
  }

  // Apply discount
  if (user.isMember) {
    total *= 0.9;
  }

  // Process payment
  const payment = processPayment(paymentInfo, total);
  if (!payment.success) return null;

  // Create order
  const order = createOrder(userId, products, total);

  // Send emails
  sendOrderConfirmation(user.email, order);
  sendShippingNotification(user.email, shippingAddress);

  return order;
}

// ✅ GOOD: Split into small functions
function processUserOrder(userId, products, paymentInfo, shippingAddress) {
  const user = validateUser(userId);
  if (!user) return null;

  const total = calculateOrderTotal(products, user);
  const payment = processPayment(paymentInfo, total);

  if (!payment.success) return null;

  const order = createOrder(userId, products, total);
  notifyUserAboutOrder(user, order, shippingAddress);

  return order;
}

function validateUser(userId) {
  const user = database.getUser(userId);
  return user && user.isActive ? user : null;
}

function calculateOrderTotal(products, user) {
  let total = products.reduce((sum, p) => sum + p.price * p.quantity, 0);
  return user.isMember ? total * 0.9 : total;
}

function notifyUserAboutOrder(user, order, shippingAddress) {
  sendOrderConfirmation(user.email, order);
  sendShippingNotification(user.email, shippingAddress);
}
```

#### 2. Avoid `else` When Possible (Early Returns)

```javascript
// ❌ BAD: Nesting with else
function getUserDiscount(user) {
  if (user) {
    if (user.isMember) {
      if (user.orders > 10) {
        return 0.2;
      } else {
        return 0.1;
      }
    } else {
      return 0;
    }
  } else {
    return 0;
  }
}

// ✅ GOOD: Early returns
function getUserDiscount(user) {
  if (!user) return 0;
  if (!user.isMember) return 0;
  if (user.orders > 10) return 0.2;

  return 0.1;
}
```

#### 3. Don't Over-Comment the Code

```javascript
// ❌ BAD: Unnecessary comments
// Declare variable for the name
let name = 'Ana';

// Increment counter by 1
counter++;

// Loop through the products array
for (let i = 0; i < products.length; i++) {
  // Get the current product
  const product = products[i];
  // Print the product name
  console.log(product.name);
}

// ✅ GOOD: Self-explanatory code (no unnecessary comments)
let customerName = 'Ana';
counter++;

for (const product of products) {
  console.log(product.name);
}

// ✅ GOOD: Useful comments that explain the "why"
// Wait 2 seconds before retrying to avoid overloading the server
setTimeout(retryRequest, 2000);

// We use SHA-256 because it's the security standard required by the bank
const hash = sha256(password);
```

#### 4. Avoid Long Lines of Code

```javascript
// ❌ BAD: Line too long
const result =
  calculateTotal(products) +
  calculateTax(products, taxRate) +
  calculateShipping(products, shippingAddress) -
  calculateDiscount(customer);

// ✅ GOOD: Split across multiple lines
const subtotal = calculateTotal(products);
const tax = calculateTax(products, taxRate);
const shipping = calculateShipping(products, shippingAddress);
const discount = calculateDiscount(customer);
const result = subtotal + tax + shipping - discount;
```

#### 5. Spacing and Logical Grouping

```javascript
// ❌ BAD: Everything cramped together
function processOrder(order) {
  const total = order.items.reduce((sum, item) => sum + item.price, 0);
  const tax = total * 0.21;
  const shipping = 10;
  const final = total + tax + shipping;
  return final;
}

// ✅ GOOD: Spacing and grouping
function processOrder(order) {
  // Calculate subtotal
  const subtotal = order.items.reduce((sum, item) => sum + item.price, 0);

  // Add taxes and shipping
  const tax = subtotal * 0.21;
  const shipping = 10;

  // Calculate final total
  const finalTotal = subtotal + tax + shipping;

  return finalTotal;
}
```

---

## 6. Avoid Deep Nesting

### ❌ Bad Practice: Deeply Nested Code

```javascript
// ❌ DISASTER: "Callback Hell" or "Pyramid of Doom"
function calculateDiscount(item, quantity) {
  if (item.category === 'clothing') {
    if (quantity >= 10) {
      if (item.brand === 'premium') {
        if (item.inStock) {
          return item.price * 0.8;
        } else {
          return item.price * 0.9;
        }
      } else {
        return item.price * 0.9;
      }
    } else {
      if (quantity >= 5) {
        return item.price * 0.95;
      } else {
        return item.price;
      }
    }
  } else if (item.category === 'electronics') {
    if (quantity >= 5) {
      if (item.warranty) {
        return item.price * 0.75;
      } else {
        return item.price * 0.8;
      }
    } else {
      return item.price * 0.9;
    }
  } else {
    return item.price;
  }
}
```

### Why Is It Bad?

| Problem                | Impact                                            |
| ---------------------- | ------------------------------------------------- |
| **Hard to read**       | You have to track multiple conditions at once     |
| **Hard to maintain**   | Adding another condition is tricky                |
| **Error-prone**        | Easy to close blocks incorrectly                  |
| **Hard to test**       | Too many possible paths                           |

### ✅ Good Practice: Flatten the Structure

#### Technique 1: Early Returns

```javascript
// ✅ GOOD: Early returns
function calculateDiscount(item, quantity) {
  // Handle special cases first
  if (item.category !== 'clothing' && item.category !== 'electronics') {
    return item.price;
  }

  // Electronics
  if (item.category === 'electronics') {
    if (quantity >= 5) {
      return item.warranty ? item.price * 0.75 : item.price * 0.8;
    }
    return item.price * 0.9;
  }

  // Clothing
  if (quantity >= 10) {
    if (item.brand === 'premium' && item.inStock) {
      return item.price * 0.8;
    }
    return item.price * 0.9;
  }

  if (quantity >= 5) {
    return item.price * 0.95;
  }

  return item.price;
}
```

#### Technique 2: Extract Functions

```javascript
// ✅ BETTER: Separate functions
function calculateDiscount(item, quantity) {
  if (item.category === 'clothing') {
    return calculateClothingDiscount(item, quantity);
  }

  if (item.category === 'electronics') {
    return calculateElectronicsDiscount(item, quantity);
  }

  return item.price;
}

function calculateClothingDiscount(item, quantity) {
  if (quantity >= 10 && item.brand === 'premium' && item.inStock) {
    return item.price * 0.8;
  }

  if (quantity >= 10) {
    return item.price * 0.9;
  }

  if (quantity >= 5) {
    return item.price * 0.95;
  }

  return item.price;
}

function calculateElectronicsDiscount(item, quantity) {
  if (quantity >= 5) {
    return item.warranty ? item.price * 0.75 : item.price * 0.8;
  }

  return item.price * 0.9;
}
```

#### Technique 3: Use Configuration Objects

```javascript
// ✅ EXCELLENT: Data-driven configuration
const DISCOUNT_RULES = {
  clothing: {
    premium_bulk: { minQuantity: 10, discount: 0.8, requiresStock: true },
    bulk: { minQuantity: 10, discount: 0.9 },
    medium: { minQuantity: 5, discount: 0.95 },
    default: { discount: 1.0 },
  },
  electronics: {
    warranty_bulk: { minQuantity: 5, discount: 0.75, requiresWarranty: true },
    bulk: { minQuantity: 5, discount: 0.8 },
    default: { discount: 0.9 },
  },
};

function calculateDiscount(item, quantity) {
  const rules = DISCOUNT_RULES[item.category];
  if (!rules) return item.price;

  const discount = findApplicableDiscount(item, quantity, rules);
  return item.price * discount;
}

function findApplicableDiscount(item, quantity, rules) {
  if (quantity >= 10 && item.brand === 'premium' && item.inStock) {
    return rules.premium_bulk?.discount || 1.0;
  }

  if (quantity >= 10) {
    return rules.bulk?.discount || 1.0;
  }

  if (quantity >= 5) {
    return rules.medium?.discount || rules.bulk?.discount || 1.0;
  }

  return rules.default.discount;
}
```

### Visual Comparison

```
BEFORE (6 nesting levels):              AFTER (2 levels max):
─────────────────────────────           ─────────────────────────────
if                                      if (!valid) return
  if
    if                                  if (category A)
      if                                    return calcA()
        if
          if                            if (category B)
            return                          return calcB()
```

---

## Summary: Good Practices Checklist

### ✅ Variables

- [ ] I avoid global variables
- [ ] I use descriptive names
- [ ] I follow conventions (camelCase, UPPER_SNAKE_CASE)
- [ ] I don't use single letters (x, y, z)
- [ ] I avoid abbreviations

### ✅ Functions

- [ ] Names with verbs (get, set, calculate)
- [ ] Small functions (< 20 lines ideally)
- [ ] One responsibility per function
- [ ] I avoid too many parameters (max 3-4)

### ✅ Structure

- [ ] Consistent indentation (2 or 4 spaces)
- [ ] I use automatic tools (Prettier)
- [ ] Lines not too long (< 80-100 characters)
- [ ] I group code logically

### ✅ Errors

- [ ] I use try-catch on risky operations
- [ ] I validate user inputs
- [ ] I log errors to the console
- [ ] I show friendly messages to the user
- [ ] I don't suppress exceptions

### ✅ Readability

- [ ] Self-explanatory code
- [ ] Comments only when necessary
- [ ] Spacing between sections
- [ ] I avoid deep nesting (max 2-3 levels)
- [ ] I use early returns

---

## Practical Exercise: Refactor Code

### Exercise: Improve this code

```javascript
// ❌ CODE WITH BAD PRACTICES
let x = 0;

function proc(a, b, c) {
  if (a > 0) {
    if (b !== null) {
      if (c.length > 0) {
        for (let i = 0; i < c.length; i++) {
          x += c[i];
        }

        return (x * a) / b;
      } else {
        return 0;
      }
    } else {
      return 0;
    }
  } else {
    return 0;
  }
}

let r = proc(10, null, [1, 2, 3]);
```

<details>
<summary>See solution</summary>

```javascript
// ✅ IMPROVED CODE
function calculateWeightedAverage(multiplier, divisor, numbers) {
  // Early validations
  if (multiplier <= 0) {
    console.warn('The multiplier must be greater than 0');
    return 0;
  }

  if (divisor === null || divisor === 0) {
    console.warn('The divisor cannot be null or 0');
    return 0;
  }

  if (!Array.isArray(numbers) || numbers.length === 0) {
    console.warn('You must provide an array of numbers');
    return 0;
  }

  // Calculate sum
  const sum = numbers.reduce((total, num) => total + num, 0);

  // Calculate result
  const result = (sum * multiplier) / divisor;

  return result;
}

// Usage
const result = calculateWeightedAverage(10, 2, [1, 2, 3]);
console.log(result); // 30
```

</details>

---

## Conclusion

### The Impact of Good Practices

**Before applying good practices:**

- 😫 Code that's hard to read
- 🐛 Frequent bugs
- ⏰ Lots of time debugging
- 💸 High maintenance costs
- 😠 Frustrated team

**After applying good practices:**

- 😊 Easy-to-understand code
- ✅ Fewer bugs
- ⚡ Faster development
- 💰 Lower costs
- 🚀 Productive team

### Remember

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

### Next Steps

1. **Practice daily** — Review your code before committing
2. **Use tools** — Prettier, ESLint, linters
3. **Code reviews** — Ask teammates for feedback
4. **Refactor** — Improve old code regularly
5. **Read others' code** — Learn from open source projects

**Clean code is a habit you develop with constant practice! 💪**

---

## Additional Resources

- **Clean Code** — Book by Robert C. Martin
- **JavaScript Style Guide** — Airbnb: https://github.com/airbnb/javascript
- **PEP 8** — Python style guide: https://pep8.org/
- **Prettier** — Automatic formatter: https://prettier.io/
- **ESLint** — JavaScript linter: https://eslint.org/

---

## Cheat Sheet: Good Practices

```javascript
// NAMES
✅ customerAge    ❌ x
✅ calculateTotal ❌ calc
✅ isLoggedIn    ❌ flag

// FUNCTIONS
✅ Small and focused
✅ Names with verbs
✅ Early returns

// STRUCTURE
✅ Consistent indentation
✅ Maximum 2-3 nesting levels
✅ Group code logically

// ERRORS
✅ try-catch on risky operations
✅ Validate inputs
✅ Log errors

// READABILITY
✅ Self-explanatory code
✅ Avoid obvious comments
✅ Spacing between sections
```
