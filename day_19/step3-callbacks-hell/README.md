# Step 3: Callbacks y el "Callback Hell" 🔥

## 🔗 ¿Por qué Este Step?

En Step 2 aprendiste que setTimeout ejecuta código **después** de un tiempo. Pero ¿qué pasa si necesitas hacer **varias operaciones en secuencia**?

Ejemplo del mundo real:
1. Pedir datos de un usuario desde el servidor (⌛ tardará X segundos)
2. Con esos datos, pedir los posts del usuario (⌛ tardará X segundos más)
3. Con el primer post, pedir los comentarios (⌛ tardará X segundos más)

**Cada paso depende del anterior.** No puedes pedir los posts sin tener el usuario primero.

Esta necesidad de **ejecutar código en secuencia de forma asíncrona** es donde surgen los callbacks... y el "Callback Hell".

---

## 🔗 Conexión: Asíncrono + Callbacks

Antes de ver qué es un callback, necesitas entender **por qué existen** y **cómo se relacionan con código asíncrono**.

### El Problema: Código Asíncrono Necesita "Avisar" Cuando Termina

**Recuerda del Step 1**: Código asíncrono = no bloquea, se ejecuta "en el futuro".

**Pregunta**: Si una operación tarda (como pedir datos a un servidor), ¿cómo sabe JavaScript qué hacer cuando termine?

#### Código Síncrono (fácil):
```javascript
// Línea por línea, en orden
const resultado1 = operacion1();     // Espera aquí hasta que termine
const resultado2 = operacion2();     // Luego esta
const resultado3 = operacion3();     // Luego esta
console.log('Todo listo');
```

**Simple**: JavaScript espera en cada línea. Cuando termina, continúa.

#### Código Asíncrono (problema):
```javascript
// ❌ ESTO NO FUNCIONA
const resultado = pedirDatosAlServidor();  // Tarda 2 segundos
console.log(resultado);                    // undefined (no ha llegado)
```

**Problema**: `pedirDatosAlServidor()` tarda 2 segundos, pero JavaScript no espera. Continúa inmediatamente y `resultado` aún no existe.

### La Solución: Callbacks

Un **callback** es una función que le dices a JavaScript: **"Cuando termines, ejecuta esto"**.

```javascript
// ✅ CON CALLBACK FUNCIONA
pedirDatosAlServidor(function(resultado) {
  // Esta función se ejecuta "en el futuro" cuando lleguen los datos
  console.log(resultado);  // Ahora sí tenemos los datos
});

console.log('Continúo mientras espero...');

// Salida:
// Continúo mientras espero...
// (2 segundos después)
// { datos: [...] }
```

### Visualización del Flujo

```
Tiempo →

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Código Síncrono:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

│ paso1() │ paso2() │ paso3() │ console.log() │
└─────────┴─────────┴─────────┴───────────────┘
   ESPERA   ESPERA    ESPERA      EJECUTA


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Código Asíncrono CON Callback:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

│ pedirDatos(callback) │ console.log() │
└──────────────────────┴───────────────┘
   LANZA (no espera)      EJECUTA
         ↓
         │ (esperando...)
         ↓
         │ (2 segundos después)
         ↓
   ┌─────────────┐
   │  callback() │  ← Se ejecuta cuando llegan los datos
   └─────────────┘
```

---

## ¿Qué es un Callback?

Un **callback** es una función que se pasa como parámetro a otra función para que se ejecute **después** de que algo termine.

**En otras palabras**: Es la manera de decirle a JavaScript "cuando termines esta operación asíncrona, ejecuta esta función".

```javascript
function hacerAlgo(callback) {
  console.log('Haciendo algo...');
  callback(); // Ejecuta la función que pasamos
}

// Pasamos una función como callback
hacerAlgo(() => {
  console.log('¡Terminé!');
});

// Salida:
// Haciendo algo...
// ¡Terminé!
```

---

## Callbacks en Operaciones Asíncronas

Los callbacks son muy comunes en operaciones asíncronas:

### Ejemplo con setTimeout

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Callback ejecutado después de 1 segundo');
}, 1000);

console.log('Fin');

