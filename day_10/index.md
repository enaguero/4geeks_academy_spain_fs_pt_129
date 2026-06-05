🇪🇸 **Español** | [🇬🇧 English](index.en.md)

# Día 10: Buenas Prácticas y Estándares de Código

## ¿Por qué son Importantes los Estándares de Código?

Imagina que entras a una cocina donde:

- Los ingredientes no tienen etiquetas
- Los cuchillos están mezclados con las cucharas
- No hay recetas escritas, todo está en la memoria del chef
- Cada cocinero organiza las cosas de forma diferente

**¿Podrías cocinar eficientemente?** Probablemente no. Lo mismo ocurre con el código.

### El Costo Real de las Malas Prácticas

Las malas prácticas no solo hacen el código difícil de leer, **cuestan dinero real** y pueden causar desastres:

#### Casos Reales de Desastres por Mal Código

**1. NASA Mars Climate Orbiter (1999) - $320 millones perdidos** 💸

- **Problema**: Un equipo usaba el sistema métrico, otro el sistema imperial
- **Resultado**: La sonda espacial se perdió en Marte
- **Causa raíz**: Falta de estándares consistentes en el código

**2. Cohete Ariane 5 de la ESA (1996) - $370 millones perdidos** 🚀

- **Problema**: Código mal escrito, difícil de leer
- **Resultado**: El cohete explotó 40 segundos después del lanzamiento
- **Causa raíz**: Error de conversión de datos no detectado por código ilegible

**3. Flash Crash del Mercado de Valores de EE.UU. (2010)** 📉

- **Problema**: Código complejo sin buenas prácticas
- **Resultado**: Pérdidas financieras masivas en minutos
- **Causa raíz**: Sistemas sin manejo adecuado de errores

### Datos que Importan

Estudios demuestran que:

- ✅ Desarrolladores que usan buenas prácticas son **40% más productivos**
- ✅ Código con buenas prácticas es **50% más barato de mantener**
- ❌ El 70% del tiempo de desarrollo se gasta **leyendo** código, no escribiéndolo

> "No soy un gran programador; solo soy un buen programador con grandes hábitos." - Kent Beck

---

## 1. Variables Globales: El Enemigo Silencioso

### ❌ Mala Práctica: Usar Variables Globales

Las **variables globales** son variables accesibles desde cualquier parte del código.

```javascript
// ❌ MAL: Variables globales
let userAge = 25;
let userName = 'Carlos';
let isLoggedIn = false;

function login(name) {
  userName = name;
  isLoggedIn = true;
  console.log(`${userName} ha iniciado sesión`);
}

function updateAge(age) {
  userAge = age;
}

function displayUser() {
  console.log(`${userName}, ${userAge} años`);
}

login('Ana');
updateAge(30);
displayUser();
```

### ¿Por qué es Malo?

| Problema                       | Descripción                                       | Consecuencia                           |
| ------------------------------ | ------------------------------------------------- | -------------------------------------- |
| **Bugs difíciles de rastrear** | Cualquier función puede modificar la variable     | No sabes qué función causó el problema |
| **Conflictos de nombres**      | Diferentes partes del código usan el mismo nombre | Sobrescrituras accidentales            |
| **Difícil de testear**         | Las funciones dependen del estado global          | No puedes probar funciones aisladas    |
| **Efectos secundarios**        | Cambiar una variable afecta todo el programa      | Comportamiento impredecible            |
| **No escalable**               | Difícil de mantener en proyectos grandes          | El código se vuelve inmanejable        |

### Ejemplo Real de Problema

```javascript
// ❌ DESASTRE ESPERANDO SUCEDER
let total = 0;

function calcularDescuento(precio) {
  total = precio * 0.9; // Modifica variable global
  return total;
}

function calcularImpuesto(precio) {
  total = precio * 1.21; // ¡Sobrescribe el total anterior!
  return total;
}

// Usuario quiere descuento + impuesto
const precioConDescuento = calcularDescuento(100); // total = 90
const precioFinal = calcularImpuesto(precioConDescuento); // total = 108.9

console.log(total); // 108.9 - ¡Se perdió el descuento!
```

