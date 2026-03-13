# Step 0.5: Glosario Técnico

## 🎯 Objetivo

Este glosario define los términos técnicos que usaremos durante todo el día 28. Si te encuentras con una palabra que no entiendes, vuelve aquí.

---

## 📖 Términos fundamentales

### Endpoint

Un **endpoint** es una URL específica de tu API donde puedes enviar peticiones.

```
Ejemplo de endpoints:
POST /api/login     ← Endpoint para hacer login
GET  /api/users     ← Endpoint para obtener usuarios
GET  /api/users/5   ← Endpoint para obtener el usuario 5
```

**Analogía**: Si tu API es un restaurante, cada endpoint es un plato del menú. Tienes que pedir el plato correcto (endpoint) para obtener lo que quieres.

---

### Header HTTP

Un **header** es información adicional que viaja junto a cada petición HTTP. Son como etiquetas en un paquete de correo.

```
Petición HTTP:
┌─────────────────────────────────────────┐
│ GET /api/profile                        │ ← La URL
├─────────────────────────────────────────┤
│ Headers:                                │
│   Content-Type: application/json        │ ← "El contenido es JSON"
│   Authorization: Bearer eyJhbG...       │ ← "Mi token es este"
│   Accept-Language: es                   │ ← "Respóndeme en español"
└─────────────────────────────────────────┘
```

El header más importante para autenticación es **Authorization**, donde enviamos nuestro token JWT.

---

### Bearer Token

**Bearer** significa "portador" en inglés. Cuando decimos `Authorization: Bearer <token>`, estamos diciendo "el portador de este token tiene permiso".

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
               ^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               Tipo   El token JWT
```

Es un estándar de la industria para enviar tokens en APIs REST.

---

### Hash vs Cifrado

Estos dos conceptos se confunden frecuentemente, pero son MUY diferentes:

| Concepto    | ¿Reversible? | Uso principal                    | Ejemplo         |
| ----------- | ------------ | -------------------------------- | --------------- |
| **Hash**    | ❌ NO        | Contraseñas                      | bcrypt, SHA-256 |
| **Cifrado** | ✅ SÍ        | Datos que necesitas leer después | AES, RSA        |

```mermaid
flowchart LR
    subgraph Hash["Hash (una sola dirección)"]
        A["'hola123'"] --> B["$2b$12$xyz..."]
        B -.-x A
    end

    subgraph Cifrado["Cifrado (dos direcciones)"]
        C["'mensaje'"] -->|"cifrar"| D["X#@!$%"]
        D -->|"descifrar"| C
    end
```

**¿Por qué usamos hash para contraseñas?**

- Si alguien hackea tu base de datos, NO puede recuperar las contraseñas
- Para verificar, hasheas la contraseña enviada y comparas hashes

---

### Base64

**Base64** es una forma de **codificar** (no cifrar) datos binarios en texto.

```
Original: {"user": "luis"}
Base64:   eyJ1c2VyIjogImx1aXMifQ==
```

⚠️ **IMPORTANTE**: Base64 NO es seguro. Cualquiera puede decodificarlo:

```javascript
atob('eyJ1c2VyIjogImx1aXMifQ=='); // → {"user": "luis"}
```

El JWT usa Base64 para el header y payload, por eso **nunca debes poner datos sensibles** (contraseñas, tarjetas de crédito) en un JWT.

---

### Serialización

**Serializar** significa convertir algo que existe **dentro de tu programa** en un formato que se puede **transmitir o guardar**.

#### ¿Por qué es necesario?

Dentro de Python, los datos viven en la **memoria RAM** como objetos complejos. Pero cuando necesitas enviar esos datos a otro lugar (a un navegador, a otra API, a un archivo), necesitas convertirlos a un formato **universal** que cualquiera pueda leer — como texto plano.

#### Analogía 1: El LEGO por correo 🧱

Imagina que tienes un LEGO armado (un castillo). No puedes enviarlo por correo así — se rompe. Lo que haces es **desarmarlo**, meterlo en una caja con **instrucciones** paso a paso, y enviarlo. La otra persona recibe la caja, lee las instrucciones, y lo arma de vuelta. Eso es serialización.

```
🏰 Castillo LEGO armado  →  📦 Caja con piezas + instrucciones  →  🏰 Castillo armado en destino
   (objeto en RAM)            (JSON / texto plano)                  (objeto en el otro programa)
   "serializar"                                                      "deserializar"
