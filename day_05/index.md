# Día 05: Git - Control de Versiones

## ¿Por qué Git es Imprescindible?

Git es el sistema de control de versiones más popular del mundo. Imagina que estás escribiendo un documento importante y:

- Quieres guardar diferentes versiones sin crear copias como `proyecto_final.doc`, `proyecto_final_v2.doc`, `proyecto_final_REAL.doc`
- Necesitas trabajar con otras personas sin pisar su trabajo
- Quieres poder volver atrás si algo sale mal
- Deseas mantener un historial completo de todos los cambios

**Git hace todo esto automáticamente**. Es como tener una máquina del tiempo para tu código.

### Beneficios Principales

1. **Historial completo**: Cada cambio queda registrado con quién, cuándo y por qué
2. **Trabajo en equipo**: Múltiples personas pueden trabajar simultáneamente
3. **Experimentación segura**: Prueba ideas sin miedo a romper el proyecto
4. **Backup automático**: Tu código está seguro en la nube (GitHub)
5. **Industria estándar**: Todas las empresas de tecnología usan Git

---

## Arquitectura de un Repositorio

Un **repositorio** (o "repo") es como una carpeta especial que Git vigila. Dentro de esta carpeta, Git guarda un historial completo de todos los cambios.

### Estructura Básica

```
mi-proyecto/
├── .git/               ← Carpeta oculta donde Git guarda todo
├── index.html
├── style.css
└── script.js
```

La carpeta `.git/` contiene:
- Todos los commits (versiones guardadas)
- Las ramas (branches)
- La configuración del repositorio
- Referencias a repositorios remotos

**Importante**: Nunca modifiques manualmente el contenido de `.git/`

---

## Objetos Commit

Un **commit** es una fotografía de tu proyecto en un momento específico. Cada commit contiene:

```
Commit #abc123
├── Mensaje: "Añadir formulario de contacto"
├── Autor: Erwin Aguero <erwin@example.com>
├── Fecha: 2025-12-15 16:30:00
├── Archivos modificados:
│   ├── index.html (+ 25 líneas)
│   └── style.css (+ 10 líneas)
└── Padre: Commit #def456
```

### Características de un Commit

- **Inmutable**: Una vez creado, no se puede cambiar
- **Único**: Tiene un identificador único (hash SHA)
- **Conectado**: Apunta al commit anterior (su "padre")
- **Descriptivo**: Tiene un mensaje explicativo

---

## Head: La Punta de la Lista

**HEAD** es un apuntador que indica dónde estás ahora mismo en el historial. Normalmente apunta al último commit de la rama actual.

```
[Commit 1] → [Commit 2] → [Commit 3] ← HEAD
```

Cuando haces un nuevo commit, HEAD se mueve automáticamente:

```
[Commit 1] → [Commit 2] → [Commit 3] → [Commit 4] ← HEAD
```

---

## Ramas (Branches): Múltiples Líneas de Desarrollo

Una **rama** es simplemente una línea de commits. Puedes tener varias ramas para trabajar en diferentes funcionalidades simultáneamente.

### Visualización de Ramas

```
                    main
                     ↓
[A] → [B] → [C] → [D] ← HEAD
             ↓
             [E] → [F]
                    ↓
                  feature-login
```

- `main`: La rama principal (antes se llamaba `master`)
- `feature-login`: Una rama para desarrollar el login
- Ambas comparten historia hasta el commit [B]

---

## Empezando un Repositorio: git init

Para crear un nuevo repositorio:

```bash
# Crear una carpeta para tu proyecto
mkdir mi-primer-proyecto
cd mi-primer-proyecto

# Inicializar Git
git init
```

Esto crea la carpeta `.git/` y convierte tu carpeta en un repositorio.

### Verificar el Estado

```bash
git status
```

Este comando te muestra:
- En qué rama estás
- Qué archivos han cambiado
- Qué está listo para ser guardado (commit)

---

## Guardando Cambios: El Proceso de Commit

Git usa un área intermedia llamada **staging area** (o índice). Es como preparar cajas antes de enviarlas.

### Los Tres Estados de un Archivo

1. **Working Directory** (Directorio de trabajo): Donde editas los archivos
2. **Staging Area** (Área de preparación): Cambios marcados para el próximo commit
3. **Repository** (Repositorio): Commits guardados permanentemente

### Flujo Completo

```bash
# 1. Crear un archivo
echo "# Mi Proyecto" > README.md

# 2. Ver el estado (archivo sin seguimiento)
git status

# 3. Añadir al staging area
git add README.md

# 4. Verificar que está listo
git status

# 5. Crear el commit
git commit -m "Añadir README inicial"

# 6. Ver el historial
git log
```

