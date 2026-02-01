# Step 6: React Hook Form 🚀

## ¿Qué es React Hook Form?

React Hook Form es una librería que simplifica la creación y validación de formularios en React. 

**Sin React Hook Form** (Step 5):
- Muchos `useState` para cada campo
- Validación manual en cada input
- Mucho código repetitivo

**Con React Hook Form**:
- Un solo hook: `useForm`
- Validación automática
- Menos código, más funcionalidad
- Mejor performance

---

## Instalación

```bash
npm install react-hook-form
```

---

## Conceptos Principales

### 1. `useForm` Hook
```javascript
const { register, handleSubmit, formState: { errors } } = useForm();
```

### 2. `register` - Vincula inputs
```javascript
<input {...register('nombre')} />
```

### 3. `handleSubmit` - Maneja envío
```javascript
<form onSubmit={handleSubmit(onSubmit)}>
```

### 4. `errors` - Muestra errores
```javascript
{errors.nombre && <p>{errors.nombre.message}</p>}
```

---

## Ejemplo 1: Formulario Simple

**Archivo**: `Ejemplo1-Simple.jsx`

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

**Ventajas**:
- `register()` vincula el input automáticamente
- Validación declarativa (en el `register`)
- `errors` muestra los mensajes automáticamente

---

## Ejemplo 2: Con Watch - Observar Cambios

**Archivo**: `Ejemplo2-Watch.jsx`

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

**`watch()`**: Observa un campo y re-renderiza cuando cambia

---

## Ejemplo 3: Validación Compleja

**Archivo**: `Ejemplo3-Complejo.jsx`

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

**Nuevos conceptos**:
- `validate`: Función de validación personalizada
- `pattern`: Validación con regex
- `minLength` / `maxLength`: Límites de caracteres

---

## Ejemplo 4: Reset - Limpiar Formulario

**Archivo**: `Ejemplo4-Reset.jsx`

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
    reset(); // Limpia el formulario
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

**`reset()`**: Limpia todos los campos a sus `defaultValues`

---

## Comparación: Manual vs React Hook Form

| Aspecto | Manual (Step 5) | React Hook Form |
|--------|-----------------|-----------------|
| Estados | Muchos `useState` | Un `useForm` |
| Validación | Manual en cada onChange | Declarativa en `register` |
| Líneas de código | 50+ | 20-30 |
| Performance | Re-renderiza más | Re-renderiza menos |
| Errores | Manuales | Automáticos |
| Reset | Manual | `reset()` |

---

## Reglas de Validación Comunes

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

## Puntos Clave ✨

1. **`register()`**: Vincula inputs automáticamente
2. **`handleSubmit()`**: Solo envía si es válido
3. **`watch()`**: Observa cambios en tiempo real
4. **`reset()`**: Limpia el formulario
5. **Menos código**: Comparado con validación manual

---

## Tu Ejercicio 🎯

Crea un `MiEjercicio.jsx` usando React Hook Form que sea un formulario de:

1. ✅ Nombre (3-30 caracteres)
2. ✅ Email (validación de formato)
3. ✅ Edad (18-100)
4. ✅ Género (radio buttons)
5. ✅ Contraseña (mínimo 8, mayúscula y número)
6. ✅ Confirmar contraseña (debe coincidir)
7. ✅ Mostrar errores automáticamente
8. ✅ Botón "Enviar" y "Limpiar"

**Pista**:
- Usa `validate` para la confirmación de contraseña
- Usa `watch()` para observar la contraseña
- Combina `minLength`, `pattern` y `required`

---

## Próximos Pasos

Una vez domines React Hook Form:

✅ Validación profesional  
✅ Menos código repetitivo  
✅ Mejor performance  

Estarás listo para:
- Proyectos reales con formularios complejos
- Integración con APIs
- TodoList Application (Proyecto Final)

---

## Instalación en Tu Proyecto

Si aún no lo has hecho:

```bash
npm install react-hook-form
```

---

## Recursos

- [React Hook Form Docs](https://react-hook-form.com/)
- [API Reference](https://react-hook-form.com/api)
- [Ejemplos](https://react-hook-form.com/form-builder)

---

**💡 Consejo**: React Hook Form es la solución estándar en proyectos profesionales. Dominarla te dará una ventaja competitiva.

## 🎉 ¡Felicitaciones!

Completaste todos los pasos del Día 18. Ahora tienes las herramientas para:

✅ Entender el ciclo de vida de componentes  
✅ Usar hooks como un profesional  
✅ Crear formularios validados  
✅ Construir aplicaciones interactivas  

**Ahora**: Crea el **Proyecto Final - TodoList Application** combinando todo lo aprendido.