```

#### Analogía 2: La receta de cocina 🍳

Un plato preparado (una paella) no lo puedes enviar por WhatsApp. Pero la **receta** sí — es texto con instrucciones. Serializar es convertir la paella en su receta; deserializar es cocinarla de vuelta.

> _"Un objeto Python es la paella. JSON es la receta. No puedes mandar una paella por HTTP, pero sí puedes mandar la receta."_

#### Analogía 3: El idioma común 🌍

Imagina que Python habla japonés, JavaScript habla inglés, y tu base de datos habla alemán. Ninguno se entiende entre sí. **JSON es el idioma universal** — todos lo hablan. Serializar es **traducir** del idioma de Python (objetos) al idioma universal (JSON).

> _"Un diccionario ya está 'casi en el idioma universal' — es fácil de traducir. Un objeto SQLAlchemy está en japonés técnico — tiene verbos, gramática compleja, contexto... necesitas un traductor manual (el método `serialize()`)."_

#### Analogía 4: La mudanza 📦

Tienes tu habitación armada: cama, escritorio, PC conectada. No puedes meter la habitación entera en un camión de mudanza así. Lo que haces es:

1. **Desarmar** los muebles
2. **Etiquetar** cada caja ("tornillos escritorio", "patas mesa")
3. Meterlo en el camión

Eso es serializar. En el destino, abres las cajas y armas todo de nuevo (deserializar).

> _"Un diccionario es como una caja ya etiquetada y lista. Un objeto SQLAlchemy es la habitación entera — hay que desarmarlo primero."_

#### Dicho de forma directa 💬

HTTP solo puede enviar **texto**. Un diccionario Python se parece mucho a JSON (que es texto), así que la conversión es automática. Pero un objeto de SQLAlchemy tiene cosas que no son texto: métodos, conexiones, sesiones de base de datos. Python te dice _"no sé cómo convertir esto a texto"_. Por eso tú escribes `serialize()` — le dices a Python exactamente qué partes del objeto quieres enviar.

---

#### ¿Qué se puede serializar directamente?

No todos los tipos de datos se pueden convertir a JSON automáticamente. La regla es simple:

| Tipo de dato         | ¿Se puede serializar a JSON? | Ejemplo                          |
| -------------------- | ---------------------------- | -------------------------------- |
| `str` (texto)        | ✅ SÍ                        | `"hola"`                         |
| `int` (entero)       | ✅ SÍ                        | `42`                             |
| `float` (decimal)    | ✅ SÍ                        | `3.14`                           |
| `bool` (booleano)    | ✅ SÍ                        | `true`                           |
| `None`               | ✅ SÍ                        | `null`                           |
| `list` (lista)       | ✅ SÍ                        | `[1, 2, 3]`                      |
| `dict` (diccionario) | ✅ SÍ                        | `{"nombre": "Luis"}`             |
| Objeto SQLAlchemy    | ❌ NO                        | `<User 5>` — Python no sabe cómo |
| `datetime`           | ❌ NO                        | Hay que convertirlo a texto      |

**¿Por qué los diccionarios SÍ y los objetos SQLAlchemy NO?**

Un **diccionario** ya es una estructura simple: claves y valores, todos son tipos básicos. JSON fue diseñado para representar exactamente eso.

Un **objeto SQLAlchemy** es un objeto complejo de Python: tiene métodos, conexiones a la base de datos, relaciones con otros objetos, estado interno... JSON no tiene forma de representar todo eso.

```python
# Diccionario → JSON funciona directamente
from flask import jsonify

