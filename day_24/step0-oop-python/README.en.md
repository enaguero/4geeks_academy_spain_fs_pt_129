[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🧭 Step 0: OOP in Python (Incremental)

## 🎯 Goal

Understand from scratch:

1. What problem Object-Oriented Programming (OOP) solves.
2. What a `class` is.
3. What an `object` is.
4. What an `attribute` is.
5. What a `method` is.

By the end, you'll be ready to model the foundation of the **Family Static API**.

---

## 1) What problem does OOP solve?

When we start out, we usually build an in-memory API with lists + dictionaries + loose functions:

```python
members = []
next_id = 1

def create_member(data):
    global next_id
    # Repeated validation (will also appear in update_member)
    if "first_name" not in data or data["first_name"] == "":
        return {"error": "first_name is required"}, 400
    if "age" not in data or data["age"] < 0:
        return {"error": "invalid age"}, 400

    member = {
        "id": next_id,
        "first_name": data["first_name"],
        "age": data["age"],
        "lucky_numbers": data.get("lucky_numbers", []),
    }
    members.append(member)
    next_id += 1
    return member, 201

def update_member(member_id, data):
    for m in members:
        if m["id"] == member_id:
            # Repeated validation (same rule in another place)
            if "age" in data and data["age"] < 0:
                return {"error": "invalid age"}, 400

            # Typical inconsistent-key bug:
            # here someone wrote "firstname" instead of "first_name"
            if "firstname" in data:
                m["firstname"] = data["firstname"]

            if "first_name" in data:
                m["first_name"] = data["first_name"]
            return m, 200
    return {"error": "member not found"}, 404
```

This approach works at first, but as the project grows real problems show up:

- **Duplicated rules**: validations repeated across `create_member`, `update_member`, etc.
- **Consistency errors**: keys get mixed up (`"firstname"` and `"first_name"`), breaking responses.
- **Hard maintenance**: if you change a rule (for example minimum age), you have to find and edit many functions.

OOP helps you organize better:

- It bundles **data + behavior** in the same unit.
- It lets you model real-world entities (`Family`, `Member`).
- It makes the code more maintainable as it grows.

---

## 2) What is a `class`?

A `class` is a **template**.  
It defines what the objects created from it will look like.

Think of it as a "mold".

```python
class Dog:
    pass
```

Here `Dog` is the template, but there is no actual dog yet.

### Mini exercise 1

1. Create a class named `Car`.
2. Create a class named `Student`.
3. Run the file and verify it doesn't raise an error.

---

## 3) What is an `object`?

An `object` is a **concrete instance** of a class.

```python
class Dog:
    pass

dog_1 = Dog()
dog_2 = Dog()

print(type(dog_1))  # <class '__main__.Dog'>
print(dog_1 == dog_2)  # False
```

Even though both come from the same class, they are different objects.

### Mini exercise 2

1. Create `car_1 = Car()` and `car_2 = Car()`.
2. Print `type(car_1)`.
3. Compare `car_1 == car_2`.

---

## 4) What is an `attribute`?

An attribute is a piece of data that lives inside the object.

To initialize attributes we normally use `__init__`:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog_1 = Dog("Toby", 4)
print(dog_1.name)  # Toby
print(dog_1.age)   # 4
```

Key points:

- `self` represents the current object.
- `self.name` and `self.age` are attributes of the object.

### Mini exercise 3

1. Define a `Student` class with `name` and `cohort` attributes.
2. Create an object `student_1`.
3. Print its attributes.

---

## 5) What is a `method`?

A method is a function defined inside the class.

It expresses the object's behavior.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: woof!"

    def birthday(self):
        self.age += 1

dog_1 = Dog("Toby", 4)
print(dog_1.bark())   # Toby says: woof!
dog_1.birthday()
print(dog_1.age)      # 5
```

`bark` and `birthday` are methods.  
`birthday` modifies the object's state (`age`).

### Mini exercise 4

1. In `Student`, create an `introduce()` method that returns a string.
2. Create a `change_cohort(new_cohort)` method to update the attribute.
3. Run it and check that the change is reflected.

---

## 6) All together: simple model for the Family API

For this day, our domain is a family and its members.

```python
class Member:
    def __init__(self, member_id, first_name, age):
        self.id = member_id
        self.first_name = first_name
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "age": self.age,
        }
```

Mental mapping:

- `class Member` -> template
- `member = Member(...)` -> concrete object
- `self.first_name` -> attribute
- `to_dict()` -> method

This maps directly to Flask:

- Flask receives an HTTP request
- Your class applies the rules
- Flask returns JSON with `to_dict()`

---

## 7) Guided practice for this step

Use the file [`oop_examples.py`](./oop_examples.py):

```bash
python day_24/step0-oop-python/oop_examples.py
```

What to observe:

- `Member` encapsulates a member's data.
- `Family` encapsulates the group's operations (`add_member`, `get_member`, `delete_member`).
- `get_all_members()` transforms objects into dictionaries to expose JSON.

---

## 8) Final validation mini-challenges

1. Add a `hobby` attribute to `Member` and reflect it in `to_dict`.
2. Create an `is_adult()` method that returns `True` if `age >= 18`.
3. Prevent creating members with negative ages.
4. In `Family`, create an `update_member_name(member_id, new_name)` method.
5. Test the happy path and an error case for each method.

---

## ✅ Learning Checklist

- [ ] I can explain what problem OOP solves.
- [ ] I can define `class`, `object`, `attribute`, `method` in my own words.
- [ ] I can create a class with `__init__`.
- [ ] I can create objects and call methods.
- [ ] I can connect this mental model with a Flask API.

---

## 📖 Official reading for this step

- [What is Object Oriented Programming?](https://4geeks.com/syllabus/spain-fs-pt-129/read/oop-in-python)
