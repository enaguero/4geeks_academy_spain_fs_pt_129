🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 📋 Día 18: TodoList Application usando React

## 🎯 Objetivos de Aprendizaje

Este día te enseñará a construir una aplicación de lista de tareas completa en React, aprendiendo conceptos clave como:

- **useEffect Hook**: Entender el ciclo de vida de componentes funcionales
- **Ciclo de Vida**: Cómo y cuándo se ejecuta el código en diferentes momentos
- **Combinación de Hooks**: Usar useState + useEffect juntos
- **Formularios en React**: Crear y manejar inputs controlados
- **Validación de Inputs**: Validar datos del usuario de forma natural
- **React Hook Form**: Usar bibliotecas profesionales para formularios complejos
- **Event & event.target**: Entender eventos en formularios

## 📚 Estructura del Día

Este día está organizado en 6 pasos incrementales, cada uno construyendo sobre el anterior:

### Step 1: useEffect Básico ⚙️
**Archivo**: `step1-useeffect-basico/`

Aprenderás qué es useEffect, cuándo se ejecuta y cómo usarlo.

**Conceptos**:
- Qué es useEffect
- El array de dependencias
- Limpiar efectos (cleanup)

---

### Step 2: Ciclo de Vida del Componente 🔄
**Archivo**: `step2-ciclo-vida/`

Entenderás cuándo se ejecuta el código durante la vida de un componente.

**Conceptos**:
- Montaje (mounting)
- Actualización (updating)
- Desmontaje (unmounting)

---

### Step 3: useState + useEffect 🔗
**Archivo**: `step3-usestate-useeffect/`

Combinarás ambos hooks para actualizar la UI automáticamente.

**Conceptos**:
- Sincronizar estado con efectos
- Evitar loops infinitos
- Re-renderizado y efectos

---

### Step 4: Formularios Básicos 📝
**Archivo**: `step4-forms-basico/`

Crearas tu primer formulario en React con inputs controlados.

**Conceptos**:
- Inputs controlados (controlled inputs)
- event.target.value
- onChange handlers
- Dos vías de vinculación de datos (two-way binding)

---

### Step 5: Validación Simple ✅
**Archivo**: `step5-validacion-simple/`

Añadirás validación manual de inputs sin librerías externas.

**Conceptos**:
- Validar inputs en tiempo real
- Mostrar mensajes de error
- Prevenir envío de formularios inválidos

---

### Step 6: React Hook Form 🚀
**Archivo**: `step6-react-hook-form/`

Usarás una librería profesional para formularios complejos.

**Conceptos**:
- Cómo funciona React Hook Form
- Registrar inputs
- Validación automática
- Manejo de errores

---

## 🚀 Cómo Usar Este Material

### 1. Seguir en orden
Cada paso depende del anterior. No saltes pasos.

### 2. Experimentar
Modifica el código, prueba cosas nuevas, rompe intencionalmente y arregla.

### 3. Practicar
Cada paso tiene ejercicios prácticos. ¡Hazlos!

### 4. Entender, no memorizar
Busca entender *por qué* funciona así, no solo *cómo*.

## 📖 Lectura Recomendada

### De 4Geeks Academy
- [Controlled vs Uncontrolled Inputs in React](https://4geeks.com/lesson/controlled-vs-uncontrolled-inputs-react-js)

### React Oficial
- [useEffect Hook - React Docs](https://react.dev/reference/react/useEffect)
- [useState Hook - React Docs](https://react.dev/reference/react/useState)

### React Hook Form
- [Documentación oficial](https://react-hook-form.com/)

## 🎓 Proyecto Final

**TodoList Application**

Al finalizar este día, crearás una aplicación completa de tareas con:

✅ Agregar tareas  
✅ Marcar tareas como completadas  
✅ Eliminar tareas  
✅ Validación de inputs  
✅ Almacenamiento local (localStorage)  
✅ Interfaz responsiva  

## 💡 Consejos Importantes

### Para Principiantes

1. **Lee todo primero**: Antes de escribir código, lee los tutoriales
2. **Copia y entiende**: No solo copies el código, entiende cada línea
3. **Escribe a mano**: Si es posible, escribe el código en lugar de copiar/pegar
4. **Experimenta**: Cambia valores, añade console.logs, prueba cosas

### Conceptos Clave

- **Renderizado**: React dibuja la UI en función del estado
- **Estado (State)**: Datos que cambian en el componente
- **Efectos (Effects)**: Código que se ejecuta en ciertos momentos
- **Validación**: Asegurar que los datos son correctos antes de usarlos

## ⚠️ Errores Comunes

### Error: "React Hook 'useState' is called in a loop"
**Causa**: Llamando hooks condicionalmente  
**Solución**: Los hooks siempre deben estar en la raíz del componente

### Error: "setState during render"
**Causa**: Llamar setState directamente en el componente  
**Solución**: Usa useEffect para los efectos secundarios

### Error: "Too many re-renders"
**Causa**: Efecto que causa estado infinito  
**Solución**: Añade dependencias correctas al array de dependencias

## 🆘 Necesitas Ayuda?

1. Lee el tutorial paso a paso
2. Busca el concepto en Google
3. Pregunta en el canal de Slack oficial
4. Revisa la sección "Errores Comunes"

## 📊 Progreso

Marca cada paso cuando lo completes:

- [ ] Step 1: useEffect Básico
- [ ] Step 2: Ciclo de Vida
- [ ] Step 3: useState + useEffect
- [ ] Step 4: Formularios Básicos
- [ ] Step 5: Validación Simple
- [ ] Step 6: React Hook Form
- [ ] Proyecto Final: TodoList

---

**¡Vamos a construir! 💪**

Recuerda: cada desarrollador profesional pasó por esto. Tómate tu tiempo, practica mucho y diviértete aprendiendo.
