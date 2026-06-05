🇪🇸 **Español** | [🇬🇧 English](index.en.md)

# Día 14: Unit Testing con Jest 🧪

## Introducción

El testing (pruebas) es una de las habilidades más importantes en el desarrollo profesional de software. Hoy aprenderás a escribir **pruebas unitarias** (unit tests) usando **Jest**, el framework de testing más popular de JavaScript.

### ¿Por qué hacer testing?

Imagina que construyes una calculadora. Cada vez que añades una nueva función, ¿cómo sabes que no has roto algo que ya funcionaba? **Los tests automatizan esta verificación**.

### Empresas que usan Jest

- 🐦 Twitter
- 📷 Instagram
- 📌 Pinterest
- 🏠 Airbnb
- 🎵 Spotify

---

## Parte 1: ¿Qué es Unit Testing?

### Concepto Básico

**Unit Testing** = Probar las **piezas más pequeñas** de tu código de forma **aislada**.

### Analogía: La Fábrica de Juguetes 🏭

Imagina una fábrica que produce coches de juguete:

| Enfoque | Descripción |
|---------|-------------|
| **Sin tests** | Produces 1000 coches y al final descubres que las ruedas están mal |
| **Con unit tests** | Pruebas cada rueda antes de ensamblar el coche |

### ¿Qué es una "Unit" (Unidad)?

En JavaScript, una **unit** normalmente es una **función**:

```javascript
// Esta es una unidad
function sum(a, b) {
    return a + b;
}

// Esta es otra unidad
function multiply(a, b) {
    return a * b;
}
```

### Características de los Unit Tests

✅ **Rápidos** - Se ejecutan en milisegundos  
✅ **Independientes** - Un test no depende de otro  
✅ **Repetibles** - Siempre dan el mismo resultado  
✅ **Automáticos** - No requieren intervención manual

---

## Parte 2: ¿Qué es Jest?

### Definición

**Jest** es un framework de testing para JavaScript creado por Facebook (Meta). Es el estándar de facto para testing en JavaScript moderno.

### Ventajas de Jest

| Característica | Beneficio |
|----------------|-----------|
| 🚀 **Zero Config** | Funciona sin configuración |
| ⚡ **Rápido** | Ejecuta tests en paralelo |
| 📸 **Snapshots** | Detecta cambios visuales |
| 🎯 **Todo incluido** | No necesitas librerías adicionales |
| 📝 **Mensajes claros** | Errores fáciles de entender |

### Filosofía de Jest

> "Tests should be delightful to write"  
> (Los tests deberían ser un placer escribirlos)

---

## Parte 3: Anatomía de un Test

### La Estructura Básica

Todo test tiene 3 partes:

```javascript
test('descripción de lo que pruebas', () => {
    // 1. ARRANGE (Preparar): Configurar datos
    const input = 5;
    
    // 2. ACT (Actuar): Ejecutar la función
    const result = doubleit(input);
    
    // 3. ASSERT (Afirmar): Verificar el resultado
    expect(result).toBe(10);
});
```

### Ejemplo Visual

```
┌─────────────────────────────────────┐
│  test('suma 2 + 3 = 5')             │
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

## Parte 4: Tu Primer Test - Paso a Paso

Vamos a crear nuestro primer test desde cero.

### Paso 1: Crear la Estructura del Proyecto

```bash
mkdir mi-primer-test
cd mi-primer-test
npm init -y
```

Esto crea un archivo `package.json`.

### Paso 2: Instalar Jest

```bash
npm install --save-dev jest
```

**💡 Nota**: `--save-dev` instala Jest solo para desarrollo, no para producción.

### Paso 3: Configurar npm para Ejecutar Tests

Abre `package.json` y modifica la sección `"scripts"`:

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

### Paso 4: Crear la Función a Probar

Crea un archivo llamado `sum.js`:

```javascript
function sum(a, b) {
    return a + b;
}

module.exports = sum;
```

### 🔍 Explicación

```javascript
module.exports = sum;
```

Esto **exporta** la función para que pueda ser importada en otros archivos.

### Paso 5: Crear el Archivo de Test

Crea un archivo llamado `sum.test.js`:

```javascript
const sum = require('./sum');

