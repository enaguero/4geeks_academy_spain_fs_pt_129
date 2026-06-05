[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 3: JWT in Flask with flask-jwt-extended

## 🎯 Goal

Implement full authentication in Flask:

- User registration with hashed password
- Login that returns a JWT
- Endpoints protected with `@jwt_required()`
- Get the current user with `get_jwt_identity()`

---

## 📦 Installation

```bash
pip install flask flask-sqlalchemy flask-jwt-extended bcrypt python-dotenv
```

---

## 🗺️ Endpoint map

```mermaid
flowchart LR
    subgraph Public["🌐 Public Endpoints"]
        R[POST /api/signup]
        L[POST /api/login]
    end

    subgraph Protected["🔒 Protected Endpoints"]
        P[GET /api/profile]
        U[PUT /api/profile]
        PR[GET /api/private]
    end

    R -->|Creates user| DB[(Database)]
    L -->|Verifies credentials| DB
    L -->|Returns JWT| Client
    Client -->|JWT in header| P
    Client -->|JWT in header| U
    Client -->|JWT in header| PR
```

---

## 1️⃣ Basic configuration

### `app.py`

```python
import os
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
import bcrypt
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ⚠️ IMPORTANT: Change in production
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-dev-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)
```

### `.env`

```env
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=my-super-secret-key-change-in-production
```

---

## 2️⃣ User Model

### Before the code: What is a Hash?

Before looking at the model, you need to understand why we use `bcrypt` and what it means to "hash" a password.

#### The problem: How to store passwords?

```python
# ❌ NEVER do this - store password in plain text
class User(db.Model):
    password = db.Column(db.String(80))  # "hola123" → "hola123" is stored
```

If someone hacks your database, they have ALL the passwords.

#### The solution: Hash (one-way function)

A **hash** is like a **digital blender**:

```mermaid
flowchart LR
    subgraph Blender["🔄 Hash (bcrypt)"]
        direction TB
        Input["'hola123'"] --> Process["Mathematical<br/>algorithm"]
        Process --> Output["'$2b$12$LQv3c...'"]
    end

    subgraph Impossible["❌ Cannot be reversed"]
        Output2["'$2b$12$LQv3c...'"] -.-> Input2["'???'"]
    end
```

| Concept           | Blender analogy                                    |
| ----------------- | -------------------------------------------------- |
| **Hash**          | Blend a fruit → you get juice                      |
| **Irreversible**  | You CAN'T "un-blend" the juice → recover the fruit |
| **Deterministic** | The same fruit always produces the same juice      |
| **Verification**  | To check, you blend another fruit and compare juices |

#### So how do we verify passwords?

```mermaid
sequenceDiagram
    participant U as User
    participant S as Server
    participant DB as Database

    Note over U,DB: During registration
    U->>S: password = "hola123"
    S->>S: hash = bcrypt("hola123") → "$2b$12$LQv..."
    S->>DB: Save hash (NOT the password)

    Note over U,DB: During login
    U->>S: password = "hola123"
    S->>DB: Get stored hash
    DB-->>S: "$2b$12$LQv..."
    S->>S: bcrypt("hola123") → matches "$2b$12$LQv..."?
    S-->>U: ✅ Correct password
```

#### Why bcrypt and not another hash?

| Algorithm  | Speed                  | Security    | For passwords?       |
| ---------- | ---------------------- | ----------- | -------------------- |
| MD5        | Very fast              | ❌ Broken   | ❌ NO                |
| SHA-256    | Very fast              | ✅ Secure   | ❌ NO (too fast)     |
| **bcrypt** | Slow (on purpose)      | ✅ Secure   | ✅ YES               |

**bcrypt is slow on purpose**: If an attacker tries to guess millions of passwords, each attempt takes ~100ms. That makes brute force impractical.

---

### Before the code: What is serializing?

When Flask responds to a request, it needs to send data in **JSON** format (plain text). But SQLAlchemy returns **Python objects** — and Python doesn't know how to automatically convert a complex object to JSON.

```python
# This does NOT work:
user = User.query.get(5)
return jsonify(user)  # ❌ TypeError: Object of type User is not JSON serializable
```

Why does it fail? Because `user` is an object with methods, database connections, internal state... JSON only understands simple types: strings, numbers, lists, and dictionaries.

The solution is to create a `serialize()` method that **extracts the data** from the object and puts it into a dictionary:

```python
# This DOES work:
return jsonify(user.serialize())  # ✅ → {"id": 5, "email": "luis@example.com", ...}
```

```mermaid
flowchart LR
    A["🐍 Python object<br/>User(id=5, email='luis@...', password_hash='$2b$...')"] -->|"serialize()"| B["📖 Dictionary<br/>{id: 5, email: 'luis@...'}<br/>(no password!)"]
    B -->|"jsonify()"| C["📤 JSON over HTTP<br/>id: 5, email: luis@..."]
```

> 💡 `serialize()` also acts as a **security filter**: you decide which fields to expose and which to hide (like `password_hash`).

---

### The model code

```python
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def set_password(self, password):
        """Hashes and stores the password"""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            salt
        ).decode('utf-8')

    def check_password(self, password):
        """Verifies whether the password is correct"""
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password_hash.encode('utf-8')
        )

    def serialize(self):
        """Returns public data (NEVER the password)"""
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
```

> ⚠️ **NEVER** store passwords in plain text. Always use a hash with bcrypt.

---

## 3️⃣ Endpoint: Signup

```python
@app.route("/api/signup", methods=["POST"])
def signup():
    body = request.get_json()

    # Validation
    if not body:
        return jsonify({"error": "Body required"}), 400

    required_fields = ["email", "username", "password"]
    for field in required_fields:
        if field not in body or not body[field]:
            return jsonify({"error": f"{field} is required"}), 400

    # Check that it does not exist
    existing_user = User.query.filter(
        (User.email == body["email"]) | (User.username == body["username"])
    ).first()

    if existing_user:
        return jsonify({"error": "Email or username already registered"}), 400

    # Create user
    new_user = User(
        email=body["email"],
        username=body["username"]
    )
    new_user.set_password(body["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": new_user.serialize()
    }), 201
```

### Signup flow

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant DB as Database

    C->>S: POST /api/signup<br/>{email, username, password}
    S->>S: Validate fields
    S->>DB: Does email/username exist?
    DB-->>S: Does not exist
    S->>S: Hash password with bcrypt
    S->>DB: INSERT user
    DB-->>S: OK
    S-->>C: 201 {message, user}
```

---

## 4️⃣ Endpoint: Login

```python
@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()

    # Validation
    if not body or "email" not in body or "password" not in body:
        return jsonify({"error": "Email and password are required"}), 400

    # Find user
    user = User.query.filter_by(email=body["email"]).first()

    # Verify credentials
    if user is None or not user.check_password(body["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT
    # The "identity" is what get_jwt_identity() will return later
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": user.serialize()
    }), 200
```

### Login flow

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant DB as Database

    C->>S: POST /api/login<br/>{email, password}
    S->>DB: SELECT user WHERE email=?
    DB-->>S: User data (with password_hash)
    S->>S: bcrypt.checkpw(password, hash)
    alt Correct password
        S->>S: create_access_token(identity=user.id)
        S-->>C: 200 {access_token, user}
    else Incorrect password
        S-->>C: 401 {error: "Invalid credentials"}
    end
```

---

## 🔑 Deep dive: `create_access_token`, `@jwt_required()` and `get_jwt_identity()`

This is the trinity of `flask-jwt-extended`. Understanding how they connect is **fundamental**.

This is also the **best place in day 28** to explain decorators: here `@jwt_required()` is no longer isolated theory but a real piece of the authentication flow you just built with login + token.

### First: What is a decorator in Python?

If you see `@something` above a function and you don't get what it does, this section is for you.

A **decorator** is a function that **"wraps" another function** to add functionality without modifying its code.

#### Analogy: The security guard

```mermaid
flowchart LR
    subgraph NoDecorator["❌ No decorator"]
        R1["Request"] --> F1["get_profile()"]
        F1 --> D1["Returns data"]
    end

    subgraph WithDecorator["✅ With @jwt_required()"]
        R2["Request"] --> G["🔒 Guard<br/>(jwt_required)"]
        G -->|"Valid token"| F2["get_profile()"]
        G -->|"Invalid token"| X["❌ 401 Error"]
        F2 --> D2["Returns data"]
    end
```

It's like placing a **security guard** at the door of a function:

```python
# WITHOUT decorator - anyone can enter
def get_profile():
    return {"user": "secret data"}

# WITH decorator - the guard checks first
@jwt_required()  # ← "Before letting through, verify the token"
def get_profile():
    return {"user": "secret data"}
```

#### How does it work under the hood? (optional)

If you are curious, a decorator is just a function that takes another function:

```python
# This:
@jwt_required()
def get_profile():
    pass

# Is equivalent to this:
def get_profile():
    pass
get_profile = jwt_required()(get_profile)  # Wraps the function
```

You don't need to understand this to use decorators — just know that they **add extra behavior** to your functions.

#### In the context of this day: what exactly does `@jwt_required()` do?

In JWT, the decorator plays this role:

1. The user logs in and the backend creates a token with `create_access_token(...)`.
2. The frontend stores that token and sends it in the `Authorization` header.
3. When a request reaches a protected route, `@jwt_required()` runs **before** your function.
4. If the token fails, Flask responds with `401` and your function **doesn't even execute**.
5. If the token is valid, then it enters your function and `get_jwt_identity()` can read the `identity` stored in the JWT.

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    return {"user_id": current_user_id}, 200
```

Real execution order in this example:

1. Flask detects that the URL `/api/profile` corresponds to `get_profile`.
2. `@jwt_required()` inspects the `Authorization` header.
3. Verifies the token format, signature, and expiration.
4. Only if everything is fine does `get_profile()` run.
5. Inside `get_profile()`, `get_jwt_identity()` retrieves the authenticated user.

---

### The complete identity cycle

```mermaid
flowchart LR
    subgraph Login["🔐 During Login"]
        A["user.id = 5"]
        B["create_access_token(identity='5')"]
        C["JWT generated with sub='5'"]
    end

    subgraph Token["📦 Inside the JWT"]
        D["payload: {sub: '5', exp: ...}"]
    end

    subgraph Request["🔒 In protected endpoint"]
        E["@jwt_required()"]
        F["get_jwt_identity()"]
        G["Returns '5'"]
    end

    A --> B --> C --> D
    D -->|"Authorization: Bearer token"| E
    E -->|"Valid token"| F --> G
```

### What does each function do?

| Function                          | When is it used                       | What it does                                       |
| --------------------------------- | ------------------------------------- | -------------------------------------------------- |
| `create_access_token(identity=X)` | In the **login**                      | Creates a JWT with `X` stored in the `sub` claim   |
| `@jwt_required()`                 | As **decorator** on endpoints         | Verifies that the request has a valid JWT          |
| `get_jwt_identity()`              | **Inside** the protected endpoint     | Extracts and returns the `identity` value from the token |

---

### 📌 `create_access_token(identity=...)` in detail

This function **generates the JWT** and stores the `identity` inside the token:

```python
# In login, after verifying credentials:
access_token = create_access_token(identity=str(user.id))
```

**What is stored as identity?**

You can store whatever you want, but the most common is the **user ID**:

```python
# ✅ Recommended option: Only the ID (string)
access_token = create_access_token(identity=str(user.id))

# ⚠️ Also possible: a dictionary
access_token = create_access_token(identity={
    "id": user.id,
    "email": user.email,
    "role": "admin"
})

# ❌ NOT recommended: sensitive data
access_token = create_access_token(identity={
    "password": user.password  # Never do this!
})
```

**Why string and not int?**

`flask-jwt-extended` serializes the identity to JSON. It is good practice to use strings to avoid problems:

```python
# ✅ Recommended
create_access_token(identity=str(user.id))  # "5"

# ⚠️ Also works, but...
create_access_token(identity=user.id)  # 5
```

---

### 📌 `@jwt_required()` in detail

This **decorator** does several things automatically:

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()  # 👈 This decorator...
def get_profile():
    # ... endpoint code
```

**What does the decorator do?**

```mermaid
flowchart TD
    A["Request arrives at endpoint"] --> B{"Authorization header exists?"}
    B -->|No| C["❌ 401: Token required"]
    B -->|Yes| D{"Correct format?<br/>Bearer JWT_TOKEN"}
    D -->|No| E["❌ 401: Invalid format"]
    D -->|Yes| F{"Valid signature?<br/>Verify with SECRET_KEY"}
    F -->|No| G["❌ 401: Invalid token"]
    F -->|Yes| H{"Token expired?<br/>Check exp claim"}
    H -->|Yes| I["❌ 401: Token expired"]
    H -->|No| J["✅ Execute endpoint function"]
```

**Decorator variants:**

```python
# Mandatory token (most common)
@jwt_required()
def protected_endpoint():
    pass

# Optional token - does not fail if there is no token
@jwt_required(optional=True)
def mixed_endpoint():
    user_id = get_jwt_identity()  # None if no token
    if user_id:
        # Authenticated user
    else:
        # Anonymous user

# Only refresh tokens (to renew access tokens)
@jwt_required(refresh=True)
def refresh_token():
    pass
```

---

### 📌 `get_jwt_identity()` in detail

This function **extracts the identity** from the token that was already verified by `@jwt_required()`:

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    # Get the identity we stored at login
    current_user_id = get_jwt_identity()

    # current_user_id = "5" (the string we passed to create_access_token)

    # Now we can look up the user in the DB
    user = User.query.get(current_user_id)
```

**The complete flow visualized:**

```mermaid
sequenceDiagram
    participant Client
    participant Decorator as "@jwt_required()"
    participant Function as "get_profile()"
    participant DB as Database

    Note over Client,DB: 1. Previous login generated token with identity="5"

    Client->>Decorator: GET /api/profile<br/>Authorization: Bearer eyJ...
    Decorator->>Decorator: Extract token from header
    Decorator->>Decorator: Verify signature with SECRET_KEY
    Decorator->>Decorator: Verify it is not expired

    alt Invalid token
        Decorator-->>Client: 401 Error
    else Valid token
        Decorator->>Function: Allow execution
        Function->>Function: get_jwt_identity() → "5"
        Function->>DB: SELECT * FROM users WHERE id = 5
        DB-->>Function: User data
        Function-->>Client: 200 {user data}
    end
```

---

### 🎯 Common pattern: Helper to get the current user

Instead of repeating code, create a helper:

```python
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

def get_current_user():
    """
    Gets the current user from the JWT token.
    Must be used inside an endpoint with @jwt_required()
    """
    user_id = get_jwt_identity()
    if user_id is None:
        return None
    return User.query.get(user_id)


# Usage in endpoints:
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user = get_current_user()
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.serialize()), 200


