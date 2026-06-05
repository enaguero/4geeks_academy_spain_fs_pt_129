🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🚨 Step 5: Status Codes y Manejo de Errores (Flask)

## 🎯 Objetivo

Responder de forma semántica y profesional con códigos HTTP correctos.

---

## 🧰 Requisitos para correr este step

- Setup transversal completado en Step 0
- Entorno virtual activo
- Dependencias instaladas desde `day_23/requirements.txt`

---

## 📦 Instalación (si aún no instalaste dependencias)

```bash
source .venv/bin/activate
pip install -r day_23/requirements.txt
```

---

## ▶️ Cómo correr este step

```bash
flask --app day_23/flask_api/step5-status-codes-y-errores/main.py --debug run
```

---

## 🧠 ¿Por qué importa?

Una API no solo debe "funcionar", también debe comunicar bien.

Analogía diaria:
- Si vas al banco y te dicen "ok" para todo, no sabes si tu trámite salió.
- Los status codes son ese semáforo: verde, amarillo, rojo.

---

## 📌 Guía rápida de códigos

- `200 OK`: lectura o actualización exitosa
- `201 Created`: recurso creado
- `204 No Content`: eliminado sin body
- `400 Bad Request`: datos mal formados
- `404 Not Found`: recurso inexistente
- `422 Unprocessable Entity`: validación fallida de body

---

## 🧩 Patrón recomendado de error

```json
{
  "detail": "Mensaje claro para cliente"
}
```

---

## 🧪 Ejercicios

1. Devuelve `409 Conflict` cuando intentes crear un recurso duplicado
2. Usa `204` real en delete (sin body)
3. Homogeneiza mensajes de error para toda la API
