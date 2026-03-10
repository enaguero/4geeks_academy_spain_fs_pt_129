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