@app.route("/api/favorites", methods=["GET"])
@jwt_required()
def get_favorites():
    user = get_current_user()
    return jsonify([fav.serialize() for fav in user.favorites]), 200
```

---

### 🛡️ Pattern: Verify ownership (authorization)

A very common case is verifying that the user can only access **their own resources**:

```python
@app.route("/api/users/<int:user_id>/posts", methods=["GET"])
@jwt_required()
def get_user_posts(user_id):
    current_user_id = get_jwt_identity()

    # 🛡️ Verify that it is the same user
    if int(current_user_id) != user_id:
        return jsonify({"error": "Not authorized"}), 403

    user = User.query.get(user_id)
    return jsonify([post.serialize() for post in user.posts]), 200
```

**Authorization diagram:**

```mermaid
flowchart TD
    A["GET /api/users/5/posts"] --> B["@jwt_required() verifies token"]
    B --> C["get_jwt_identity() → '3'"]
    C --> D{"current_user_id == user_id?<br/>3 == 5?"}
    D -->|"No"| E["❌ 403 Forbidden<br/>Not your resource"]
    D -->|"Yes"| F["✅ 200 Return posts"]
```

---

### 🔄 Pattern: Refresh Tokens

For long sessions without asking for login constantly:

```python
from flask_jwt_extended import create_refresh_token, jwt_required, get_jwt_identity

