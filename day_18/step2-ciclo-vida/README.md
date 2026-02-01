# Step 2: Ciclo de Vida del Componente 🔄

## ¿Qué es el Ciclo de Vida?

El ciclo de vida es el conjunto de fases por las que pasa un componente React desde que se crea hasta que se destruye.

## Las 3 Fases del Ciclo de Vida

### 1️⃣ Montaje (Mounting) 🚀
El componente se crea y aparece en la pantalla

**Eventos que ocurren**:
- El componente se renderiza por primera vez
- Los datos iniciales se cargan
- Se pueden hacer suscripciones (listeners, API calls, etc.)

**useEffect equivalente**:
```javascript
useEffect(() => {
  console.log('Componente montado!');
}, []); // Array vacío = solo al montar
```

---

### 2️⃣ Actualización (Updating) 🔄
El componente detecta cambios y se actualiza

**Eventos que ocurren**:
- El estado cambia
- Los props cambian
- El componente se re-renderiza
- Se pueden hacer actualizaciones basadas en cambios

**useEffect equivalente**:
```javascript
useEffect(() => {
  console.log('El componente se actualizó!');
}, [dependencia]); // Con dependencias
```

---

### 3️⃣ Desmontaje (Unmounting) 🗑️
El componente desaparece de la pantalla

**Eventos que ocurren**:
- El componente se elimina de la pantalla
- Se limpian recursos (listeners, intervals, etc.)
- Se cierra la conexión a APIs

**useEffect equivalente**:
```javascript
useEffect(() => {
  return () => {
    console.log('Componente desmontado!');
    // Aquí limpias recursos
  };
}, []);
```

---

## Ejemplos Concretos del Ciclo de Vida

### Ejemplo 1: Las 3 fases en un componente

**Archivo**: `Ejemplo1-TresFases.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo1TresFases() {
  const [contador, setContador] = useState(0);

  // FASE 1: MONTAJE
  useEffect(() => {
    console.log('📍 MONTAJE - Componente creado');
    console.log('El componente aparece por primera vez en la pantalla');
  }, []);

  // FASE 2: ACTUALIZACIÓN
  useEffect(() => {
    console.log(`📍 ACTUALIZACIÓN - Contador ahora es: ${contador}`);
    console.log('El componente se actualizó porque el estado cambió');
  }, [contador]);

  // FASE 3: DESMONTAJE
  useEffect(() => {
    return () => {
      console.log('📍 DESMONTAJE - Componente eliminado');
      console.log('El componente desaparece de la pantalla');
    };
  }, []);

  return (
    <div>
      <h2>Contador: {contador}</h2>
      <button onClick={() => setContador(contador + 1)}>
        Incrementar
      </button>
      <p>Abre la consola para ver las fases</p>
    </div>
  );
}

export default Ejemplo1TresFases;
```

**Cómo probar**:
1. Abre la consola (F12)
2. El componente se monta → ves "MONTAJE"
3. Haz click → ves "ACTUALIZACIÓN"
4. Cambia a otra página o recarga → ves "DESMONTAJE"

---

### Ejemplo 2: Cargar datos en el montaje

**Archivo**: `Ejemplo2-CargarDatos.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo2CargarDatos() {
  const [usuarios, setUsuarios] = useState([]);
  const [cargando, setCargando] = useState(true);

  // Se ejecuta solo en MONTAJE
  useEffect(() => {
    console.log('Cargando datos...');
    
    // Simular obtener datos de una API
    setTimeout(() => {
      const datosSimulados = [
        { id: 1, nombre: 'Juan' },
        { id: 2, nombre: 'María' },
        { id: 3, nombre: 'Carlos' }
      ];
      
      setUsuarios(datosSimulados);
      setCargando(false);
      console.log('✅ Datos cargados');
    }, 2000); // Esperar 2 segundos
  }, []); // Solo al montar

  if (cargando) {
    return <p>⏳ Cargando usuarios...</p>;
  }

  return (
    <div>
      <h2>Usuarios:</h2>
      <ul>
        {usuarios.map(user => (
          <li key={user.id}>{user.nombre}</li>
        ))}
      </ul>
    </div>
  );
}

export default Ejemplo2CargarDatos;
```

**Fase**: MONTAJE  
**Uso**: Cargar datos iniciales cuando el componente aparece

---

### Ejemplo 3: Limpiar en desmontaje

**Archivo**: `Ejemplo3-Limpiar.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo3Limpiar() {
  const [escuchando, setEscuchando] = useState(false);

  useEffect(() => {
    if (!escuchando) return;

    console.log('📡 Listener activado');
    
    const handleClick = () => {
      console.log('El usuario hizo click en la ventana');
    };

    // MONTAJE: Añadir listener
    window.addEventListener('click', handleClick);

    // DESMONTAJE: Remover listener
    return () => {
      console.log('🗑️ Listener removido');
      window.removeEventListener('click', handleClick);
    };
  }, [escuchando]);

  return (
    <div>
      <button onClick={() => setEscuchando(!escuchando)}>
        {escuchando ? 'Dejar de escuchar' : 'Escuchar clicks'}
      </button>
      {escuchando && <p>Haz click en la pantalla</p>}
    </div>
  );
}

export default Ejemplo3Limpiar;
```

**Fases**: MONTAJE y DESMONTAJE  
**Uso**: Añadir listener en montaje, remover en desmontaje para evitar memory leaks

---

### Ejemplo 4: Responder a cambios

**Archivo**: `Ejemplo4-ResponderCambios.jsx`

