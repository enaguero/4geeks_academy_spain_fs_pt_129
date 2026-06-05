[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 📦 Step 3: Lists in Python

## 🎯 Objective

Learn to store multiple values in a single variable and manipulate them safely.

---

## 📋 Create lists

```python
nombres = ["Ana", "Luis", "Marta"]
numeros = [10, 20, 30, 40]
mixta = ["Python", 3, True]
```

---

## 🔎 Access by index

```python
frutas = ["manzana", "pera", "plátano"]

print(frutas[0])   # manzana
print(frutas[-1])  # plátano
```

---

## ✂️ Slicing

```python
numeros = [1, 2, 3, 4, 5, 6]

print(numeros[1:4])   # [2, 3, 4]
print(numeros[:3])    # [1, 2, 3]
print(numeros[3:])    # [4, 5, 6]
```

---

## 🛠️ Most-used methods

```python
tareas = ["estudiar", "entrenar"]

tareas.append("leer")
print(tareas)  # ['estudiar', 'entrenar', 'leer']

tareas.remove("entrenar")
print(tareas)  # ['estudiar', 'leer']

ultima = tareas.pop()
print(ultima)  # leer
print(tareas)  # ['estudiar']
```

Sorting:

```python
nums = [8, 3, 10, 1]
nums.sort()
print(nums)  # [1, 3, 8, 10]
```

---

## 🧪 Exercises

1. Create a list with 5 favorite foods
2. Add a new food using `append()`
3. Remove one using `remove()`
4. Print the first and the last item
5. Sort a list of numbers from smallest to largest

---

## ⚠️ Common mistakes

1. Trying to access indices that don't exist
2. Confusing `remove(valor)` with `pop(indice)`
3. Modifying a list while iterating over it without care