data = {"nombre": "Luis", "edad": 25}
jsonify(data)  # ✅ → {"nombre": "Luis", "edad": 25}

# Objeto SQLAlchemy → JSON NO funciona
user = User.query.get(5)
jsonify(user)  # ❌ TypeError: Object of type User is not JSON serializable
```

#### La solución: el método `serialize()`

Por eso creamos un método `serialize()` en nuestros modelos — para **extraer manualmente** los datos del objeto y ponerlos en un diccionario:

```python
def serialize(self):
    return {
        "id": self.id,           # int → ✅ serializable
        "email": self.email,     # str → ✅ serializable
        "username": self.username # str → ✅ serializable
        # password_hash → ❌ NO lo incluimos por seguridad
    }

# Ahora sí funciona:
jsonify(user.serialize())  # ✅ → {"id": 5, "email": "luis@example.com", ...}
```

> 💡 **Resumen**: Serializar = convertir un objeto complejo en un diccionario/JSON que se pueda enviar por HTTP. En Flask, lo hacemos con un método `serialize()` en cada modelo.

---

### Stateless vs Stateful

| Término       | Significado                                                      | Ejemplo                |
| ------------- | ---------------------------------------------------------------- | ---------------------- |
| **Stateful**  | El servidor **recuerda** información entre peticiones            | Sesiones tradicionales |
| **Stateless** | El servidor **NO recuerda** nada, cada petición es independiente | JWT                    |

```mermaid
flowchart TD
    subgraph Stateful["Stateful (con memoria)"]
        S1["Servidor"] -->|"recuerda"| M1["Memoria<br/>Usuario 5 está logueado"]
    end

    subgraph Stateless["Stateless (sin memoria)"]
        S2["Servidor"] -->|"no recuerda nada"| M2["(vacío)"]
        T["Token JWT<br/>contiene: user_id=5"] -->|"cada petición"| S2
    end
```

JWT permite APIs **stateless** porque toda la información necesaria viaja en el token.

---

### Decorador (Python)

Un **decorador** es una función que "envuelve" otra función para añadirle funcionalidad.

En este día, quédate aquí con la definición breve. La explicación que realmente importa en contexto está en [step3-jwt-flask-backend](../step3-jwt-flask-backend/README.md), justo cuando usamos `@jwt_required()` para proteger endpoints.

```python
# El @ indica que es un decorador
@jwt_required()      # ← Decorador: "verifica el token antes de ejecutar"
def get_profile():   # ← Función decorada
    return {"data": "..."}
```

**Analogía**: Es como poner un guardia de seguridad en la puerta. Antes de que alguien entre a tu función, el guardia (decorador) verifica si tiene permiso.

---

### localStorage

**localStorage** es un almacén de datos en el navegador del usuario. Los datos persisten incluso si cierra el navegador.

```javascript
// Guardar
localStorage.setItem('token', 'abc123');

// Leer
const token = localStorage.getItem('token'); // → 'abc123'

// Borrar
localStorage.removeItem('token');
```

**Características:**

- Solo guarda **strings** (usa `JSON.stringify()` para objetos)
- Persiste hasta que se borre explícitamente
- Accesible solo desde el mismo dominio
- Capacidad: ~5MB

**Ver tus datos**: Abre DevTools (F12) → Application → Local Storage

---

### Context (React)

**Context** es un mecanismo de React para compartir datos entre componentes sin pasar props manualmente.

```mermaid
flowchart TD
    subgraph SinContext["❌ Sin Context (Prop Drilling)"]
        A1["App"] -->|"user"| B1["Layout"]
        B1 -->|"user"| C1["Sidebar"]
        C1 -->|"user"| D1["UserMenu"]
    end

    subgraph ConContext["✅ Con Context"]
        A2["App + UserContext.Provider"] --> B2["Layout"]
        B2 --> C2["Sidebar"]
        C2 --> D2["UserMenu<br/>useContext(UserContext)"]
        A2 -.->|"acceso directo"| D2
    end