```javascript
import { useState, useEffect } from 'react';

function Ejemplo4ResponderCambios() {
  const [tema, setTema] = useState('claro');
  const [ancho, setAncho] = useState(window.innerWidth);

  // Responde a cambios en el tema
  useEffect(() => {
    console.log(`Tema cambió a: ${tema}`);
    document.body.style.backgroundColor = tema === 'claro' ? 'white' : 'black';
    document.body.style.color = tema === 'claro' ? 'black' : 'white';
  }, [tema]); // Se ejecuta cuando tema cambia

  // Responde a cambios de tamaño de ventana
  useEffect(() => {
    const handleResize = () => {
      setAncho(window.innerWidth);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // Solo se monta/desmonta

  return (
    <div>
      <button onClick={() => setTema(tema === 'claro' ? 'oscuro' : 'claro')}>
        Cambiar a {tema === 'claro' ? 'oscuro' : 'claro'}
      </button>
      <p>Ancho de ventana: {ancho}px</p>
      <p>Tema: {tema}</p>
    </div>
  );
}

export default Ejemplo4ResponderCambios;
```

**Fases**: MONTAJE y ACTUALIZACIÓN  
**Uso**: Hacer acciones cuando el usuario cambia algo

---

## Diagrama del Ciclo de Vida

```
┌─────────────────────────────────────────────────┐
│                    CICLO DE VIDA                │
└─────────────────────────────────────────────────┘

         ┌──────────────────┐
         │  1️⃣ MONTAJE     │
         │  (Primer render) │
         └────────┬─────────┘
                  ↓
    ┌─────────────────────────────────┐
    │  Componente aparece en pantalla  │
    │  - Cargar datos iniciales        │
    │  - Activar listeners             │
    │  - Inicializar variables         │
    └────────────┬────────────────────┘
                 ↓
         ┌──────────────────┐
         │  2️⃣ ACTUALIZACIÓN│
         │  (Re-renders)    │
         └────────┬─────────┘
                  ↓
    ┌─────────────────────────────────┐
    │  Componente se actualiza         │
    │  - Estado cambia                 │
    │  - Props cambian                 │
    │  - Se ejecuta el efecto          │
    └────────────┬────────────────────┘
                 ↓ (cuando desaparece)
         ┌──────────────────┐
         │  3️⃣ DESMONTAJE   │
         │  (Último render)  │
         └────────┬─────────┘
                  ↓
    ┌─────────────────────────────────┐
    │  Componente desaparece          │
    │  - Limpiar listeners            │
    │  - Cerrar conexiones API        │
    │  - Cancelar timers              │
    └─────────────────────────────────┘
```

---

## Tabla Resumen: useEffect en cada fase

| Fase | código | Cuándo | Uso |
|------|--------|--------|-----|
| **MONTAJE** | `useEffect(() => {...}, [])` | Una sola vez al cargar | Cargar datos, activar listeners |
| **ACTUALIZACIÓN** | `useEffect(() => {...}, [var])` | Cuando var cambia | Responder a cambios |
| **DESMONTAJE** | `return () => {...}` dentro de useEffect | Al desaparecer | Limpiar recursos |

---

## Puntos Clave ✨

1. **Montaje**: El componente nace (aparece en pantalla)
2. **Actualización**: El componente cambia (estado o props)
3. **Desmontaje**: El componente muere (desaparece)
4. **Cleanup es crítico**: Evita memory leaks y errores
5. **useEffect maneja todo**: Reemplaza los lifecycle methods de classes

---

## Errores Comunes ⚠️

### Error 1: Olvidar cleanup
```javascript
// ❌ MALO - Sin cleanup
useEffect(() => {
  window.addEventListener('scroll', handler);
  // ¿Y si el componente se desmonta?
}, []);

// ✅ BIEN - Con cleanup
useEffect(() => {
  window.addEventListener('scroll', handler);
  return () => {
    window.removeEventListener('scroll', handler);
  };
}, []);
```

### Error 2: Loop infinito en actualización
```javascript
// ❌ MALO
const [count, setCount] = useState(0);
useEffect(() => {
  setCount(count + 1); // Sin dependencias = loop infinito
});

// ✅ BIEN
useEffect(() => {
  console.log(count);
}, [count]);
```

### Error 3: Perder referencia en cleanup
```javascript
// ❌ MALO - No tiene acceso a la variable
useEffect(() => {
  const timer = setTimeout(() => {}, 1000);
  // ... código ...
}, []);

// ✅ BIEN - Guarda la referencia
useEffect(() => {
  const timer = setTimeout(() => {}, 1000);
  return () => {
    clearTimeout(timer);
  };
}, []);
```

---

## Tu Ejercicio 🎯

Crea un archivo `MiEjercicio.jsx` que implemente las 3 fases:

**Requisitos**:
1. ✅ En **MONTAJE**: Imprime "Componente cargado" en consola
2. ✅ En **ACTUALIZACIÓN**: Cuando cambies un input, imprime el valor
3. ✅ En **DESMONTAJE**: Imprime "Limpiando recursos"
4. ✅ Usa un `input` controlado para que veas la actualización

**Pista**:
- Necesitarás un `useState` para el input
- Necesitarás múltiples `useEffect` (uno por cada fase)
- ¿Cuál es el array de dependencias para cada uno?

---

## Próximos Pasos

Una vez entiendas:

✅ Las 3 fases del ciclo de vida  
✅ Cuándo ocurre cada una  
✅ Cómo limpiar en el desmontaje  

Estarás listo para:
- **Step 3**: Combinar useState + useEffect en aplicaciones reales
- **Step 4**: Crear formularios

---

## Recursos

- [React Lifecycle](https://react.dev/learn/lifecycle-of-reactive-effects)
- [useEffect en React](https://react.dev/reference/react/useEffect)

---

**💡 Consejo**: Visualiza el ciclo de vida. Imagina el componente como una persona: nace (montaje), vive (actualización), muere (desmontaje).
