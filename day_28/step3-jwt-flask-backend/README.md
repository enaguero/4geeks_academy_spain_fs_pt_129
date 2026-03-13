# Step 3: JWT en Flask con flask-jwt-extended

## 🎯 Objetivo

Implementar autenticación completa en Flask:

- Registro de usuarios con contraseña hasheada
- Login que retorna JWT
- Endpoints protegidos con `@jwt_required()`
- Obtener el usuario actual con `get_jwt_identity()`

---

## 📦 Instalación

```bash
pip install flask flask-sqlalchemy flask-jwt-extended bcrypt python-dotenv
```

---

## 🗺️ Mapa de endpoints

```mermaid
flowchart LR
    subgraph Públicos["🌐 Endpoints Públicos"]
        R[POST /api/signup]
        L[POST /api/login]
    end

    subgraph Protegidos["🔒 Endpoints Protegidos"]
        P[GET /api/profile]
        U[PUT /api/profile]
        PR[GET /api/private]
    end

    R -->|Crea usuario| DB[(Database)]
    L -->|Verifica credenciales| DB
    L -->|Retorna JWT| Cliente
    Cliente -->|JWT en header| P
    Cliente -->|JWT en header| U
    Cliente -->|JWT en header| PR
```

---

## 1️⃣ Configuración básica

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

# Configuración
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ⚠️ IMPORTANTE: Cambiar en producción
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-dev-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)
```

### `.env`

```env
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=mi-clave-super-secreta-cambiar-en-produccion
```

---

## 2️⃣ Modelo de Usuario

### Antes del código: ¿Qué es un Hash?

Antes de ver el modelo, necesitas entender por qué usamos `bcrypt` y qué significa "hashear" una contraseña.

#### El problema: ¿Cómo guardar contraseñas?

```python
# ❌ NUNCA hagas esto - guardar contraseña en texto plano
class User(db.Model):
    password = db.Column(db.String(80))  # "hola123" → se guarda "hola123"
```

Si alguien hackea tu base de datos, tiene TODAS las contraseñas.

#### La solución: Hash (función de un solo sentido)

Un **hash** es como una **licuadora digital**:

```mermaid
flowchart LR
    subgraph Licuadora["🔄 Hash (bcrypt)"]
        direction TB
        Input["'hola123'"] --> Process["Algoritmo<br/>matemático"]
        Process --> Output["'$2b$12$LQv3c...'"]
    end

    subgraph Imposible["❌ No se puede revertir"]
        Output2["'$2b$12$LQv3c...'"] -.-> Input2["'???'"]
    end
```

| Concepto         | Analogía de la licuadora                           |
| ---------------- | -------------------------------------------------- |
| **Hash**         | Licuar una fruta → obtienes jugo                   |
| **Irreversible** | NO puedes "deslicuar" el jugo → recuperar la fruta |
| **Determinista** | La misma fruta siempre da el mismo jugo            |
| **Verificación** | Para comprobar, licuas otra fruta y comparas jugos |

#### ¿Cómo verificamos contraseñas entonces?

```mermaid
sequenceDiagram
    participant U as Usuario
    participant S as Servidor
    participant DB as Database

    Note over U,DB: Durante el registro
    U->>S: password = "hola123"
    S->>S: hash = bcrypt("hola123") → "$2b$12$LQv..."
    S->>DB: Guardar hash (NO la contraseña)

    Note over U,DB: Durante el login
    U->>S: password = "hola123"
    S->>DB: Obtener hash guardado
    DB-->>S: "$2b$12$LQv..."
    S->>S: bcrypt("hola123") → ¿coincide con "$2b$12$LQv..."?
    S-->>U: ✅ Contraseña correcta
