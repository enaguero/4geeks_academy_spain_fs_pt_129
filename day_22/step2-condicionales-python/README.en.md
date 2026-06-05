[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🔀 Step 2: Conditionals in Python

## 🎯 Objective

Make decisions in your code using conditions and logical operators.

---

## 🧩 Basic structure

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Te falta poco")
else:
    print("Eres menor de edad")
```

Important rule: each block must be indented.

---

## ⚖️ Comparison operators

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

```python
nota = 7
print(nota >= 5)  # True
```

---

## 🔗 Logical operators

```python
edad = 25
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes entrar")

if edad < 18 or not tiene_entrada:
    print("No puedes entrar")
```

---

## 🎯 Real example: simple login validator

```python
usuario_correcto = "admin"
clave_correcta = "1234"

usuario = input("Usuario: ")
clave = input("Clave: ")

if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")
```

---

## 🧪 Exercises

1. Ask for a temperature and show:
   - `< 10`: "Hace frío"
   - `10-24`: "Temperatura agradable"
   - `>= 25`: "Hace calor"
2. Ask for an exam grade and classify it as: fail, pass, very good, outstanding
3. Ask for age and country. Allow registration only if age >= 18 and country == "España"

---

## ⚠️ Common mistakes

1. Writing `=` inside an `if` instead of `==`
2. Not considering edge cases (`>=` vs `>`)
3. Very long conditions without breaking them into intermediate variables