test('suma 1 + 2 para obtener 3', () => {
    expect(sum(1, 2)).toBe(3);
});
```

### 🔍 Convención de Nombres

| Archivo | Convención |
|---------|-----------|
| Función | `sum.js` |
| Test | `sum.test.js` |

Jest busca automáticamente archivos que terminen en `.test.js` o `.spec.js`.

### Paso 6: Ejecutar el Test

```bash
npm test
```

### ✅ Resultado Esperado

```
PASS  ./sum.test.js
  ✓ suma 1 + 2 para obtener 3 (2 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

🎉 **¡Felicidades! Has creado y ejecutado tu primer test.**

---

## Parte 5: Entendiendo `expect` y Matchers

### ¿Qué es `expect`?

`expect` es la función que usas para verificar resultados. Siempre va acompañada de un **matcher**.

### Sintaxis

```javascript
expect(valorActual).matcher(valorEsperado);
```

### Matchers Más Comunes

#### 1. `.toBe()` - Igualdad estricta (===)

```javascript
test('números iguales', () => {
    expect(2 + 2).toBe(4);
});

test('strings iguales', () => {
    expect('hello').toBe('hello');
});
```

#### 2. `.toEqual()` - Igualdad de contenido (objetos y arrays)

```javascript
test('objetos iguales', () => {
    const user = { name: 'Ana', age: 25 };
    expect(user).toEqual({ name: 'Ana', age: 25 });
});

test('arrays iguales', () => {
    expect([1, 2, 3]).toEqual([1, 2, 3]);
});
```

#### 3. `.toBeTruthy()` / `.toBeFalsy()`

```javascript
test('valor verdadero', () => {
    expect(true).toBeTruthy();
    expect(1).toBeTruthy();
    expect('hola').toBeTruthy();
});

test('valor falso', () => {
    expect(false).toBeFalsy();
    expect(0).toBeFalsy();
    expect('').toBeFalsy();
});
```

#### 4. `.toBeNull()` / `.toBeUndefined()`

```javascript
test('verificar null', () => {
    const data = null;
    expect(data).toBeNull();
});

test('verificar undefined', () => {
    let variable;
    expect(variable).toBeUndefined();
});
```

#### 5. `.toContain()` - Para arrays y strings

```javascript
test('array contiene elemento', () => {
    const colors = ['red', 'blue', 'green'];
    expect(colors).toContain('blue');
});

test('string contiene substring', () => {
    expect('hello world').toContain('world');
});
```

#### 6. `.toBeGreaterThan()` / `.toBeLessThan()`

```javascript
test('mayor que', () => {
    expect(10).toBeGreaterThan(5);
});

test('menor que', () => {
    expect(5).toBeLessThan(10);
});
```

### 📊 Tabla Resumen de Matchers

| Matcher | Uso | Ejemplo |
|---------|-----|---------|
| `.toBe(x)` | Igualdad estricta | `expect(2+2).toBe(4)` |
| `.toEqual(x)` | Igualdad de contenido | `expect({a:1}).toEqual({a:1})` |
| `.toBeTruthy()` | Valor verdadero | `expect(1).toBeTruthy()` |
| `.toBeFalsy()` | Valor falso | `expect(0).toBeFalsy()` |
| `.toContain(x)` | Contiene elemento | `expect([1,2]).toContain(2)` |
| `.toBeGreaterThan(x)` | Mayor que | `expect(10).toBeGreaterThan(5)` |

---

## Parte 6: Ejemplo Completo - Testing una Función Real

Vamos a probar una función más realista.

### La Función: Validador de Contraseñas

Crea `passwordValidator.js`:

```javascript
function isValidPassword(password) {
    // Reglas:
    // 1. Mínimo 8 caracteres
    // 2. Al menos una mayúscula
    // 3. Al menos un número
    
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

### Los Tests

Crea `passwordValidator.test.js`:

```javascript
const isValidPassword = require('./passwordValidator');

test('contraseña válida con todos los requisitos', () => {
    expect(isValidPassword('Password123')).toBe(true);
});

test('contraseña muy corta debe fallar', () => {
    expect(isValidPassword('Pass1')).toBe(false);
});

test('contraseña sin mayúscula debe fallar', () => {
    expect(isValidPassword('password123')).toBe(false);
});

test('contraseña sin número debe fallar', () => {
    expect(isValidPassword('Password')).toBe(false);
});

test('contraseña solo con minúsculas debe fallar', () => {
    expect(isValidPassword('helloworld')).toBe(false);
});
```

### Ejecutar Tests

```bash
npm test
```

### ✅ Resultado

```
PASS  ./passwordValidator.test.js
  ✓ contraseña válida con todos los requisitos (2 ms)
  ✓ contraseña muy corta debe fallar (1 ms)
  ✓ contraseña sin mayúscula debe fallar
  ✓ contraseña sin número debe fallar
  ✓ contraseña solo con minúsculas debe fallar

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
```

---

## Parte 7: Organizando Tests con `describe`

Cuando tienes muchos tests, es útil agruparlos.

### Sintaxis

```javascript
describe('Grupo de tests relacionados', () => {
    test('test 1', () => { /* ... */ });
    test('test 2', () => { /* ... */ });
});
```

### Ejemplo: Calculadora Completa

Crea `calculator.js`:

```javascript
const calculator = {
    sum: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b,
    divide: (a, b) => a / b
};

module.exports = calculator;
```

Crea `calculator.test.js`:

```javascript
const calculator = require('./calculator');

describe('Operaciones Básicas de Calculadora', () => {
    
    describe('Suma', () => {
        test('suma números positivos', () => {
            expect(calculator.sum(2, 3)).toBe(5);
        });
        
        test('suma números negativos', () => {
            expect(calculator.sum(-2, -3)).toBe(-5);
        });
        
        test('suma cero', () => {
            expect(calculator.sum(5, 0)).toBe(5);
        });
    });
    
    describe('Resta', () => {
        test('resta números positivos', () => {
            expect(calculator.subtract(10, 3)).toBe(7);
        });
        
        test('resta con resultado negativo', () => {
            expect(calculator.subtract(3, 10)).toBe(-7);
        });
    });
    
    describe('Multiplicación', () => {
        test('multiplica números positivos', () => {
            expect(calculator.multiply(4, 5)).toBe(20);
        });
        
        test('multiplicar por cero', () => {
            expect(calculator.multiply(10, 0)).toBe(0);
        });
    });
    
    describe('División', () => {
        test('divide números normales', () => {
            expect(calculator.divide(10, 2)).toBe(5);
        });
        
        test('división con decimales', () => {
            expect(calculator.divide(10, 3)).toBeCloseTo(3.33, 2);
        });
    });
});
```

### 🔍 Nuevo Matcher: `.toBeCloseTo()`

```javascript
expect(calculator.divide(10, 3)).toBeCloseTo(3.33, 2);
```

- **3.33**: Valor esperado
- **2**: Número de decimales de precisión

Útil para comparar números con decimales.

---

## Parte 8: Testing de Funciones que Usan Arrays

### La Función

Crea `arrayHelpers.js`:

```javascript
const arrayHelpers = {
    // Filtra números pares
    getEvenNumbers: (numbers) => {
        return numbers.filter(num => num % 2 === 0);
    },
    
    // Obtiene el máximo
    getMax: (numbers) => {
        return Math.max(...numbers);
    },
    
    // Suma todos los elementos
    sumAll: (numbers) => {
        return numbers.reduce((sum, num) => sum + num, 0);
    },
    
    // Elimina duplicados
    removeDuplicates: (array) => {
        return [...new Set(array)];
    }
};

module.exports = arrayHelpers;
```

### Los Tests

Crea `arrayHelpers.test.js`:

```javascript
const arrayHelpers = require('./arrayHelpers');

describe('Array Helpers', () => {
    
    describe('getEvenNumbers', () => {
        test('devuelve solo números pares', () => {
            const result = arrayHelpers.getEvenNumbers([1, 2, 3, 4, 5, 6]);
            expect(result).toEqual([2, 4, 6]);
        });
        
        test('devuelve array vacío si no hay pares', () => {
            const result = arrayHelpers.getEvenNumbers([1, 3, 5]);
            expect(result).toEqual([]);
        });
    });
    
    describe('getMax', () => {
        test('encuentra el número máximo', () => {
            expect(arrayHelpers.getMax([3, 7, 2, 9, 1])).toBe(9);
        });
        
        test('funciona con números negativos', () => {
            expect(arrayHelpers.getMax([-5, -2, -10])).toBe(-2);
        });
    });
    
    describe('sumAll', () => {
        test('suma todos los números', () => {
            expect(arrayHelpers.sumAll([1, 2, 3, 4])).toBe(10);
        });
        
        test('devuelve 0 para array vacío', () => {
            expect(arrayHelpers.sumAll([])).toBe(0);
        });
    });
    
    describe('removeDuplicates', () => {
        test('elimina elementos duplicados', () => {
            const result = arrayHelpers.removeDuplicates([1, 2, 2, 3, 3, 3, 4]);
            expect(result).toEqual([1, 2, 3, 4]);
        });
        
        test('mantiene array sin duplicados igual', () => {
            const result = arrayHelpers.removeDuplicates([1, 2, 3]);
            expect(result).toEqual([1, 2, 3]);
        });
    });
});
```

---

## Parte 9: Testing de Casos Extremos (Edge Cases)

### ¿Qué son los Edge Cases?

Son situaciones **poco comunes pero posibles** que pueden romper tu código.

### Ejemplo: Función de División Segura

Crea `safeDivide.js`:

```javascript
function safeDivide(a, b) {
    // Edge case: División por cero
    if (b === 0) {
        throw new Error('No se puede dividir por cero');
    }
    
    // Edge case: Parámetros no numéricos
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('Ambos parámetros deben ser números');
    }
    
    return a / b;
}