### Comandos Importantes

```bash
# Añadir un archivo específico
git add index.html

# Añadir todos los archivos modificados
git add .

# Ver qué cambió en los archivos
git diff

# Ver qué está en staging
git diff --staged

# Hacer commit con mensaje
git commit -m "Tu mensaje descriptivo aquí"
```

**Consejos para Mensajes de Commit**:
- Usa presente: "Añadir" no "Añadido"
- Sé descriptivo pero conciso: "Añadir validación al formulario de contacto"
- No uses puntos finales
- Ejemplos buenos: "Corregir bug en cálculo de precio", "Mejorar diseño responsive del header"

---

## Referenciándose a un Commit

Hay varias formas de referirse a un commit:

### Por Hash (SHA)

```bash
# Hash completo
git show abc123def456789...

# Hash corto (primeros 7 caracteres)
git show abc123d
```

### Por Referencia Relativa

```bash
# El último commit
HEAD

# Un commit antes del HEAD
HEAD~1

# Dos commits antes
HEAD~2

# El commit padre directo
HEAD^
```

### Por Rama

```bash
# El último commit de main
main

# El último commit de feature-login
feature-login
```

---

## Creando una Rama

Las ramas te permiten experimentar sin afectar el código principal.

```bash
# Crear una nueva rama
git branch feature-menu

# Ver todas las ramas
git branch

# Crear y cambiar a una rama en un solo comando
git checkout -b feature-footer
```

### Cuándo Crear Ramas

- Para cada nueva funcionalidad
- Para arreglar bugs
- Para experimentar con ideas
- Para trabajar en algo sin afectar `main`

---

## Cambiando Entre Ramas

```bash
# Cambiar a una rama existente
git checkout main
git checkout feature-menu

# Forma moderna (Git 2.23+)
git switch main
git switch feature-menu
```

**Importante**: Antes de cambiar de rama, asegúrate de:
1. Hacer commit de tus cambios, o
2. Guardarlos temporalmente con `git stash`

---

## Fusionando Ramas: Merge

Cuando terminas el trabajo en una rama, puedes **fusionarla** (merge) con otra.

### Ejemplo Práctico

```bash
# Estás en feature-login y terminaste el trabajo
git checkout main          # Cambiar a main
git merge feature-login    # Fusionar feature-login en main
```

### Tipos de Merge

**1. Fast-Forward** (avance rápido):
```
Antes:
main:    [A] → [B]
                ↓
feature:        [C] → [D]

Después:
main:    [A] → [B] → [C] → [D]
```

**2. Merge Commit** (commit de fusión):
```
Antes:
main:    [A] → [B] → [C]
                ↓
feature:        [D] → [E]

Después:
main:    [A] → [B] → [C] → [F (merge)]
                ↓           ↗
feature:        [D] → [E] ─┘
```

---

## Resolviendo Conflictos

Un **conflicto** ocurre cuando dos ramas modifican la misma línea de código.

### Ejemplo de Conflicto

Tienes este archivo en `main`:
```html
<h1>Bienvenido a mi sitio</h1>
```

Y en `feature-header`:
```html
<h1>Bienvenido a mi página web</h1>
```

Al hacer merge, Git no sabe cuál versión usar:

```html
<<<<<<< HEAD
<h1>Bienvenido a mi sitio</h1>
=======
<h1>Bienvenido a mi página web</h1>
>>>>>>> feature-header
```

### Resolviendo el Conflicto

```bash
# 1. Git te avisa del conflicto
git merge feature-header
# Auto-merging index.html
# CONFLICT (content): Merge conflict in index.html

# 2. Abrir el archivo y elegir qué mantener
# Editar manualmente para dejar:
<h1>Bienvenido a mi página web</h1>

# 3. Marcar como resuelto
git add index.html

# 4. Completar el merge
git commit -m "Resolver conflicto en título del header"
```

### Consejos para Evitar Conflictos

- Hacer commits frecuentes y pequeños
- Comunicarse con el equipo sobre qué archivos están modificando
- Actualizar tu rama regularmente con `git pull`
- No trabajar todos en los mismos archivos al mismo tiempo

---

## Colaboración con Git

Git brilla cuando trabajas en equipo. El modelo de **control de versiones distribuido** permite que cada persona tenga una copia completa del repositorio.

### Control de Versiones Centralizado vs Distribuido