```

#### ¿Por qué bcrypt y no otro hash?

| Algoritmo  | Velocidad           | Seguridad | ¿Para contraseñas? |
| ---------- | ------------------- | --------- | ------------------ |
| MD5        | Muy rápido          | ❌ Roto   | ❌ NO              |
| SHA-256    | Muy rápido          | ✅ Seguro | ❌ NO (muy rápido) |
| **bcrypt** | Lento (a propósito) | ✅ Seguro | ✅ SÍ              |

**bcrypt es lento a propósito**: Si un atacante intenta adivinar millones de contraseñas, cada intento tarda ~100ms. Eso hace que fuerza bruta sea impracticable.

---

### Antes del código: ¿Qué es serializar?

Cuando Flask responde a una petición, necesita enviar datos en formato **JSON** (texto plano). Pero SQLAlchemy nos devuelve **objetos Python** — y Python no sabe cómo convertir automáticamente un objeto complejo a JSON.

```python
# Esto NO funciona:
user = User.query.get(5)
return jsonify(user)  # ❌ TypeError: Object of type User is not JSON serializable
```

¿Por qué falla? Porque `user` es un objeto con métodos, conexiones a la base de datos, estado interno... JSON solo entiende tipos simples: textos, números, listas y diccionarios.

La solución es crear un método `serialize()` que **extraiga los datos** del objeto y los ponga en un diccionario:

```python
# Esto SÍ funciona:
return jsonify(user.serialize())  # ✅ → {"id": 5, "email": "luis@example.com", ...}
```

```mermaid
flowchart LR
    A["🐍 Objeto Python<br/>User(id=5, email='luis@...', password_hash='$2b$...')"] -->|"serialize()"| B["📖 Diccionario<br/>{id: 5, email: 'luis@...'}<br/>(sin password!)"]
    B -->|"jsonify()"| C["📤 JSON por HTTP<br/>id: 5, email: luis@..."]
```

> 💡 `serialize()` también actúa como **filtro de seguridad**: decides qué campos exponer y cuáles ocultar (como `password_hash`).

---

### El código del modelo

```python
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def set_password(self, password):
        """Hashea y guarda la contraseña"""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            salt
        ).decode('utf-8')

    def check_password(self, password):
        """Verifica si la contraseña es correcta"""
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password_hash.encode('utf-8')
        )

    def serialize(self):
        """Retorna datos públicos (NUNCA el password)"""
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
```

> ⚠️ **NUNCA** guardes contraseñas en texto plano. Siempre usa hash con bcrypt.

---

## 3️⃣ Endpoint: Registro (Signup)

```python
@app.route("/api/signup", methods=["POST"])
def signup():
    body = request.get_json()

    # Validación
    if not body:
        return jsonify({"error": "Body requerido"}), 400

    required_fields = ["email", "username", "password"]
    for field in required_fields:
        if field not in body or not body[field]:
            return jsonify({"error": f"{field} es requerido"}), 400

    # Verificar que no exista
    existing_user = User.query.filter(
        (User.email == body["email"]) | (User.username == body["username"])
    ).first()

    if existing_user:
        return jsonify({"error": "El email o username ya está registrado"}), 400

    # Crear usuario
    new_user = User(
        email=body["email"],
        username=body["username"]
    )
    new_user.set_password(body["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Usuario creado exitosamente",
        "user": new_user.serialize()
    }), 201
```

### Flujo de signup

```mermaid
sequenceDiagram
    participant C as Cliente
    participant S as Servidor
    participant DB as Database

    C->>S: POST /api/signup<br/>{email, username, password}
    S->>S: Validar campos
    S->>DB: ¿Existe email/username?
    DB-->>S: No existe
    S->>S: Hashear password con bcrypt
    S->>DB: INSERT usuario
    DB-->>S: OK
    S-->>C: 201 {message, user}
```

---

## 4️⃣ Endpoint: Login

```python
@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()

    # Validación
    if not body or "email" not in body or "password" not in body:
        return jsonify({"error": "Email y password son requeridos"}), 400

    # Buscar usuario
    user = User.query.filter_by(email=body["email"]).first()

    # Verificar credenciales
    if user is None or not user.check_password(body["password"]):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Crear token JWT
    # El "identity" es lo que get_jwt_identity() retornará después
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login exitoso",
        "access_token": access_token,
        "user": user.serialize()
    }), 200