@app.route("/api/login", methods=["POST"])
def login():
    # ... verify credentials ...

    # Create both tokens
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,    # Expires in 1 hour
        "refresh_token": refresh_token   # Expires in 30 days
    }), 200


@app.route("/api/refresh", methods=["POST"])
@jwt_required(refresh=True)  # 👈 Only accepts refresh tokens
def refresh():
    current_user_id = get_jwt_identity()

    # Create new access token
    new_access_token = create_access_token(identity=current_user_id)

    return jsonify({
        "access_token": new_access_token
    }), 200
```

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    Note over C,S: Initial login
    C->>S: POST /api/login
    S-->>C: {access_token, refresh_token}

    Note over C,S: Use access_token (1 hour)
    C->>S: GET /api/profile (access_token)
    S-->>C: 200 {data}

    Note over C,S: Access token expires
    C->>S: GET /api/profile (expired access_token)
    S-->>C: 401 Token expired

    Note over C,S: Renew with refresh_token
    C->>S: POST /api/refresh (refresh_token)
    S-->>C: {access_token: new}

    Note over C,S: Continue with new token
    C->>S: GET /api/profile (new access_token)
    S-->>C: 200 {data}
```

---

### 📋 Summary: The JWT trinity

```mermaid
flowchart TB
    subgraph Create["1️⃣ CREATE (Login)"]
        CA["create_access_token(identity=user.id)"]
        CB["Stores identity in the JWT 'sub' claim"]
    end

    subgraph Protect["2️⃣ PROTECT (Decorator)"]
        PA["@jwt_required()"]
        PB["Verifies token before running the endpoint"]
    end

    subgraph Use["3️⃣ USE (Inside the endpoint)"]
        UA["get_jwt_identity()"]
        UB["Retrieves the stored identity"]
    end

    Create --> Protect --> Use
```