### ✅ Buena Práctica: Usar Parámetros y Valores de Retorno

```javascript
// ✅ BIEN: Sin variables globales
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
  console.log(`${user.userName}, ${user.age} años`);
}

// Uso
let currentUser = login('Ana');
currentUser = updateAge(currentUser, 30);
displayUser(currentUser);
```

### Ventajas de Evitar Variables Globales

✅ **Predecible**: Cada función solo modifica lo que recibe  
✅ **Testeable**: Puedes probar funciones independientemente  
✅ **Mantenible**: Fácil encontrar dónde se usa cada variable  
✅ **Sin efectos secundarios**: Una función no afecta a otras  
✅ **Reutilizable**: Funciones funcionan en cualquier contexto

### Ejemplo Corregido: Sistema de Descuentos

```javascript
// ✅ BIEN: Funciones puras sin variables globales
function calcularDescuento(precio, porcentaje) {
  return precio * (1 - porcentaje / 100);
}

function calcularImpuesto(precio, tasaImpuesto) {
  return precio * (1 + tasaImpuesto / 100);
}

function calcularPrecioFinal(precio, descuento, impuesto) {
  const precioConDescuento = calcularDescuento(precio, descuento);
  const precioConImpuesto = calcularImpuesto(precioConDescuento, impuesto);
  return precioConImpuesto;
}

// Uso claro y predecible
const precioFinal = calcularPrecioFinal(100, 10, 21);
console.log(precioFinal); // 108.9 - ¡Correcto!
```

---

## 2. Nombres de Variables: Tu Código Debe Hablar

### ❌ Mala Práctica: Nombres Crípticos o Poco Descriptivos

```javascript
// ❌ MAL: Nombres sin significado
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

// ¿Qué hace esto? 🤔
for (let i = 0; i < data.length; i++) {
  if (data[i] > temp) {
    n++;
  }
}
```

### ¿Por qué es Malo?

| Problema                  | Ejemplo               | Impacto                           |
| ------------------------- | --------------------- | --------------------------------- |
| **No sabes qué contiene** | `let x = 25`          | ¿Edad? ¿Precio? ¿Temperatura?     |
| **Pérdida de tiempo**     | `function calc(p, q)` | Tienes que leer toda la función   |
| **Difícil de mantener**   | `let temp = 1000`     | ¿Temporal? ¿Temperatura? ¿Límite? |
| **Errores al modificar**  | `a, b, c`             | Confundes variables fácilmente    |

### Ejemplo Real: Código Ilegible

```javascript
// ❌ PESADILLA DE MANTENIMIENTO
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

**¿Puedes entender qué hace esta función en 5 segundos?** Probablemente no.

### ✅ Buena Práctica: Nombres Descriptivos y Claros

```javascript
// ✅ BIEN: Nombres que explican su propósito
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

// Ahora es obvio qué hace esto
for (let i = 0; i < products.length; i++) {
  if (products[i].price > maximumPrice) {
    itemCount++;
  }
}
```

### Convenciones de Nombres en JavaScript

#### 1. **Variables y Funciones**: camelCase

```javascript
// ✅ Variables
let firstName = 'María';
let productPrice = 99.99;
let isAvailable = true;
let orderTotal = 0;