module.exports = safeDivide;
```

### Tests con `.toThrow()`

Crea `safeDivide.test.js`:

```javascript
const safeDivide = require('./safeDivide');

describe('safeDivide', () => {
    
    test('divide números normales', () => {
        expect(safeDivide(10, 2)).toBe(5);
    });
    
    test('lanza error al dividir por cero', () => {
        expect(() => safeDivide(10, 0)).toThrow('No se puede dividir por cero');
    });
    
    test('lanza error con parámetro no numérico', () => {
        expect(() => safeDivide('10', 2)).toThrow('Ambos parámetros deben ser números');
    });
    
    test('lanza error con ambos parámetros no numéricos', () => {
        expect(() => safeDivide('a', 'b')).toThrow();
    });
});
```

### 🔍 Sintaxis de `.toThrow()`

```javascript
// Para funciones que lanzan errores, DEBES envolverlas en una función arrow
expect(() => safeDivide(10, 0)).toThrow();

// ❌ INCORRECTO
expect(safeDivide(10, 0)).toThrow(); // No funciona

// ✅ CORRECTO
expect(() => safeDivide(10, 0)).toThrow();
```

---

## Parte 10: Testing de Strings

### La Función

Crea `stringHelpers.js`:

```javascript
const stringHelpers = {
    // Convierte a mayúsculas
    isUpperCase: (str) => {
        if (typeof str !== 'string') return false;
        return str === str.toUpperCase() && str !== '';
    },
    
    // Cuenta vocales
    countVowels: (str) => {
        const vowels = str.match(/[aeiouAEIOU]/g);
        return vowels ? vowels.length : 0;
    },
    
    // Invierte string
    reverse: (str) => {
        return str.split('').reverse().join('');
    },
    
    // Es palíndromo
    isPalindrome: (str) => {
        const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
        return cleaned === cleaned.split('').reverse().join('');
    }
};