**Centralizado** (antiguo):
```
        Servidor Central
              ↓
    ┌─────────┼─────────┐
Usuario 1  Usuario 2  Usuario 3
```
- Un solo punto de fallo
- Requiere conexión constante

**Distribuido** (Git):
```
    Repo Local 1 ←→ GitHub ←→ Repo Local 2
                      ↕
                 Repo Local 3
```
- Cada persona tiene el historial completo
- Trabaja sin conexión
- Múltiples backups naturales

---

## Especificación de Remotos

Un **remoto** es una versión de tu repositorio alojada en internet (generalmente en GitHub, GitLab o Bitbucket).

### Ver Remotos

```bash
# Listar remotos
git remote -v

# Resultado típico:
# origin  https://github.com/usuario/proyecto.git (fetch)
# origin  https://github.com/usuario/proyecto.git (push)
```

**origin**: Es el nombre predeterminado para el remoto principal.

---

## GitHub.com: Tu Repositorio en la Nube

**GitHub** es una plataforma que aloja repositorios Git y añade:

- **Colaboración**: Pull requests, issues, proyectos
- **Visualización**: Interfaz web para explorar código
- **CI/CD**: Automatización con GitHub Actions
- **Comunidad**: Millones de proyectos open source
- **Portafolio**: Tu perfil muestra tu trabajo

### Crear un Repositorio en GitHub

1. Ve a https://github.com
2. Clic en el botón "+" arriba a la derecha
3. Selecciona "New repository"
4. Dale un nombre: `mi-primer-proyecto`
5. Elige público o privado
6. **NO** marques "Initialize with README" (ya tienes uno local)
7. Clic en "Create repository"

---

## Añadiendo un Remoto

Después de crear el repo en GitHub:

```bash
# Añadir el remoto
git remote add origin https://github.com/tu-usuario/mi-primer-proyecto.git

# Verificar
git remote -v
```

---

## Subiendo Cambios: git push

**Push** = "empujar" tus commits locales al repositorio remoto.

```bash
# Primera vez (establece conexión)
git push -u origin main

# Después, simplemente:
git push
```

### Qué Hace Push

```
TU COMPUTADORA                    GITHUB
     main                          main
      ↓                             ↓
[A] → [B] → [C] → [D]  ────push───→ [A] → [B] → [C] → [D]
```

---

## Descargando Cambios: git pull

**Pull** = "jalar" cambios del remoto a tu repositorio local.

```bash
# Descargar y fusionar cambios
git pull

# Equivale a:
# git fetch (descargar)
# git merge (fusionar)
```

### Qué Hace Pull

```
TU COMPUTADORA                    GITHUB
     main                          main
      ↓                             ↓
[A] → [B] → [C]  ←────pull──── [A] → [B] → [C] → [D] → [E]
```

Después del pull, tu local tendrá [D] y [E] también.

---

## Clonando un Repositorio: git clone

**Clone** crea una copia completa de un repositorio remoto en tu computadora.

```bash
# Clonar un repositorio
git clone https://github.com/usuario/proyecto.git

# Clonar con un nombre diferente
git clone https://github.com/usuario/proyecto.git mi-copia-local
```

### Cuándo Usar Clone

- Unirse a un proyecto existente
- Copiar proyectos open source
- Trabajar en una nueva computadora
- Colaborar con un compañero de equipo

---

## Timeline de Trabajo en Equipo: Ejemplo Práctico

### Escenario: Desarrollo de una Landing Page

**Equipo**: Ana (diseñadora front-end) y Carlos (desarrollador)

**Proyecto**: Crear una landing page para una cafetería

**Objetivo**: Ana trabaja en el diseño/estilos, Carlos en la funcionalidad del formulario de contacto

### Setup Inicial (Día 1 - Lunes)

**Carlos** (líder del proyecto):

```bash
# 1. Crear el proyecto localmente
mkdir cafeteria-landing
cd cafeteria-landing
git init

# 2. Crear estructura básica
echo "# Landing Cafetería La Esquina" > README.md
mkdir css js
touch index.html css/style.css js/app.js

# 3. Hacer commit inicial
git add .
git commit -m "Inicializar proyecto con estructura básica"

# 4. Crear repo en GitHub y subirlo
git remote add origin https://github.com/carlos/cafeteria-landing.git
git push -u origin main
```

**Ana** (se une al proyecto):

```bash
# 1. Clonar el repositorio
git clone https://github.com/carlos/cafeteria-landing.git
cd cafeteria-landing

# 2. Verificar que todo está bien
git log
git branch
```

---

### Desarrollo Paralelo (Día 2 - Martes)