// Salida:
// Inicio
// Fin
// (espera 1 segundo)
// Callback ejecutado después de 1 segundo
```

### Ejemplo con Eventos

```javascript
const boton = document.querySelector('button');

// El callback se ejecuta cuando haces clic
boton.addEventListener('click', () => {
  console.log('¡Botón clickeado!');
});
```

---

## Callbacks para Secuencias

¿Qué pasa si necesitas hacer **varias operaciones en secuencia**?

### Escenario: Pedir datos de un usuario

1. Obtener usuario por ID
2. Obtener sus posts
3. Obtener comentarios del primer post

```javascript
// Simular operaciones asíncronas
function obtenerUsuario(id, callback) {
  setTimeout(() => {
    console.log('Usuario obtenido');
    callback({ id: id, nombre: 'Juan' });
  }, 1000);
}

function obtenerPosts(userId, callback) {
  setTimeout(() => {
    console.log('Posts obtenidos');
    callback([{ id: 1, titulo: 'Primer post' }]);
  }, 1000);
}

function obtenerComentarios(postId, callback) {
  setTimeout(() => {
    console.log('Comentarios obtenidos');
    callback(['Comentario 1', 'Comentario 2']);
  }, 1000);
}

// Usarlos en secuencia...
obtenerUsuario(1, (usuario) => {
  console.log('Usuario:', usuario.nombre);
  
  obtenerPosts(usuario.id, (posts) => {
    console.log('Posts:', posts.length);
    
    obtenerComentarios(posts[0].id, (comentarios) => {
      console.log('Comentarios:', comentarios.length);
    });
  });
});
```

**Problema**: Ya empieza a verse anidado y difícil de leer...

---

## El "Callback Hell" (Pirámide de la Muerte) 💀

Cuando tienes muchas operaciones asíncronas secuenciales, tu código se convierte en una **pirámide indentada**.

### Ejemplo del Mundo Real: Sistema de Login

Imagina que estás construyendo un login. Necesitas:

1. Validar el email del usuario
2. Buscar el usuario en la base de datos
3. Verificar la contraseña
4. Generar un token de sesión
5. Guardar la sesión
6. Cargar los datos del perfil
7. Redirigir al dashboard

**Cada paso tarda tiempo y depende del anterior.** Así se ve con callbacks:

```javascript
validarEmail(email, (errorValidacion, emailValido) => {
  if (errorValidacion) {
    console.log('Error: Email inválido');
    return;
  }
  
  buscarUsuario(emailValido, (errorBusqueda, usuario) => {
    if (errorBusqueda) {
      console.log('Error: Usuario no encontrado');
      return;
    }
    
    verificarPassword(usuario, password, (errorPassword, esValido) => {
      if (errorPassword || !esValido) {
        console.log('Error: Contraseña incorrecta');
        return;
      }
      
      generarToken(usuario.id, (errorToken, token) => {
        if (errorToken) {
          console.log('Error: No se pudo generar token');
          return;
        }
        
        guardarSesion(token, (errorSesion) => {
          if (errorSesion) {
            console.log('Error: No se pudo guardar sesión');
            return;
          }
          
          cargarPerfil(usuario.id, (errorPerfil, perfil) => {
            if (errorPerfil) {
              console.log('Error: No se pudo cargar perfil');
              return;
            }
            
            redirigirDashboard(perfil, (errorRedireccion) => {
              if (errorRedireccion) {
                console.log('Error: No se pudo redirigir');
                return;
              }
              
              console.log('✅ Login exitoso!');
            });
          });
        });
      });
    });
  });
});
```

### ¿Ves el Problema? 😱

**Cuenta los niveles de indentación**: 7 niveles hacia la derecha.

Ahora imagina:
- ❌ Necesitas agregar un paso más (nivel 8)
- ❌ Necesitas cambiar el orden de algo
- ❌ Hay un bug en el paso 5 y tienes que debuggearlo
- ❌ Necesitas agregar logs en cada paso
- ❌ El código tiene 200 líneas y está así de anidado

**Es una pesadilla.**

### ¿Por qué es un Problema REAL?

1. **❌ Difícil de leer**: Tu vista tiene que seguir la pirámide hacia la derecha
2. **❌ Difícil de mantener**: Agregar o quitar un paso requiere cambiar muchas líneas
3. **❌ Difícil de debuggear**: ¿Dónde está el error? ¿En qué nivel?
4. **❌ Difícil de testear**: No puedes probar "verificarPassword" sin ejecutar todo lo anterior
5. **❌ Código duplicado**: `if (error) { console.log(...); return; }` se repite 7 veces
6. **❌ No puedes reutilizar**: Cada paso está encerrado en el anterior

### Visualización del Problema

```
Código normal (ideal):        Callback Hell (realidad):