module.exports = stringHelpers;
```

### Los Tests

Crea `stringHelpers.test.js`:

```javascript
const stringHelpers = require('./stringHelpers');

describe('String Helpers', () => {
    
    describe('isUpperCase', () => {
        test('detecta string en mayúsculas', () => {
            expect(stringHelpers.isUpperCase('HELLO')).toBe(true);
        });
        
        test('detecta string en minúsculas', () => {
            expect(stringHelpers.isUpperCase('hello')).toBe(false);
        });
        
        test('detecta string mezclado', () => {
            expect(stringHelpers.isUpperCase('Hello')).toBe(false);
        });
        
        test('devuelve false para no-string', () => {
            expect(stringHelpers.isUpperCase(123)).toBe(false);
        });
    });
    
    describe('countVowels', () => {
        test('cuenta vocales correctamente', () => {
            expect(stringHelpers.countVowels('hello')).toBe(2);
        });
        
        test('cuenta vocales en mayúsculas', () => {
            expect(stringHelpers.countVowels('AEIOU')).toBe(5);
        });
        
        test('devuelve 0 si no hay vocales', () => {
            expect(stringHelpers.countVowels('xyz')).toBe(0);
        });
    });
    
    describe('reverse', () => {
        test('invierte string simple', () => {
            expect(stringHelpers.reverse('hello')).toBe('olleh');
        });
        
        test('invierte string vacío', () => {
            expect(stringHelpers.reverse('')).toBe('');
        });
    });
    
    describe('isPalindrome', () => {
        test('detecta palíndromo simple', () => {
            expect(stringHelpers.isPalindrome('oso')).toBe(true);
        });
        
        test('detecta palíndromo con espacios', () => {
            expect(stringHelpers.isPalindrome('anita lava la tina')).toBe(true);
        });
        
        test('detecta no-palíndromo', () => {
            expect(stringHelpers.isPalindrome('hello')).toBe(false);
        });
    });
});
```

---

## Parte 11: Modo Watch - Testing Continuo

### ¿Qué es el Modo Watch?

Jest puede **quedarse ejecutándose** y re-ejecutar tests automáticamente cuando guardas cambios.

### Activar Watch Mode

```bash
npm test -- --watch
```

o añade un script en `package.json`:

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

Ahora ejecuta:

```bash
npm run test:watch
```

### Ventajas

- ✅ Tests se ejecutan automáticamente al guardar
- ✅ Solo ejecuta tests relacionados con archivos modificados
- ✅ Feedback instantáneo
- ✅ Perfecto durante el desarrollo

---

## Parte 12: Coverage (Cobertura de Tests)

### ¿Qué es Coverage?

**Coverage** te dice qué porcentaje de tu código está cubierto por tests.

### Ver Coverage

```bash
npm test -- --coverage
```

### Ejemplo de Reporte

```
----------------------|---------|----------|---------|---------|
File                  | % Stmts | % Branch | % Funcs | % Lines |
----------------------|---------|----------|---------|---------|
All files             |     100 |      100 |     100 |     100 |
 calculator.js        |     100 |      100 |     100 |     100 |
 stringHelpers.js     |     100 |      100 |     100 |     100 |