**Ana** trabaja en el diseño:

```bash
# 1. Crear rama para su trabajo
git checkout -b feature-diseno-header

# 2. Trabajar en index.html y style.css
# (Añade HTML del header con logo y navegación)
# (Añade estilos para el header)

# 3. Hacer commits frecuentes
git add index.html css/style.css
git commit -m "Añadir estructura HTML del header"

# 4. Continuar trabajando
# (Añade más estilos)
git add css/style.css
git commit -m "Estilizar header con colores de marca"

# 5. Subir su rama a GitHub
git push -u origin feature-diseno-header
```

**Carlos** trabaja en el formulario (al mismo tiempo):

```bash
# 1. Crear su propia rama
git checkout -b feature-formulario-contacto

# 2. Trabajar en el formulario
# (Añade HTML del formulario en index.html)
# (Añade validación en js/app.js)

# 3. Hacer commits
git add index.html js/app.js
git commit -m "Añadir formulario de contacto con validación"

# 4. Subir su rama
git push -u origin feature-formulario-contacto
```

**Estado en GitHub**:
```
main:                     [A: commit inicial]
                               ↓
feature-diseno-header:         [B] → [C]
                               ↓
feature-formulario-contacto:   [D]
```

---

### Integración (Día 3 - Miércoles Mañana)

**Ana** termina primero y hace **Pull Request** en GitHub:

1. Va a GitHub.com
2. Clic en "Pull requests" → "New pull request"
3. Base: `main` ← Compare: `feature-diseno-header`
4. Título: "Añadir diseño del header"
5. Descripción: "Header con logo, navegación y estilos de marca"
6. Clic en "Create pull request"

**Carlos** revisa el código de Ana:

1. Ve el Pull Request en GitHub
2. Revisa los cambios línea por línea
3. Deja un comentario: "¡Se ve genial! Solo un detalle: ¿podrías aumentar el padding del header en móviles?"
4. Ana hace el ajuste:

```bash
# Ana sigue en su rama
git checkout feature-diseno-header

# Hace el cambio solicitado
# (Edita style.css)

git add css/style.css
git commit -m "Aumentar padding del header en móviles"
git push
```

**Carlos** aprueba y fusiona:

1. En GitHub, clic en "Approve"
2. Clic en "Merge pull request"
3. Clic en "Confirm merge"
4. El trabajo de Ana ahora está en `main`

---

### Actualización Local (Miércoles Tarde)

**Carlos** debe actualizar su copia local:

```bash
# 1. Volver a main
git checkout main

# 2. Descargar cambios que Ana subió
git pull

# Ahora Carlos tiene el header de Ana en su main local
```

**Ana** puede borrar su rama:

```bash
# Volver a main
git checkout main

# Descargar cambios (ya incluye su trabajo fusionado)
git pull

# Borrar rama local (ya no la necesita)
git branch -d feature-diseno-header

# Borrar rama remota
git push origin --delete feature-diseno-header
```

---

### Continuación del Trabajo (Jueves)

**Carlos** sigue con su formulario:

```bash
# 1. Volver a su rama
git checkout feature-formulario-contacto

# 2. IMPORTANTE: Actualizar su rama con los cambios de main
git merge main

# Esto trae el header de Ana a su rama
```

Si hay conflictos (ambos editaron la misma línea de `index.html`):

```bash
# Git marca el conflicto
# CONFLICT (content): Merge conflict in index.html

# Carlos abre index.html y ve:
<<<<<<< HEAD
    <div class="formulario">
=======
    <header class="header">
>>>>>>> main

# Carlos resuelve manualmente, manteniendo ambas secciones:
    <header class="header">
        <!-- código del header de Ana -->
    </header>
    <div class="formulario">
        <!-- código del formulario de Carlos -->
    </div>

# Marca como resuelto
git add index.html
git commit -m "Fusionar main con feature-formulario-contacto"

# Sube los cambios
git push
```

---

### Finalización (Viernes)

**Carlos** crea Pull Request para su formulario:

1. En GitHub: Pull Request de `feature-formulario-contacto` a `main`
2. Ana revisa y aprueba
3. Carlos fusiona

**Ambos actualizan main**:

```bash
git checkout main
git pull
```

**Estado final**:
```
main: [A] → [B] → [C] → [merge Ana] → [D] → [merge Carlos]
```

---

### Resumen del Timeline Completo