// ✅ Funciones
function calculateDiscount() {}
function getUserById() {}
function processPayment() {}
```

#### 2. **Constantes**: UPPER_SNAKE_CASE

```javascript
// ✅ Constantes
const MAX_USERS = 100;
const API_KEY = 'abc123';
const TAX_RATE = 0.21;
const DATABASE_URL = 'https://api.example.com';
```

#### 3. **Clases**: PascalCase

```javascript
// ✅ Clases
class UserAccount {}
class ShoppingCart {}
class ProductCatalog {}
```

### Reglas de Oro para Nombres de Variables

| Regla                     | ❌ Mal              | ✅ Bien                         |
| ------------------------- | ------------------- | ------------------------------- |
| **Sé descriptivo**        | `let d = 10`        | `let daysUntilDelivery = 10`    |
| **Evita abreviaturas**    | `let usrNm = "Ana"` | `let userName = "Ana"`          |
| **No uses letras solas**  | `let x, y, z`       | `let width, height, depth`      |
| **Indica el tipo**        | `let data`          | `let userList` o `let userData` |
| **Usa nombres completos** | `let prod`          | `let product`                   |
| **Evita números**         | `let user1, user2`  | `let currentUser, previousUser` |

### Ejemplo Corregido: Código Legible

```javascript
// ✅ CÓDIGO QUE SE EXPLICA SOLO
function calculateOrderTotal(customer) {
  let orderTotal = 0;

  for (let i = 0; i < customer.orders.length; i++) {
    const order = customer.orders[i];
    orderTotal += order.price * order.quantity;
  }

  if (customer.isMember) {
    orderTotal *= 0.9; // 10% descuento para miembros
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

### Nombres de Funciones: Deben Describir la Acción

```javascript
// ❌ MAL: Verbos vagos o sin verbos
function user(id) {}
function data() {}
function process(x) {}

// ✅ BIEN: Verbo + sustantivo
function getUser(id) {}
function fetchUserData() {}
function processPayment(transaction) {}
function validateEmail(email) {}
function calculateTotalPrice(items) {}
```

### Tabla de Verbos Comunes

| Acción        | Verbo                  | Ejemplo                                |
| ------------- | ---------------------- | -------------------------------------- |
| Obtener datos | `get`, `fetch`         | `getUserById()`, `fetchProducts()`     |
| Crear         | `create`, `add`        | `createAccount()`, `addToCart()`       |
| Actualizar    | `update`, `set`        | `updateProfile()`, `setPrice()`        |
| Eliminar      | `delete`, `remove`     | `deleteUser()`, `removeItem()`         |
| Validar       | `validate`, `check`    | `validateForm()`, `checkPassword()`    |
| Calcular      | `calculate`, `compute` | `calculateTotal()`, `computeAverage()` |
| Mostrar       | `show`, `display`      | `showModal()`, `displayResults()`      |

---

## 3. Indentación: La Arquitectura Visual del Código

### ❌ Mala Práctica: Código Sin Indentación

```javascript
// ❌ PESADILLA: Sin indentación
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

**¿Puedes identificar dónde empieza y termina cada bloque?** Es casi imposible.

### ✅ Buena Práctica: Indentación Consistente

```javascript
// ✅ CLARO: Indentación correcta
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

### Ventajas de la Buena Indentación

✅ **Legibilidad instantánea**: Ves la estructura del código de un vistazo  
✅ **Detectar errores**: Los bloques mal cerrados se ven inmediatamente  
✅ **Navegación rápida**: Encuentras funciones y bloques fácilmente  
✅ **Colaboración**: Todo el equipo lee el código igual  
✅ **Profesionalismo**: Demuestra atención al detalle

### Reglas de Indentación

| Lenguaje       | Espacios Recomendados | Estándar           |
| -------------- | --------------------- | ------------------ |
| **JavaScript** | 2 o 4 espacios        | Airbnb: 2 espacios |
| **Python**     | 4 espacios            | PEP 8: 4 espacios  |
| **HTML/CSS**   | 2 espacios            | Común: 2 espacios  |
| **Java**       | 4 espacios            | Oracle: 4 espacios |

### Herramientas Automáticas: Prettier

```javascript
// Antes de Prettier (código desordenado)
function ejemplo() {
  const x = 10;
  if (x > 5) {
    console.log('grande');
  } else {
    console.log('pequeño');
  }
}

// Después de Prettier (automáticamente formateado)
function ejemplo() {
  const x = 10;

  if (x > 5) {
    console.log('grande');
  } else {
    console.log('pequeño');
  }
}
```

**Configuración de Prettier** (`.prettierrc`):

```json
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "useTabs": false,
  "printWidth": 80
}
```

### Ejemplo Visual: Niveles de Indentación

```javascript
function calculateOrderDiscount(order) {
  // Nivel 0
  if (order.customer.isMember) {
    // Nivel 1
    if (order.total > 100) {
      // Nivel 2
      if (order.items.length > 5) {
        // Nivel 3
        return order.total * 0.8; // Nivel 4 ⚠️ Muy profundo
      }
    }
  }
  return order.total;
}

// ✅ MEJOR: Reducir niveles de anidación
function calculateOrderDiscount(order) {
  // Nivel 0
  if (!order.customer.isMember) {
    // Nivel 1
    return order.total;
  }

  if (order.total <= 100) {
    // Nivel 1
    return order.total * 0.95;
  }

  if (order.items.length <= 5) {
    // Nivel 1
    return order.total * 0.9;
  }

  return order.total * 0.8; // Nivel 0
}
```

---

## 4. Manejo de Errores: No Dejes que Tu Programa Explote

### ❌ Mala Práctica: Ignorar Errores

```javascript
// ❌ MAL: Sin manejo de errores
function getUserData(userId) {
  const response = fetch(`/api/users/${userId}`);
  const data = response.json();
  return data;
}

function divideNumbers(a, b) {
  return a / b; // ¿Qué pasa si b = 0?
}

function parseUserInput(input) {
  const data = JSON.parse(input); // ¿Qué pasa si input no es JSON válido?
  return data;
}
```

### ¿Por qué es Malo?

| Problema                 | Consecuencia               | Usuario Ve                    |
| ------------------------ | -------------------------- | ----------------------------- |
| **Crashes inesperados**  | La aplicación se congela   | Pantalla en blanco            |
| **Datos corruptos**      | Se guardan datos inválidos | Comportamiento extraño        |
| **Mensajes crípticos**   | Error no descriptivo       | "Error undefined"             |
| **Difícil de debuggear** | No sabes dónde falló       | No puedes reproducir el error |

### ✅ Buena Práctica: Manejo Proactivo de Errores

#### 1. Try-Catch en JavaScript

```javascript
// ✅ BIEN: Manejo de errores con try-catch
async function getUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);

    if (!response.ok) {
      throw new Error(`Error HTTP: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error obteniendo usuario:', error);
    // Mostrar mensaje amigable al usuario
    return null;
  }
}
```

#### 2. Validación de Entradas

```javascript
// ✅ BIEN: Validar antes de operar
function divideNumbers(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Ambos argumentos deben ser números');
  }

  if (b === 0) {
    throw new Error('No se puede dividir por cero');
  }

  return a / b;
}

