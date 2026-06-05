🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# Introducción a JavaScript - Día 7

Módulo de aprendizaje incremental sobre los fundamentos de JavaScript para principiantes.

## 📚 Estructura del Módulo

Este módulo está organizado en **5 pasos progresivos**, cada uno enfocado en conceptos específicos de JavaScript:

### Paso 1: Variables y Tipos de Datos
- Declaración de variables (`const`, `let`, `var`)
- Tipos de datos primitivos (String, Number, Boolean)
- Arrays y Objetos básicos
- Operaciones matemáticas y concatenación

### Paso 2: Funciones
- Declaración de funciones
- Funciones con parámetros
- Funciones que retornan valores
- Function scope (alcance)
- Funciones anónimas
- Arrow functions
- Funciones anidadas

### Paso 3: Condicionales
- Estructuras `if/else`
- Operadores de comparación (`===`, `!==`, `>`, `<`)
- Operadores lógicos (`&&`, `||`, `!`)
- Switch statement
- Operador ternario
- Renderizado condicional

### Paso 4: Bucles
- Bucle `for`
- Bucle `while`
- `for...of` (para arrays)
- `for...in` (para objetos)
- `break` y `continue`
- Bucles anidados

### Paso 5: Proyecto Final - Calculadora Interactiva
Proyecto integrador que combina **todos los conceptos aprendidos**:
- Variables globales y locales
- Funciones con diferentes propósitos
- Condicionales para validación
- Switch para operaciones matemáticas
- Arrays para historial
- Bucles para renderizado
- Manipulación del DOM

### Paso 6: Integración HTML + JavaScript
Cómo HTML, CSS y JavaScript trabajan juntos:
- Orden de procesamiento del navegador
- Estrategias de carga: `defer`, `async`, `type="module"`
- Manipulación del DOM en tiempo real
- Eventos y asociación de funciones
- Demos interactivas de todos los conceptos

## 🚀 Cómo Usar Este Módulo

### 1. Iniciar el Servidor

```bash
# Asegúrate de tener Flask instalado
pip3 install flask

# Inicia el servidor
python3 server.py
```

El servidor estará disponible en `http://localhost:3000`

### 2. Navegar por los Ejercicios

1. Abre tu navegador en `http://localhost:3000`
2. Verás una página de inicio con enlaces a los 5 pasos
3. Haz clic en cada paso para ir al ejercicio correspondiente
4. **Importante**: Abre la consola del navegador (F12) para ver los resultados

### 3. Completar los Ejercicios

Cada archivo HTML contiene:
- **Ejemplos demostrativos**: Código que se ejecuta automáticamente
- **Ejercicios prácticos**: Secciones marcadas con `// TODO:` que debes completar
- **Retos extra**: Ejercicios más avanzados para practicar

## 📖 Metodología de Aprendizaje

### Enfoque Incremental
Cada paso construye sobre el conocimiento del paso anterior:
- **Paso 1** → Variables (la base)
- **Paso 2** → Funciones (reutilizar código)
- **Paso 3** → Condicionales (tomar decisiones)
- **Paso 4** → Bucles (repetir tareas)
- **Paso 5** → Proyecto (aplicar todo)

### Aprender Haciendo
1. **Lee** el código de ejemplo
2. **Observa** los resultados en la consola
3. **Modifica** los valores para experimentar
4. **Completa** los ejercicios TODO
5. **Rompe** el código intencionalmente y aprende de los errores

## 💡 Tips para Estudiantes

### Usando la Consola del Navegador
```javascript
// La consola es tu mejor amiga
console.log("Hola Mundo");

// Usa console.log para debuggear
const numero = 42;
console.log("El número es:", numero);
```

### Errores Comunes
1. **Olvidar los paréntesis al llamar funciones**
   ```javascript
   saludar    // ❌ No llama la función
   saludar()  // ✅ Correcto
   ```

2. **Usar `==` en lugar de `===`**
   ```javascript
   5 == "5"   // ❌ Evita esto
   5 === "5"  // ✅ Usa esto
   ```

3. **Confundir el scope de las variables**
   ```javascript
   if (true) {
     let x = 5;
   }
   console.log(x);  // ❌ Error: x no está definida
   ```

### Experimentación
- Cambia valores y observa qué sucede
- Comenta y descomenta líneas de código
- Añade tus propios `console.log()` para entender el flujo
- No tengas miedo de romper el código - **aprenderás más de los errores**

## 🎯 Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:
- ✅ Declarar y usar variables correctamente
- ✅ Crear funciones reutilizables
- ✅ Implementar lógica condicional
- ✅ Iterar sobre arrays y objetos
- ✅ Combinar todos los conceptos en un proyecto funcional
- ✅ Debuggear código usando la consola

## 📝 Recursos Adicionales

### Documentación Oficial
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript)
- [JavaScript.info](https://javascript.info/)

### Práctica Adicional
- [FreeCodeCamp - JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- [Exercism - JavaScript Track](https://exercism.org/tracks/javascript)

### Conceptos del Tutorial Principal
Para más detalles teóricos, consulta el archivo `../index.md` en la carpeta `day_07`.

## 🔧 Solución de Problemas

### El servidor no inicia
```bash
# Verifica que Flask esté instalado
pip3 install flask

# Si usas Python 2
pip install flask
```

### La página no carga
- Asegúrate de estar en la carpeta correcta: `day_07/javascript-intro`
- Verifica que el puerto 3000 no esté en uso
- Revisa la consola del servidor para ver errores

### Los cambios no se reflejan
- Recarga la página con `Ctrl + Shift + R` (fuerza recarga sin caché)
- El servidor deshabilita el caché automáticamente

## 🎓 Para el Instructor

### Orden Recomendado de Enseñanza
1. Demostrar cada paso en vivo
2. Explicar los conceptos con ejemplos visuales
3. Dejar tiempo para que los estudiantes experimenten
4. Resolver dudas específicas
5. Revisar las soluciones de los ejercicios en grupo

### Tiempo Estimado
- Paso 1: 30 minutos
- Paso 2: 45 minutos
- Paso 3: 45 minutos
- Paso 4: 45 minutos
- Paso 5: 60 minutos (proyecto)
- **Total**: ~3.5 horas

### Conceptos Clave a Enfatizar
- **const vs let**: Siempre usar `const` por defecto
- **=== vs ==**: Siempre usar estricto
- **Scope**: Diferencia entre global y local
- **Funciones**: La importancia de reutilizar código
- **Debugging**: Usar `console.log()` constantemente

---

**¿Preguntas?** Consulta el archivo principal `day_07/index.md` o pregunta en clase.

¡Feliz programación! 💻🚀