----------------------|---------|----------|---------|---------|
```

### Interpretación

| Métrica | Significado |
|---------|-------------|
| **Stmts** (Statements) | % de líneas ejecutadas |
| **Branch** | % de condiciones if/else probadas |
| **Funcs** | % de funciones llamadas |
| **Lines** | % de líneas de código cubiertas |

### Meta Profesional

🎯 **Objetivo**: 80% - 100% de coverage en proyectos profesionales.

---

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Testing de Función de Email ⭐

Crea una función que valide emails y escribe tests para ella.

```javascript
// emailValidator.js
function isValidEmail(email) {
    // Debe contener @ y un dominio
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

module.exports = isValidEmail;
```

**Tests que debes escribir:**
- Email válido: `test@example.com`
- Email sin @: `testexample.com`
- Email sin dominio: `test@`
- Email vacío: `""`

### Ejercicio 2: Testing de Función de Edades ⭐⭐

```javascript
// ageClassifier.js
function classifyAge(age) {
    if (age < 0) return 'inválido';
    if (age < 13) return 'niño';
    if (age < 18) return 'adolescente';
    if (age < 65) return 'adulto';
    return 'adulto mayor';
}

module.exports = classifyAge;
```

**Escribe tests para:**
- Cada categoría
- Límites (0, 12, 13, 17, 18, 64, 65)
- Valores negativos

### Ejercicio 3: Testing de Carrito de Compras ⭐⭐⭐

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

**Escribe tests para:**
- Añadir items
- Calcular total
- Contar items
- Limpiar carrito

---

## Resumen: Conceptos Clave

### Unit Testing
✅ Prueba las unidades más pequeñas de código  
✅ Debe ser rápido, independiente y repetible  
✅ Detecta bugs antes de producción

### Jest
✅ Framework de testing #1 en JavaScript  
✅ Zero configuration  
✅ Rápido y con mensajes claros

### Estructura de un Test
✅ **ARRANGE**: Preparar datos  
✅ **ACT**: Ejecutar función  
✅ **ASSERT**: Verificar resultado

### Matchers Esenciales
✅ `.toBe()` - Igualdad estricta  
✅ `.toEqual()` - Igualdad de contenido  
✅ `.toContain()` - Contiene elemento  
✅ `.toThrow()` - Lanza error

### Organización
✅ `describe()` - Agrupa tests relacionados  
✅ Archivos `.test.js` para tests  
✅ Un archivo de test por archivo de código

### Comandos Importantes
```bash
npm test              # Ejecutar tests
npm test -- --watch   # Modo continuo
npm test -- --coverage # Ver cobertura
```

---

## Cheat Sheet: Jest

```javascript
// ESTRUCTURA BÁSICA
test('descripción', () => {
    expect(resultado).matcher(esperado);
});

// AGRUPAR TESTS
describe('grupo', () => {
    test('test 1', () => { /* ... */ });
    test('test 2', () => { /* ... */ });
});

// MATCHERS COMUNES
expect(x).toBe(y)              // Igualdad estricta
expect(x).toEqual(y)           // Igualdad de contenido
expect(x).toBeTruthy()         // Valor verdadero
expect(x).toBeFalsy()          // Valor falso
expect(x).toBeNull()           // Es null
expect(x).toBeUndefined()      // Es undefined
expect(x).toContain(y)         // Contiene elemento
expect(x).toBeGreaterThan(y)   // Mayor que
expect(x).toBeLessThan(y)      // Menor que
expect(x).toBeCloseTo(y, d)    // Cercano a (decimales)
expect(() => x()).toThrow()    // Lanza error

// NÚMEROS
expect(10).toBeGreaterThan(5)
expect(5).toBeLessThan(10)
expect(4.23).toBeCloseTo(4.2, 1)

// ARRAYS
expect([1,2,3]).toContain(2)
expect([1,2,3]).toEqual([1,2,3])
expect([1,2,3]).toHaveLength(3)

// OBJETOS
expect({a:1}).toEqual({a:1})
expect({a:1,b:2}).toHaveProperty('a')

// STRINGS
expect('hello world').toContain('world')
expect('hello').toMatch(/ell/)
```

---

## Buenas Prácticas

### ✅ DO (Hacer)

1. **Nombra tests descriptivamente**
   ```javascript
   test('devuelve array vacío cuando no hay elementos pares', () => {})
   ```

2. **Un test, una cosa**
   ```javascript
   // ✅ Bueno
   test('suma números positivos', () => {})
   test('suma números negativos', () => {})
   
   // ❌ Malo
   test('suma todo tipo de números', () => {
       // Muchas verificaciones aquí
   })
   ```

3. **Testa edge cases**
   ```javascript
   test('maneja división por cero', () => {})
   test('maneja string vacío', () => {})
   test('maneja array vacío', () => {})
   ```

4. **Tests independientes**
   ```javascript
   // Cada test debe poder ejecutarse solo
   ```

### ❌ DON'T (No Hacer)

1. **No testear implementación, testea comportamiento**
   ```javascript
   // ❌ Malo: Testear cómo lo hace
   test('usa el método .filter()', () => {})
   
   // ✅ Bueno: Testear qué hace
   test('devuelve solo números pares', () => {})
   ```

2. **No usar valores mágicos**
   ```javascript
   // ❌ Malo
   expect(calculate()).toBe(42); // ¿Por qué 42?
   
   // ✅ Bueno
   const expected = price * taxRate;
   expect(calculate(price, taxRate)).toBe(expected);
   ```

3. **No tests dependientes**
   ```javascript
   // ❌ Malo: Test 2 depende de Test 1
   let user;
   test('crear usuario', () => {
       user = createUser();
   });
   test('actualizar usuario', () => {
       updateUser(user); // Depende del anterior
   });
   ```

---

## 🔗 Recursos Adicionales

- **Jest Docs**: https://jestjs.io/docs/getting-started
- **Jest Cheat Sheet**: https://github.com/sapegin/jest-cheat-sheet
- **4Geeks - Unit Testing**: https://4geeks.com/lesson/how-to-create-unit-testing-with-javascript-and-jest
- **Testing Best Practices**: https://testingjavascript.com/

---

## 🎉 ¡Felicidades!

Ahora sabes:

- ✅ Qué es unit testing y por qué es importante
- ✅ Cómo instalar y configurar Jest
- ✅ Escribir tests con `test()` y `expect()`
- ✅ Usar matchers comunes
- ✅ Organizar tests con `describe()`
- ✅ Testear edge cases
- ✅ Ver coverage de tests
- ✅ Usar watch mode para desarrollo continuo

**Próximo paso**: Practica escribiendo tests para tus propias funciones. El testing es una habilidad que mejora con la práctica.

---

## 💡 Pensamiento Final

> "Code without tests is broken by design"  
> (Código sin tests está roto por diseño)  
> — Jacob Kaplan-Moss (co-creador de Django)

El testing no es opcional en el desarrollo profesional. Es una inversión que:
- 💰 Ahorra tiempo a largo plazo
- 🐛 Detecta bugs antes de producción
- 📚 Documenta cómo usar tu código
- 🔒 Da confianza para refactorizar
- 🚀 Permite entregar código con calidad

**¡Empieza a escribir tests hoy!**

<citations>
  <document>
      <document_type>RULE</document_type>
      <document_id>/Users/erwinaguero/teaching/4geeks_academy_spain_fs_pt_129/WARP.md</document_id>
  </document>
</citations>