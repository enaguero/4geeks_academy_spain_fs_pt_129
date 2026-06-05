[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 6: React Hook Form 🚀

## What is React Hook Form?

React Hook Form is a library that simplifies creating and validating forms in React.

**Without React Hook Form** (Step 5):
- Many `useState` calls, one per field
- Manual validation on each input
- Lots of repetitive code

**With React Hook Form**:
- A single hook: `useForm`
- Automatic validation
- Less code, more functionality
- Better performance

---

## Installation

```bash
npm install react-hook-form
```

---

## Main Concepts

### 1. `useForm` Hook
```javascript
const { register, handleSubmit, formState: { errors } } = useForm();
```

### 2. `register` - Binds inputs
```javascript
<input {...register('nombre')} />
```

### 3. `handleSubmit` - Handles submission
```javascript
<form onSubmit={handleSubmit(onSubmit)}>
```

### 4. `errors` - Shows errors
```javascript
{errors.nombre && <p>{errors.nombre.message}</p>}
```

---

## Example 1: Simple Form

**File**: `Ejemplo1-Simple.jsx`

```javascript
import { useForm } from 'react-hook-form';

function Ejemplo1Simple() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (datos) => {
    console.log('Datos válidos:', datos);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Nombre:</label>
        <input
          {...register('nombre', { 
            required: 'El nombre es requerido',
            minLength: { value: 3, message: 'Mínimo 3 caracteres' }
          })}
          placeholder="Juan"
        />
        {errors.nombre && <p style={{ color: 'red' }}>{errors.nombre.message}</p>}
      </div>

      <div>
        <label>Email:</label>
        <input
          {...register('email', { 
            required: 'El email es requerido',
            pattern: {
              value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
              message: 'Email inválido'
            }
          })}
          placeholder="tu@email.com"
        />
        {errors.email && <p style={{ color: 'red' }}>{errors.email.message}</p>}
      </div>

      <button type="submit">Enviar</button>
    </form>
  );
}

export default Ejemplo1Simple;
```

**Benefits**:
- `register()` binds the input automatically
- Declarative validation (inside `register`)
- `errors` displays messages automatically

---

## Example 2: Using Watch - Observe Changes

**File**: `Ejemplo2-Watch.jsx`

```javascript
import { useForm } from 'react-hook-form';

function Ejemplo2Watch() {
  const { register, handleSubmit, watch, formState: { errors } } = useForm({
    defaultValues: {
      pais: 'españa'
    }
  });

  const paisSeleccionado = watch('pais');

  const ciudadesPorPais = {
    españa: ['Madrid', 'Barcelona'],
    mexico: ['México DF', 'Guadalajara'],
    colombia: ['Bogotá', 'Medellín']
  };

  const onSubmit = (datos) => {
    console.log('Datos:', datos);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>País:</label>
        <select {...register('pais')}>
          <option value="españa">España</option>
          <option value="mexico">México</option>
          <option value="colombia">Colombia</option>
        </select>
      </div>

      <div>
        <label>Ciudad:</label>
        <select {...register('ciudad', { required: 'Selecciona ciudad' })}>
          <option value="">Elige una ciudad</option>
          {ciudadesPorPais[paisSeleccionado].map(c => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
        {errors.ciudad && <p style={{ color: 'red' }}>{errors.ciudad.message}</p>}
      </div>

      <button type="submit">Enviar</button>
    </form>
  );
}

export default Ejemplo2Watch;
```

**`watch()`**: Observes a field and re-renders when it changes

---

## Example 3: Complex Validation

**File**: `Ejemplo3-Complejo.jsx`

```javascript
import { useForm } from 'react-hook-form';

function Ejemplo3Complejo() {
  const { register, handleSubmit, watch, formState: { errors } } = useForm();

  const password = watch('password');

  const onSubmit = (datos) => {
    console.log('Usuario registrado:', datos);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Username:</label>
        <input
          {...register('username', {
            required: 'Username es requerido',
            minLength: { value: 3, message: 'Mínimo 3 caracteres' },
            maxLength: { value: 20, message: 'Máximo 20 caracteres' },
            pattern: {
              value: /^[a-zA-Z0-9_]+$/,
              message: 'Solo letras, números y guiones bajos'
            }
          })}
          placeholder="juan_2024"
        />
        {errors.username && <p style={{ color: 'red' }}>{errors.username.message}</p>}
      </div>

      <div>
        <label>Email:</label>
        <input
          type="email"
          {...register('email', {
            required: 'Email es requerido',
            pattern: {
              value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
              message: 'Email inválido'
            }
          })}
          placeholder="tu@email.com"
        />
        {errors.email && <p style={{ color: 'red' }}>{errors.email.message}</p>}
      </div>

      <div>
        <label>Contraseña:</label>
        <input
          type="password"
          {...register('password', {
            required: 'Contraseña requerida',
            minLength: { value: 8, message: 'Mínimo 8 caracteres' },
            pattern: {
              value: /^(?=.*[A-Z])(?=.*\d)/,
              message: 'Debe contener mayúscula y número'
            }
          })}
          placeholder="Contraseña fuerte"
        />
        {errors.password && <p style={{ color: 'red' }}>{errors.password.message}</p>}
      </div>

      <div>
        <label>Confirmar Contraseña:</label>
        <input
          type="password"
          {...register('confirmPassword', {
            required: 'Confirma la contraseña',
            validate: (value) => 
              value === password || 'Las contraseñas no coinciden'
          })}
          placeholder="Confirmar"
        />
        {errors.confirmPassword && <p style={{ color: 'red' }}>{errors.confirmPassword.message}</p>}
      </div>

      <button type="submit">Registrarse</button>
    </form>
  );
}

export default Ejemplo3Complejo;
```

**New concepts**:
- `validate`: Custom validation function
- `pattern`: Regex-based validation
- `minLength` / `maxLength`: Character limits

---

## Example 4: Reset - Clear the Form

**File**: `Ejemplo4-Reset.jsx`

```javascript
import { useForm } from 'react-hook-form';

function Ejemplo4Reset() {
  const { register, handleSubmit, reset, formState: { errors } } = useForm({
    defaultValues: {
      nombre: '',
      email: ''
    }
  });

  const onSubmit = (datos) => {
    console.log('Enviado:', datos);
    reset(); // Clear the form
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <input
          {...register('nombre', { required: 'Requerido' })}
          placeholder="Nombre"
        />
        {errors.nombre && <p>{errors.nombre.message}</p>}
      </div>

      <div>
        <input
          {...register('email', { required: 'Requerido' })}
          placeholder="Email"
        />
        {errors.email && <p>{errors.email.message}</p>}
      </div>

      <button type="submit">Enviar</button>
      <button type="button" onClick={() => reset()}>Limpiar</button>
    </form>
  );
}

export default Ejemplo4Reset;
```

**`reset()`**: Clears all fields back to their `defaultValues`

---

## Comparison: Manual vs React Hook Form

| Aspect | Manual (Step 5) | React Hook Form |
|--------|-----------------|-----------------|
| State | Many `useState` calls | One `useForm` |
| Validation | Manual on each onChange | Declarative in `register` |
| Lines of code | 50+ | 20-30 |
| Performance | More re-renders | Fewer re-renders |
| Errors | Manual | Automatic |
| Reset | Manual | `reset()` |

---

## Common Validation Rules

```javascript
register('campo', {
  required: 'Campo requerido',
  minLength: { value: 5, message: 'Mínimo 5' },
  maxLength: { value: 20, message: 'Máximo 20' },
  pattern: { value: /regex/, message: 'Formato inválido' },
  validate: (value) => value > 0 || 'Debe ser positivo',
  min: { value: 0, message: 'Mínimo 0' },
  max: { value: 100, message: 'Máximo 100' }
})
```

---

## Key Points ✨

1. **`register()`**: Binds inputs automatically
2. **`handleSubmit()`**: Only submits when valid
3. **`watch()`**: Observes real-time changes
4. **`reset()`**: Clears the form
5. **Less code**: Compared to manual validation

---

## Your Exercise 🎯

Create a `MiEjercicio.jsx` using React Hook Form that is a form with:

1. ✅ Name (3-30 characters)
2. ✅ Email (format validation)
3. ✅ Age (18-100)
4. ✅ Gender (radio buttons)
5. ✅ Password (at least 8 characters, uppercase and number)
6. ✅ Confirm password (must match)
7. ✅ Show errors automatically
8. ✅ "Enviar" and "Limpiar" buttons

**Hint**:
- Use `validate` for password confirmation
- Use `watch()` to observe the password
- Combine `minLength`, `pattern`, and `required`

---

## Next Steps

Once you master React Hook Form:

✅ Professional validation  
✅ Less repetitive code  
✅ Better performance  

You'll be ready for:
- Real projects with complex forms
- API integration
- TodoList Application (Final Project)

---

## Installing in Your Project

If you haven't already:

```bash
npm install react-hook-form
```

---

## Resources

- [React Hook Form Docs](https://react-hook-form.com/)
- [API Reference](https://react-hook-form.com/api)
- [Examples](https://react-hook-form.com/form-builder)

---

**💡 Tip**: React Hook Form is the standard solution in professional projects. Mastering it will give you a competitive edge.

## 🎉 Congratulations!

You completed every step of Day 18. Now you have the tools to:

✅ Understand the component lifecycle  
✅ Use hooks like a professional  
✅ Build validated forms  
✅ Create interactive applications  

**Now**: Build the **Final Project - TodoList Application** combining everything you learned.