```

Para autenticación, creamos un `AuthContext` que contiene el token, usuario, y funciones de login/logout.

---

### Provider (React)

Un **Provider** es un componente que "provee" datos a todos sus hijos a través de Context.

```jsx
// El Provider envuelve la app y "provee" los datos
<AuthProvider>
  <App /> {/* Todos los componentes dentro tienen acceso */}
</AuthProvider>
```

---

### children (React)

**children** es una prop especial que representa todo lo que pones entre las etiquetas de un componente.

```jsx
<MiComponente>
  <p>Esto es children</p>
  <button>Esto también</button>
</MiComponente>;

// Dentro de MiComponente:
function MiComponente({ children }) {
  return <div className="wrapper">{children}</div>;
  // children = <p>Esto es children</p><button>Esto también</button>
}
```

---

### Navigate (React Router)

`Navigate` es un **componente** que redirige al usuario a otra página automáticamente.

```jsx
import { Navigate } from 'react-router-dom';

// Si no está autenticado, lo manda a /login
if (!isAuthenticated) {
  return <Navigate to="/login" />;
}
```

---

### useNavigate (React Router)

`useNavigate` es un **hook** que te da una función para cambiar de página desde tu código JavaScript.

```jsx
import { useNavigate } from 'react-router-dom';

const navigate = useNavigate();

// Después de hacer login exitoso:
navigate('/dashboard'); // Ir a /dashboard

// Volver atrás:
navigate(-1); // Equivalente a presionar "back" en el navegador
```

**Diferencia con `<Link>`**: Usas `useNavigate` cuando quieres navegar **después de una acción** (como un login exitoso), no cuando el usuario hace click en un link.

---

### useLocation (React Router)

`useLocation` es un **hook** que te dice en qué página estás y qué datos extra vinieron con la navegación.

```jsx
import { useLocation } from 'react-router-dom';

const location = useLocation();

console.log(location.pathname); // "/login"
console.log(location.state); // { from: "/dashboard" }
```

---

### bcrypt.checkpw (Python)

`checkpw` significa **"check password"**. Es una función que compara una contraseña en texto plano con un hash guardado.

```python
# Verifica si la contraseña coincide
bcrypt.checkpw(password_text, password_hash)
# Retorna: True o False
```

**No puedes "deshacer" un hash**, pero sí puedes comparar si dos contraseñas generan el mismo hash.

---

## 📋 Referencia rápida

| Término        | Definición en una línea                           |
| -------------- | ------------------------------------------------- |
| Endpoint       | URL específica de tu API                          |
| Header         | Metadatos que viajan con una petición HTTP        |
| Bearer         | Tipo de token en el header Authorization          |
| Hash           | Función de un solo sentido (irreversible)         |
| Cifrado        | Función reversible (puedes descifrar)             |
| Base64         | Codificación de texto (NO segura)                 |
| Stateless      | El servidor no guarda estado entre peticiones     |
| Decorador      | Función que envuelve otra función                 |
| localStorage   | Almacén persistente en el navegador               |
| Context        | Mecanismo de React para compartir datos           |
| Provider       | Componente que "provee" datos via Context         |
| children       | Lo que pones entre las etiquetas de un componente |
| Navigate       | Componente que redirige a otra página             |
| useNavigate    | Hook para navegar programáticamente               |
| useLocation    | Hook que dice en qué página estás                 |
| bcrypt.checkpw | Función que compara contraseña con hash           |

---

## ✅ Checklist

- [ ] Entiendo qué es un endpoint
- [ ] Sé qué son los headers HTTP y para qué sirve Authorization
- [ ] Entiendo la diferencia entre hash y cifrado
- [ ] Sé que Base64 NO es seguro
- [ ] Entiendo qué significa stateless
- [ ] Sé qué hace un decorador en Python
- [ ] Entiendo qué es localStorage y cómo usarlo
- [ ] Sé para qué sirve Context en React
- [ ] Entiendo la diferencia entre `Navigate` y `useNavigate`
- [ ] Sé cuándo usar `useLocation`
- [ ] Entiendo qué hace `bcrypt.checkpw`
