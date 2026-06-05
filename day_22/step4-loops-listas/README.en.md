[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🔁 Step 4: Loops and Lists

## 🎯 Objective

Iterate over repetitive data without copying code, using `for`, `while`, and utilities like `range` and `enumerate`.

---

## ✅ `for` loop with lists

```python
nombres = ["Ana", "Luis", "Marta"]

for nombre in nombres:
    print("Hola", nombre)
```

---

## 🔢 `range()` to repeat N times

```python
for i in range(5):
    print(i)
```

Result: `0, 1, 2, 3, 4`

---

## 🏷️ `enumerate()` for index + value

```python
frutas = ["manzana", "pera", "plátano"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

---

## 🔄 `while` loop

```python
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
```

Use `while` when you don't know exactly how many iterations there will be.

---

## ⛔ `break` and `continue`

```python
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue   # skip 3
    if n == 5:
        break      # end the loop
    print(n)
```

---

## 🧪 Exercises

1. Iterate over a list of grades and print each one
2. Count how many grades are >= 5
3. Ask the user for numbers until they enter `0` (using `while`)
4. Print only the even numbers from 1 to 20

---

## ⚠️ Common mistakes

1. Creating infinite loops with `while`
2. Updating the counter in the wrong direction
3. Using `break` when `continue` was needed (or vice versa)