```

### Flujo de login

```mermaid
sequenceDiagram
    participant C as Cliente
    participant S as Servidor
    participant DB as Database

    C->>S: POST /api/login<br/>{email, password}
    S->>DB: SELECT user WHERE email=?
    DB-->>S: User data (con password_hash)
    S->>S: bcrypt.checkpw(password, hash)
    alt Password correcto
        S->>S: create_access_token(identity=user.id)
        S-->>C: 200 {access_token, user}
    else Password incorrecto
        S-->>C: 401 {error: "Credenciales inválidas"}
    end
```

---

## 🔑 Profundizando: `create_access_token`, `@jwt_required()` y `get_jwt_identity()`

Esta es la trinidad de `flask-jwt-extended`. Entender cómo se conectan es **fundamental**.

Este también es el **mejor lugar del día 28** para explicar decoradores: aquí `@jwt_required()` ya no es teoría aislada, sino una pieza real del flujo de autenticación que acabas de construir con login + token.

### Primero: ¿Qué es un decorador en Python?

Si ves `@algo` arriba de una función y no entiendes qué hace, esta sección es para ti.

Un **decorador** es una función que **"envuelve" otra función** para añadirle funcionalidad sin modificar su código.

#### Analogía: El guardia de seguridad

```mermaid
flowchart LR
    subgraph SinDecorador["❌ Sin decorador"]
        R1["Request"] --> F1["get_profile()"]
        F1 --> D1["Retorna datos"]
    end

    subgraph ConDecorador["✅ Con @jwt_required()"]
        R2["Request"] --> G["🔒 Guardia<br/>(jwt_required)"]
        G -->|"Token válido"| F2["get_profile()"]
        G -->|"Token inválido"| X["❌ 401 Error"]
        F2 --> D2["Retorna datos"]
    end
```

Es como poner un **guardia de seguridad** en la puerta de una función:

```python
# SIN decorador - cualquiera puede entrar
def get_profile():
    return {"user": "datos secretos"}

# CON decorador - el guardia verifica primero
@jwt_required()  # ← "Antes de dejar pasar, verifica el token"
def get_profile():
    return {"user": "datos secretos"}
```

#### ¿Cómo funciona por dentro? (opcional)

Si tienes curiosidad, un decorador es solo una función que recibe otra función:

```python
# Esto:
@jwt_required()
def get_profile():
    pass

# Es equivalente a esto:
def get_profile():
    pass
get_profile = jwt_required()(get_profile)  # Envuelve la función
```

No necesitas entender esto para usar decoradores — solo saber que **añaden comportamiento extra** a tus funciones.

#### En el contexto de este día: ¿qué hace exactamente `@jwt_required()`?

En JWT, el decorador cumple este papel:

1. El usuario hace login y el backend crea un token con `create_access_token(...)`.
2. El frontend guarda ese token y lo envía en el header `Authorization`.
3. Cuando llega una petición a una ruta protegida, `@jwt_required()` corre **antes** que tu función.
4. Si el token falla, Flask responde con `401` y tu función **ni siquiera se ejecuta**.
5. Si el token es válido, entonces sí entra a tu función y `get_jwt_identity()` puede leer el `identity` guardado en el JWT.

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    return {"user_id": current_user_id}, 200
```

Orden real de ejecución en este ejemplo:

1. Flask detecta que la URL `/api/profile` corresponde a `get_profile`.
2. `@jwt_required()` inspecciona el header `Authorization`.
3. Verifica formato, firma y expiración del token.
4. Solo si todo está bien se ejecuta `get_profile()`.
5. Dentro de `get_profile()`, `get_jwt_identity()` recupera el usuario autenticado.

---

### El ciclo completo del identity