| Día | Hora | Quién | Acción | Comando |
|-----|------|-------|--------|---------|
| Lun | 10:00 | Carlos | Crea repo y sube a GitHub | `git init`, `git push` |
| Lun | 11:00 | Ana | Clona el proyecto | `git clone` |
| Mar | 09:00 | Ana | Crea rama de diseño | `git checkout -b feature-diseno-header` |
| Mar | 09:00 | Carlos | Crea rama de formulario | `git checkout -b feature-formulario-contacto` |
| Mar | 12:00 | Ana | Sube cambios | `git push` |
| Mar | 15:00 | Carlos | Sube cambios | `git push` |
| Mié | 09:00 | Ana | Crea Pull Request | (En GitHub) |
| Mié | 10:00 | Carlos | Revisa y solicita cambios | (En GitHub) |
| Mié | 11:00 | Ana | Corrige y sube | `git commit`, `git push` |
| Mié | 12:00 | Carlos | Aprueba y fusiona | (En GitHub) |
| Mié | 14:00 | Carlos | Actualiza su main local | `git pull` |
| Jue | 09:00 | Carlos | Actualiza su rama con main | `git merge main` |
| Jue | 09:30 | Carlos | Resuelve conflictos | `git add`, `git commit` |
| Vie | 10:00 | Carlos | Pull Request final | (En GitHub) |
| Vie | 11:00 | Ana | Revisa y aprueba | (En GitHub) |
| Vie | 12:00 | Ambos | Actualizan main | `git pull` |

---

## Comandos Git Más Importantes (Cheat Sheet)

### Configuración Inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Básicos

```bash
git init                          # Inicializar repositorio
git status                        # Ver estado
git add archivo.html              # Añadir archivo
git add .                         # Añadir todos los archivos
git commit -m "Mensaje"           # Crear commit
git log                           # Ver historial
git log --oneline                 # Historial resumido
```

### Ramas

```bash
git branch                        # Listar ramas
git branch nombre-rama            # Crear rama
git checkout nombre-rama          # Cambiar a rama
git checkout -b nombre-rama       # Crear y cambiar
git merge nombre-rama             # Fusionar rama
git branch -d nombre-rama         # Borrar rama local
```

### Remotos

```bash
git remote add origin URL         # Añadir remoto
git remote -v                     # Ver remotos
git push -u origin main           # Subir por primera vez
git push                          # Subir cambios
git pull                          # Descargar cambios
git clone URL                     # Clonar repositorio
```

### Útiles

```bash
git diff                          # Ver cambios no staged
git diff --staged                 # Ver cambios staged
git restore archivo.html          # Descartar cambios
git restore --staged archivo.html # Quitar de staging
git stash                         # Guardar cambios temporalmente
git stash pop                     # Recuperar cambios guardados
```

---

## Ejercicios Prácticos

### Ejercicio 1: Tu Primer Repositorio

1. Crea una carpeta llamada `portfolio`
2. Inicializa Git
3. Crea `index.html` con tu nombre
4. Haz commit de los cambios
5. Crea una cuenta en GitHub
6. Crea un repositorio en GitHub llamado `portfolio`
7. Conecta tu repo local con GitHub
8. Sube tus cambios

### Ejercicio 2: Trabajo con Ramas

1. En tu proyecto `portfolio`, crea una rama `feature-about`
2. Añade una sección "Sobre mí" en el HTML
3. Haz commit
4. Vuelve a `main`
5. Fusiona `feature-about` en `main`
6. Sube los cambios a GitHub

### Ejercicio 3: Colaboración (con un compañero)

1. Uno de ustedes crea un repo nuevo en GitHub con un `index.html` básico
2. Añade a tu compañero como colaborador (Settings → Collaborators)
3. El otro clona el repositorio
4. Cada uno crea su propia rama y añade contenido diferente
5. Suban sus ramas a GitHub
6. Creen Pull Requests
7. Revisen el código del otro
8. Fusionen los cambios
9. Ambos actualicen su `main` local

---

## Recursos Adicionales

- **Documentación oficial**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com/
- **Git Visualizer**: https://git-school.github.io/visualizing-git/
- **Practice Git**: https://learngitbranching.js.org/

---

## Conclusión

Git es una herramienta poderosa que:
- Te protege de perder trabajo
- Facilita la colaboración en equipo
- Es esencial en la industria del software
- Mejora con la práctica

**Próximos pasos**:
1. Practica los comandos básicos diariamente
2. Usa Git en todos tus proyectos
3. Colabora con otros para aprender el flujo completo
4. Explora características avanzadas (rebase, cherry-pick, etc.)

¡Recuerda: Git parece complicado al principio, pero con práctica se vuelve natural!
