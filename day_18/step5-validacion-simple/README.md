# Step 5: Validación Simple ✅

## ¿Qué es Validación?

Validación es verificar que los datos que el usuario envía sean correctos **antes** de usarlos.

```javascript
// Ejemplos de validación
- ¿El email tiene @?
- ¿La contraseña tiene al menos 8 caracteres?
- ¿El nombre no está vacío?
- ¿La edad es un número positivo?
```

## Validación en Tiempo Real vs Al Enviar

### Tiempo Real
- Se valida mientras escribes
- Muestra errores inmediatamente
- Mejor UX

### Al Enviar
- Se valida cuando haces click "Enviar"
- Más simple de implementar
- Retroalimentación menos inmediata

---

## Ejemplo 1: Validación Simple de Email

**Archivo**: `Ejemplo1-EmailValidacion.jsx`

```javascript
import { useState } from 'react';

function Ejemplo1EmailValidacion() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const validarEmail = (value) => {
    // Validación simple: contiene @ y .
    if (value === '') {
      setError('El email es requerido');
      return false;
    }

    if (!value.includes('@')) {
      setError('El email debe contener @');
      return false;
    }

    if (!value.includes('.')) {
      setError('El email debe contener un punto');
      return false;
    }

    // Validación más completa con regex
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regex.test(value)) {
      setError('Formato de email inválido');
      return false;
    }

    setError('');
    return true;
  };

  const handleChange = (e) => {
    const value = e.target.value;
    setEmail(value);
    validarEmail(value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validarEmail(email)) {
      console.log('✅ Email válido:', email);
      setEmail('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={email}
        onChange={handleChange}
        placeholder="tu@email.com"
        style={{
          borderColor: error ? 'red' : email && !error ? 'green' : 'gray'
        }}
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {email && !error && <p style={{ color: 'green' }}>✅ Email válido</p>}
      <button type="submit" disabled={!email || error !== ''}>
        Enviar
      </button>
    </form>
  );
}

export default Ejemplo1EmailValidacion;
```

---

## Ejemplo 2: Validación de Contraseña

**Archivo**: `Ejemplo2-PasswordValidacion.jsx`

```javascript
import { useState } from 'react';

function Ejemplo2PasswordValidacion() {
  const [password, setPassword] = useState('');
  const [errores, setErrores] = useState([]);

  const validarPassword = (value) => {
    const nuevosErrores = [];

    if (value.length === 0) {
      nuevosErrores.push('La contraseña es requerida');
    } else {
      if (value.length < 8) {
        nuevosErrores.push('Mínimo 8 caracteres');
      }
      if (!/[A-Z]/.test(value)) {
        nuevosErrores.push('Debe contener una mayúscula');
      }
      if (!/[0-9]/.test(value)) {
        nuevosErrores.push('Debe contener un número');
      }
      if (!/[!@#$%^&*]/.test(value)) {
        nuevosErrores.push('Debe contener un carácter especial (!@#$%^&*)');
      }
    }

    setErrores(nuevosErrores);
    return nuevosErrores.length === 0;
  };

  const handleChange = (e) => {
    const value = e.target.value;
    setPassword(value);
    validarPassword(value);
  };

  return (
    <div>
      <input
        type="password"
        value={password}
        onChange={handleChange}
        placeholder="Contraseña fuerte"
      />

      {errores.length > 0 && (
        <div style={{ color: 'red' }}>
          <h4>Requisitos:</h4>
          <ul>
            {errores.map((error, i) => (
              <li key={i}>{error}</li>
            ))}
          </ul>
        </div>
      )}

      {password && errores.length === 0 && (
        <p style={{ color: 'green' }}>✅ Contraseña válida</p>
      )}

      <p>Fuerza: {password.length > 0 ? `${errores.length === 0 ? 'Fuerte' : 'Débil'}` : 'N/A'}</p>
    </div>
  );
}

export default Ejemplo2PasswordValidacion;
```

---

## Ejemplo 3: Formulario con Múltiples Validaciones

**Archivo**: `Ejemplo3-FormularioCompleto.jsx`