```mermaid
flowchart LR
    subgraph Login["🔐 Durante el Login"]
        A["user.id = 5"]
        B["create_access_token(identity='5')"]
        C["JWT generado con sub='5'"]
    end

    subgraph Token["📦 Dentro del JWT"]
        D["payload: {sub: '5', exp: ...}"]
    end

    subgraph Request["🔒 En endpoint protegido"]
        E["@jwt_required()"]
        F["get_jwt_identity()"]
        G["Retorna '5'"]
    end

    A --> B --> C --> D
    D -->|"Authorization: Bearer token"| E
    E -->|"Token válido"| F --> G
```

### ¿Qué hace cada función?

| Función                           | Cuándo se usa                     | Qué hace                                          |
| --------------------------------- | --------------------------------- | ------------------------------------------------- |
| `create_access_token(identity=X)` | En el **login**                   | Crea un JWT con `X` guardado en el claim `sub`    |
| `@jwt_required()`                 | Como **decorador** de endpoints   | Verifica que el request tenga un JWT válido       |
| `get_jwt_identity()`              | **Dentro** del endpoint protegido | Extrae y retorna el valor de `identity` del token |

---

### 📌 `create_access_token(identity=...)` en detalle

Esta función **genera el JWT** y guarda el `identity` dentro del token:

```python
# En el login, después de verificar credenciales:
access_token = create_access_token(identity=str(user.id))
```

**¿Qué se guarda como identity?**

Puedes guardar lo que quieras, pero lo más común es el **ID del usuario**:

```python
# ✅ Opción recomendada: Solo el ID (string)
access_token = create_access_token(identity=str(user.id))

# ⚠️ También posible: Un diccionario
access_token = create_access_token(identity={
    "id": user.id,
    "email": user.email,
    "role": "admin"
})

# ❌ NO recomendado: Datos sensibles
access_token = create_access_token(identity={
    "password": user.password  # ¡NUNCA hagas esto!
})
```

**¿Por qué string y no int?**

`flask-jwt-extended` serializa el identity a JSON. Es buena práctica usar strings para evitar problemas:

```python
# ✅ Recomendado
create_access_token(identity=str(user.id))  # "5"

# ⚠️ También funciona, pero...
create_access_token(identity=user.id)  # 5
```

---

### 📌 `@jwt_required()` en detalle

Este **decorador** hace varias cosas automáticamente:

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()  # 👈 Este decorador...
def get_profile():
    # ... código del endpoint
```

**¿Qué hace el decorador?**

```mermaid
flowchart TD
    A["Request llega al endpoint"] --> B{"¿Header Authorization existe?"}
    B -->|No| C["❌ 401: Token requerido"]
    B -->|Sí| D{"¿Formato correcto?<br/>Bearer TOKEN_JWT"}
    D -->|No| E["❌ 401: Formato inválido"]
    D -->|Sí| F{"¿Firma válida?<br/>Verificar con SECRET_KEY"}
    F -->|No| G["❌ 401: Token inválido"]
    F -->|Sí| H{"¿Token expirado?<br/>Verificar claim exp"}
    H -->|Sí| I["❌ 401: Token expirado"]
    H -->|No| J["✅ Ejecutar función del endpoint"]
```

**Variantes del decorador:**

```python
# Token obligatorio (más común)
@jwt_required()
def endpoint_protegido():
    pass

# Token opcional - no falla si no hay token
@jwt_required(optional=True)
def endpoint_mixto():
    user_id = get_jwt_identity()  # None si no hay token
    if user_id:
        # Usuario autenticado
    else:
        # Usuario anónimo

# Solo refresh tokens (para renovar access tokens)
@jwt_required(refresh=True)
def refresh_token():
    pass
```

---

### 📌 `get_jwt_identity()` en detalle

Esta función **extrae el identity** del token que ya fue verificado por `@jwt_required()`:

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    # Obtener el identity que guardamos en el login
    current_user_id = get_jwt_identity()

    # current_user_id = "5" (el string que pasamos a create_access_token)

    # Ahora podemos buscar al usuario en la DB
    user = User.query.get(current_user_id)
```