// Uso seguro
try {
  const result = divideNumbers(10, 2);
  console.log(result); // 5
} catch (error) {
  console.error('Error en división:', error.message);
}
```

#### 3. Catch en Promesas

```javascript
// ✅ BIEN: Siempre incluye .catch()
fetch('/api/products')
  .then((response) => response.json())
  .then((data) => {
    console.log('Productos:', data);
  })
  .catch((error) => {
    console.error('Error cargando productos:', error);
    // Mostrar mensaje al usuario
    displayErrorMessage('No se pudieron cargar los productos');
  });
```

#### 4. Manejo de JSON Inválido

```javascript
// ✅ BIEN: Validar JSON antes de parsear
function parseUserInput(input) {
  try {
    const data = JSON.parse(input);
    return { success: true, data: data };
  } catch (error) {
    console.error('JSON inválido:', error);
    return { success: false, error: 'Formato inválido' };
  }
}

// Uso
const result = parseUserInput('{"name": "Ana"}');
if (result.success) {
  console.log('Datos:', result.data);
} else {
  console.log('Error:', result.error);
}
```

### Buenas Prácticas de Manejo de Errores

| Práctica                    | ❌ Mal               | ✅ Bien                                |
| --------------------------- | -------------------- | -------------------------------------- |
| **Loguea errores**          | Silenciar errores    | `console.error()` o sistema de logs    |
| **Mensajes descriptivos**   | `"Error"`            | `"Error al cargar productos: timeout"` |
| **Recuperación graceful**   | App se congela       | Mostrar mensaje y alternativas         |
| **No suprimas excepciones** | `catch {}` vacío     | Loguea y maneja el error               |
| **Valida entradas**         | Confía en el usuario | Valida antes de procesar               |

### Ejemplo Completo: Formulario con Manejo de Errores

```javascript
// ✅ BIEN: Manejo robusto de errores
async function submitContactForm(formData) {
  // 1. Validar datos
  if (!formData.email || !formData.message) {
    return {
      success: false,
      error: 'Email y mensaje son requeridos',
    };
  }

  // 2. Validar formato de email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(formData.email)) {
    return {
      success: false,
      error: 'Email inválido',
    };
  }

  // 3. Enviar datos con manejo de errores
  try {
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    if (!response.ok) {
      throw new Error(`Error del servidor: ${response.status}`);
    }

    const result = await response.json();

    return {
      success: true,
      message: 'Mensaje enviado correctamente',
    };
  } catch (error) {
    console.error('Error enviando formulario:', error);

    return {
      success: false,
      error: 'No se pudo enviar el mensaje. Inténtalo más tarde.',
    };
  }
}

