[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 14: Unit Testing with Jest 🧪

## Introduction

Testing is one of the most important skills in professional software development. Today you'll learn how to write **unit tests** using **Jest**, the most popular testing framework for JavaScript.

### Why Do Testing?

Imagine you're building a calculator. Every time you add a new function, how do you know you haven't broken something that was already working? **Tests automate this verification**.

### Companies That Use Jest

- 🐦 Twitter
- 📷 Instagram
- 📌 Pinterest
- 🏠 Airbnb
- 🎵 Spotify

---

## Part 1: What Is Unit Testing?

### Basic Concept

**Unit Testing** = Testing the **smallest pieces** of your code in **isolation**.

### Analogy: The Toy Factory 🏭

Imagine a factory that produces toy cars:

| Approach | Description |
|----------|-------------|
| **Without tests** | You produce 1000 cars and only at the end discover that the wheels are bad |
| **With unit tests** | You test every wheel before assembling the car |

### What Is a "Unit"?

In JavaScript, a **unit** is usually a **function**:

```javascript
// This is one unit
function sum(a, b) {
    return a + b;
}

// This is another unit
function multiply(a, b) {
    return a * b;
}
```

### Characteristics of Unit Tests

✅ **Fast** — They run in milliseconds
✅ **Independent** — One test doesn't depend on another
✅ **Repeatable** — They always give the same result
✅ **Automatic** — They require no manual intervention

---

## Part 2: What Is Jest?

### Definition

**Jest** is a JavaScript testing framework created by Facebook (Meta). It's the de facto standard for testing in modern JavaScript.

### Advantages of Jest

| Feature | Benefit |
|---------|---------|
| 🚀 **Zero Config** | Works without configuration |
| ⚡ **Fast** | Runs tests in parallel |
| 📸 **Snapshots** | Detects visual changes |
| 🎯 **All-in-one** | You don't need additional libraries |
| 📝 **Clear messages** | Easy-to-understand errors |

### Jest's Philosophy

> "Tests should be delightful to write"

---

## Part 3: Anatomy of a Test

### The Basic Structure

Every test has 3 parts:

```javascript
test('description of what you test', () => {
    // 1. ARRANGE: Set up data
    const input = 5;

    // 2. ACT: Execute the function
    const result = doubleit(input);

    // 3. ASSERT: Verify the result
    expect(result).toBe(10);
});
```

### Visual Example

```
┌─────────────────────────────────────┐
│  test('sum 2 + 3 = 5')              │
│  ┌───────────────────────────────┐  │
│  │ 1. ARRANGE                    │  │
│  │    const a = 2;               │  │
│  │    const b = 3;               │  │
│  └───────────────────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │ 2. ACT                        │  │
│  │    const result = sum(a, b);  │  │
│  └───────────────────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │ 3. ASSERT                     │  │
│  │    expect(result).toBe(5);    │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## Part 4: Your First Test — Step by Step

Let's create our first test from scratch.

### Step 1: Create the Project Structure

```bash
mkdir my-first-test
cd my-first-test
npm init -y
```

This creates a `package.json` file.

### Step 2: Install Jest

```bash
npm install --save-dev jest
```

**💡 Note**: `--save-dev` installs Jest only for development, not for production.

### Step 3: Configure npm to Run Tests

Open `package.json` and modify the `"scripts"` section:

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

### Step 4: Create the Function to Test

Create a file called `sum.js`:

```javascript
function sum(a, b) {
    return a + b;
}

module.exports = sum;
```

### 🔍 Explanation

```javascript
module.exports = sum;
```

This **exports** the function so it can be imported into other files.

### Step 5: Create the Test File

Create a file called `sum.test.js`:

```javascript
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});
```

### 🔍 Naming Convention

| File | Convention |
|------|------------|
| Function | `sum.js` |
| Test | `sum.test.js` |

Jest automatically looks for files ending in `.test.js` or `.spec.js`.

### Step 6: Run the Test

```bash
npm test
```

### ✅ Expected Result

```
PASS  ./sum.test.js
  ✓ adds 1 + 2 to equal 3 (2 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

🎉 **Congratulations! You've created and run your first test.**

---

## Part 5: Understanding `expect` and Matchers

### What Is `expect`?

`expect` is the function you use to verify results. It's always followed by a **matcher**.

### Syntax

```javascript
expect(actualValue).matcher(expectedValue);
```

### Most Common Matchers

#### 1. `.toBe()` — Strict equality (===)

```javascript
test('equal numbers', () => {
    expect(2 + 2).toBe(4);
});

test('equal strings', () => {
    expect('hello').toBe('hello');
});
```

#### 2. `.toEqual()` — Content equality (objects and arrays)

```javascript
test('equal objects', () => {
    const user = { name: 'Ana', age: 25 };
    expect(user).toEqual({ name: 'Ana', age: 25 });
});

test('equal arrays', () => {
    expect([1, 2, 3]).toEqual([1, 2, 3]);
});
```

#### 3. `.toBeTruthy()` / `.toBeFalsy()`

```javascript
test('truthy value', () => {
    expect(true).toBeTruthy();
    expect(1).toBeTruthy();
    expect('hello').toBeTruthy();
});

test('falsy value', () => {
    expect(false).toBeFalsy();
    expect(0).toBeFalsy();
    expect('').toBeFalsy();
});
```

#### 4. `.toBeNull()` / `.toBeUndefined()`

```javascript
test('check null', () => {
    const data = null;
    expect(data).toBeNull();
});

test('check undefined', () => {
    let variable;
    expect(variable).toBeUndefined();
});
```

#### 5. `.toContain()` — For arrays and strings

```javascript
test('array contains element', () => {
    const colors = ['red', 'blue', 'green'];
    expect(colors).toContain('blue');
});

test('string contains substring', () => {
    expect('hello world').toContain('world');
});
```

#### 6. `.toBeGreaterThan()` / `.toBeLessThan()`

```javascript
test('greater than', () => {
    expect(10).toBeGreaterThan(5);
});

test('less than', () => {
    expect(5).toBeLessThan(10);
});
```

### 📊 Matchers Summary Table

| Matcher | Use | Example |
|---------|-----|---------|
| `.toBe(x)` | Strict equality | `expect(2+2).toBe(4)` |
| `.toEqual(x)` | Content equality | `expect({a:1}).toEqual({a:1})` |
| `.toBeTruthy()` | Truthy value | `expect(1).toBeTruthy()` |
| `.toBeFalsy()` | Falsy value | `expect(0).toBeFalsy()` |
| `.toContain(x)` | Contains element | `expect([1,2]).toContain(2)` |
| `.toBeGreaterThan(x)` | Greater than | `expect(10).toBeGreaterThan(5)` |

---

## Part 6: Complete Example — Testing a Real Function

Let's test a more realistic function.

### The Function: Password Validator

Create `passwordValidator.js`:

```javascript
function isValidPassword(password) {
    // Rules:
    // 1. Minimum 8 characters
    // 2. At least one uppercase letter
    // 3. At least one number

    if (password.length < 8) {
        return false;
    }

    if (!/[A-Z]/.test(password)) {
        return false;
    }

    if (!/[0-9]/.test(password)) {
        return false;
    }

    return true;
}

module.exports = isValidPassword;
```

### The Tests

Create `passwordValidator.test.js`:

```javascript
const isValidPassword = require('./passwordValidator');

test('valid password meeting all requirements', () => {
    expect(isValidPassword('Password123')).toBe(true);
});

test('too-short password should fail', () => {
    expect(isValidPassword('Pass1')).toBe(false);
});

test('password without uppercase should fail', () => {
    expect(isValidPassword('password123')).toBe(false);
});

test('password without number should fail', () => {
    expect(isValidPassword('Password')).toBe(false);
});

test('lowercase-only password should fail', () => {
    expect(isValidPassword('helloworld')).toBe(false);
});
```

### Run Tests

```bash
npm test
```

### ✅ Result

```
PASS  ./passwordValidator.test.js
  ✓ valid password meeting all requirements (2 ms)
  ✓ too-short password should fail (1 ms)
  ✓ password without uppercase should fail
  ✓ password without number should fail
  ✓ lowercase-only password should fail

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
```

---

## Part 7: Organizing Tests with `describe`

When you have many tests, it's useful to group them.

### Syntax

```javascript
describe('Group of related tests', () => {
    test('test 1', () => { /* ... */ });
    test('test 2', () => { /* ... */ });
});
```

### Example: Full Calculator

Create `calculator.js`:

```javascript
const calculator = {
    sum: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b,
    divide: (a, b) => a / b
};

module.exports = calculator;
```

Create `calculator.test.js`:

```javascript
const calculator = require('./calculator');

describe('Basic Calculator Operations', () => {

    describe('Sum', () => {
        test('adds positive numbers', () => {
            expect(calculator.sum(2, 3)).toBe(5);
        });

        test('adds negative numbers', () => {
            expect(calculator.sum(-2, -3)).toBe(-5);
        });

        test('adds zero', () => {
            expect(calculator.sum(5, 0)).toBe(5);
        });
    });

    describe('Subtraction', () => {
        test('subtracts positive numbers', () => {
            expect(calculator.subtract(10, 3)).toBe(7);
        });

        test('subtracts to a negative result', () => {
            expect(calculator.subtract(3, 10)).toBe(-7);
        });
    });

    describe('Multiplication', () => {
        test('multiplies positive numbers', () => {
            expect(calculator.multiply(4, 5)).toBe(20);
        });

        test('multiplying by zero', () => {
            expect(calculator.multiply(10, 0)).toBe(0);
        });
    });

    describe('Division', () => {
        test('divides normal numbers', () => {
            expect(calculator.divide(10, 2)).toBe(5);
        });

        test('division with decimals', () => {
            expect(calculator.divide(10, 3)).toBeCloseTo(3.33, 2);
        });
    });
});
```

### 🔍 New Matcher: `.toBeCloseTo()`

```javascript
expect(calculator.divide(10, 3)).toBeCloseTo(3.33, 2);
```

- **3.33**: Expected value
- **2**: Number of decimal places of precision

Useful for comparing numbers with decimals.

---

## Part 8: Testing Functions That Use Arrays

### The Function

Create `arrayHelpers.js`:

```javascript
const arrayHelpers = {
    // Filter even numbers
    getEvenNumbers: (numbers) => {
        return numbers.filter(num => num % 2 === 0);
    },

    // Get the maximum
    getMax: (numbers) => {
        return Math.max(...numbers);
    },

    // Sum all elements
    sumAll: (numbers) => {
        return numbers.reduce((sum, num) => sum + num, 0);
    },

    // Remove duplicates
    removeDuplicates: (array) => {
        return [...new Set(array)];
    }
};

module.exports = arrayHelpers;
```

### The Tests

Create `arrayHelpers.test.js`:

```javascript
const arrayHelpers = require('./arrayHelpers');

describe('Array Helpers', () => {

    describe('getEvenNumbers', () => {
        test('returns only even numbers', () => {
            const result = arrayHelpers.getEvenNumbers([1, 2, 3, 4, 5, 6]);
            expect(result).toEqual([2, 4, 6]);
        });

        test('returns empty array when no evens', () => {
            const result = arrayHelpers.getEvenNumbers([1, 3, 5]);
            expect(result).toEqual([]);
        });
    });

    describe('getMax', () => {
        test('finds the max number', () => {
            expect(arrayHelpers.getMax([3, 7, 2, 9, 1])).toBe(9);
        });

        test('works with negative numbers', () => {
            expect(arrayHelpers.getMax([-5, -2, -10])).toBe(-2);
        });
    });

    describe('sumAll', () => {
        test('sums all numbers', () => {
            expect(arrayHelpers.sumAll([1, 2, 3, 4])).toBe(10);
        });

        test('returns 0 for empty array', () => {
            expect(arrayHelpers.sumAll([])).toBe(0);
        });
    });

    describe('removeDuplicates', () => {
        test('removes duplicate elements', () => {
            const result = arrayHelpers.removeDuplicates([1, 2, 2, 3, 3, 3, 4]);
            expect(result).toEqual([1, 2, 3, 4]);
        });

        test('keeps array without duplicates the same', () => {
            const result = arrayHelpers.removeDuplicates([1, 2, 3]);
            expect(result).toEqual([1, 2, 3]);
        });
    });
});
```

---

## Part 9: Testing Edge Cases

### What Are Edge Cases?

They are **uncommon but possible** situations that can break your code.

### Example: Safe Division Function

Create `safeDivide.js`:

```javascript
function safeDivide(a, b) {
    // Edge case: Division by zero
    if (b === 0) {
        throw new Error('Cannot divide by zero');
    }

    // Edge case: Non-numeric parameters
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('Both parameters must be numbers');
    }

    return a / b;
}

module.exports = safeDivide;
```

### Tests with `.toThrow()`

Create `safeDivide.test.js`:

```javascript
const safeDivide = require('./safeDivide');

describe('safeDivide', () => {

    test('divides normal numbers', () => {
        expect(safeDivide(10, 2)).toBe(5);
    });

    test('throws error when dividing by zero', () => {
        expect(() => safeDivide(10, 0)).toThrow('Cannot divide by zero');
    });

    test('throws error with non-numeric parameter', () => {
        expect(() => safeDivide('10', 2)).toThrow('Both parameters must be numbers');
    });

    test('throws error with both non-numeric parameters', () => {
        expect(() => safeDivide('a', 'b')).toThrow();
    });
});
```

### 🔍 Syntax of `.toThrow()`

```javascript
// For functions that throw errors, you MUST wrap them in an arrow function
expect(() => safeDivide(10, 0)).toThrow();

// ❌ INCORRECT
expect(safeDivide(10, 0)).toThrow(); // Doesn't work

// ✅ CORRECT
expect(() => safeDivide(10, 0)).toThrow();
```

---

## Part 10: Testing Strings

### The Function

Create `stringHelpers.js`:

```javascript
const stringHelpers = {
    // Check if uppercase
    isUpperCase: (str) => {
        if (typeof str !== 'string') return false;
        return str === str.toUpperCase() && str !== '';
    },

    // Count vowels
    countVowels: (str) => {
        const vowels = str.match(/[aeiouAEIOU]/g);
        return vowels ? vowels.length : 0;
    },

    // Reverse string
    reverse: (str) => {
        return str.split('').reverse().join('');
    },

    // Is palindrome
    isPalindrome: (str) => {
        const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
        return cleaned === cleaned.split('').reverse().join('');
    }
};

module.exports = stringHelpers;
```

### The Tests

Create `stringHelpers.test.js`:

```javascript
const stringHelpers = require('./stringHelpers');

describe('String Helpers', () => {

    describe('isUpperCase', () => {
        test('detects uppercase string', () => {
            expect(stringHelpers.isUpperCase('HELLO')).toBe(true);
        });

        test('detects lowercase string', () => {
            expect(stringHelpers.isUpperCase('hello')).toBe(false);
        });

        test('detects mixed-case string', () => {
            expect(stringHelpers.isUpperCase('Hello')).toBe(false);
        });

        test('returns false for non-string', () => {
            expect(stringHelpers.isUpperCase(123)).toBe(false);
        });
    });

    describe('countVowels', () => {
        test('counts vowels correctly', () => {
            expect(stringHelpers.countVowels('hello')).toBe(2);
        });

        test('counts uppercase vowels', () => {
            expect(stringHelpers.countVowels('AEIOU')).toBe(5);
        });

        test('returns 0 when there are no vowels', () => {
            expect(stringHelpers.countVowels('xyz')).toBe(0);
        });
    });

    describe('reverse', () => {
        test('reverses simple string', () => {
            expect(stringHelpers.reverse('hello')).toBe('olleh');
        });

        test('reverses empty string', () => {
            expect(stringHelpers.reverse('')).toBe('');
        });
    });

    describe('isPalindrome', () => {
        test('detects simple palindrome', () => {
            expect(stringHelpers.isPalindrome('oso')).toBe(true);
        });

        test('detects palindrome with spaces', () => {
            expect(stringHelpers.isPalindrome('anita lava la tina')).toBe(true);
        });

        test('detects non-palindrome', () => {
            expect(stringHelpers.isPalindrome('hello')).toBe(false);
        });
    });
});
```

---

## Part 11: Watch Mode — Continuous Testing

### What Is Watch Mode?

Jest can **stay running** and re-run tests automatically when you save changes.

### Activate Watch Mode

```bash
npm test -- --watch
```

Or add a script in `package.json`:

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

Now run:

```bash
npm run test:watch
```

### Advantages

- ✅ Tests run automatically on save
- ✅ Only runs tests related to modified files
- ✅ Instant feedback
- ✅ Perfect during development

---

## Part 12: Coverage (Test Coverage)

### What Is Coverage?

**Coverage** tells you what percentage of your code is covered by tests.

### View Coverage

```bash
npm test -- --coverage
```

### Example Report

```
----------------------|---------|----------|---------|---------|
File                  | % Stmts | % Branch | % Funcs | % Lines |
----------------------|---------|----------|---------|---------|
All files             |     100 |      100 |     100 |     100 |
 calculator.js        |     100 |      100 |     100 |     100 |
 stringHelpers.js     |     100 |      100 |     100 |     100 |
----------------------|---------|----------|---------|---------|
```

### Interpretation

| Metric | Meaning |
|--------|---------|
| **Stmts** (Statements) | % of lines executed |
| **Branch** | % of if/else conditions tested |
| **Funcs** | % of functions called |
| **Lines** | % of code lines covered |

### Professional Target

🎯 **Goal**: 80% — 100% coverage on professional projects.

---

## 🎯 Practical Exercises

### Exercise 1: Email Function Testing ⭐

Create a function that validates emails and write tests for it.

```javascript
// emailValidator.js
function isValidEmail(email) {
    // Must contain @ and a domain
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

module.exports = isValidEmail;
```

**Tests you should write:**
- Valid email: `test@example.com`
- Email without @: `testexample.com`
- Email without domain: `test@`
- Empty email: `""`

### Exercise 2: Age Function Testing ⭐⭐

```javascript
// ageClassifier.js
function classifyAge(age) {
    if (age < 0) return 'invalid';
    if (age < 13) return 'child';
    if (age < 18) return 'teenager';
    if (age < 65) return 'adult';
    return 'senior';
}

module.exports = classifyAge;
```

**Write tests for:**
- Each category
- Boundaries (0, 12, 13, 17, 18, 64, 65)
- Negative values

### Exercise 3: Shopping Cart Testing ⭐⭐⭐

```javascript
// shoppingCart.js
const shoppingCart = {
    items: [],

    addItem: function(item) {
        this.items.push(item);
    },

    getTotal: function() {
        return this.items.reduce((sum, item) => sum + item.price, 0);
    },

    getItemCount: function() {
        return this.items.length;
    },

    clear: function() {
        this.items = [];
    }
};

module.exports = shoppingCart;
```

**Write tests for:**
- Adding items
- Calculating total
- Counting items
- Clearing the cart

---

## Summary: Key Concepts

### Unit Testing
✅ Tests the smallest units of code
✅ Must be fast, independent, and repeatable
✅ Detects bugs before production

### Jest
✅ #1 testing framework in JavaScript
✅ Zero configuration
✅ Fast with clear messages

### Test Structure
✅ **ARRANGE**: Set up data
✅ **ACT**: Execute the function
✅ **ASSERT**: Verify the result

### Essential Matchers
✅ `.toBe()` — Strict equality
✅ `.toEqual()` — Content equality
✅ `.toContain()` — Contains element
✅ `.toThrow()` — Throws error

### Organization
✅ `describe()` — Groups related tests
✅ `.test.js` files for tests
✅ One test file per code file

### Important Commands
```bash
npm test              # Run tests
npm test -- --watch   # Continuous mode
npm test -- --coverage # View coverage
```

---

## Cheat Sheet: Jest

```javascript
// BASIC STRUCTURE
test('description', () => {
    expect(result).matcher(expected);
});

// GROUP TESTS
describe('group', () => {
    test('test 1', () => { /* ... */ });
    test('test 2', () => { /* ... */ });
});

// COMMON MATCHERS
expect(x).toBe(y)              // Strict equality
expect(x).toEqual(y)           // Content equality
expect(x).toBeTruthy()         // Truthy value
expect(x).toBeFalsy()          // Falsy value
expect(x).toBeNull()           // Is null
expect(x).toBeUndefined()      // Is undefined
expect(x).toContain(y)         // Contains element
expect(x).toBeGreaterThan(y)   // Greater than
expect(x).toBeLessThan(y)      // Less than
expect(x).toBeCloseTo(y, d)    // Close to (decimals)
expect(() => x()).toThrow()    // Throws error

// NUMBERS
expect(10).toBeGreaterThan(5)
expect(5).toBeLessThan(10)
expect(4.23).toBeCloseTo(4.2, 1)

// ARRAYS
expect([1,2,3]).toContain(2)
expect([1,2,3]).toEqual([1,2,3])
expect([1,2,3]).toHaveLength(3)

// OBJECTS
expect({a:1}).toEqual({a:1})
expect({a:1,b:2}).toHaveProperty('a')

// STRINGS
expect('hello world').toContain('world')
expect('hello').toMatch(/ell/)
```

---

## Good Practices

### ✅ DO

1. **Name tests descriptively**
   ```javascript
   test('returns empty array when no even elements', () => {})
   ```

2. **One test, one thing**
   ```javascript
   // ✅ Good
   test('adds positive numbers', () => {})
   test('adds negative numbers', () => {})

   // ❌ Bad
   test('adds all kinds of numbers', () => {
       // Many checks here
   })
   ```

3. **Test edge cases**
   ```javascript
   test('handles division by zero', () => {})
   test('handles empty string', () => {})
   test('handles empty array', () => {})
   ```

4. **Independent tests**
   ```javascript
   // Each test must be runnable on its own
   ```

### ❌ DON'T

1. **Don't test implementation, test behavior**
   ```javascript
   // ❌ Bad: Test how it does it
   test('uses the .filter() method', () => {})

   // ✅ Good: Test what it does
   test('returns only even numbers', () => {})
   ```

2. **Don't use magic values**
   ```javascript
   // ❌ Bad
   expect(calculate()).toBe(42); // Why 42?

   // ✅ Good
   const expected = price * taxRate;
   expect(calculate(price, taxRate)).toBe(expected);
   ```

3. **No dependent tests**
   ```javascript
   // ❌ Bad: Test 2 depends on Test 1
   let user;
   test('create user', () => {
       user = createUser();
   });
   test('update user', () => {
       updateUser(user); // Depends on the previous one
   });
   ```

---

## 🔗 Additional Resources

- **Jest Docs**: https://jestjs.io/docs/getting-started
- **Jest Cheat Sheet**: https://github.com/sapegin/jest-cheat-sheet
- **4Geeks - Unit Testing**: https://4geeks.com/lesson/how-to-create-unit-testing-with-javascript-and-jest
- **Testing Best Practices**: https://testingjavascript.com/

---

## 🎉 Congratulations!

You now know:

- ✅ What unit testing is and why it matters
- ✅ How to install and configure Jest
- ✅ How to write tests with `test()` and `expect()`
- ✅ How to use common matchers
- ✅ How to organize tests with `describe()`
- ✅ How to test edge cases
- ✅ How to view test coverage
- ✅ How to use watch mode for continuous development

**Next step**: Practice by writing tests for your own functions. Testing is a skill that gets better with practice.

---

## 💡 Final Thought

> "Code without tests is broken by design"
> — Jacob Kaplan-Moss (co-creator of Django)

Testing is not optional in professional development. It's an investment that:
- 💰 Saves time in the long run
- 🐛 Detects bugs before production
- 📚 Documents how to use your code
- 🔒 Gives confidence to refactor
- 🚀 Lets you ship quality code

**Start writing tests today!**
