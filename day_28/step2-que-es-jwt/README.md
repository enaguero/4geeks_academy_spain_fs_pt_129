# Step 1: ¿Qué es un JWT?

## 🎯 Objetivo

Entender la **estructura interna** de un JWT, qué información contiene, cómo se firma, y por qué es seguro.

---

## 📦 JWT = JSON Web Token

Un JWT es simplemente una **cadena de texto** que contiene información codificada en formato JSON. Se usa para transmitir información de forma segura entre dos partes.

### Ejemplo de un JWT real

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikx1aXMiLCJpYXQiOjE1MTYyMzkwMjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

¿Parece aleatorio? No lo es. Son **3 partes separadas por puntos**:

```
HEADER.PAYLOAD.SIGNATURE
```

---

## 🧬 Anatomía de un JWT

```mermaid
flowchart LR
    subgraph JWT["Token JWT Completo"]
        direction TB
        H["🔵 HEADER<br/>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"]
        P["🟢 PAYLOAD<br/>eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikx1aXMi..."]
        S["🔴 SIGNATURE<br/>SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"]
    end

    H --- P --- S
```

### Parte 1: Header (Cabecera) 🔵

Contiene metadatos sobre el token:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

| Campo | Significado                               |
| ----- | ----------------------------------------- |
| `alg` | Algoritmo de firma (HS256 = HMAC SHA-256) |
| `typ` | Tipo de token (siempre "JWT")             |

**Codificado en Base64URL** → `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`

---

### Parte 2: Payload (Carga útil) 🟢

Contiene los **claims** — datos sobre el usuario y el token:

```json
{
  "sub": "5",
  "email": "luis@example.com",
  "username": "luis_dev",
  "iat": 1709913600,
  "exp": 1709917200
}
```

| Claim   | Significado                | Ejemplo                       |
| ------- | -------------------------- | ----------------------------- |
| `sub`   | Subject — ID del usuario   | `"5"`                         |
| `email` | Email del usuario          | `"luis@example.com"`          |
| `iat`   | Issued At — cuándo se creó | `1709913600` (timestamp)      |
| `exp`   | Expiration — cuándo expira | `1709917200` (1 hora después) |
| `iss`   | Issuer — quién lo emitió   | `"mi-api.com"`                |

**Codificado en Base64URL** → `eyJzdWIiOiI1IiwiZW1haWwiOiJsdWlzQGV4YW1wbGUuY29tIi4uLn0`

> ⚠️ **IMPORTANTE**: El payload está **codificado, NO cifrado**. Cualquiera puede leerlo decodificando el Base64. **NUNCA pongas contraseñas ni datos sensibles aquí.**

---

### Parte 3: Signature (Firma) 🔴

Es lo que hace el JWT **seguro**. Se calcula así:

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  SECRET_KEY
)
```

```mermaid
flowchart LR
    H[Header codificado] --> CONCAT
    P[Payload codificado] --> CONCAT
    CONCAT["header.payload"] --> HMAC
    SK[SECRET_KEY<br/>Solo el servidor la conoce] --> HMAC
    HMAC[HMACSHA256] --> SIG[Signature]
```

**¿Por qué es seguro?**

- Solo el servidor conoce el `SECRET_KEY`
- Si alguien modifica el payload, la firma ya no coincide
- El servidor puede verificar que el token es auténtico

---

## 🔍 Decodificando un JWT

Puedes ver el contenido de cualquier JWT en [jwt.io](https://jwt.io):

```
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1IiwiZW1haWwiOiJsdWlzQGV4YW1wbGUuY29tIiwiaWF0IjoxNzA5OTEzNjAwLCJleHAiOjE3MDk5MTcyMDB9.abc123signature
```

**Decodificado:**

| Parte     | JSON                                                                              |
| --------- | --------------------------------------------------------------------------------- |
| Header    | `{"alg": "HS256", "typ": "JWT"}`                                                  |
| Payload   | `{"sub": "5", "email": "luis@example.com", "iat": 1709913600, "exp": 1709917200}` |
| Signature | (no se puede decodificar, es un hash)                                             |

### En Python

Este código te permite **ver qué hay dentro de un JWT** (sin verificar la firma). Es útil para entender cómo funciona internamente.

```python
import base64
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1In0.signature"

