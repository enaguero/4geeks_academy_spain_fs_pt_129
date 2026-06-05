🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🖥️ El Desafío de la Terminal - CMD Challenge

Presentación interactiva usando Reveal.js para enseñar comandos básicos de terminal a través de un desafío práctico.

## 📋 Descripción

Esta presentación contiene **22 slides** con instrucciones progresivas para que los estudiantes practiquen comandos de terminal de forma divertida y competitiva.

## 🚀 Cómo usar

### Opción 1: Abrir directamente en el navegador

Simplemente abre el archivo `index.html` en tu navegador:

```bash
open index.html
# o en Linux/Windows
xdg-open index.html  # Linux
start index.html     # Windows
```

### Opción 2: Servidor local con Python

Si prefieres usar un servidor local:

```bash
python3 -m http.server 8000
```

Luego abre en tu navegador: `http://localhost:8000`

### Opción 3: Live Server (VS Code)

Si usas VS Code, instala la extensión "Live Server" y haz clic derecho en `index.html` → "Open with Live Server"

## 🎯 Estructura de la Presentación

1. **Portada** - Introducción al desafío
2. **Bienvenida** - Explicación del propósito
3. **Reglas** - Cómo funciona el desafío competitivo
4. **Comandos básicos** - Referencia rápida
5. **Preparación** - Checklist antes de empezar
6. **Instrucciones 1-16** - Desafíos prácticos progresivos
7. **Felicitaciones** - Slide de cierre
8. **Recursos** - Material adicional
9. **Consejos** - Tips finales

Total: **22 slides**

## 🎮 Navegación

- **Flechas ← →** o **Espacio**: Siguiente/anterior slide
- **ESC**: Vista general de todas las slides
- **F**: Pantalla completa
- **S**: Modo presentador (notas del orador)
- **?**: Ayuda de atajos de teclado

## 📝 Instrucciones para el Profesor

### Antes de la Clase

1. Asegúrate de que los estudiantes tengan:
   - Terminal instalada (bash/zsh)
   - La carpeta `thecmdchallenge/` descargada (del repo original de 4Geeks)
   - Conocimientos básicos de navegación en directorios

### Durante la Clase

1. Proyecta la presentación
2. Lee cada instrucción en voz alta
3. Da tiempo para que los estudiantes completen el desafío
4. El primer estudiante en terminar debe:
   - Levantar la mano
   - Explicar su solución a la clase
   - Mostrar el comando que usó
5. Avanza a la siguiente slide

### Dinámica del Desafío

- **Competitivo**: El primero en completar cada instrucción gana
- **Educativo**: El ganador explica su solución (todos aprenden)
- **Progresivo**: Las instrucciones van aumentando en dificedad
- **Divertido**: Los desafíos usan archivos con nombres graciosos

## 🎨 Personalización

### Cambiar Tema

En la línea 9 de `index.html`, puedes cambiar el tema:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/theme/black.css">
```

Temas disponibles:
- `black.css` (actual)
- `white.css`
- `league.css`
- `beige.css`
- `sky.css`
- `night.css`
- `serif.css`
- `simple.css`
- `solarized.css`

### Modificar Contenido

Cada slide es una sección `<section>...</section>`. Puedes:
- Añadir más slides
- Modificar instrucciones existentes
- Cambiar colores de fondo con `data-background-color="#color"`
- Añadir gradientes con `data-background-gradient`

## 📦 Dependencias

La presentación usa CDN, así que **no necesitas instalar nada**:

- Reveal.js 5.0.4
- Plugin de resaltado de sintaxis

Todo se carga automáticamente desde CDN.

## 🔗 Enlaces Útiles

- [Reveal.js Documentación](https://revealjs.com/)
- [Desafío Original (en inglés)](https://breatheco-de.github.io/exercise-terminal-challenge-slides/#/0)
- [Repositorio Original 4Geeks](https://github.com/breatheco-de/exercise-terminal-challenge-slides)

## 📄 Archivos Incluidos

```
challenge_instructions/
├── index.html          # Presentación Reveal.js
├── README.md          # Este archivo
├── slides-data.json   # Datos originales del desafío
└── terminal-challenge.html  # HTML original descargado (referencia)
```

## 🎓 Nivel de Estudiantes

- **Público objetivo**: Principiantes en desarrollo web
- **Conocimientos previos**: Haber abierto la terminal al menos una vez
- **Duración estimada**: 60-90 minutos (dependiendo del grupo)

## 💡 Tips para el Profesor

1. **Pausa entre slides**: Da tiempo suficiente para cada desafío
2. **Ayuda selectiva**: Deja que intenten primero, ayuda si se atascan
3. **Promueve la colaboración**: Los estudiantes pueden ayudarse (después del ganador)
4. **Refuerza conceptos**: Usa las explicaciones de los ganadores para enseñar
5. **Celebra los errores**: Son oportunidades de aprendizaje

## 🐛 Solución de Problemas

### La presentación no carga
- Verifica tu conexión a internet (usa CDN)
- Intenta abrir con otro navegador
- Revisa la consola del navegador (F12) para errores

### Los comandos no funcionan en Windows
- Usa Git Bash o WSL (Windows Subsystem for Linux)
- O usa Gitpod/Cloud IDE como sugiere el desafío original

### Los archivos del desafío no existen
- Asegúrate de que los estudiantes clonaron el repo correcto:
  ```bash
  git clone https://github.com/breatheco-de/exercise-terminal-challenge.git
  ```

---

**Creado para**: 4Geeks Academy Spain - Full Stack PT Cohort 129  
**Basado en**: [Terminal Challenge de BreatheCode](https://breatheco-de.github.io/exercise-terminal-challenge-slides/)  
**Tecnología**: Reveal.js 5.0.4
