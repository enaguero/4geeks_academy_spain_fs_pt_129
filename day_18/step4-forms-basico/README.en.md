[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 4: Basic Forms in React 📝

## What is a Controlled Form?

A **controlled form** is one where React controls each input's value via state.

```javascript
// ❌ BAD - Uncontrolled input
<input type="text" placeholder="Nombre" />

// ✅ GOOD - Controlled input (bound to state)
const [nombre, setNombre] = useState('');
<input 
  type="text" 
  value={nombre}
  onChange={(e) => setNombre(e.target.value)}
/>
```

## The event.target Concept

When you type in an input, React creates an event. You can read the value like this:

```javascript
const handleChange = (event) => {
  // event.target is the <input> element
  // event.target.value is what you typed
  console.log(event.target.value);
  
  setState(event.target.value);
};

<input onChange={handleChange} />
```

---

## Example 1: Simple Form - Signup

**File**: `Ejemplo1-RegistroSimple.jsx`

```javascript
import { useState } from 'react';

function Ejemplo1RegistroSimple() {
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');
  const [edad, setEdad] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault(); // Prevents page reload
    console.log('Formulario enviado:');
    console.log(`Nombre: ${nombre}`);
    console.log(`Email: ${email}`);
    console.log(`Edad: ${edad}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Nombre:</label>
        <input
          type="text"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          placeholder="Juan"
        />
      </div>

      <div>
        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="juan@email.com"
        />
      </div>

      <div>
        <label>Edad:</label>
        <input
          type="number"
          value={edad}
          onChange={(e) => setEdad(e.target.value)}
          placeholder="25"
        />
      </div>

      <button type="submit">Enviar</button>

      <div>
        <h3>Datos escritos:</h3>
        <p>Nombre: {nombre}</p>
        <p>Email: {email}</p>
        <p>Edad: {edad}</p>
      </div>
    </form>
  );
}

export default Ejemplo1RegistroSimple;
```

**Key concept**:
- `value={nombre}` → Binds state to the input
- `onChange={(e) => setNombre(e.target.value)}` → Updates state as you type
- Data is shown in real time below

---

## Example 2: Form with Select

**File**: `Ejemplo2-FormularioSelect.jsx`

```javascript
import { useState } from 'react';

function Ejemplo2FormularioSelect() {
  const [pais, setPais] = useState('españa');
  const [ciudad, setCiudad] = useState('');

  const ciudadesPorPais = {
    españa: ['Madrid', 'Barcelona', 'Valencia'],
    mexico: ['Ciudad de México', 'Guadalajara', 'Monterrey'],
    colombia: ['Bogotá', 'Medellín', 'Cali']
  };

  return (
    <form>
      <div>
        <label>País:</label>
        <select
          value={pais}
          onChange={(e) => setPais(e.target.value)}
        >
          <option value="españa">España</option>
          <option value="mexico">México</option>
          <option value="colombia">Colombia</option>
        </select>
      </div>

      <div>
        <label>Ciudad:</label>
        <select
          value={ciudad}
          onChange={(e) => setCiudad(e.target.value)}
        >
          <option value="">Selecciona una ciudad</option>
          {ciudadesPorPais[pais].map((c, i) => (
            <option key={i} value={c}>{c}</option>
          ))}
        </select>
      </div>

      <div>
        <h3>Seleccionaste:</h3>
        <p>País: {pais}</p>
        <p>Ciudad: {ciudad || '(no seleccionada)'}</p>
      </div>
    </form>
  );
}

export default Ejemplo2FormularioSelect;
```

**Key concept**:
- `<select>` works like an input
- `value` and `onChange` control the selected option
- You can generate options dynamically with `.map()`

---

## Example 3: Textarea

**File**: `Ejemplo3-Textarea.jsx`

```javascript
import { useState } from 'react';

function Ejemplo3Textarea() {
  const [comentario, setComentario] = useState('');

  const handleEnviar = () => {
    if (comentario.trim() === '') {
      alert('Por favor escribe algo');
      return;
    }

    console.log('Comentario:', comentario);
    console.log('Caracteres:', comentario.length);
    setComentario(''); // Clear after submitting
  };

  return (
    <form onSubmit={(e) => e.preventDefault()}>
      <label>Deja un comentario:</label>
      <textarea
        value={comentario}
        onChange={(e) => setComentario(e.target.value)}
        placeholder="Escribe tu comentario aquí..."
        rows="5"
      />

      <div>
        <p>Caracteres: {comentario.length}</p>
        <button onClick={handleEnviar}>Enviar comentario</button>
      </div>

      {comentario && (
        <div>
          <h3>Previsualización:</h3>
          <p>{comentario}</p>
        </div>
      )}
    </form>
  );
}

export default Ejemplo3Textarea;
```

**Key concept**:
- `<textarea>` behaves like an input
- `value` and `onChange` work the same way
- You can clear with `setComentario('')` after submitting

---

## Example 4: Checkboxes

**File**: `Ejemplo4-Checkboxes.jsx`

```javascript
import { useState } from 'react';