// Uso
const result = await submitContactForm({
  email: 'ana@example.com',
  message: 'Hola!',
});

if (result.success) {
  showSuccessMessage(result.message);
} else {
  showErrorMessage(result.error);
}
```

---

## 5. Legibilidad (Readability): Código que Se Explica Solo

La legibilidad es **la característica más importante** de un buen código. El código se lee 10 veces más de lo que se escribe.

### Principios de Legibilidad

#### 1. Funciones Pequeñas y Enfocadas

```javascript
// ❌ MAL: Función gigante que hace todo
function processUserOrder(userId, products, paymentInfo, shippingAddress) {
  // Validar usuario
  const user = database.getUser(userId);
  if (!user) return null;
  if (!user.isActive) return null;

  // Calcular total
  let total = 0;
  for (let i = 0; i < products.length; i++) {
    total += products[i].price * products[i].quantity;
  }

  // Aplicar descuento
  if (user.isMember) {
    total *= 0.9;
  }

  // Procesar pago
  const payment = processPayment(paymentInfo, total);
  if (!payment.success) return null;

  // Crear orden
  const order = createOrder(userId, products, total);

  // Enviar emails
  sendOrderConfirmation(user.email, order);
  sendShippingNotification(user.email, shippingAddress);

  return order;
}

// ✅ BIEN: Dividido en funciones pequeñas
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

#### 2. Evita `else` Cuando Sea Posible (Early Returns)

```javascript
// ❌ MAL: Anidación con else
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

// ✅ BIEN: Early returns (salidas tempranas)
function getUserDiscount(user) {
  if (!user) return 0;
  if (!user.isMember) return 0;
  if (user.orders > 10) return 0.2;

  return 0.1;
}
```

#### 3. No Sobre-Comentes el Código

```javascript
// ❌ MAL: Comentarios innecesarios
// Declarar variable para el nombre
let name = 'Ana';

// Incrementar contador en 1
counter++;

// Recorrer el array de productos
for (let i = 0; i < products.length; i++) {
  // Obtener el producto actual
  const product = products[i];
  // Imprimir el nombre del producto
  console.log(product.name);
}

// ✅ BIEN: Código auto-explicativo (sin comentarios innecesarios)
let customerName = 'Ana';
counter++;

for (const product of products) {
  console.log(product.name);
}

// ✅ BIEN: Comentarios útiles que explican el "por qué"
// Esperamos 2 segundos antes de reintentar para evitar sobrecargar el servidor
setTimeout(retryRequest, 2000);

// Usamos SHA-256 porque es el estándar de seguridad requerido por el banco
const hash = sha256(password);
```