# Extraer el payload (segunda parte)
payload_b64 = token.split(".")[1]

# Añadir padding si es necesario
payload_b64 += "=" * (4 - len(payload_b64) % 4)

# Decodificar
payload = json.loads(base64.urlsafe_b64decode(payload_b64))
print(payload)  # {'sub': '5'}
```

#### Explicación línea por línea:

```python
import base64  # Librería para codificar/decodificar Base64
import json    # Librería para trabajar con JSON
```

```python
token = "eyJhbG...eyJzdW...signature"
#       ^^^^^^^^ ^^^^^^^ ^^^^^^^^^
#       Header   Payload Signature
#       (parte 0)(parte 1)(parte 2)
```

```python
payload_b64 = token.split(".")[1]
#                   ^^^^^^^^^^
#                   Divide por "." y toma el índice [1] (segunda parte)
#                   Resultado: "eyJzdWIiOiI1In0"
```

```python
payload_b64 += "=" * (4 - len(payload_b64) % 4)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#              Base64 necesita que la longitud sea múltiplo de 4
#              Esto añade "=" al final si es necesario (padding)
```

```python
payload = json.loads(base64.urlsafe_b64decode(payload_b64))
#         ^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         |          Decodifica Base64 → bytes
#         Convierte bytes JSON a diccionario Python
```

```python
print(payload)  # {'sub': '5'}
```

> 💡 **Nota**: En la práctica, no necesitas hacer esto manualmente. Las librerías como `flask-jwt-extended` lo hacen por ti. Este ejemplo es solo para entender cómo funciona internamente.

---

## ⏰ Expiración del Token

Los JWT tienen fecha de expiración por seguridad:

```mermaid
flowchart LR
    subgraph Token["JWT"]
        EXP["exp: 1709917200<br/>(8 marzo 2024, 13:00)"]
    end

    subgraph Check["Verificación"]
        NOW["Hora actual"]
        VALID["✅ Token válido"]
        EXPIRED["❌ Token expirado"]
    end

    Token --> Check
    NOW -->|antes de exp| VALID
    NOW -->|después de exp| EXPIRED
```

**Tiempos típicos de expiración:**

- Access token: 15 minutos - 1 hora
- Refresh token: 7 días - 30 días

---

## 🔐 ¿Por qué JWT es seguro?

### 1. La firma garantiza integridad

```mermaid
flowchart TD
    subgraph Ataque["❌ Intento de ataque"]
        A1["Atacante obtiene JWT"]
        A2["Modifica payload:<br/>sub: '1' → sub: '999'"]
        A3["Envía token modificado"]
        A4["Servidor verifica firma"]
        A5["❌ Firma NO coincide<br/>Token rechazado"]
    end

    A1 --> A2 --> A3 --> A4 --> A5
```

### 2. Solo el servidor puede crear tokens válidos

```mermaid
flowchart TD
    subgraph Legitimo["✅ Flujo legítimo"]
        L1["Servidor genera JWT"]
        L2["Firma con SECRET_KEY"]
        L3["Cliente recibe token"]
        L4["Cliente envía token"]
        L5["Servidor verifica con SECRET_KEY"]
        L6["✅ Firma coincide"]
    end

    L1 --> L2 --> L3 --> L4 --> L5 --> L6