---

## 5️⃣ Protected endpoint: Profile

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()  # 🔒 Requires valid token
def get_profile():
    # Get user ID from token
    current_user_id = get_jwt_identity()

    # Find user in database
    user = User.query.get(current_user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.serialize()), 200
```

### How to send the token

The client must send the token in the `Authorization` header:

```http
GET /api/profile HTTP/1.1
Host: localhost:5000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Protected endpoint flow

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant JWT as JWT Manager
    participant DB as Database

    C->>S: GET /api/profile<br/>Header: Authorization: Bearer JWT_TOKEN
    S->>JWT: Verify token signature
    alt Valid token
        JWT-->>S: identity = "5"
        S->>DB: SELECT user WHERE id=5
        DB-->>S: User data
        S-->>C: 200 {user data}
    else Invalid/expired token
        JWT-->>S: Error
        S-->>C: 401 {error: "Invalid token"}
    end
```

---

## 6️⃣ Update profile (authorization)

```python
@app.route("/api/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    # Get authenticated user ID
    current_user_id = get_jwt_identity()

    # 🛡️ Authorization: You can only edit YOUR profile
    if int(current_user_id) != user_id:
        return jsonify({"error": "Not authorized to edit this user"}), 403

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    body = request.get_json()

    # Update allowed fields
    if "username" in body:
        user.username = body["username"]
    if "email" in body:
        user.email = body["email"]

    db.session.commit()

    return jsonify(user.serialize()), 200
```

---

## 7️⃣ JWT error handling

`flask-jwt-extended` lets you customize error responses:

```python
# Token expired
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "error": "Token expired",
        "message": "Please log in again"
    }), 401