**El flujo completo visualizado:**

```mermaid
sequenceDiagram
    participant Cliente
    participant Decorador as "@jwt_required()"
    participant Funcion as "get_profile()"
    participant DB as Database

    Note over Cliente,DB: 1. Login previo generó token con identity="5"

    Cliente->>Decorador: GET /api/profile<br/>Authorization: Bearer eyJ...
    Decorador->>Decorador: Extraer token del header
    Decorador->>Decorador: Verificar firma con SECRET_KEY
    Decorador->>Decorador: Verificar que no expiró

    alt Token inválido
        Decorador-->>Cliente: 401 Error
    else Token válido
        Decorador->>Funcion: Permitir ejecución
        Funcion->>Funcion: get_jwt_identity() → "5"
        Funcion->>DB: SELECT * FROM users WHERE id = 5
        DB-->>Funcion: User data
        Funcion-->>Cliente: 200 {user data}
    end
```

---

### 🎯 Patrón común: Helper para obtener el usuario actual

En lugar de repetir código, crea un helper:

```python
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

def get_current_user():
    """
    Obtiene el usuario actual del token JWT.
    Debe usarse dentro de un endpoint con @jwt_required()
    """
    user_id = get_jwt_identity()
    if user_id is None:
        return None
    return User.query.get(user_id)


# Uso en endpoints:
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user = get_current_user()
    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.serialize()), 200


@app.route("/api/favorites", methods=["GET"])
@jwt_required()
def get_favorites():
    user = get_current_user()
    return jsonify([fav.serialize() for fav in user.favorites]), 200
```

---

### 🛡️ Patrón: Verificar ownership (autorización)

Un caso muy común es verificar que el usuario solo pueda acceder a **sus propios recursos**:

```python
@app.route("/api/users/<int:user_id>/posts", methods=["GET"])
@jwt_required()
def get_user_posts(user_id):
    current_user_id = get_jwt_identity()

    # 🛡️ Verificar que es el mismo usuario
    if int(current_user_id) != user_id:
        return jsonify({"error": "No autorizado"}), 403

    user = User.query.get(user_id)
    return jsonify([post.serialize() for post in user.posts]), 200
```

**Diagrama de autorización:**

```mermaid
flowchart TD
    A["GET /api/users/5/posts"] --> B["@jwt_required() verifica token"]
    B --> C["get_jwt_identity() → '3'"]
    C --> D{"¿current_user_id == user_id?<br/>¿3 == 5?"}
    D -->|"No"| E["❌ 403 Forbidden<br/>No es tu recurso"]
    D -->|"Sí"| F["✅ 200 Retornar posts"]
```

---

### 🔄 Patrón: Refresh Tokens

Para sesiones largas sin pedir login constantemente:

```python
from flask_jwt_extended import create_refresh_token, jwt_required, get_jwt_identity

@app.route("/api/login", methods=["POST"])
def login():
    # ... verificar credenciales ...

    # Crear ambos tokens
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,    # Expira en 1 hora
        "refresh_token": refresh_token   # Expira en 30 días
    }), 200


@app.route("/api/refresh", methods=["POST"])
@jwt_required(refresh=True)  # 👈 Solo acepta refresh tokens
def refresh():
    current_user_id = get_jwt_identity()

    # Crear nuevo access token
    new_access_token = create_access_token(identity=current_user_id)

    return jsonify({
        "access_token": new_access_token
    }), 200
```

```mermaid
sequenceDiagram
    participant C as Cliente
    participant S as Servidor

    Note over C,S: Login inicial
    C->>S: POST /api/login
    S-->>C: {access_token, refresh_token}

    Note over C,S: Usar access_token (1 hora)
    C->>S: GET /api/profile (access_token)
    S-->>C: 200 {data}

    Note over C,S: Access token expira
    C->>S: GET /api/profile (access_token expirado)
    S-->>C: 401 Token expirado

    Note over C,S: Renovar con refresh_token
    C->>S: POST /api/refresh (refresh_token)
    S-->>C: {access_token: nuevo}

    Note over C,S: Continuar con nuevo token
    C->>S: GET /api/profile (nuevo access_token)
    S-->>C: 200 {data}
```

