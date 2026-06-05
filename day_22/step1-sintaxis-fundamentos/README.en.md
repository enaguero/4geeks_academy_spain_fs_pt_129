[🇪🇸 Español](README.md) | 🇬🇧 **English**

# ✍️ Step 1: Python Syntax and Fundamentals

## 🎯 Objective

Write your first Python programs by understanding variables, types, and basic operations.

---

## 🧱 Key syntax rules

1. Python uses **indentation** (spaces) for code blocks.
2. You don't need `;` at the end of a line.
3. Variables are assigned with `=`.

Example:

```python
nombre = "Ana"
edad = 28
print(nombre)
print(edad)
```

---

## 📦 Basic data types

```python
nombre = "Carlos"      # str
edad = 31               # int
altura = 1.78           # float
es_estudiante = True    # bool
```

Check a variable's type:

```python
print(type(nombre))
print(type(edad))
```

---

## 🖨️ Input and output

```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

`input()` returns a string. For numbers, convert it:

```python
edad = int(input("Tu edad: "))
print("El próximo año tendrás", edad + 1)
```

---

## 🔢 Basic operators

```python
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division (float)
print(a // b)  # integer division
print(a % b)   # modulo
```

---

## 🆚 Mini bridge with JavaScript

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

Key changes:
- No `{}`
- No `;`
- Indentation is required

---

## 🧪 Short exercises

1. Ask for a name and a city, print: `"Hola <nombre>, vives en <ciudad>"`
2. Ask for two numbers and print their sum, difference, and product
3. Ask for an age and print how many years are left until 100

---

## ⚠️ Common mistakes

1. Forgetting to convert `input()` to a number when needed
2. Mixing tabs and spaces in the same file
3. Writing `===` like in JavaScript (Python uses `==`)