#### 4. Evita Líneas de Código Largas

```javascript
// ❌ MAL: Línea demasiado larga
const result =
  calculateTotal(products) +
  calculateTax(products, taxRate) +
  calculateShipping(products, shippingAddress) -
  calculateDiscount(customer);

// ✅ BIEN: Dividido en múltiples líneas
const subtotal = calculateTotal(products);
const tax = calculateTax(products, taxRate);
const shipping = calculateShipping(products, shippingAddress);
const discount = calculateDiscount(customer);
const result = subtotal + tax + shipping - discount;
```

#### 5. Espaciado y Agrupación Lógica

```javascript
// ❌ MAL: Todo pegado
function processOrder(order) {
  const total = order.items.reduce((sum, item) => sum + item.price, 0);
  const tax = total * 0.21;
  const shipping = 10;
  const final = total + tax + shipping;
  return final;
}

// ✅ BIEN: Espaciado y agrupación
function processOrder(order) {
  // Calcular subtotal
  const subtotal = order.items.reduce((sum, item) => sum + item.price, 0);

  // Añadir impuestos y envío
  const tax = subtotal * 0.21;
  const shipping = 10;

  // Calcular total final
  const finalTotal = subtotal + tax + shipping;

  return finalTotal;
}
```

---

## 6. Evitar Anidación Profunda (Nesting)

### ❌ Mala Práctica: Código Profundamente Anidado

