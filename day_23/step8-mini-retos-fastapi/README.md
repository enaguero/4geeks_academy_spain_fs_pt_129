# 🧠 Step 8: Mini Retos FastAPI

## 🎯 Objetivo

Consolidar routing, validación y diseño HTTP en problemas pequeños y realistas.

---

## ✅ Reto 1: API de Inventario

### Enunciado
Crea endpoints para gestionar productos:

- `GET /products`
- `POST /products`
- `PUT /products/{id}`
- `DELETE /products/{id}`

Campos mínimos: `name`, `price`, `stock`.

Reglas:
- `price > 0`
- `stock >= 0`

---

## ✅ Reto 2: Filtros por Query

### Enunciado
En `GET /products`, añade filtros:

- `?min_price=`
- `?max_price=`
- `?in_stock=true|false`

Objetivo: practicar query params y condiciones combinadas.

---

## ✅ Reto 3: Reserva de Turnos

### Enunciado
API de turnos médicos con `doctor`, `patient`, `date`, `status`.

Reglas:
- No permitir doble reserva mismo doctor y fecha
- `status` permitido: `pending`, `confirmed`, `cancelled`

---

## ✅ Reto 4: Paginación Simple

### Enunciado
Implementa paginación en listados:

- `GET /products?offset=0&limit=10`

Devuelve:
- `items`
- `total`
- `offset`
- `limit`

---

## 🔍 Checklist de calidad

- [ ] Hay validación de entrada con Pydantic
- [ ] Se usan status codes semánticos
- [ ] Los errores tienen mensaje claro
- [ ] Endpoints tienen nombres consistentes
- [ ] Probaste casos felices y casos de error
