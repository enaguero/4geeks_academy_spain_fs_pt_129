[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧩 Step 5: Functions in Python

## 🎯 Objective

Create reusable blocks of code to write cleaner and more maintainable programs.

---

## 🛠️ Basic syntax

```python
def saludar():
    print("Hola")

saludar()
```

---

## 🎛️ Parameters and arguments

```python
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Ana")
saludar_persona("Pedro")
```

---

## ↩️ Returning values with `return`

```python
def sumar(a, b):
    return a + b

resultado = sumar(4, 6)
print(resultado)  # 10
```

Without `return`, the function returns `None`.

---

## 🧩 Default parameters

```python
def saludar(nombre, idioma="es"):
    if idioma == "es":
        return f"Hola {nombre}"
    if idioma == "en":
        return f"Hello {nombre}"
    return f"Saludo no disponible para {nombre}"

print(saludar("Ana"))
print(saludar("John", "en"))
```

---

## 📍 Basic scope

```python
mensaje = "global"

def demo():
    mensaje = "local"
    print(mensaje)

print(mensaje)  # global
demo()          # local
print(mensaje)  # global
```

The local variable only exists inside the function.

---

## 🧪 Exercises

1. Create a function `es_par(numero)` that returns `True/False`
2. Create a function `calcular_descuento(precio, porcentaje)`
3. Create a function `clasificar_nota(nota)` that returns text
4. Create a function `resumen_lista(lista)` that returns the number of elements

---

## ⚠️ Common mistakes

1. Confusing `print()` with `return`
2. Defining a function but forgetting to call it
3. Not validating input types when the function needs it
