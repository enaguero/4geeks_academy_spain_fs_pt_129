🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# Step 1: Síncrono vs Asíncrono 🔄

## ¿Qué es Código Síncrono?

**Código síncrono** es código que se ejecuta **línea por línea**, en orden, esperando que cada operación termine antes de continuar con la siguiente.

### Ejemplo de Vida Real: Fila en el Supermercado 🛒

Imagina una fila en el supermercado con **una sola caja**:

1. La persona 1 llega a la caja
2. El cajero escanea todos sus productos (⏳ 5 minutos)
3. La persona 1 paga y se va
4. **Ahora** la persona 2 puede avanzar
5. El cajero escanea sus productos (⏳ 3 minutos)
6. Y así sucesivamente...

**Problema**: Si una operación tarda mucho, todo se bloquea esperándola.

### Código Síncrono en JavaScript

```javascript
console.log('1. Inicio');
console.log('2. Procesando...');
console.log('3. Fin');

// Salida:
// 1. Inicio
// 2. Procesando...
// 3. Fin
```

Todo se ejecuta en orden, sin sorpresas.

---

## ¿Qué es Código Asíncrono?

**Código asíncrono** permite que el programa **continúe ejecutándose** mientras espera que una operación lenta termine.

### Ejemplo de Vida Real: Restaurante 🍽️

Imagina un restaurante donde:

1. El mesero toma tu pedido
2. **No se queda parado esperando** que la cocina prepare tu comida
3. Va a tomar pedidos de otras mesas
4. Cuando tu comida está lista, te la trae
5. Mientras tanto, ha atendido a 10 mesas más

**Ventaja**: El mesero (tu programa) no se bloquea esperando. Puede hacer otras cosas.

### Código Asíncrono en JavaScript

```javascript
console.log('1. Inicio');

// Esto se ejecuta DESPUÉS (asíncrono)
setTimeout(() => {
  console.log('2. Procesando...');
}, 2000);

console.log('3. Fin');

// Salida:
// 1. Inicio
// 3. Fin
// (espera 2 segundos)
// 2. Procesando...
```

¿Ves la diferencia? El orden de ejecución **no es el orden en que escribiste el código**.

---

## Comparación Visual

### Síncrono
```
Tarea 1 ━━━━━━━━━━━━━> [TERMINA]
                          │
                          ▼
                      Tarea 2 ━━━━━> [TERMINA]
                                       │
                                       ▼
                                   Tarea 3 ━━━> [TERMINA]
```

Todo en secuencia. Una tarea **bloquea** la siguiente.

### Asíncrono
```
Tarea 1 ━━━━━━━━━━━━━> [TERMINA]
                          │
                          ├─> Tarea 2 (espera) ━━━━━━━> [TERMINA]
                          │
                          └─> Tarea 3 ━━━> [TERMINA]
```

Varias tareas pueden estar "en progreso" al mismo tiempo.

---

## ¿Por Qué Necesitamos Asincronía?

En desarrollo web, muchas operaciones **tardan tiempo**:

- 🌐 Pedir datos a un servidor por internet
- 📁 Leer archivos del sistema
- 💾 Consultar bases de datos
- ⏱️ Esperar un tiempo determinado (timers)

Si usáramos código síncrono, **tu aplicación se congelaría** esperando cada operación.

### Ejemplo: Sin Asincronía (Código Bloqueante)

```javascript
console.log('Pidiendo datos al servidor...');
// Imagina que esto tarda 5 segundos
esperarRespuestaDelServidor(); // ⏸️ TODO SE CONGELA AQUÍ
console.log('Datos recibidos');
```

Durante esos 5 segundos:
- ❌ No puedes hacer clic en botones
- ❌ No puedes escribir en inputs
- ❌ La aplicación está "muerta"

### Ejemplo: Con Asincronía (Código No Bloqueante)

```javascript
console.log('Pidiendo datos al servidor...');

// Operación asíncrona (veremos cómo funciona en los siguientes steps)
pedirDatosAlServidor(function(datos) {
  console.log('Datos recibidos:', datos);
});

console.log('Mientras tanto, puedo hacer otras cosas');

// Salida inmediata:
// Pidiendo datos al servidor...
// Mientras tanto, puedo hacer otras cosas
// (luego de unos segundos)
// Datos recibidos: {...}
```

