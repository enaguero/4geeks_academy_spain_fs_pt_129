# Step 4: Formularios Básicos en React 📝

## ¿Qué es un Formulario Controlado?

Un **formulario controlado** es cuando React controla el valor de cada input mediante el estado.

```javascript
// ❌ MALO - Input no controlado
<input type="text" placeholder="Nombre" />

// ✅ BIEN - Input controlado (vinculado con estado)
const [nombre, setNombre] = useState('');
<input 
  type="text" 
  value={nombre}
  onChange={(e) => setNombre(e.target.value)}
/>
```

## El Concepto de event.target

Cuando escribes en un input, React crea un evento. Puedes acceder al valor así:

```javascript
const handleChange = (event) => {
  // event.target es el elemento <input>
  // event.target.value es lo que escribiste
  console.log(event.target.value);
  
  setState(event.target.value);
};

<input onChange={handleChange} />
```

---

## Ejemplo 1: Formulario Simple - Registro

**Archivo**: `Ejemplo1-RegistroSimple.jsx`

```javascript
import { useState } from 'react';

function Ejemplo1RegistroSimple() {
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');
  const [edad, setEdad] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault(); // Evita que la página se recargue
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

**Concepto clave**:
- `value={nombre}` → Vincula el estado al input
- `onChange={(e) => setNombre(e.target.value)}` → Actualiza el estado cuando escribes
- Los datos se muestran en tiempo real debajo

---

## Ejemplo 2: Formulario con Select

**Archivo**: `Ejemplo2-FormularioSelect.jsx`

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

**Concepto clave**:
- Los `<select>` funcionan igual que los inputs
- `value` y `onChange` controlan la opción seleccionada
- Puedes generar opciones dinámicamente con `.map()`

---

## Ejemplo 3: Textarea

**Archivo**: `Ejemplo3-Textarea.jsx`

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
    setComentario(''); // Limpiar después de enviar
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

**Concepto clave**:
- Los `<textarea>` funcionan como inputs
- `value` y `onChange` funcionan igual
- Puedes limpiar con `setComentario('')` después de enviar

---

## Ejemplo 4: Checkboxes

**Archivo**: `Ejemplo4-Checkboxes.jsx`

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
    // Crear un nuevo objeto con el checkbox actualizado
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

**Concepto clave**:
- Para checkboxes, usa `checked` en lugar de `value`
- `e.target.checked` te da true/false
- Para múltiples checkboxes, crea un objeto de estados

---

## Ejemplo 5: Radio Buttons

**Archivo**: `Ejemplo5-RadioButtons.jsx`

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

**Concepto clave**:
- Los radio buttons se controlan con `value` y `checked`
- Solo un radio button puede estar seleccionado a la vez
- El valor debe ser comparado: `checked={genero === 'masculino'}`

---

## Resumen: Tipos de Inputs

| Tipo | Propiedad | Evento |
|------|-----------|--------|
| text, email, number | `value` | `onChange` |
| textarea | `value` | `onChange` |
| select | `value` | `onChange` |
| checkbox | `checked` | `onChange` + `e.target.checked` |
| radio | `checked` | `onChange` + `e.target.value` |

---

## Puntos Clave ✨

1. **Vinculación en dos direcciones**: El estado controla el input, el input actualiza el estado
2. **event.target**: Acceso al elemento que cambió
3. **event.target.value**: El nuevo valor escrito
4. **event.target.checked**: Para checkboxes y radios
5. **Prevenir recarga**: `e.preventDefault()` en onSubmit

---

## Tu Ejercicio 🎯

Crea un `MiEjercicio.jsx` que sea un formulario de contacto con:

1. ✅ Input de nombre (texto)
2. ✅ Input de email
3. ✅ Textarea para el mensaje
4. ✅ Select con opciones: "Consulta", "Soporte", "Otro"
5. ✅ Checkbox "Deseo ser contactado"
6. ✅ Botón "Enviar" que imprima los datos en consola
7. ✅ Limpie el formulario después de enviar

**Pista**:
- Necesitarás 5 estados (nombre, email, mensaje, tipo, contacto)
- En onSubmit, imprime todos los datos
- Usa `setNombre('')` etc. para limpiar

---

## Próximos Pasos

Una vez domines formularios básicos:

✅ Inputs controlados  
✅ event.target  
✅ Múltiples estados en un formulario  

Estarás listo para:
- **Step 5**: Validación de inputs
- **Step 6**: React Hook Form

---

**💡 Consejo**: Los formularios son el corazón de las aplicaciones web. Domina esto y tendrás superpoderes.