# Invalid token
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "error": "Invalid token",
        "message": "Invalid token signature"
    }), 401


# Missing token
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "error": "Token required",
        "message": "Access token required"
    }), 401
```

---

## 📁 Full code: `app.py`

```python
import os
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
import bcrypt
from dotenv import load_dotenv

load_dotenv()

# =========================
# Configuration
# =========================
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)


# =========================
# Model
# =========================
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


# =========================
# JWT error handlers
# =========================
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Token required"}), 401


# =========================
# Public endpoints
# =========================
@app.route("/api/signup", methods=["POST"])
def signup():
    body = request.get_json()

    if not body:
        return jsonify({"error": "Body required"}), 400

    for field in ["email", "username", "password"]:
        if field not in body or not body[field]:
            return jsonify({"error": f"{field} is required"}), 400

    existing = User.query.filter(
        (User.email == body["email"]) | (User.username == body["username"])
    ).first()

    if existing:
        return jsonify({"error": "Email or username already exists"}), 400

    new_user = User(email=body["email"], username=body["username"])
    new_user.set_password(body["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created", "user": new_user.serialize()}), 201


@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()

    if not body or "email" not in body or "password" not in body:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=body["email"]).first()

    if user is None or not user.check_password(body["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "user": user.serialize()
    }), 200