---

### 📋 Resumen: La trinidad JWT

```mermaid
flowchart TB
    subgraph Crear["1️⃣ CREAR (Login)"]
        CA["create_access_token(identity=user.id)"]
        CB["Guarda identity en el claim 'sub' del JWT"]
    end

    subgraph Proteger["2️⃣ PROTEGER (Decorador)"]
        PA["@jwt_required()"]
        PB["Verifica token antes de ejecutar el endpoint"]
    end

    subgraph Usar["3️⃣ USAR (Dentro del endpoint)"]
        UA["get_jwt_identity()"]
        UB["Recupera el identity guardado"]
    end

    Crear --> Proteger --> Usar
```

---

## 5️⃣ Endpoint protegido: Profile

```python
@app.route("/api/profile", methods=["GET"])
@jwt_required()  # 🔒 Requiere token válido
def get_profile():
    # Obtener el ID del usuario desde el token
    current_user_id = get_jwt_identity()

    # Buscar usuario en la base de datos
    user = User.query.get(current_user_id)

    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(user.serialize()), 200
```

### Cómo enviar el token

El cliente debe enviar el token en el header `Authorization`:

```http
GET /api/profile HTTP/1.1
Host: localhost:5000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Flujo de endpoint protegido

```mermaid
sequenceDiagram
    participant C as Cliente
    participant S as Servidor
    participant JWT as JWT Manager
    participant DB as Database

    C->>S: GET /api/profile<br/>Header: Authorization: Bearer TOKEN_JWT
    S->>JWT: Verificar firma del token
    alt Token válido
        JWT-->>S: identity = "5"
        S->>DB: SELECT user WHERE id=5
        DB-->>S: User data
        S-->>C: 200 {user data}
    else Token inválido/expirado
        JWT-->>S: Error
        S-->>C: 401 {error: "Token inválido"}
    end
```

---

## 6️⃣ Actualizar perfil (autorización)

```python
@app.route("/api/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    # Obtener ID del usuario autenticado
    current_user_id = get_jwt_identity()

    # 🛡️ Autorización: Solo puedes editar TU perfil
    if int(current_user_id) != user_id:
        return jsonify({"error": "No autorizado para editar este usuario"}), 403

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    body = request.get_json()

    # Actualizar campos permitidos
    if "username" in body:
        user.username = body["username"]
    if "email" in body:
        user.email = body["email"]

    db.session.commit()

    return jsonify(user.serialize()), 200
```

---

## 7️⃣ Manejo de errores JWT

`flask-jwt-extended` permite personalizar las respuestas de error:

```python
# Token expirado
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "error": "Token expirado",
        "message": "Por favor, inicia sesión nuevamente"
    }), 401


# Token inválido
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "error": "Token inválido",
        "message": "Firma de token inválida"
    }), 401


# Token faltante
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "error": "Token requerido",
        "message": "Se requiere token de acceso"
    }), 401
