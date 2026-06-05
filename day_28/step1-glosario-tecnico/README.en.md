[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 0.5: Technical Glossary

## 🎯 Goal

This glossary defines the technical terms we will use throughout day 28. If you come across a word you don't understand, come back here.

---

## 📖 Fundamental terms

### Endpoint

An **endpoint** is a specific URL of your API where you can send requests.

```
Endpoint examples:
POST /api/login     ← Endpoint to log in
GET  /api/users     ← Endpoint to get users
GET  /api/users/5   ← Endpoint to get user 5
```

**Analogy**: If your API is a restaurant, each endpoint is a dish on the menu. You have to order the right dish (endpoint) to get what you want.

---

### HTTP Header

A **header** is additional information that travels along with each HTTP request. They are like labels on a mail package.

```
HTTP request:
┌─────────────────────────────────────────┐
│ GET /api/profile                        │ ← The URL
├─────────────────────────────────────────┤
│ Headers:                                │
│   Content-Type: application/json        │ ← "The content is JSON"
│   Authorization: Bearer eyJhbG...       │ ← "My token is this one"
│   Accept-Language: en                   │ ← "Respond in English"
└─────────────────────────────────────────┘
```

The most important header for authentication is **Authorization**, where we send our JWT token.

---

### Bearer Token

**Bearer** means "the one who carries". When we say `Authorization: Bearer <token>`, we are saying "the bearer of this token has permission".

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
               ^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               Type   The JWT token
```

It is an industry standard for sending tokens in REST APIs.

---

### Hash vs Encryption

These two concepts are often confused, but they are VERY different:

| Concept        | Reversible? | Primary use                       | Example         |
| -------------- | ----------- | --------------------------------- | --------------- |
| **Hash**       | ❌ NO       | Passwords                         | bcrypt, SHA-256 |
| **Encryption** | ✅ YES      | Data you need to read back later  | AES, RSA        |

```mermaid
flowchart LR
    subgraph Hash["Hash (one-way)"]
        A["'hola123'"] --> B["$2b$12$xyz..."]
        B -.-x A
    end

    subgraph Encryption["Encryption (two-way)"]
        C["'message'"] -->|"encrypt"| D["X#@!$%"]
        D -->|"decrypt"| C
    end
```

**Why do we use hash for passwords?**

- If someone hacks your database, they CANNOT recover the passwords
- To verify, you hash the submitted password and compare hashes

---

### Base64

**Base64** is a way to **encode** (not encrypt) binary data as text.

```
Original: {"user": "luis"}
Base64:   eyJ1c2VyIjogImx1aXMifQ==
```

⚠️ **IMPORTANT**: Base64 is NOT secure. Anyone can decode it:

```javascript
atob('eyJ1c2VyIjogImx1aXMifQ=='); // → {"user": "luis"}
```

The JWT uses Base64 for the header and payload, which is why **you should never put sensitive data** (passwords, credit cards) in a JWT.

---

### Serialization

To **serialize** means to convert something that exists **inside your program** into a format that can be **transmitted or stored**.

#### Why is it necessary?

Inside Python, data lives in **RAM** as complex objects. But when you need to send that data somewhere else (to a browser, to another API, to a file), you need to convert it to a **universal** format that anyone can read — such as plain text.

#### Analogy 1: The LEGO by mail 🧱

Imagine you have a built LEGO model (a castle). You can't send it by mail like that — it would break. What you do is **take it apart**, put it in a box with **step-by-step instructions**, and ship it. The other person receives the box, reads the instructions, and puts it back together. That's serialization.

```
🏰 Assembled LEGO castle  →  📦 Box with pieces + instructions  →  🏰 Assembled castle at destination
   (object in RAM)            (JSON / plain text)                  (object in the other program)
   "serialize"                                                      "deserialize"
```

#### Analogy 2: The cooking recipe 🍳

A prepared dish (a paella) can't be sent over WhatsApp. But the **recipe** can — it's text with instructions. Serializing is converting the paella into its recipe; deserializing is cooking it back.

> _"A Python object is the paella. JSON is the recipe. You can't send a paella over HTTP, but you can send the recipe."_

#### Analogy 3: The common language 🌍

Imagine that Python speaks Japanese, JavaScript speaks English, and your database speaks German. None of them understand each other. **JSON is the universal language** — everyone speaks it. Serializing is **translating** from Python's language (objects) into the universal language (JSON).

> _"A dictionary is already 'almost in the universal language' — it's easy to translate. A SQLAlchemy object is in technical Japanese — it has verbs, complex grammar, context... you need a manual translator (the `serialize()` method)."_

#### Analogy 4: The move 📦

You have your room assembled: bed, desk, PC plugged in. You can't fit the whole room into a moving truck like that. What you do is:

1. **Disassemble** the furniture
2. **Label** each box ("desk screws", "table legs")
3. Load it into the truck

That's serializing. At the destination, you open the boxes and put everything together again (deserialize).

> _"A dictionary is like a box already labeled and ready. A SQLAlchemy object is the entire room — you have to disassemble it first."_

#### Put plainly 💬

HTTP can only send **text**. A Python dictionary looks a lot like JSON (which is text), so the conversion is automatic. But a SQLAlchemy object has things that aren't text: methods, connections, database sessions. Python tells you _"I don't know how to convert this to text"_. That's why you write `serialize()` — you tell Python exactly which parts of the object you want to send.

---

#### What can be serialized directly?

Not all data types can be converted to JSON automatically. The rule is simple:

| Data type            | Can it be serialized to JSON? | Example                          |
| -------------------- | ----------------------------- | -------------------------------- |
| `str` (text)         | ✅ YES                        | `"hola"`                         |
| `int` (integer)      | ✅ YES                        | `42`                             |
| `float` (decimal)    | ✅ YES                        | `3.14`                           |
| `bool` (boolean)     | ✅ YES                        | `true`                           |
| `None`               | ✅ YES                        | `null`                           |
| `list` (list)        | ✅ YES                        | `[1, 2, 3]`                      |
| `dict` (dictionary)  | ✅ YES                        | `{"name": "Luis"}`               |
| SQLAlchemy object    | ❌ NO                         | `<User 5>` — Python doesn't know |
| `datetime`           | ❌ NO                         | Must be converted to text        |

**Why do dictionaries work but SQLAlchemy objects don't?**

A **dictionary** is already a simple structure: keys and values, all basic types. JSON was designed to represent exactly that.

A **SQLAlchemy object** is a complex Python object: it has methods, database connections, relationships with other objects, internal state... JSON has no way to represent all of that.

```python
# Dictionary → JSON works directly
from flask import jsonify

data = {"name": "Luis", "age": 25}
jsonify(data)  # ✅ → {"name": "Luis", "age": 25}

# SQLAlchemy object → JSON does NOT work
user = User.query.get(5)
jsonify(user)  # ❌ TypeError: Object of type User is not JSON serializable
```

#### The solution: the `serialize()` method

That's why we create a `serialize()` method in our models — to **manually extract** the data from the object and put it into a dictionary:

```python
def serialize(self):
    return {
        "id": self.id,           # int → ✅ serializable
        "email": self.email,     # str → ✅ serializable
        "username": self.username # str → ✅ serializable
        # password_hash → ❌ we don't include it for security
    }

# Now it works:
jsonify(user.serialize())  # ✅ → {"id": 5, "email": "luis@example.com", ...}
```

> 💡 **Summary**: Serializing = converting a complex object into a dictionary/JSON that can be sent over HTTP. In Flask, we do it with a `serialize()` method on each model.

---

### Stateless vs Stateful

| Term          | Meaning                                                        | Example                |
| ------------- | -------------------------------------------------------------- | ---------------------- |
| **Stateful**  | The server **remembers** information between requests          | Traditional sessions   |
| **Stateless** | The server does **NOT remember** anything, each request is independent | JWT                    |

```mermaid
flowchart TD
    subgraph Stateful["Stateful (with memory)"]
        S1["Server"] -->|"remembers"| M1["Memory<br/>User 5 is logged in"]
    end

    subgraph Stateless["Stateless (no memory)"]
        S2["Server"] -->|"remembers nothing"| M2["(empty)"]
        T["JWT Token<br/>contains: user_id=5"] -->|"every request"| S2
    end
```

JWT enables **stateless** APIs because all the information needed travels inside the token.

---

### Decorator (Python)

A **decorator** is a function that "wraps" another function to add functionality.

For today, stick with the short definition here. The explanation that really matters in context is in [step3-jwt-flask-backend](../step3-jwt-flask-backend/README.md), right where we use `@jwt_required()` to protect endpoints.

```python
# The @ indicates it is a decorator
@jwt_required()      # ← Decorator: "verify the token before executing"
def get_profile():   # ← Decorated function
    return {"data": "..."}
```

**Analogy**: It's like placing a security guard at the door. Before anyone enters your function, the guard (decorator) verifies whether they have permission.

---

### localStorage

**localStorage** is a data store in the user's browser. The data persists even if they close the browser.

```javascript
// Save
localStorage.setItem('token', 'abc123');

// Read
const token = localStorage.getItem('token'); // → 'abc123'

// Delete
localStorage.removeItem('token');
```

**Characteristics:**

- Only stores **strings** (use `JSON.stringify()` for objects)
- Persists until explicitly cleared
- Accessible only from the same domain
- Capacity: ~5MB

**See your data**: Open DevTools (F12) → Application → Local Storage

---

### Context (React)

**Context** is a React mechanism for sharing data between components without manually passing props.

```mermaid
flowchart TD
    subgraph WithoutContext["❌ Without Context (Prop Drilling)"]
        A1["App"] -->|"user"| B1["Layout"]
        B1 -->|"user"| C1["Sidebar"]
        C1 -->|"user"| D1["UserMenu"]
    end

    subgraph WithContext["✅ With Context"]
        A2["App + UserContext.Provider"] --> B2["Layout"]
        B2 --> C2["Sidebar"]
        C2 --> D2["UserMenu<br/>useContext(UserContext)"]
        A2 -.->|"direct access"| D2
    end
```

For authentication, we create an `AuthContext` that contains the token, user, and login/logout functions.

---

### Provider (React)

A **Provider** is a component that "provides" data to all its children through Context.

```jsx
// The Provider wraps the app and "provides" the data
<AuthProvider>
  <App /> {/* All components inside have access */}
</AuthProvider>
```

---

### children (React)

**children** is a special prop that represents everything you place between the tags of a component.

```jsx
<MyComponent>
  <p>This is children</p>
  <button>This too</button>
</MyComponent>;

// Inside MyComponent:
function MyComponent({ children }) {
  return <div className="wrapper">{children}</div>;
  // children = <p>This is children</p><button>This too</button>
}
```

---

### Navigate (React Router)

`Navigate` is a **component** that automatically redirects the user to another page.

```jsx
import { Navigate } from 'react-router-dom';

// If not authenticated, send them to /login
if (!isAuthenticated) {
  return <Navigate to="/login" />;
}
```

---

### useNavigate (React Router)

`useNavigate` is a **hook** that gives you a function to change pages from your JavaScript code.

```jsx
import { useNavigate } from 'react-router-dom';

const navigate = useNavigate();

// After a successful login:
navigate('/dashboard'); // Go to /dashboard

// Go back:
navigate(-1); // Equivalent to pressing "back" in the browser
```

**Difference from `<Link>`**: You use `useNavigate` when you want to navigate **after an action** (like a successful login), not when the user clicks a link.

---

### useLocation (React Router)

`useLocation` is a **hook** that tells you which page you are on and what extra data came along with the navigation.

```jsx
import { useLocation } from 'react-router-dom';

const location = useLocation();

console.log(location.pathname); // "/login"
console.log(location.state); // { from: "/dashboard" }
```

---

### bcrypt.checkpw (Python)

`checkpw` stands for **"check password"**. It is a function that compares a plaintext password against a stored hash.

```python
# Check whether the password matches
bcrypt.checkpw(password_text, password_hash)
# Returns: True or False
```

**You can't "undo" a hash**, but you can compare whether two passwords produce the same hash.

---

## 📋 Quick reference

| Term            | One-line definition                                |
| --------------- | -------------------------------------------------- |
| Endpoint        | Specific URL of your API                           |
| Header          | Metadata that travels with an HTTP request         |
| Bearer          | Token type in the Authorization header             |
| Hash            | One-way function (irreversible)                    |
| Encryption      | Reversible function (you can decrypt)              |
| Base64          | Text encoding (NOT secure)                         |
| Stateless       | The server does not store state between requests   |
| Decorator       | Function that wraps another function               |
| localStorage    | Persistent store in the browser                    |
| Context         | React mechanism for sharing data                   |
| Provider        | Component that "provides" data via Context         |
| children        | What you place between a component's tags          |
| Navigate        | Component that redirects to another page           |
| useNavigate     | Hook to navigate programmatically                  |
| useLocation     | Hook that tells you which page you are on          |
| bcrypt.checkpw  | Function that compares a password against a hash   |

---

## ✅ Checklist

- [ ] I understand what an endpoint is
- [ ] I know what HTTP headers are and what Authorization is for
- [ ] I understand the difference between hash and encryption
- [ ] I know that Base64 is NOT secure
- [ ] I understand what stateless means
- [ ] I know what a decorator does in Python
- [ ] I understand what localStorage is and how to use it
- [ ] I know what Context is for in React
- [ ] I understand the difference between `Navigate` and `useNavigate`
- [ ] I know when to use `useLocation`
- [ ] I understand what `bcrypt.checkpw` does