```javascript
import { useState } from 'react';

function Ejemplo3FormularioCompleto() {
  const [form, setForm] = useState({
    nombre: '',
    edad: '',
    telefono: ''
  });

  const [errores, setErrores] = useState({});

  const validar = (datos) => {
    const nuevosErrores = {};

    // Validar nombre
    if (datos.nombre.trim() === '') {
      nuevosErrores.nombre = 'El nombre es requerido';
    } else if (datos.nombre.length < 3) {
      nuevosErrores.nombre = 'El nombre debe tener al menos 3 caracteres';
    }

    // Validar edad
    if (datos.edad === '') {
      nuevosErrores.edad = 'La edad es requerida';
    } else if (isNaN(datos.edad)) {
      nuevosErrores.edad = 'La edad debe ser un número';
    } else if (datos.edad < 18 || datos.edad > 120) {
      nuevosErrores.edad = 'La edad debe estar entre 18 y 120';
    }

    // Validar teléfono
    if (datos.telefono.trim() === '') {
      nuevosErrores.telefono = 'El teléfono es requerido';
    } else if (!/^\d{9,}$/.test(datos.telefono.replace(/\D/g, ''))) {
      nuevosErrores.telefono = 'El teléfono debe tener al menos 9 dígitos';
    }

    return nuevosErrores;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    const nuevoForm = { ...form, [name]: value };
    setForm(nuevoForm);
    
    // Validar en tiempo real
    const nuevosErrores = validar(nuevoForm);
    setErrores(nuevosErrores);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const nuevosErrores = validar(form);
    setErrores(nuevosErrores);

    if (Object.keys(nuevosErrores).length === 0) {
      console.log('✅ Formulario válido:', form);
      setForm({ nombre: '', edad: '', telefono: '' });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Nombre:</label>
        <input
          type="text"
          name="nombre"
          value={form.nombre}
          onChange={handleChange}
          style={{ borderColor: errores.nombre ? 'red' : 'green' }}
        />
        {errores.nombre && <p style={{ color: 'red' }}>{errores.nombre}</p>}
      </div>

      <div>
        <label>Edad:</label>
        <input
          type="number"
          name="edad"
          value={form.edad}
          onChange={handleChange}
          style={{ borderColor: errores.edad ? 'red' : form.edad ? 'green' : 'gray' }}
        />
        {errores.edad && <p style={{ color: 'red' }}>{errores.edad}</p>}
      </div>

      <div>
        <label>Teléfono:</label>
        <input
          type="text"
          name="telefono"
          value={form.telefono}
          onChange={handleChange}
          placeholder="123456789"
          style={{ borderColor: errores.telefono ? 'red' : form.telefono ? 'green' : 'gray' }}
        />
        {errores.telefono && <p style={{ color: 'red' }}>{errores.telefono}</p>}
      </div>

      <button 
        type="submit" 
        disabled={Object.keys(errores).length > 0 || !form.nombre || !form.edad || !form.telefono}
      >
        {Object.keys(errores).length > 0 ? 'Corrige los errores' : 'Enviar'}
      </button>
    </form>
  );
}

export default Ejemplo3FormularioCompleto;
```

---

## Técnicas de Validación Comunes

### 1. Regex (Expresiones Regulares)
```javascript
// Email
/^[^\s@]+@[^\s@]+\.[^\s@]+$/

// Teléfono (10 dígitos)
/^\d{10}$/

// Solo letras
/^[a-zA-Z]+$/

// Alfanumérico
/^[a-zA-Z0-9]+$/
```

### 2. Métodos de String
```javascript
value.trim() === '' // Está vacío
value.length >= 8 // Longitud mínima
value.includes('@') // Contiene caracter
```

### 3. Métodos de Number
```javascript
isNaN(value) // No es número
value >= 0 // Rango
```

---

## Puntos Clave ✨

1. **Validación en tiempo real**: Mejor UX
2. **Validar al enviar**: Captura todos los errores a la vez
3. **Mostrar errores claros**: Ayuda al usuario
4. **Deshabilitar envío**: Si hay errores
5. **Limpiar después de enviar**: Reset el formulario

---

## Tu Ejercicio 🎯

Crea un `MiEjercicio.jsx` que sea un formulario de registro con:

1. ✅ Username (3-20 caracteres, sin espacios)
2. ✅ Email (validación de formato)
3. ✅ Edad (18-99)
4. ✅ Teléfono (solo números)
5. ✅ Mostrar errores en rojo
6. ✅ Bordes verdes si es válido
7. ✅ Botón deshabilitado si hay errores

---

## Próximos Pasos

Una vez domines validación manual:

✅ Entiendes regex  
✅ Sabes validar antes de enviar  
✅ Creas mensajes de error claros  

Estarás listo para:
- **Step 6**: React Hook Form (validación automática)

---

**💡 Consejo**: La validación del lado del cliente es para UX. **Siempre valida también en el servidor** por seguridad.
