# Resolución de Conflictos en Git: Ejemplo Completo

## Introducción

Este documento es una guía práctica diseñada para estudiantes que están aprendiendo a trabajar en equipo con Git. El objetivo principal es **entender cómo y por qué surgen los conflictos** cuando varios desarrolladores modifican el mismo archivo, y más importante aún, **cómo resolverlos de manera efectiva**.

A lo largo de este tutorial encontrarás:
- Un **diagrama visual** que muestra el flujo completo del proceso
- Un **timeline realista** con horarios y pasos específicos que seguirían dos desarrolladores
- **Ejemplos de código** que muestran exactamente cómo se ve un conflicto y cómo resolverlo
- **Comandos prácticos** que necesitarás en situaciones reales

Este es un escenario muy común en el mundo profesional: dos desarrolladores trabajan en ramas diferentes, uno hace merge primero sin problemas, y el segundo debe resolver conflictos antes de poder integrar su código. ¡No te preocupes! Aunque parezca complicado al principio, resolver conflictos es una habilidad fundamental que dominarás con práctica.

## Conceptos Fundamentales: Merge vs Rebase

Antes de ver el ejemplo completo, es importante entender las dos formas principales de integrar cambios en Git: **merge** y **rebase**. Ambas sirven para combinar ramas, pero lo hacen de manera diferente.

### Git Merge

**¿Qué es?**

`git merge` combina los cambios de dos ramas creando un **nuevo commit de merge**. Es como unir dos caminos que se separaron, manteniendo el historial de ambos.

**¿Cómo funciona?**

Cuando haces merge, Git:
1. Encuentra el commit común más reciente entre ambas ramas (el "ancestro común")
2. Compara los cambios de ambas ramas desde ese punto
3. Combina los cambios y crea un nuevo commit que tiene dos "padres"

**Ventajas:**
- Mantiene el historial completo y verdadero de cómo se desarrolló el proyecto
- Es más seguro y fácil de entender para principiantes
- Los conflictos se resuelven una sola vez

#### Ejemplo Visual: Situación Inicial

```mermaid
gitGraph
    commit id: "A (Initial)"
    commit id: "B (Add README)"
    branch feature
    checkout feature
    commit id: "C (Add login)"
    commit id: "D (Add logout)"
    checkout main
    commit id: "E (Fix bug)"
```

**Comandos para crear este escenario:**

```bash
# 1. Crear el repositorio y commits iniciales
git init
echo "Project" > README.md
git add . && git commit -m "A: Initial commit"          # Commit A
echo "# Features" >> README.md
git add . && git commit -m "B: Add README"              # Commit B

# 2. Crear rama feature y hacer commits
git checkout -b feature
echo "login()" > auth.js
git add . && git commit -m "C: Add login"               # Commit C
echo "logout()" >> auth.js
git add . && git commit -m "D: Add logout"              # Commit D

# 3. Mientras tanto, en main hubo un cambio
git checkout main
echo "fix" > bugfix.js
git add . && git commit -m "E: Fix bug"                 # Commit E
```

#### Después de Git Merge

```mermaid
gitGraph
    commit id: "A (Initial)"
    commit id: "B (Add README)"
    branch feature
    checkout feature
    commit id: "C (Add login)"
    commit id: "D (Add logout)"
    checkout main
    commit id: "E (Fix bug)"
    merge feature id: "F (Merge)" tag: "2 padres"
    commit id: "G (Continue)"
```

**Comandos para hacer el merge:**

```bash
# Estamos en main, queremos integrar feature
git checkout main
git merge feature

# Git crea automáticamente el commit F
# Si hay conflictos:
# 1. Editas los archivos en conflicto
# 2. git add archivo-resuelto.js
# 3. git commit -m "F: Merge feature into main"

# Continuar trabajando
echo "new feature" > new.js
git add . && git commit -m "G: Continue work"           # Commit G
```

**Ver el historial resultante:**

```bash
git log --oneline --graph --all
```

**Salida:**
```
*   G - Continue work
*   F - Merge feature into main (2 padres: D y E)
|\  
| * D - Add logout
| * C - Add login
* | E - Fix bug
|/  
* B - Add README
* A - Initial commit
```

Nota cómo el commit F tiene **dos líneas** que suben ("|\\"): una hacia D y otra hacia E.

### Git Rebase

**¿Qué es?**

`git rebase` "reescribe" el historial moviendo tus commits para que parezca que empezaste tu trabajo desde el último commit de la otra rama. Es como decir: "quiero que mis cambios estén *después* de los cambios de main".

**¿Cómo funciona?**

Cuando haces rebase, Git:
1. Guarda temporalmente tus commits
2. Actualiza tu rama al último commit de la rama base
3. Aplica tus commits uno por uno encima