# =========================
# Protected endpoints
# =========================
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.serialize()), 200


@app.route("/api/private", methods=["GET"])
@jwt_required()
def private():
    current_user_id = get_jwt_identity()
    return jsonify({
        "message": "This is a private endpoint",
        "user_id": current_user_id
    }), 200


# =========================
# Main
# =========================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

## 🧪 Testing with cURL

### 1. Register user

```bash
curl -X POST http://localhost:5000/api/signup \
  -H "Content-Type: application/json" \
  -d '{"email": "ana@example.com", "username": "ana_dev", "password": "secreto123"}'
```

### 2. Log in

```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email": "ana@example.com", "password": "secreto123"}'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": { "id": 1, "email": "ana@example.com", "username": "ana_dev" }
}
```

### 3. Access protected endpoint

```bash
curl -X GET http://localhost:5000/api/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### 4. Without token (error)

```bash
curl -X GET http://localhost:5000/api/profile
# {"error": "Token required"}
```

---

## 🧪 Mini-challenges

### Challenge 1: Add a field to the user

Modify the signup endpoint so it also stores the `full_name` field:

```python
# POST /api/signup
# Body: {"email": "...", "username": "...", "password": "...", "full_name": "Juan Pérez"}
```

<details>
<summary>Hint</summary>

1. Add the column to the model: `full_name = db.Column(db.String(120))`
2. In the signup endpoint, read `body["full_name"]`
3. Assign it when creating the user: `new_user.full_name = body.get("full_name", "")`

</details>

### Challenge 2: Endpoint that returns "Hello, {username}"

Create a protected endpoint `GET /api/hello` that returns a personalized greeting:

```python
# GET /api/hello (with token)
# Response: {"message": "Hello, luis_dev!"}
```

<details>
<summary>Solution</summary>

```python
@app.route("/api/hello", methods=["GET"])
@jwt_required()
def hello():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"Hello, {user.username}!"})
```

</details>

### Challenge 3: Validate password length

Modify the signup endpoint to reject passwords shorter than 6 characters:

```python
# POST /api/signup with password = "123"
# Response: 400 {"error": "Password must be at least 6 characters"}
```

<details>
<summary>Solution</summary>

```python
# In the signup endpoint, before creating the user:
if len(body["password"]) < 6:
    return jsonify({"error": "Password must be at least 6 characters"}), 400
```

</details>

---

## ✅ Checklist for this step

- [ ] I configured `flask-jwt-extended` with a `JWT_SECRET_KEY`
- [ ] My User model has `set_password` and `check_password` with bcrypt
- [ ] I have an `/api/signup` endpoint that hashes the password
- [ ] I have an `/api/login` endpoint that returns a JWT with `create_access_token(identity=user.id)`
- [ ] My protected endpoints use `@jwt_required()`
- [ ] I understand that `@jwt_required()` verifies the token BEFORE running the function
- [ ] I use `get_jwt_identity()` to obtain the user's ID from the token
- [ ] I understand the relationship: `create_access_token(identity=X)` → `get_jwt_identity()` returns `X`
- [ ] I implemented ownership verification (the user only accesses THEIR resources)
- [ ] I tested the endpoints with cURL or Postman
- [ ] I understand when to use `@jwt_required(optional=True)`
