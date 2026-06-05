[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 1: What is a JWT?

## 🎯 Goal

Understand the **internal structure** of a JWT, what information it contains, how it is signed, and why it is secure.

---

## 📦 JWT = JSON Web Token

A JWT is simply a **string of text** that contains information encoded in JSON format. It is used to securely transmit information between two parties.

### Example of a real JWT

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikx1aXMiLCJpYXQiOjE1MTYyMzkwMjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Looks random? It's not. There are **3 parts separated by dots**:

```
HEADER.PAYLOAD.SIGNATURE
```

---

## 🧬 Anatomy of a JWT

```mermaid
flowchart LR
    subgraph JWT["Complete JWT Token"]
        direction TB
        H["🔵 HEADER<br/>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"]
        P["🟢 PAYLOAD<br/>eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikx1aXMi..."]
        S["🔴 SIGNATURE<br/>SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"]
    end

    H --- P --- S
```

### Part 1: Header 🔵

Contains metadata about the token:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

| Field | Meaning                                   |
| ----- | ----------------------------------------- |
| `alg` | Signing algorithm (HS256 = HMAC SHA-256)  |
| `typ` | Token type (always "JWT")                 |

**Encoded in Base64URL** → `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`

---

### Part 2: Payload 🟢

Contains the **claims** — data about the user and the token:

```json
{
  "sub": "5",
  "email": "luis@example.com",
  "username": "luis_dev",
  "iat": 1709913600,
  "exp": 1709917200
}
```

| Claim   | Meaning                       | Example                        |
| ------- | ----------------------------- | ------------------------------ |
| `sub`   | Subject — user ID             | `"5"`                          |
| `email` | User email                    | `"luis@example.com"`           |
| `iat`   | Issued At — when it was created | `1709913600` (timestamp)     |
| `exp`   | Expiration — when it expires  | `1709917200` (1 hour later)    |
| `iss`   | Issuer — who issued it        | `"my-api.com"`                 |

**Encoded in Base64URL** → `eyJzdWIiOiI1IiwiZW1haWwiOiJsdWlzQGV4YW1wbGUuY29tIi4uLn0`

> ⚠️ **IMPORTANT**: The payload is **encoded, NOT encrypted**. Anyone can read it by decoding the Base64. **NEVER put passwords or sensitive data here.**

---

### Part 3: Signature 🔴

This is what makes the JWT **secure**. It is computed like this:

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  SECRET_KEY
)
```

```mermaid
flowchart LR
    H[Encoded header] --> CONCAT
    P[Encoded payload] --> CONCAT
    CONCAT["header.payload"] --> HMAC
    SK[SECRET_KEY<br/>Only the server knows it] --> HMAC
    HMAC[HMACSHA256] --> SIG[Signature]
```

**Why is it secure?**

- Only the server knows the `SECRET_KEY`
- If someone modifies the payload, the signature no longer matches
- The server can verify that the token is authentic

---

## 🔍 Decoding a JWT

You can view the contents of any JWT at [jwt.io](https://jwt.io):

```
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1IiwiZW1haWwiOiJsdWlzQGV4YW1wbGUuY29tIiwiaWF0IjoxNzA5OTEzNjAwLCJleHAiOjE3MDk5MTcyMDB9.abc123signature
```

**Decoded:**

| Part      | JSON                                                                              |
| --------- | --------------------------------------------------------------------------------- |
| Header    | `{"alg": "HS256", "typ": "JWT"}`                                                  |
| Payload   | `{"sub": "5", "email": "luis@example.com", "iat": 1709913600, "exp": 1709917200}` |
| Signature | (cannot be decoded, it is a hash)                                                 |

### In Python

This code lets you **see what is inside a JWT** (without verifying the signature). It is useful for understanding how it works internally.

```python
import base64
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1In0.signature"

# Extract the payload (second part)
payload_b64 = token.split(".")[1]

# Add padding if needed
payload_b64 += "=" * (4 - len(payload_b64) % 4)

# Decode
payload = json.loads(base64.urlsafe_b64decode(payload_b64))
print(payload)  # {'sub': '5'}
```

#### Line-by-line explanation:

```python
import base64  # Library to encode/decode Base64
import json    # Library to work with JSON
```

```python
token = "eyJhbG...eyJzdW...signature"
#       ^^^^^^^^ ^^^^^^^ ^^^^^^^^^
#       Header   Payload Signature
#       (part 0) (part 1) (part 2)
```

```python
payload_b64 = token.split(".")[1]
#                   ^^^^^^^^^^
#                   Splits by "." and takes index [1] (second part)
#                   Result: "eyJzdWIiOiI1In0"
```

```python
payload_b64 += "=" * (4 - len(payload_b64) % 4)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#              Base64 requires the length to be a multiple of 4
#              This appends "=" at the end if needed (padding)
```

```python
payload = json.loads(base64.urlsafe_b64decode(payload_b64))
#         ^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         |          Decodes Base64 → bytes
#         Converts JSON bytes to Python dictionary
```

```python
print(payload)  # {'sub': '5'}
```

> 💡 **Note**: In practice, you don't need to do this manually. Libraries like `flask-jwt-extended` do it for you. This example is just to understand how it works internally.

---

## ⏰ Token Expiration

JWTs have an expiration date for security:

```mermaid
flowchart LR
    subgraph Token["JWT"]
        EXP["exp: 1709917200<br/>(March 8 2024, 13:00)"]
    end

    subgraph Check["Verification"]
        NOW["Current time"]
        VALID["✅ Valid token"]
        EXPIRED["❌ Expired token"]
    end

    Token --> Check
    NOW -->|before exp| VALID
    NOW -->|after exp| EXPIRED
