# 🧪 Step 6: Documentación y Pruebas

## 🎯 Objetivo

Probar tu API de forma sistemática y entender la documentación automática de FastAPI.

---

## 📘 Documentación automática

Cuando levantas FastAPI, obtienes:

- `/docs` -> Swagger UI interactivo
- `/redoc` -> documentación alternativa más narrativa

Esto te permite probar endpoints sin Postman en fase inicial.

---

## 🧠 Analogía diaria

`/docs` es como el manual de un electrodoméstico con botones de prueba incorporados.
No solo explica, también te deja interactuar.

---

## 🔍 Qué validar en cada endpoint

1. Caso feliz (`200` / `201`)
2. Datos inválidos (`422`)
3. Recurso inexistente (`404`)
4. Conflictos de negocio (`409`)

---

## 🛠️ Estrategia de pruebas manuales

1. Empieza por `GET` para inspeccionar estado inicial
2. Crea datos con `POST`
3. Edita con `PUT`
4. Elimina con `DELETE`
5. Repite `GET` para verificar consistencia

---

## ✅ Resultado esperado de este step

Ser capaz de decir: "mi API funciona" con evidencia reproducible (requests concretas), no por intuición.
