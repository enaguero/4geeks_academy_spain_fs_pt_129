🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🔁 Step 4: Loops y Listas

## 🎯 Objetivo

Recorrer datos repetitivos sin copiar código, usando `for`, `while` y utilidades como `range` y `enumerate`.

---

## ✅ Loop `for` con listas

```python
nombres = ["Ana", "Luis", "Marta"]

for nombre in nombres:
    print("Hola", nombre)
```

---

## 🔢 `range()` para repetir N veces

```python
for i in range(5):
    print(i)
```

Resultado: `0, 1, 2, 3, 4`

---

## 🏷️ `enumerate()` para índice + valor

```python
frutas = ["manzana", "pera", "plátano"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

---

## 🔄 Loop `while`

```python
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
```

Usa `while` cuando no sabes exactamente cuántas iteraciones habrá.

---

## ⛔ `break` y `continue`

```python
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue   # salta el 3
    if n == 5:
        break      # termina el loop
    print(n)
```

---

## 🧪 Ejercicios

1. Recorre una lista de notas e imprime cada una
2. Cuenta cuántas notas son >= 5
3. Pide números al usuario hasta que escriba `0` (con `while`)
4. Imprime solo números pares del 1 al 20

---

## ⚠️ Errores comunes

1. Crear bucles infinitos con `while`
2. Modificar el contador en dirección equivocada
3. Usar `break` cuando se necesitaba `continue` (o viceversa)