Tu aplicación **sigue funcionando** mientras espera la respuesta.

---

## Operaciones Síncronas Comunes

```javascript
// Operaciones matemáticas
let suma = 5 + 3; // Instantáneo

// Condicionales
if (suma > 5) {
  console.log('Mayor');
}

// Bucles
for (let i = 0; i < 10; i++) {
  console.log(i); // Se ejecuta todo inmediatamente
}

// Variables
let nombre = 'Juan';
console.log(nombre); // Instantáneo
```

Todas estas operaciones **se ejecutan al instante**.

---

## Operaciones Asíncronas Comunes

```javascript
// setTimeout (esperar un tiempo)
setTimeout(() => {
  console.log('Después de 1 segundo');
}, 1000);

// Pedir datos a un servidor
pedirDatos('url', (datos) => {
  console.log(datos); // Se ejecuta cuando lleguen
});

// Eventos del usuario
button.addEventListener('click', () => {
  console.log('Clic!'); // Se ejecuta cuando el usuario haga clic
});

// Leer archivos
leerArchivo('archivo.txt', (contenido) => {
  console.log(contenido); // Se ejecuta cuando termine de leer
});
```

Estas operaciones **no se completan inmediatamente**.

---

## Ejemplo Práctico: Cocinar 🍳

### Versión Síncrona (Ineficiente)
```javascript
console.log('Poner agua a hervir'); // ⏳ 5 minutos
esperarQueHierva(); // BLOQUEO - no haces nada más

console.log('Cortar verduras'); // ⏳ 3 minutos
esperarQueTermines(); // BLOQUEO

console.log('Cocinar pasta'); // ⏳ 10 minutos
esperarQueSeCocine(); // BLOQUEO

// Tiempo total: 5 + 3 + 10 = 18 minutos
```

### Versión Asíncrona (Eficiente)
```javascript
console.log('Poner agua a hervir'); // ⏳ 5 minutos en segundo plano

// Mientras hierve el agua...
console.log('Cortar verduras'); // ⏳ 3 minutos

// Cuando el agua hierve (callback)
cuandoHierva(() => {
  console.log('Cocinar pasta'); // ⏳ 10 minutos
});

// Tiempo total: ~13 minutos (tareas en paralelo)
```

---

## Puntos Clave ✨

1. **Síncrono** = Una cosa después de otra, en orden
2. **Asíncrono** = Varias cosas pueden estar "en progreso"
3. **JavaScript es asíncrono** para operaciones lentas (pedir datos al servidor, setTimeout, etc.)
4. **No bloquear** = Tu aplicación sigue funcionando mientras espera
5. **Orden de ejecución** puede ser diferente al orden del código

---

## Tu Ejercicio 🎯

Predice la salida de este código:

```javascript
console.log('A');

setTimeout(() => {
  console.log('B');
}, 0); // ⚠️ 0 milisegundos

console.log('C');

// ❓ ¿Qué se imprime primero?
```

**Respuesta**: A, C, B

**¿Por qué?** Aunque setTimeout tiene 0ms, sigue siendo **asíncrono**. JavaScript primero ejecuta todo el código síncrono (A, C) y luego procesa las operaciones asíncronas (B).

---

## Próximos Pasos

Una vez entiendas síncrono vs asíncrono:

✅ Concepto de código bloqueante vs no bloqueante  
✅ Por qué JavaScript necesita asincronía  
✅ Diferencia entre operaciones instantáneas y lentas  

Estarás listo para:
- **Step 2**: setTimeout - Tu primera herramienta asíncrona
- **Step 3**: Callbacks y el "Callback Hell"
- **Step 4**: Promises - La solución moderna

---

**💡 Consejo**: Este es el concepto MÁS IMPORTANTE del día. Si lo entiendes bien, todo lo demás tendrá sentido.

**🎯 Regla de oro**: Si una operación tarda tiempo (red, archivos, timers), JavaScript la hace asíncrona para no bloquear tu aplicación.