```

**Typical expiration times:**

- Access token: 15 minutes - 1 hour
- Refresh token: 7 days - 30 days

---

## 🔐 Why is JWT secure?

### 1. The signature guarantees integrity

```mermaid
flowchart TD
    subgraph Attack["❌ Attack attempt"]
        A1["Attacker obtains JWT"]
        A2["Modifies payload:<br/>sub: '1' → sub: '999'"]
        A3["Sends modified token"]
        A4["Server verifies signature"]
        A5["❌ Signature does NOT match<br/>Token rejected"]
    end

    A1 --> A2 --> A3 --> A4 --> A5
```

### 2. Only the server can create valid tokens

```mermaid
flowchart TD
    subgraph Legit["✅ Legitimate flow"]
        L1["Server generates JWT"]
        L2["Signs with SECRET_KEY"]
        L3["Client receives token"]
        L4["Client sends token"]
        L5["Server verifies with SECRET_KEY"]
        L6["✅ Signature matches"]
    end

    L1 --> L2 --> L3 --> L4 --> L5 --> L6
```

---

## 🚫 What JWT does NOT do

| JWT does NOT...        | Why                                           |
| ---------------------- | --------------------------------------------- |
| Encrypt the data       | The payload is readable by anyone (Base64)    |
| Prevent token theft    | If someone gets your token, they can use it   |
| Revoke tokens          | Once issued, valid until expiration           |

### Mitigations

| Problem         | Solution                                |
| --------------- | --------------------------------------- |
| Sensitive data  | Don't put it in the payload             |
| Token theft     | HTTPS, HttpOnly cookies, short tokens   |
| Revocation      | Blacklist in Redis, very short tokens   |

---

## 📋 Standard JWT claims

| Claim | Name       | Description                    |
| ----- | ---------- | ------------------------------ |
| `iss` | Issuer     | Who issued the token           |
| `sub` | Subject    | User ID (the "subject")        |
| `aud` | Audience   | Who it is intended for         |
| `exp` | Expiration | When it expires (timestamp)    |
| `nbf` | Not Before | Not valid before this date     |
| `iat` | Issued At  | When it was created            |
| `jti` | JWT ID     | Unique token ID                |

### Custom claims

You can add any data you need:

```json
{
  "sub": "5",
  "email": "luis@example.com",
  "role": "admin",
  "plan": "premium",
  "org_id": "42"
}
```

---

## 🧪 Practice: Inspect a JWT

1. Go to [jwt.io](https://jwt.io)
2. Paste this token:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJhbmFAZXhhbXBsZS5jb20iLCJ1c2VybmFtZSI6ImFuYV9kZXYiLCJpYXQiOjE3MDk5MTM2MDAsImV4cCI6MTcwOTkxNzIwMH0.abc123
```

3. Observe:
   - What algorithm does it use?
   - What is the user's email?
   - When does it expire? (convert the timestamp)

---

## 🧪 Mini-challenge: Decode and analyze

### Challenge 1: What does this token contain?

Decode this JWT at [jwt.io](https://jwt.io) and answer the questions:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJNYXJpYSBHYXJjaWEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3MDk5MTM2MDAsImV4cCI6MTcwOTkyMDgwMH0.fake_signature
```

| Question                                          | Your answer  |
| ------------------------------------------------- | ------------ |
| What is the user ID (sub)?                        |              |
| What is the name?                                 |              |
| What role does it have?                           |              |
| In how many hours does it expire? (compute exp - iat) |          |

<details>
<summary>See answers</summary>

| Question             | Answer                                       |
| -------------------- | -------------------------------------------- |
| User ID (sub)        | `42`                                         |
| Name                 | `Maria Garcia`                               |
| Role                 | `admin`                                      |
| Hours until expiry   | `(1709920800 - 1709913600) / 3600 = 2 hours` |

</details>

### Challenge 2: Why is this a security problem?

A junior developer created this token:

```json
{
  "sub": "1",
  "email": "admin@company.com",
  "password": "admin123",
  "creditCard": "4111-1111-1111-1111"
}
```

What's wrong? Why is it dangerous?

<details>
<summary>See answer</summary>

**Serious problems:**

1. **Password in the payload** — Anyone can decode the JWT with Base64 and see the password
2. **Credit card** — Sensitive data exposed
3. **The payload is NOT encrypted** — Only encoded in Base64, which is reversible

**Remember:** The JWT payload is like writing on a postcard — the mail carrier (and anyone else) can read it. Only put information you're OK with anyone seeing.

</details>

---

## ✅ Checklist for this step

- [ ] I know a JWT has 3 parts: header.payload.signature
- [ ] I understand the payload is encoded, NOT encrypted
- [ ] I know which common claims exist (sub, exp, iat)
- [ ] I understand how the signature guarantees integrity
- [ ] I know why I should not put sensitive data in the JWT
