# Step 4: Proyectos oficiales del día (Instagram + StarWars)

## 🎯 Objetivo

Pasar de ejemplos guiados a modelado de un dominio real siguiendo el enunciado oficial.

---

## 🔗 Proyectos del syllabus

- [Building Instagram.com Database Model](https://4geeks.com/syllabus/spain-fs-pt-129/project/instagram-data-modeling)
- [Data Modeling a StarWars Blog](https://4geeks.com/syllabus/spain-fs-pt-129/project/data-modeling-starwars)

---

## 1) Estrategia recomendada (bootcamp)

1. Lista entidades (tablas) primero.
2. Define PK/FK y tipos de relación.
3. Dibuja ERD rápido en papel/pizarra.
4. Crea modelos SQLAlchemy.
5. Corre migración inicial.
6. Inserta datos de prueba.
7. Ejecuta queries de negocio con joins.

---

## 2) Checklist mínimo para Instagram

- [ ] `users`
- [ ] `posts`
- [ ] `comments`
- [ ] `follows` (tabla puente)
- [ ] `likes` (tabla puente)
- [ ] Relaciones `1-N` (`user -> posts`, `post -> comments`)
- [ ] Relaciones `N-N` (`users <-> users` por follows, `users <-> posts` por likes)

---

## 3) Checklist mínimo para StarWars Blog

- [ ] `users`
- [ ] `characters`
- [ ] `planets`
- [ ] `favorites` (usuario puede guardar personajes/planetas)
- [ ] Al menos una relación `1-N`
- [ ] Al menos una relación `N-N`
- [ ] Queries de favoritos por usuario

---

## 4) Criterios de calidad para corrección

- El modelo evita duplicación de datos obvia.
- Llaves foráneas reflejan reglas del negocio.
- Las relaciones permiten resolver casos reales con joins.
- Las migraciones reproducen el esquema en cualquier máquina.
- El equipo puede explicar por qué eligió cada relación.

---

## ✅ Entregable sugerido del día

- Modelo en SQLAlchemy completo.
- Carpeta de migraciones funcionando.
- Script o notebook con consultas CRUD + joins.
- Captura o export del ERD.
