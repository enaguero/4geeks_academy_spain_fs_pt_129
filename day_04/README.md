🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# Tutorial: La Terminal, Comandos y Rutas

## 📺 Videos de Referencia

- [¿Qué es la terminal?](https://www.youtube.com/watch?v=3xQRR3iNqDQ)
- [¿Qué son los comandos?](https://www.youtube.com/watch?v=f0K0jA7O9w8)
- [Rutas relativas y absolutas](https://youtu.be/e9NjhfsdEGA?si=bxXnOoZHZbK5MkPU)

---

## 🗂️ El Sistema de Archivos y Carpetas

Antes de empezar a usar la terminal, es importante entender cómo está organizado tu ordenador.

### ¿Qué es un sistema de archivos?

Cuando compras un ordenador, ya viene con una **estructura de carpetas organizada** instalada por defecto. Esta estructura es como un gran árbol de carpetas que contiene todo lo necesario para que el sistema operativo funcione.

A medida que usas tu ordenador, vas agregando tus propios archivos y carpetas a esta estructura (documentos, fotos, proyectos, etc.).

### Estructura básica del sistema

Todo el sistema de archivos comienza desde una carpeta raíz (la "base" del árbol):

**En Mac/Linux:** La raíz se llama `/`  
**En Windows:** La raíz suele ser `C:\`

### Carpetas principales del sistema (Mac/Linux)

Desde la raíz (`/`), el sistema tiene varias carpetas importantes:

```
/
├── Users/           # Carpeta de todos los usuarios
│   ├── tu_nombre/   # Tu carpeta personal (aquí guardas TUS archivos)
│   │   ├── Documents/
│   │   ├── Downloads/
│   │   ├── Desktop/
│   │   └── Pictures/
│   └── otro_usuario/
├── Applications/    # Programas instalados (Chrome, VS Code, etc.)
├── System/          # Archivos del sistema operativo (no tocar)
├── Library/         # Configuraciones del sistema
├── tmp/             # Archivos temporales
└── etc/             # Configuraciones globales
```

### Tu carpeta personal

La carpeta más importante para ti es **tu carpeta personal** (también llamada "home"):

```
/Users/tu_nombre/     # En Mac/Linux
C:\Users\tu_nombre\   # En Windows
```

Esta es donde guardas:
- 📄 Documentos (`Documents/`)
- 📥 Descargas (`Downloads/`)
- 🖼️ Imágenes (`Pictures/`)
- 🖥️ Escritorio (`Desktop/`)
- 💻 Tus proyectos de programación

### Analogía visual

Piensa en el sistema de archivos como un **edificio de apartamentos**:

- **La raíz (`/`)** es el edificio completo
- **`/Users/`** es un piso donde viven todos los usuarios
- **`/Users/tu_nombre/`** es TU apartamento específico
- **`/Users/tu_nombre/Documents/`** es una habitación dentro de tu apartamento
- **`/Users/tu_nombre/Documents/proyecto.txt`** es un objeto dentro de esa habitación

### ¿Por qué es importante entender esto?

1. **Cuando abres la terminal**, siempre estás "ubicado" en alguna carpeta (normalmente tu carpeta personal)
2. **Los comandos operan** en la carpeta donde estás ubicado
3. **Para moverte entre carpetas** necesitas entender esta estructura
4. **Tus proyectos de programación** estarán en algún lugar de esta estructura

### Ejemplo práctico

Si creas un proyecto web en tu carpeta personal:

```
/Users/tu_nombre/
└── projects/
    └── mi_web/
        ├── index.html
        ├── css/
        │   └── style.css
        └── images/
            └── logo.png
```

La ruta completa al archivo `style.css` sería:
```
/Users/tu_nombre/projects/mi_web/css/style.css
```

---

## 🖥️ ¿Qué es la Terminal?

La **terminal** (también llamada consola o línea de comandos) es una interfaz de texto que nos permite comunicarnos directamente con el sistema operativo de nuestro ordenador.

### ¿Por qué usarla?

- Es más **rápida** que usar la interfaz gráfica
- Permite **automatizar** tareas repetitivas
- Es la forma principal de trabajar con servidores y herramientas de desarrollo
- Muchas herramientas de programación solo funcionan por terminal

### Ejemplo visual:

**Interfaz Gráfica:** Hacer clic en carpetas, arrastrar archivos  
**Terminal:** Escribir comandos como `cd carpeta` o `mkdir nueva_carpeta`

---

## ⌨️ ¿Qué son los Comandos?

Los **comandos** son instrucciones que escribimos en la terminal para que el ordenador realice acciones específicas.

### Estructura básica de un comando:

```bash
comando [opciones] [argumentos]
```

### Comandos básicos esenciales:

#### 1. **pwd** (Print Working Directory)
Muestra la ruta donde estás ubicado actualmente.

```bash
pwd
# Resultado ejemplo: /Users/tu_usuario/Documents
```

#### 2. **ls** (List)
Lista los archivos y carpetas del directorio actual.

```bash
ls
# Muestra: archivo1.txt  carpeta1/  imagen.png

ls -l
# Muestra información detallada (permisos, tamaño, fecha)

ls -a
# Muestra archivos ocultos también
```

#### 3. **cd** (Change Directory)
Cambia de directorio (carpeta).

```bash
cd Documents        # Entra a la carpeta Documents
cd ..              # Sube un nivel (carpeta padre)
cd ~               # Va a tu carpeta personal
cd /               # Va a la raíz del sistema
```

#### 4. **mkdir** (Make Directory)
Crea una nueva carpeta.

```bash
mkdir mi_proyecto
mkdir -p carpeta1/carpeta2/carpeta3  # Crea carpetas anidadas
```

#### 5. **touch**
Crea un archivo vacío.

```bash
touch index.html
touch style.css script.js
```

#### 6. **rm** (Remove)
Elimina archivos o carpetas.

```bash
rm archivo.txt              # Elimina un archivo
rm -r carpeta/              # Elimina una carpeta y su contenido
rm -rf carpeta/             # Fuerza la eliminación (¡usar con cuidado!)
```

#### 7. **cp** (Copy)
Copia archivos o carpetas.

```bash
cp archivo.txt copia.txt
cp -r carpeta1/ carpeta2/
```

#### 8. **mv** (Move)
Mueve o renombra archivos/carpetas.

```bash
mv archivo.txt nueva_carpeta/        # Mueve el archivo
mv nombre_viejo.txt nombre_nuevo.txt # Renombra el archivo
```

#### 9. **cat**
Muestra el contenido de un archivo.

```bash
cat index.html
```

#### 10. **clear**
Limpia la pantalla de la terminal.

```bash
clear
```

---

## 📂 Rutas: Relativas vs Absolutas

Una **ruta** es la ubicación de un archivo o carpeta en el sistema de archivos.

### 🔹 Ruta Absoluta

Es la ruta **completa** desde la raíz del sistema hasta el archivo.

**En el sistema operativo:**

```bash
/Users/erwin/projects/mi_web/index.html
```

- Siempre empieza desde la raíz (`/` en Mac/Linux, `C:\` en Windows)
- No importa dónde estés, siempre funciona igual
- Es como dar la dirección completa: "Calle Principal 123, Madrid, España"

**Ejemplos:**

```bash
cd /Users/erwin/Documents
cat /etc/hosts
ls /var/www/html
```

### 🔹 Ruta Relativa

Es la ruta **en relación** a donde estás actualmente.

**En el sistema operativo:**

Si estás en `/Users/erwin/projects/` y quieres ir a `mi_web`:

```bash
cd mi_web              # Ruta relativa
cd ./mi_web            # Ruta relativa explícita (mismo efecto)
cd ../otros_proyectos  # Sube un nivel y entra a otra carpeta
```

- Depende de tu ubicación actual
- Usa `.` para referirse al directorio actual
- Usa `..` para referirse al directorio padre
- Es como dar direcciones: "dos calles más adelante, gira a la derecha"

### Símbolos importantes:

| Símbolo | Significado |
|---------|------------|
| `/` | Raíz del sistema (o separador de carpetas) |
| `~` | Tu carpeta personal |
| `.` | Directorio actual |
| `..` | Directorio padre (un nivel arriba) |

---

## 🌐 Rutas en Desarrollo Web (HTML, CSS, JS)

Cuando trabajamos con páginas web, también usamos rutas para enlazar archivos entre sí.

### Estructura típica de un proyecto web:

```
mi_proyecto/
├── index.html
├── about.html
├── css/
│   ├── style.css
│   └── reset.css
├── js/
│   └── script.js
└── images/
    └── logo.png
```

### 🔹 Rutas Relativas en HTML

Las rutas relativas son las más comunes en desarrollo web porque el proyecto puede moverse a diferentes servidores sin romper los enlaces.

**Ejemplo: index.html**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Sitio Web</title>
    
    <!-- Ruta relativa al CSS (entra en carpeta css) -->
    <link rel="stylesheet" href="css/style.css">
    
    <!-- Otro CSS en la misma carpeta -->
    <link rel="stylesheet" href="css/reset.css">
</head>
<body>
    <!-- Ruta relativa a imagen (entra en carpeta images) -->
    <img src="images/logo.png" alt="Logo">
    
    <!-- Enlace a otra página en el mismo directorio -->
    <a href="about.html">Acerca de</a>
    
    <!-- Ruta relativa al JavaScript (entra en carpeta js) -->
    <script src="js/script.js"></script>
</body>
</html>
```

**Si about.html está dentro de una carpeta:**

```
mi_proyecto/
├── index.html
├── pages/
│   └── about.html
└── css/
    └── style.css
```

**En index.html:**

```html
<a href="pages/about.html">Acerca de</a>
```

**En pages/about.html para volver a index.html:**

```html
<!-- Sube un nivel con ../ -->
<a href="../index.html">Inicio</a>

<!-- Para usar el CSS, también sube un nivel -->
<link rel="stylesheet" href="../css/style.css">
```

### 🔹 Rutas Absolutas en HTML

Las rutas absolutas en web pueden ser:

**1. Desde la raíz del servidor (comienzan con `/`):**

```html
<link rel="stylesheet" href="/css/style.css">
<img src="/images/logo.png" alt="Logo">
```

**2. URL completa:**

```html
<link rel="stylesheet" href="https://ejemplo.com/css/style.css">
<img src="https://ejemplo.com/images/logo.png" alt="Logo">
```

### 📋 Comparación Práctica

Supongamos esta estructura:

```
proyecto/
├── index.html
├── pages/
│   └── contact.html
└── assets/
    ├── css/
    │   └── style.css
    └── images/
        └── bg.jpg
```

**Desde index.html:**

```html
<!-- Relativa -->
<link rel="stylesheet" href="assets/css/style.css">
<img src="assets/images/bg.jpg">

<!-- Absoluta (desde raíz del servidor) -->
<link rel="stylesheet" href="/assets/css/style.css">
<img src="/assets/images/bg.jpg">
```

**Desde pages/contact.html:**

```html
<!-- Relativa (sube un nivel con ../) -->
<link rel="stylesheet" href="../assets/css/style.css">
<img src="../assets/images/bg.jpg">
<a href="../index.html">Volver al inicio</a>

<!-- Absoluta (desde raíz del servidor) -->
<link rel="stylesheet" href="/assets/css/style.css">
<img src="/assets/images/bg.jpg">
<a href="/index.html">Volver al inicio</a>
```

### ✅ Buenas Prácticas

1. **Usa rutas relativas** en proyectos locales y sitios pequeños
2. **Usa rutas absolutas desde la raíz** (`/`) en proyectos grandes para evitar confusión
3. **Mantén una estructura organizada** con carpetas para CSS, JS e imágenes
4. **Prueba tus enlaces** antes de subir a producción
5. **Usa nombres descriptivos** sin espacios (usa guiones: `mi-archivo.html`)

---

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Comandos básicos

Crea esta estructura usando solo comandos:

```bash
mkdir mi_primer_proyecto
cd mi_primer_proyecto
mkdir css js images
touch index.html
touch css/style.css
touch js/script.js
ls -R
```

### Ejercicio 2: Navegación

```bash
# Estás en mi_primer_proyecto/
cd css              # Entra a css
pwd                 # ¿Dónde estás?
cd ..               # Vuelve a mi_primer_proyecto
cd js               # Entra a js
cd ../css           # Desde js, ve a css
cd ~                # Ve a tu carpeta personal
```

### Ejercicio 3: Rutas en HTML

Crea un `index.html` con enlaces correctos a:
- Un archivo CSS en carpeta `css/`
- Un archivo JS en carpeta `js/`
- Una imagen en carpeta `images/`
- Otra página HTML en carpeta `pages/`

---

## 📚 Resumen

| Concepto | Definición | Ejemplo |
|----------|------------|---------||
| **Terminal** | Interfaz de texto para comandos | Terminal de Mac, CMD en Windows |
| **Comando** | Instrucción para el sistema | `ls`, `cd`, `mkdir` |
| **Ruta Absoluta (Sistema)** | Desde la raíz del sistema | `/Users/erwin/proyecto/index.html` |
| **Ruta Relativa (Sistema)** | Desde ubicación actual | `../carpeta/archivo.txt` |
| **Ruta Relativa (Web)** | Desde archivo actual | `css/style.css`, `../images/logo.png` |
| **Ruta Absoluta (Web)** | Desde raíz del servidor o URL completa | `/css/style.css`, `https://site.com/img.png` |

---

## 🚀 Siguientes Pasos

1. Practica los comandos básicos creando y navegando carpetas
2. Crea un proyecto web simple con la estructura de carpetas recomendada
3. Experimenta con rutas relativas en HTML
4. Aprende Git y GitHub (próximo tema)

¡Recuerda: la práctica hace al maestro! 💪