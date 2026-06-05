[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 4: Official projects of the day (Instagram + StarWars)

## 🎯 Goal

Move from guided examples to modeling a real domain following the official brief.

---

## 🔗 Syllabus projects

- [Building Instagram.com Database Model](https://4geeks.com/syllabus/spain-fs-pt-129/project/instagram-data-modeling)
- [Data Modeling a StarWars Blog](https://4geeks.com/syllabus/spain-fs-pt-129/project/data-modeling-starwars)

---

## 1) Recommended strategy (bootcamp)

1. List the entities (tables) first.
2. Define PKs/FKs and relationship types.
3. Sketch a quick ERD on paper/whiteboard.
4. Create the SQLAlchemy models.
5. Run the initial migration.
6. Insert test data.
7. Run business queries with joins.

---

## 2) Minimum checklist for Instagram

- [ ] `users`
- [ ] `posts`
- [ ] `comments`
- [ ] `follows` (junction table)
- [ ] `likes` (junction table)
- [ ] `1-N` relationships (`user -> posts`, `post -> comments`)
- [ ] `N-N` relationships (`users <-> users` through follows, `users <-> posts` through likes)

---

## 3) Minimum checklist for the StarWars Blog

- [ ] `users`
- [ ] `characters`
- [ ] `planets`
- [ ] `favorites` (user can save characters/planets)
- [ ] At least one `1-N` relationship
- [ ] At least one `N-N` relationship
- [ ] Queries for favorites per user

---

## 4) Quality criteria for grading

- The model avoids obvious data duplication.
- Foreign keys reflect the business rules.
- The relationships allow real-world cases to be solved with joins.
- The migrations reproduce the schema on any machine.
- The team can explain why each relationship was chosen.

---

## ✅ Suggested deliverable for the day

- Complete SQLAlchemy model.
- Working migrations folder.
- Script or notebook with CRUD + join queries.
- Screenshot or export of the ERD.