```

---

## 📁 Código completo: `app.py`

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
# Configuración
# =========================
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)


# =========================
# Modelo
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
# Error handlers JWT
# =========================
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token expirado"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Token inválido"}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Token requerido"}), 401


# =========================
# Endpoints públicos
# =========================
@app.route("/api/signup", methods=["POST"])
def signup():
    body = request.get_json()

    if not body:
        return jsonify({"error": "Body requerido"}), 400

    for field in ["email", "username", "password"]:
        if field not in body or not body[field]:
            return jsonify({"error": f"{field} es requerido"}), 400

    existing = User.query.filter(
        (User.email == body["email"]) | (User.username == body["username"])
    ).first()

    if existing:
        return jsonify({"error": "El email o username ya existe"}), 400

    new_user = User(email=body["email"], username=body["username"])
    new_user.set_password(body["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario creado", "user": new_user.serialize()}), 201


@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()

    if not body or "email" not in body or "password" not in body:
        return jsonify({"error": "Email y password requeridos"}), 400

    user = User.query.filter_by(email=body["email"]).first()

    if user is None or not user.check_password(body["password"]):
        return jsonify({"error": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "user": user.serialize()
    }), 200


# =========================
# Endpoints protegidos
# =========================
@app.route("/api/profile", methods=["GET"])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(user.serialize()), 200


@app.route("/api/private", methods=["GET"])
@jwt_required()
def private():
    current_user_id = get_jwt_identity()
    return jsonify({
        "message": "Este es un endpoint privado",
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

## 🧪 Probando con cURL

### 1. Registrar usuario

```bash
curl -X POST http://localhost:5000/api/signup \
  -H "Content-Type: application/json" \
  -d '{"email": "ana@example.com", "username": "ana_dev", "password": "secreto123"}'
```

### 2. Hacer login

```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email": "ana@example.com", "password": "secreto123"}'
```

**Respuesta:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": { "id": 1, "email": "ana@example.com", "username": "ana_dev" }
}
```

### 3. Acceder a endpoint protegido

```bash
curl -X GET http://localhost:5000/api/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### 4. Sin token (error)

```bash
curl -X GET http://localhost:5000/api/profile
# {"error": "Token requerido"}
```

---

## 🧪 Mini-retos

### Reto 1: Agrega un campo al usuario

Modifica el endpoint de signup para que también guarde el campo `full_name`:

```python
# POST /api/signup
# Body: {"email": "...", "username": "...", "password": "...", "full_name": "Juan Pérez"}
```

<details>
<summary>Pista</summary>

1. Agrega la columna al modelo: `full_name = db.Column(db.String(120))`
2. En el endpoint de signup, lee `body["full_name"]`
3. Asígnalo al crear el usuario: `new_user.full_name = body.get("full_name", "")`

</details>

### Reto 2: Endpoint que retorna "Hola, {username}"

Crea un endpoint protegido `GET /api/hello` que retorne un saludo personalizado:

```python
# GET /api/hello (con token)
# Response: {"message": "Hola, luis_dev!"}
```

<details>
<summary>Solución</summary>

```python
@app.route("/api/hello", methods=["GET"])
@jwt_required()
def hello():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify({"message": f"Hola, {user.username}!"})
```

</details>

### Reto 3: Validar longitud de contraseña

Modifica el endpoint de signup para rechazar contraseñas menores a 6 caracteres:

```python
# POST /api/signup con password = "123"
# Response: 400 {"error": "La contraseña debe tener al menos 6 caracteres"}
```

<details>
<summary>Solución</summary>

```python
# En el endpoint de signup, antes de crear el usuario:
if len(body["password"]) < 6:
    return jsonify({"error": "La contraseña debe tener al menos 6 caracteres"}), 400
```

</details>

---

## ✅ Checklist de este step

- [ ] Configuré `flask-jwt-extended` con un `JWT_SECRET_KEY`
- [ ] Mi modelo User tiene `set_password` y `check_password` con bcrypt
- [ ] Tengo endpoint `/api/signup` que hashea la contraseña
- [ ] Tengo endpoint `/api/login` que retorna un JWT con `create_access_token(identity=user.id)`
- [ ] Mis endpoints protegidos usan `@jwt_required()`
- [ ] Entiendo que `@jwt_required()` verifica el token ANTES de ejecutar la función
- [ ] Uso `get_jwt_identity()` para obtener el ID del usuario del token
- [ ] Entiendo la relación: `create_access_token(identity=X)` → `get_jwt_identity()` retorna `X`
- [ ] Implementé verificación de ownership (el usuario solo accede a SUS recursos)
- [ ] Probé los endpoints con cURL o Postman
- [ ] Entiendo cuándo usar `@jwt_required(optional=True)`
