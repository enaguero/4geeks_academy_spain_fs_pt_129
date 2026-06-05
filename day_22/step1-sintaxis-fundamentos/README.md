🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# ✍️ Step 1: Sintaxis y Fundamentos de Python

## 🎯 Objetivo

Escribir tus primeros programas en Python entendiendo variables, tipos y operaciones básicas.

---

## 🧱 Reglas clave de sintaxis

1. Python usa **indentación** (espacios) para bloques de código.
2. No necesitas `;` al final de línea.
3. Variables se asignan con `=`.

Ejemplo:

```python
nombre = "Ana"
edad = 28
print(nombre)
print(edad)
```

---

## 📦 Tipos de datos básicos

```python
nombre = "Carlos"      # str
edad = 31               # int
altura = 1.78           # float
es_estudiante = True    # bool
```

Ver tipo de dato:

```python
print(type(nombre))
print(type(edad))
```

---

## 🖨️ Entrada y salida

```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

`input()` devuelve string. Para números, convierte:

```python
edad = int(input("Tu edad: "))
print("El próximo año tendrás", edad + 1)
```

---

## 🔢 Operadores básicos

```python
a = 10
b = 3

print(a + b)   # suma
print(a - b)   # resta
print(a * b)   # multiplicación
print(a / b)   # división (float)
print(a // b)  # división entera
print(a % b)   # módulo
```

---

## 🆚 Mini puente con JavaScript

```javascript
// JavaScript
let nombre = "Ana";
if (nombre === "Ana") {
  console.log("Hola");
}
```

```python
# Python
nombre = "Ana"
if nombre == "Ana":
    print("Hola")
```

Cambios clave:
- No `{}`
- No `;`
- Indentación obligatoria

---

## 🧪 Ejercicios cortos

1. Pide nombre y ciudad, imprime: `"Hola <nombre>, vives en <ciudad>"`
2. Pide dos números e imprime suma, resta y multiplicación
3. Pide edad e imprime cuántos años faltan para 100

---

## ⚠️ Errores comunes

1. Olvidar convertir `input()` a número cuando hace falta
2. Mezclar tabs y espacios en el mismo archivo
3. Escribir `===` como en JavaScript (en Python se usa `==`)