Paso 1                        Paso 1
Paso 2                          Paso 2  
  Paso 3                            Paso 3
Paso 4                                Paso 4
Paso 5                                    Paso 5
Paso 6                                        Paso 6
Paso 7                                            Paso 7
                                                      💀
```

---

## Ejemplo Real: Callback Hell

Imagina que necesitas:

1. Autenticarte con un servidor
2. Obtener datos de usuario
3. Obtener configuración del usuario
4. Obtener notificaciones
5. Renderizar todo

```javascript
autenticar('usuario', 'password', (error, token) => {
  if (error) {
    console.log('Error de autenticación:', error);
    return;
  }
  
  obtenerUsuario(token, (error, usuario) => {
    if (error) {
      console.log('Error obteniendo usuario:', error);
      return;
    }
    
    obtenerConfiguracion(usuario.id, (error, config) => {
      if (error) {
        console.log('Error obteniendo config:', error);
        return;
      }
      
      obtenerNotificaciones(usuario.id, (error, notificaciones) => {
        if (error) {
          console.log('Error obteniendo notificaciones:', error);
          return;
        }
        
        renderizar(usuario, config, notificaciones, (error) => {
          if (error) {
            console.log('Error renderizando:', error);
            return;
          }
          
          console.log('¡Todo listo!');
        });
      });
    });
  });
});
```

**Resultado**: Un código imposible de mantener 😱

---

## Visualización del Problema

### Sin Callback Hell (Ideal)
```
Paso 1
Paso 2
Paso 3
Paso 4
```

### Con Callback Hell (Realidad)
```
Paso 1
  Paso 2
    Paso 3
      Paso 4
        Paso 5
          Paso 6
            Paso 7
              ¡Ayuda!
```

---

## Intentos de Solución: Funciones Nombradas

Puedes intentar evitar la pirámide usando funciones nombradas:

```javascript
function paso3(resultado3) {
  console.log('Paso 3:', resultado3);
}

function paso2(resultado2) {
  hacerAlgo3(resultado2, paso3);
}

function paso1(resultado1) {
  hacerAlgo2(resultado1, paso2);
}

hacerAlgo1(paso1);
```

**Problema**: Aunque es menos anidado, sigue siendo difícil de seguir el flujo del código.

---

## Manejo de Errores en Callbacks

El manejo de errores es repetitivo y propenso a errores:

```javascript
function obtenerDatos(callback) {
  setTimeout(() => {
    const error = null; // o un error real
    const datos = { nombre: 'Juan' };
    
    if (error) {
      callback(error, null);
    } else {
      callback(null, datos);
    }
  }, 1000);
}

