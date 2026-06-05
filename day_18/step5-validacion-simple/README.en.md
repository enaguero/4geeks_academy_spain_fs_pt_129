[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 5: Simple Validation ✅

## What is Validation?

Validation is verifying that the data the user submits is correct **before** using it.

```javascript
// Validation examples
- Does the email contain @?
- Does the password have at least 8 characters?
- Is the name not empty?
- Is the age a positive number?
```

## Real-Time Validation vs On Submit

### Real-Time
- Validates as you type
- Shows errors immediately
- Better UX

### On Submit
- Validates when you click "Enviar"
- Simpler to implement
- Less immediate feedback

---

## Example 1: Simple Email Validation

**File**: `Ejemplo1-EmailValidacion.jsx`

```javascript
import { useState } from 'react';

function Ejemplo1EmailValidacion() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const validarEmail = (value) => {
    // Simple validation: contains @ and .
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

    // Stricter validation with regex
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

## Example 2: Password Validation

**File**: `Ejemplo2-PasswordValidacion.jsx`

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

## Example 3: Form with Multiple Validations

**File**: `Ejemplo3-FormularioCompleto.jsx`

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

    // Validate name
    if (datos.nombre.trim() === '') {
      nuevosErrores.nombre = 'El nombre es requerido';
    } else if (datos.nombre.length < 3) {
      nuevosErrores.nombre = 'El nombre debe tener al menos 3 caracteres';
    }

    // Validate age
    if (datos.edad === '') {
      nuevosErrores.edad = 'La edad es requerida';
    } else if (isNaN(datos.edad)) {
      nuevosErrores.edad = 'La edad debe ser un número';
    } else if (datos.edad < 18 || datos.edad > 120) {
      nuevosErrores.edad = 'La edad debe estar entre 18 y 120';
    }

    // Validate phone
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
    
    // Real-time validation
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

## Common Validation Techniques

### 1. Regex (Regular Expressions)
```javascript
// Email
/^[^\s@]+@[^\s@]+\.[^\s@]+$/

// Phone (10 digits)
/^\d{10}$/

// Letters only
/^[a-zA-Z]+$/

// Alphanumeric
/^[a-zA-Z0-9]+$/
```

### 2. String methods
```javascript
value.trim() === '' // Is empty
value.length >= 8 // Minimum length
value.includes('@') // Contains character
```

### 3. Number methods
```javascript
isNaN(value) // Not a number
value >= 0 // Range
```

---

## Key Points ✨

1. **Real-time validation**: Better UX
2. **Validate on submit**: Catches all errors at once
3. **Show clear errors**: Help the user
4. **Disable submit**: When there are errors
5. **Clear after submit**: Reset the form

---

## Your Exercise 🎯

Create a `MiEjercicio.jsx` that is a signup form with:

1. ✅ Username (3-20 characters, no spaces)
2. ✅ Email (format validation)
3. ✅ Age (18-99)
4. ✅ Phone (numbers only)
5. ✅ Show errors in red
6. ✅ Green borders if valid
7. ✅ Disabled button when there are errors

---

## Next Steps

Once you master manual validation:

✅ You understand regex  
✅ You can validate before submitting  
✅ You create clear error messages  

You'll be ready for:
- **Step 6**: React Hook Form (automatic validation)

---

**💡 Tip**: Client-side validation is for UX. **Always validate on the server too** for security.
