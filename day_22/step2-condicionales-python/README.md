🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🔀 Step 2: Condicionales en Python

## 🎯 Objetivo

Tomar decisiones en el código usando condiciones y operadores lógicos.

---

## 🧩 Estructura básica

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Te falta poco")
else:
    print("Eres menor de edad")
```

Regla importante: cada bloque debe ir indentado.

---

## ⚖️ Operadores de comparación

- `==` igual que
- `!=` diferente de
- `>` mayor que
- `<` menor que
- `>=` mayor o igual
- `<=` menor o igual

```python
nota = 7
print(nota >= 5)  # True
```

---

## 🔗 Operadores lógicos

```python
edad = 25
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes entrar")

if edad < 18 or not tiene_entrada:
    print("No puedes entrar")
```

---

## 🎯 Ejemplo real: validador simple de login

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

## 🧪 Ejercicios

1. Pedir temperatura y mostrar:
   - `< 10`: "Hace frío"
   - `10-24`: "Temperatura agradable"
   - `>= 25`: "Hace calor"
2. Pedir nota de examen y clasificar en: suspenso, aprobado, notable, sobresaliente
3. Pide edad y país. Permite registro solo si edad >= 18 y país == "España"

---

## ⚠️ Errores comunes

1. Escribir `=` dentro de `if` en vez de `==`
2. No contemplar casos límite (`>=` vs `>`)
3. Condiciones muy largas sin dividirlas en variables intermedias