```javascript
// ❌ DESASTRE: "Callback Hell" o "Pyramid of Doom"
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

### ¿Por qué es Malo?

| Problema                | Impacto                                            |
| ----------------------- | -------------------------------------------------- |
| **Difícil de leer**     | Tienes que rastrear múltiples condiciones a la vez |
| **Difícil de mantener** | Añadir una condición más es complicado             |
| **Propenso a errores**  | Es fácil cerrar mal los bloques                    |
| **Difícil de testear**  | Muchos caminos posibles                            |

### ✅ Buena Práctica: Aplanar la Estructura

#### Técnica 1: Early Returns (Salidas Tempranas)

```javascript
// ✅ BIEN: Early returns
function calculateDiscount(item, quantity) {
  // Manejar casos especiales primero
  if (item.category !== 'clothing' && item.category !== 'electronics') {
    return item.price;
  }

  // Electrónicos
  if (item.category === 'electronics') {
    if (quantity >= 5) {
      return item.warranty ? item.price * 0.75 : item.price * 0.8;
    }
    return item.price * 0.9;
  }

  // Ropa
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

#### Técnica 2: Extraer Funciones

```javascript
// ✅ MEJOR: Funciones separadas
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

#### Técnica 3: Usar Objetos de Configuración

```javascript
// ✅ EXCELENTE: Configuración basada en datos
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

### Comparación Visual

```
ANTES (6 niveles de anidación):          DESPUÉS (2 niveles máximo):
─────────────────────────────            ─────────────────────────────
if                                       if (!válido) return
  if
    if                                   if (categoría A)
      if                                     return calculoA()
        if
          if                             if (categoría B)
            return                           return calculoB()
```

---

## Resumen: Checklist de Buenas Prácticas

### ✅ Variables

- [ ] Evito variables globales
- [ ] Uso nombres descriptivos
- [ ] Sigo convenciones (camelCase, UPPER_SNAKE_CASE)
- [ ] No uso letras solas (x, y, z)
- [ ] Evito abreviaturas

### ✅ Funciones

- [ ] Nombres con verbos (get, set, calculate)
- [ ] Funciones pequeñas (< 20 líneas idealmente)
- [ ] Una responsabilidad por función
- [ ] Evito muchos parámetros (máx 3-4)

### ✅ Estructura

- [ ] Indentación consistente (2 o 4 espacios)
- [ ] Uso herramientas automáticas (Prettier)
- [ ] Líneas no muy largas (< 80-100 caracteres)
- [ ] Agrupo código lógicamente

### ✅ Errores

- [ ] Uso try-catch en operaciones riesgosas
- [ ] Valido entradas del usuario
- [ ] Logueo errores en console
- [ ] Muestro mensajes amigables al usuario
- [ ] No suprimo excepciones

### ✅ Legibilidad

- [ ] Código auto-explicativo
- [ ] Comentarios solo cuando es necesario
- [ ] Espaciado entre secciones
- [ ] Evito anidación profunda (max 2-3 niveles)
- [ ] Uso early returns

---

## Ejercicio Práctico: Refactorizar Código

### Ejercicio: Mejora este código

```javascript
// ❌ CÓDIGO CON MALAS PRÁCTICAS
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
<summary>Ver solución</summary>

```javascript
// ✅ CÓDIGO MEJORADO
function calculateWeightedAverage(multiplier, divisor, numbers) {
  // Validaciones tempranas
  if (multiplier <= 0) {
    console.warn('El multiplicador debe ser mayor a 0');
    return 0;
  }

  if (divisor === null || divisor === 0) {
    console.warn('El divisor no puede ser null o 0');
    return 0;
  }

  if (!Array.isArray(numbers) || numbers.length === 0) {
    console.warn('Debe proporcionar un array de números');
    return 0;
  }

  // Calcular suma
  const sum = numbers.reduce((total, num) => total + num, 0);

  // Calcular resultado
  const result = (sum * multiplier) / divisor;

  return result;
}

// Uso
const result = calculateWeightedAverage(10, 2, [1, 2, 3]);
console.log(result); // 30
```

</details>

---

## Conclusión

### El Impacto de las Buenas Prácticas

**Antes de aplicar buenas prácticas:**

- 😫 Código difícil de leer
- 🐛 Bugs frecuentes
- ⏰ Mucho tiempo debuggeando
- 💸 Costos altos de mantenimiento
- 😠 Equipo frustrado

**Después de aplicar buenas prácticas:**

- 😊 Código fácil de entender
- ✅ Menos bugs
- ⚡ Desarrollo más rápido
- 💰 Menores costos
- 🚀 Equipo productivo

### Recuerda

> "Cualquier tonto puede escribir código que una computadora entienda. Los buenos programadores escriben código que los humanos pueden entender." - Martin Fowler

### Próximos Pasos

1. **Practica diariamente** - Revisa tu código antes de hacer commit
2. **Usa herramientas** - Prettier, ESLint, linters
3. **Code reviews** - Pide feedback a compañeros
4. **Refactoriza** - Mejora código antiguo regularmente
5. **Lee código de otros** - Aprende de proyectos open source

**¡El código limpio es un hábito que se desarrolla con práctica constante! 💪**

---

## Recursos Adicionales

- **Clean Code** - Libro de Robert C. Martin
- **JavaScript Style Guide** - Airbnb: https://github.com/airbnb/javascript
- **PEP 8** - Guía de estilo de Python: https://pep8.org/
- **Prettier** - Formateador automático: https://prettier.io/
- **ESLint** - Linter para JavaScript: https://eslint.org/

---

## Cheat Sheet: Buenas Prácticas

```javascript
// NOMBRES
✅ customerAge    ❌ x
✅ calculateTotal ❌ calc
✅ isLoggedIn    ❌ flag

// FUNCIONES
✅ Pequeñas y enfocadas
✅ Nombres con verbos
✅ Early returns

// ESTRUCTURA
✅ Indentación consistente
✅ Máximo 2-3 niveles de anidación
✅ Agrupar código lógicamente

// ERRORES
✅ try-catch en operaciones riesgosas
✅ Validar entradas
✅ Loguear errores

// LEGIBILIDAD
✅ Código auto-explicativo
✅ Evitar comentarios obvios
✅ Espaciado entre secciones
```