```

---

## 🚫 Lo que JWT NO hace

| JWT NO...              | Por qué                                       |
| ---------------------- | --------------------------------------------- |
| Cifra los datos        | El payload es legible por cualquiera (Base64) |
| Previene robo de token | Si alguien obtiene tu token, puede usarlo     |
| Revoca tokens          | Una vez emitido, válido hasta expirar         |

### Mitigaciones

| Problema        | Solución                                |
| --------------- | --------------------------------------- |
| Datos sensibles | No ponerlos en el payload               |
| Robo de token   | HTTPS, HttpOnly cookies, tokens cortos  |
| Revocación      | Lista negra en Redis, tokens muy cortos |

---

## 📋 Claims estándar de JWT

| Claim | Nombre     | Descripción                   |
| ----- | ---------- | ----------------------------- |
| `iss` | Issuer     | Quién emitió el token         |
| `sub` | Subject    | ID del usuario (el "sujeto")  |
| `aud` | Audience   | Para quién está destinado     |
| `exp` | Expiration | Cuándo expira (timestamp)     |
| `nbf` | Not Before | No válido antes de esta fecha |
| `iat` | Issued At  | Cuándo se creó                |
| `jti` | JWT ID     | ID único del token            |

### Claims personalizados

Puedes añadir cualquier dato que necesites:

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

## 🧪 Práctica: Inspecciona un JWT

1. Ve a [jwt.io](https://jwt.io)
2. Pega este token:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJhbmFAZXhhbXBsZS5jb20iLCJ1c2VybmFtZSI6ImFuYV9kZXYiLCJpYXQiOjE3MDk5MTM2MDAsImV4cCI6MTcwOTkxNzIwMH0.abc123
```

3. Observa:
   - ¿Qué algoritmo usa?
   - ¿Cuál es el email del usuario?
   - ¿Cuándo expira? (convierte el timestamp)

---

## 🧪 Mini-reto: Decodifica y analiza

### Reto 1: ¿Qué contiene este token?

Decodifica este JWT en [jwt.io](https://jwt.io) y responde las preguntas:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJNYXJpYSBHYXJjaWEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3MDk5MTM2MDAsImV4cCI6MTcwOTkyMDgwMH0.fake_signature
```

| Pregunta                                      | Tu respuesta |
| --------------------------------------------- | ------------ |
| ¿Cuál es el ID del usuario (sub)?             |              |
| ¿Cuál es el nombre?                           |              |
| ¿Qué rol tiene?                               |              |
| ¿En cuántas horas expira? (calcula exp - iat) |              |

<details>
<summary>Ver respuestas</summary>

| Pregunta             | Respuesta                                    |
| -------------------- | -------------------------------------------- |
| ID del usuario (sub) | `42`                                         |
| Nombre               | `Maria Garcia`                               |
| Rol                  | `admin`                                      |
| Horas hasta expirar  | `(1709920800 - 1709913600) / 3600 = 2 horas` |

</details>

### Reto 2: ¿Por qué esto es un problema de seguridad?

Un desarrollador junior creó este token:

```json
{
  "sub": "1",
  "email": "admin@empresa.com",
  "password": "admin123",
  "creditCard": "4111-1111-1111-1111"
}
```

¿Qué está mal? ¿Por qué es peligroso?

<details>
<summary>Ver respuesta</summary>

**Problemas graves:**

1. **Contraseña en el payload** — Cualquiera puede decodificar el JWT con Base64 y ver la contraseña
2. **Tarjeta de crédito** — Datos sensibles expuestos
3. **El payload NO está cifrado** — Solo codificado en Base64, que es reversible

**Recuerda:** El payload del JWT es como escribir en una postal — el cartero (y cualquiera) puede leerlo. Solo guarda información que es OK si alguien la ve.

</details>

---

## ✅ Checklist de este step

- [ ] Sé que un JWT tiene 3 partes: header.payload.signature
- [ ] Entiendo que el payload está codificado, NO cifrado
- [ ] Sé qué claims comunes existen (sub, exp, iat)
- [ ] Entiendo cómo la firma garantiza integridad
- [ ] Sé por qué no debo poner datos sensibles en el JWT
