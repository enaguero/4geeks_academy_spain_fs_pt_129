# 🧪 Step 6: Documentación y Pruebas (Flask)

## 🎯 Objetivo

Probar tu API de forma sistemática y mantener documentación mínima de endpoints.

---

## 🧰 Requisitos para correr este step

- Setup transversal completado en Step 0
- Entorno virtual activo
- Tener una API corriendo (recomendado: Step 5 o Step 7 de Flask)

---

## 📦 Instalación (si aún no instalaste dependencias)

```bash
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## ▶️ Cómo correr este step

1. Levanta una API de referencia (ejemplo con Step 5):

```bash
flask --app day_23/flask_api/step5-status-codes-y-errores/main.py --debug run
```

2. Usa `day_23/flask_api/step6-documentacion-y-pruebas/checks.http` como guía de requests.

---

## 📘 Documentación recomendada en Flask

Flask no genera `/docs` automáticamente por defecto.
Para este step, documenta manualmente:

- Lista de endpoints
- Ejemplos de body JSON
- Status codes esperados
- Errores posibles (`404`, `409`, `422`)

Puedes hacerlo en un `README.md` de proyecto o usar extensiones OpenAPI si quieres ir más allá.

---

## 🧠 Analogía diaria

`checks.http` es como una lista de verificación operativa:
siempre ejecutas los mismos checks para validar calidad.

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