**Ventajas:**
- Historial lineal y más limpio (sin commits de merge)
- Más fácil de leer y seguir
- Profesional para proyectos open source

**Desventajas:**
- Reescribe el historial (puede ser peligroso en ramas compartidas)
- Si hay conflictos, debes resolverlos commit por commit
- Requiere más experiencia

#### Ejemplo Visual: Situación Inicial (igual que merge)

```mermaid
gitGraph
    commit id: "A (Initial)"
    commit id: "B (Add README)"
    branch feature
    checkout feature
    commit id: "C (Add login)"
    commit id: "D (Add logout)"
    checkout main
    commit id: "E (Fix bug)"
```

**Comandos para crear este escenario:**

```bash
# Mismo escenario que el ejemplo de merge
git init
echo "Project" > README.md
git add . && git commit -m "A: Initial commit"          # Commit A
echo "# Features" >> README.md
git add . && git commit -m "B: Add README"              # Commit B

git checkout -b feature
echo "login()" > auth.js
git add . && git commit -m "C: Add login"               # Commit C
echo "logout()" >> auth.js
git add . && git commit -m "D: Add logout"              # Commit D

git checkout main
echo "fix" > bugfix.js
git add . && git commit -m "E: Fix bug"                 # Commit E
```

#### Después de Git Rebase

```mermaid
gitGraph
    commit id: "A (Initial)"
    commit id: "B (Add README)"
    commit id: "E (Fix bug)"
    commit id: "C' (Add login)" type: HIGHLIGHT
    commit id: "D' (Add logout)" type: HIGHLIGHT tag: "Lineal!"
```

**Comandos para hacer el rebase:**

```bash
# Estamos en feature, queremos "mover" nuestros commits después de E
git checkout feature
git rebase main

# Git hace internamente:
# 1. Guarda temporalmente C y D
# 2. Mueve feature a donde está main (commit E)
# 3. Aplica C creando C' (nuevo hash)
# 4. Aplica D creando D' (nuevo hash)

# Si hay conflictos durante la aplicación de C:
#   - Editas y resuelves el conflicto
#   - git add archivo-resuelto.js
#   - git rebase --continue
# Si hay conflictos durante la aplicación de D:
#   - Repites el proceso
#   - git add archivo-resuelto.js
#   - git rebase --continue

# Para abortar en cualquier momento:
git rebase --abort
```

**Ver el historial resultante:**

```bash
git log --oneline --graph --all
```

**Salida:**
```
* D' - Add logout (nuevo hash: abc123)
* C' - Add login (nuevo hash: def456)
* E - Fix bug
* B - Add README
* A - Initial commit
```

**Comparación de hashes ANTES y DESPUÉS del rebase:**

```bash
# ANTES del rebase (en feature):
# C = 789xyz
# D = 456uvw

# DESPUÉS del rebase (en feature):
# C' = def456  (DIFERENTE! Mismo contenido, nuevo hash)
# D' = abc123  (DIFERENTE! Mismo contenido, nuevo hash)
```

Nota cómo:
1. El historial es **completamente lineal** (no hay bifurcaciones)
2. C' y D' son **nuevos commits** con hashes diferentes
3. Los commits originales C y D ya no existen en el historial

### ¿Cuándo usar cada uno?

| Situación | Usar |
|-----------|------|
| Eres principiante | **Merge** |
| Trabajas en equipo en una rama compartida | **Merge** |
| Quieres mantener historial completo | **Merge** |
| Trabajas solo en tu rama | **Rebase** |
| Quieres historial limpio antes de hacer PR | **Rebase** |
| Proyecto open source con lineamientos estrictos | **Rebase** |

**Regla de oro**: ¡**NUNCA** hagas rebase de commits que ya has compartido (pushed) a una rama pública donde otros trabajan!

## Diagrama del Flujo de Trabajo

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Feature: base code"
    
    branch rama-A
    branch rama-B
    
    checkout rama-A
    commit id: "Dev A: modifica header"
    commit id: "Dev A: añade estilos"
    
    checkout main
    merge rama-A tag: "Merge sin conflicto ✓"
    
    checkout rama-B
    commit id: "Dev B: modifica header (conflicto!)"
    commit id: "Dev B: añade footer"
    
    checkout main
    commit id: "Intento merge rama-B ✗"
    
    checkout rama-B
    commit id: "Dev B: resuelve conflicto"
    
    checkout main
    merge rama-B tag: "Merge exitoso ✓"