// Usar:
obtenerDatos((error, datos) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  
  console.log('Datos:', datos);
  
  // Si necesitas otra operación, anidas de nuevo...
  otraOperacion(datos, (error, resultado) => {
    if (error) {
      console.log('Error:', error);
      return;
    }
    
    // Y así sucesivamente...
  });
});
```

**Problema**: Tienes que verificar `if (error)` en cada nivel.

---

## Comparación: Callbacks vs Código Síncrono

### Código Síncrono (Fácil de leer)
```javascript
try {
  const usuario = obtenerUsuario(1);
  const posts = obtenerPosts(usuario.id);
  const comentarios = obtenerComentarios(posts[0].id);
  console.log('Listo!');
} catch (error) {
  console.log('Error:', error);
}
```

### Callbacks (Difícil de leer)
```javascript
obtenerUsuario(1, (error, usuario) => {
  if (error) return console.log(error);
  
  obtenerPosts(usuario.id, (error, posts) => {
    if (error) return console.log(error);
    
    obtenerComentarios(posts[0].id, (error, comentarios) => {
      if (error) return console.log(error);
      
      console.log('Listo!');
    });
  });
});
```

---

## ¿Cuál es la Solución?

### 🎉 Promises al Rescate (Preview del Step 4)

La comunidad de JavaScript vio este problema y en 2015 introdujo **Promises** (promesas) para solucionarlo.

**¿Qué cambia?** En lugar de pasar callbacks, las funciones **devuelven promesas** que puedes encadenar.

### Comparación: Antes vs Después

#### Antes (Callbacks - 7 niveles de indentación):
```javascript
validarEmail(email, (error, emailValido) => {
  if (error) return console.log(error);
  
  buscarUsuario(emailValido, (error, usuario) => {
    if (error) return console.log(error);
    
    verificarPassword(usuario, password, (error, esValido) => {
      if (error) return console.log(error);
      
      generarToken(usuario.id, (error, token) => {
        // ... y sigue y sigue y sigue
      });
    });
  });
});
```

#### Después (Promises - flujo lineal):
```javascript
validarEmail(email)
  .then(emailValido => buscarUsuario(emailValido))
  .then(usuario => verificarPassword(usuario, password))
  .then(esValido => generarToken(usuario.id))
  .then(token => guardarSesion(token))
  .then(() => cargarPerfil(usuario.id))
  .then(perfil => redirigirDashboard(perfil))
  .then(() => {
    console.log('✅ Login exitoso!');
  })
  .catch(error => {
    // UN SOLO lugar para manejar TODOS los errores
    console.log('❌ Error:', error.message);
  });
```

### ¿Ves la Diferencia? 🤯

**Con Promises**:
- ✅ **Sin pirámide**: Todo es lineal (hacia abajo, no hacia la derecha)
- ✅ **Un solo `.catch()`**: Maneja TODOS los errores en un lugar
- ✅ **Más legible**: Lees de arriba hacia abajo como un libro
- ✅ **Fácil de modificar**: Agregar un paso = agregar una línea `.then()`
- ✅ **Reutilizable**: Cada función devuelve una Promise que puedes usar donde quieras

### El Concepto Clave

En lugar de:
```javascript
funcion(parametros, callback)  // Paso el callback
```

Ahora:
```javascript
funcion(parametros)           // Devuelve una Promise
  .then(resultado => ...)     // Hago algo con el resultado
```

**En Step 4 aprenderás exactamente qué es una Promise y cómo funciona.** Por ahora, solo necesitas entender que **solucionan el Callback Hell**.

---

## Puntos Clave ✨

1. **Callback**: Función que se ejecuta después de otra operación
2. **Callback Hell**: Pirámide de callbacks anidados
3. **Problemas**: Difícil de leer, mantener, debuggear y testear
4. **Solución**: Promises (Step 4) y async/await (Step 5)
5. **Manejo de errores**: Repetitivo en cada nivel con callbacks

---

## Tu Ejercicio 🎯

Analiza este código y cuenta cuántos niveles de anidación tiene:

```javascript
operacion1((resultado1) => {
  operacion2(resultado1, (resultado2) => {
    operacion3(resultado2, (resultado3) => {
      operacion4(resultado3, (resultado4) => {
        console.log('Final:', resultado4);
      });
    });
  });
});
```

**Respuesta**: 4 niveles de anidación

**Pregunta**: ¿Cómo manejarías errores en cada operación? (Spoiler: tedioso)

---

## Próximos Pasos

Ahora que entiendes el problema del Callback Hell:

✅ Qué son los callbacks  
✅ Por qué los callbacks anidados son problemáticos  
✅ Dificultades de mantenimiento y manejo de errores  

Estarás listo para:
- **Step 4**: Promises - La solución al Callback Hell
- **Step 5**: Async/Await - Sintaxis más limpia sobre Promises

---

**💡 Consejo**: El Callback Hell fue un problema real en JavaScript antiguo. Por eso se crearon las Promises. Entender el problema te ayudará a apreciar la solución.

**🎯 Regla**: Si ves más de 2-3 niveles de callbacks anidados, probablemente necesitas Promises o async/await.

**📖 Historia**: Antes del 2015 (ES6), todos teníamos que lidiar con Callback Hell. Las Promises cambiaron todo.