function Ejemplo4Checkboxes() {
  const [aceptaTerminos, setAceptaTerminos] = useState(false);
  const [suscribirse, setSuscribirse] = useState(false);
  const [intereses, setIntereses] = useState({
    deportes: false,
    musica: false,
    tecnologia: false
  });

  const handleCheckboxChange = (interes) => {
    // Create a new object with the updated checkbox
    setIntereses({
      ...intereses,
      [interes]: !intereses[interes]
    });
  };

  return (
    <form>
      <div>
        <label>
          <input
            type="checkbox"
            checked={aceptaTerminos}
            onChange={(e) => setAceptaTerminos(e.target.checked)}
          />
          Acepto los términos y condiciones
        </label>
      </div>

      <div>
        <label>
          <input
            type="checkbox"
            checked={suscribirse}
            onChange={(e) => setSuscribirse(e.target.checked)}
          />
          Suscribirse a novedades
        </label>
      </div>

      <div>
        <p>¿Cuáles son tus intereses?</p>
        <label>
          <input
            type="checkbox"
            checked={intereses.deportes}
            onChange={() => handleCheckboxChange('deportes')}
          />
          Deportes
        </label>
        <label>
          <input
            type="checkbox"
            checked={intereses.musica}
            onChange={() => handleCheckboxChange('musica')}
          />
          Música
        </label>
        <label>
          <input
            type="checkbox"
            checked={intereses.tecnologia}
            onChange={() => handleCheckboxChange('tecnologia')}
          />
          Tecnología
        </label>
      </div>

      <div>
        <h3>Seleccionaste:</h3>
        <p>Acepta términos: {aceptaTerminos ? 'Sí' : 'No'}</p>
        <p>Suscribirse: {suscribirse ? 'Sí' : 'No'}</p>
        <p>
          Intereses: {Object.keys(intereses).filter(k => intereses[k]).join(', ') || 'Ninguno'}
        </p>
      </div>
    </form>
  );
}

export default Ejemplo4Checkboxes;
```

**Key concept**:
- For checkboxes, use `checked` instead of `value`
- `e.target.checked` gives you true/false
- For multiple checkboxes, use a state object

---

## Example 5: Radio Buttons

**File**: `Ejemplo5-RadioButtons.jsx`

```javascript
import { useState } from 'react';

function Ejemplo5RadioButtons() {
  const [genero, setGenero] = useState('otro');
  const [suscripcion, setSuscripcion] = useState('basica');

  return (
    <form>
      <div>
        <p>¿Cuál es tu género?</p>
        <label>
          <input
            type="radio"
            value="masculino"
            checked={genero === 'masculino'}
            onChange={(e) => setGenero(e.target.value)}
          />
          Masculino
        </label>
        <label>
          <input
            type="radio"
            value="femenino"
            checked={genero === 'femenino'}
            onChange={(e) => setGenero(e.target.value)}
          />
          Femenino
        </label>
        <label>
          <input
            type="radio"
            value="otro"
            checked={genero === 'otro'}
            onChange={(e) => setGenero(e.target.value)}
          />
          Otro
        </label>
      </div>

      <div>
        <p>Elige tu plan de suscripción:</p>
        <label>
          <input
            type="radio"
            value="basica"
            checked={suscripcion === 'basica'}
            onChange={(e) => setSuscripcion(e.target.value)}
          />
          Básica ($9/mes)
        </label>
        <label>
          <input
            type="radio"
            value="premium"
            checked={suscripcion === 'premium'}
            onChange={(e) => setSuscripcion(e.target.value)}
          />
          Premium ($19/mes)
        </label>
      </div>

      <div>
        <h3>Tu selección:</h3>
        <p>Género: {genero}</p>
        <p>Suscripción: {suscripcion}</p>
      </div>
    </form>
  );
}

export default Ejemplo5RadioButtons;
```

**Key concept**:
- Radio buttons are controlled with `value` and `checked`
- Only one radio can be selected at a time
- The value must be compared: `checked={genero === 'masculino'}`

---

## Summary: Input Types

| Type | Property | Event |
|------|----------|-------|
| text, email, number | `value` | `onChange` |
| textarea | `value` | `onChange` |
| select | `value` | `onChange` |
| checkbox | `checked` | `onChange` + `e.target.checked` |
| radio | `checked` | `onChange` + `e.target.value` |

---

## Key Points ✨

1. **Two-way binding**: State controls the input, the input updates state
2. **event.target**: Access to the element that changed
3. **event.target.value**: The new typed value
4. **event.target.checked**: For checkboxes and radios
5. **Prevent reload**: `e.preventDefault()` on onSubmit

---

## Your Exercise 🎯

Create a `MiEjercicio.jsx` that is a contact form with:

1. ✅ Name input (text)
2. ✅ Email input
3. ✅ Textarea for the message
4. ✅ Select with options: "Consulta", "Soporte", "Otro"
5. ✅ Checkbox "Deseo ser contactado"
6. ✅ "Enviar" button that prints the data to the console
7. ✅ Clears the form after submission

**Hint**:
- You'll need 5 states (nombre, email, mensaje, tipo, contacto)
- On onSubmit, log all the data
- Use `setNombre('')` etc. to clear

---

## Next Steps

Once you master basic forms:

✅ Controlled inputs  
✅ event.target  
✅ Multiple states in a form  

You'll be ready for:
- **Step 5**: Input validation
- **Step 6**: React Hook Form

---

**💡 Tip**: Forms are at the heart of web applications. Master this and you'll have superpowers.