```

## Timeline Realista

### Día 1 - Lunes (Mañana)
**09:00** - Ambos desarrolladores empiezan a trabajar

**Desarrollador A:**
```bash
git checkout -b rama-A
# Trabaja en el archivo index.html
```

**Desarrollador B:**
```bash
git checkout -b rama-B
# Trabaja en el mismo archivo index.html (¡sin saberlo!)
```

### Día 1 - Lunes (Tarde)
**16:00** - Desarrollador A termina primero

```bash
# Desarrollador A en rama-A
git add .
git commit -m "feat: actualiza el header con nuevo logo"
git push origin rama-A
```

**16:30** - Desarrollador A crea Pull Request y es aprobado

```bash
# En GitHub/GitLab: Merge rama-A → main
# El main ahora tiene los cambios de A
```

### Día 2 - Martes (Mañana)
**10:00** - Desarrollador B termina su trabajo

```bash
# Desarrollador B en rama-B
git add .
git commit -m "feat: mejora el header y añade footer"
git push origin rama-B
```

**10:15** - Desarrollador B crea Pull Request pero... ¡CONFLICTO! ⚠️

### Día 2 - Martes (Resolución)
**10:30** - Desarrollador B empieza a resolver el conflicto

```bash
# Paso 1: Actualizar main local
git checkout main
git pull origin main

# Paso 2: Volver a rama-B y hacer rebase/merge
git checkout rama-B
git merge main
# ¡Git detecta conflicto en index.html!
```

**10:35** - Git muestra el conflicto en `index.html`:

```html
<header>
<<<<<<< HEAD (rama-B)
    <h1>Mi Sitio Web - Versión 2.0</h1>
    <img src="logo-blue.png" alt="Logo">
=======
    <h1>Mi Sitio Web Renovado</h1>
    <img src="logo-new.png" alt="Logo">
>>>>>>> main (rama-A)
</header>
```

**10:45** - Desarrollador B resuelve manualmente:

```html
<header>
    <h1>Mi Sitio Web Renovado - Versión 2.0</h1>
    <img src="logo-new.png" alt="Logo">
</header>
```

**10:50** - Completa el merge:

```bash
git add index.html
git commit -m "fix: resuelve conflicto de merge con rama-A"
git push origin rama-B
```

**11:00** - Pull Request se actualiza y ahora se puede mergear sin conflictos ✓

```bash
# En GitHub/GitLab: Merge rama-B → main
```

## Ejemplo Práctico Completo

### Estado Inicial: `index.html` en main

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Sitio</title>
</head>
<body>
    <header>
        <h1>Mi Sitio Web</h1>
        <img src="logo.png" alt="Logo">
    </header>
    <main>
        <p>Contenido principal</p>
    </main>
</body>
</html>
```

### Cambios del Desarrollador A (rama-A)

```html
<header>
    <h1>Mi Sitio Web Renovado</h1>
    <img src="logo-new.png" alt="Logo">
</header>
```

### Cambios del Desarrollador B (rama-B)

```html
<header>
    <h1>Mi Sitio Web - Versión 2.0</h1>
    <img src="logo-blue.png" alt="Logo">
</header>
<footer>
    <p>© 2025 Mi Empresa</p>
</footer>
```

### Archivo Final Después de Resolver Conflicto

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Sitio</title>
</head>
<body>
    <header>
        <!-- Combinación de ambos cambios -->
        <h1>Mi Sitio Web Renovado - Versión 2.0</h1>
        <img src="logo-new.png" alt="Logo">
    </header>
    <main>
        <p>Contenido principal</p>
    </main>
    <footer>
        <!-- Footer de Desarrollador B se mantiene -->
        <p>© 2025 Mi Empresa</p>
    </footer>
</body>
</html>
```

## Comandos Clave para Resolver Conflictos

```bash
# 1. Ver el estado del conflicto
git status

# 2. Ver los archivos en conflicto
git diff

# 3. Después de resolver manualmente
git add archivo-resuelto.html

# 4. Continuar el merge
git commit -m "fix: resuelve conflicto"

# 5. Si quieres abortar el merge
git merge --abort

# 6. Ver quién hizo qué cambios
git log --oneline --graph --all
```

## Resumen del Timeline

| Tiempo | Acción |
|--------|--------|
| **2-3 horas** | Desarrollo en ramas paralelas |
| **15 min** | Primer merge (sin conflicto) |
| **30-45 min** | Detectar + resolver conflicto |
| **Total: ~3-4 horas** | Para todo el proceso |

## Tips para Evitar Conflictos

1. **Comunicación**: Los devs deben avisar en qué archivos trabajan
2. **Pull frecuente**: Actualizar `main` cada mañana
3. **Ramas pequeñas**: Mergear rápido, no acumular cambios
4. **Revisar antes de push**: `git pull origin main` antes de hacer PR

## Recursos Adicionales

- [Documentación oficial de Git sobre merge](https://git-scm.com/docs/git-merge)
- [Atlassian: Tutorial de resolución de conflictos](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
- [GitHub: Resolver conflictos](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts)
