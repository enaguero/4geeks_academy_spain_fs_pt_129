[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Tutorial: The Terminal, Commands, and Paths

## 📺 Reference Videos

- [¿Qué es la terminal?](https://www.youtube.com/watch?v=3xQRR3iNqDQ)
- [¿Qué son los comandos?](https://www.youtube.com/watch?v=f0K0jA7O9w8)
- [Rutas relativas y absolutas](https://youtu.be/e9NjhfsdEGA?si=bxXnOoZHZbK5MkPU)

---

## 🗂️ The File System and Folders

Before you start using the terminal, it's important to understand how your computer is organized.

### What is a file system?

When you buy a computer, it already comes with an **organized folder structure** installed by default. This structure is like a big tree of folders that contains everything the operating system needs to work.

As you use your computer, you add your own files and folders to this structure (documents, photos, projects, etc.).

### Basic system structure

The whole file system starts from a root folder (the "base" of the tree):

**On Mac/Linux:** The root is called `/`  
**On Windows:** The root is usually `C:\`

### Main system folders (Mac/Linux)

From the root (`/`), the system has several important folders:

```
/
├── Users/           # Folder for all users
│   ├── tu_nombre/   # Your personal folder (where YOUR files live)
│   │   ├── Documents/
│   │   ├── Downloads/
│   │   ├── Desktop/
│   │   └── Pictures/
│   └── otro_usuario/
├── Applications/    # Installed programs (Chrome, VS Code, etc.)
├── System/          # Operating system files (don't touch)
├── Library/         # System configuration
├── tmp/             # Temporary files
└── etc/             # Global configuration
```

### Your personal folder

The most important folder for you is **your personal folder** (also called "home"):

```
/Users/tu_nombre/     # On Mac/Linux
C:\Users\tu_nombre\   # On Windows
```

This is where you store:
- 📄 Documents (`Documents/`)
- 📥 Downloads (`Downloads/`)
- 🖼️ Pictures (`Pictures/`)
- 🖥️ Desktop (`Desktop/`)
- 💻 Your coding projects

### Visual analogy

Think of the file system as an **apartment building**:

- **The root (`/`)** is the whole building
- **`/Users/`** is a floor where all the users live
- **`/Users/tu_nombre/`** is YOUR specific apartment
- **`/Users/tu_nombre/Documents/`** is a room inside your apartment
- **`/Users/tu_nombre/Documents/proyecto.txt`** is an object inside that room

### Why is it important to understand this?

1. **When you open the terminal**, you're always "located" in some folder (usually your personal folder)
2. **Commands operate** on the folder where you're located
3. **To move between folders** you need to understand this structure
4. **Your coding projects** will live somewhere inside this structure

### Practical example

If you create a web project in your personal folder:

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

The full path to the `style.css` file would be:
```
/Users/tu_nombre/projects/mi_web/css/style.css
```

---

## 🖥️ What is the Terminal?

The **terminal** (also called console or command line) is a text-based interface that lets us communicate directly with our computer's operating system.

### Why use it?

- It's **faster** than using the graphical interface
- It lets you **automate** repetitive tasks
- It's the main way to work with servers and developer tools
- Many programming tools only work from the terminal

### Visual example:

**Graphical Interface:** Clicking folders, dragging files  
**Terminal:** Typing commands like `cd carpeta` or `mkdir nueva_carpeta`

---

## ⌨️ What Are Commands?

**Commands** are instructions we type in the terminal to make the computer perform specific actions.

### Basic command structure:

```bash
command [options] [arguments]
```

### Essential basic commands:

#### 1. **pwd** (Print Working Directory)
Shows the path where you are currently located.

```bash
pwd
# Example result: /Users/tu_usuario/Documents
```

#### 2. **ls** (List)
Lists the files and folders in the current directory.

```bash
ls
# Shows: archivo1.txt  carpeta1/  imagen.png

ls -l
# Shows detailed info (permissions, size, date)

ls -a
# Shows hidden files too
```

#### 3. **cd** (Change Directory)
Changes directory (folder).

```bash
cd Documents        # Enter the Documents folder
cd ..              # Go up one level (parent folder)
cd ~               # Go to your personal folder
cd /               # Go to the system root
```

#### 4. **mkdir** (Make Directory)
Creates a new folder.

```bash
mkdir mi_proyecto
mkdir -p carpeta1/carpeta2/carpeta3  # Creates nested folders
```

#### 5. **touch**
Creates an empty file.

```bash
touch index.html
touch style.css script.js
```

#### 6. **rm** (Remove)
Removes files or folders.

```bash
rm archivo.txt              # Remove a file
rm -r carpeta/              # Remove a folder and its contents
rm -rf carpeta/             # Force removal (use with caution!)
```

#### 7. **cp** (Copy)
Copies files or folders.

```bash
cp archivo.txt copia.txt
cp -r carpeta1/ carpeta2/
```

#### 8. **mv** (Move)
Moves or renames files/folders.

```bash
mv archivo.txt nueva_carpeta/        # Move the file
mv nombre_viejo.txt nombre_nuevo.txt # Rename the file
```

#### 9. **cat**
Shows the contents of a file.

```bash
cat index.html
```

#### 10. **clear**
Clears the terminal screen.

```bash
clear
```

---

## 📂 Paths: Relative vs Absolute

A **path** is the location of a file or folder in the file system.

### 🔹 Absolute Path

The **full** path from the system root to the file.

**In the operating system:**

```bash
/Users/erwin/projects/mi_web/index.html
```

- Always starts from the root (`/` on Mac/Linux, `C:\` on Windows)
- It always works the same no matter where you are
- It's like giving a full address: "123 Main Street, Madrid, Spain"

**Examples:**

```bash
cd /Users/erwin/Documents
cat /etc/hosts
ls /var/www/html
```

### 🔹 Relative Path

The path **relative** to where you currently are.

**In the operating system:**

If you're in `/Users/erwin/projects/` and want to go to `mi_web`:

```bash
cd mi_web              # Relative path
cd ./mi_web            # Explicit relative path (same effect)
cd ../otros_proyectos  # Go up one level and into another folder
```

- It depends on your current location
- Use `.` to refer to the current directory
- Use `..` to refer to the parent directory
- It's like giving directions: "two blocks down, turn right"

### Important symbols:

| Symbol | Meaning |
|---------|------------|
| `/` | System root (or folder separator) |
| `~` | Your personal folder |
| `.` | Current directory |
| `..` | Parent directory (one level up) |

---

## 🌐 Paths in Web Development (HTML, CSS, JS)

When we work with web pages, we also use paths to link files to each other.

### Typical web project structure:

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

### 🔹 Relative Paths in HTML

Relative paths are the most common in web development because the project can be moved to different servers without breaking links.

**Example: index.html**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
    
    <!-- Relative path to CSS (enters the css folder) -->
    <link rel="stylesheet" href="css/style.css">
    
    <!-- Another CSS in the same folder -->
    <link rel="stylesheet" href="css/reset.css">
</head>
<body>
    <!-- Relative path to image (enters the images folder) -->
    <img src="images/logo.png" alt="Logo">
    
    <!-- Link to another page in the same directory -->
    <a href="about.html">About</a>
    
    <!-- Relative path to JavaScript (enters the js folder) -->
    <script src="js/script.js"></script>
</body>
</html>
```

**If about.html is inside a folder:**

```
mi_proyecto/
├── index.html
├── pages/
│   └── about.html
└── css/
    └── style.css
```

**In index.html:**

```html
<a href="pages/about.html">About</a>
```

**In pages/about.html to get back to index.html:**

```html
<!-- Go up one level with ../ -->
<a href="../index.html">Home</a>

<!-- To use the CSS, also go up one level -->
<link rel="stylesheet" href="../css/style.css">
```

### 🔹 Absolute Paths in HTML

Absolute paths in web can be:

**1. From the server root (start with `/`):**

```html
<link rel="stylesheet" href="/css/style.css">
<img src="/images/logo.png" alt="Logo">
```

**2. Full URL:**

```html
<link rel="stylesheet" href="https://ejemplo.com/css/style.css">
<img src="https://ejemplo.com/images/logo.png" alt="Logo">
```

### 📋 Practical Comparison

Suppose this structure:

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

**From index.html:**

```html
<!-- Relative -->
<link rel="stylesheet" href="assets/css/style.css">
<img src="assets/images/bg.jpg">

<!-- Absolute (from server root) -->
<link rel="stylesheet" href="/assets/css/style.css">
<img src="/assets/images/bg.jpg">
```

**From pages/contact.html:**

```html
<!-- Relative (go up one level with ../) -->
<link rel="stylesheet" href="../assets/css/style.css">
<img src="../assets/images/bg.jpg">
<a href="../index.html">Back to home</a>

<!-- Absolute (from server root) -->
<link rel="stylesheet" href="/assets/css/style.css">
<img src="/assets/images/bg.jpg">
<a href="/index.html">Back to home</a>
```

### ✅ Best Practices

1. **Use relative paths** in local projects and small sites
2. **Use absolute paths from the root** (`/`) in large projects to avoid confusion
3. **Keep an organized structure** with folders for CSS, JS, and images
4. **Test your links** before deploying to production
5. **Use descriptive names** without spaces (use hyphens: `mi-archivo.html`)

---

## 🎯 Hands-on Exercises

### Exercise 1: Basic commands

Create this structure using only commands:

```bash
mkdir mi_primer_proyecto
cd mi_primer_proyecto
mkdir css js images
touch index.html
touch css/style.css
touch js/script.js
ls -R
```

### Exercise 2: Navigation

```bash
# You're in mi_primer_proyecto/
cd css              # Enter css
pwd                 # Where are you?
cd ..               # Go back to mi_primer_proyecto
cd js               # Enter js
cd ../css           # From js, go to css
cd ~                # Go to your personal folder
```

### Exercise 3: Paths in HTML

Create an `index.html` with correct links to:
- A CSS file in the `css/` folder
- A JS file in the `js/` folder
- An image in the `images/` folder
- Another HTML page in the `pages/` folder

---

## 📚 Summary

| Concept | Definition | Example |
|----------|------------|---------||
| **Terminal** | Text-based interface for commands | Mac Terminal, CMD on Windows |
| **Command** | Instruction for the system | `ls`, `cd`, `mkdir` |
| **Absolute Path (System)** | From the system root | `/Users/erwin/proyecto/index.html` |
| **Relative Path (System)** | From the current location | `../carpeta/archivo.txt` |
| **Relative Path (Web)** | From the current file | `css/style.css`, `../images/logo.png` |
| **Absolute Path (Web)** | From server root or full URL | `/css/style.css`, `https://site.com/img.png` |

---

## 🚀 Next Steps

1. Practice the basic commands by creating and navigating folders
2. Create a simple web project with the recommended folder structure
3. Experiment with relative paths in HTML
4. Learn Git and GitHub (next topic)

Remember: practice makes perfect! 💪
