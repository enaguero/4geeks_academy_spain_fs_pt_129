[🇪🇸 Español](live_class.md) | 🇬🇧 **English**

# Build Your First API

- Create the endpoints (or the URLs) that a server "exposes".
- Calls the documentation we've seen in contact list, star wars, etc.
- API: Application Programming Interface.

1. We're in a circular loop: client calls the server and the server responds to the client.
2. The client uses a protocol: HTTP/HTTPS
3. Communication methods of the protocol: GET, POST, PATCH, PUT, DELETE.
   3.1 -> PATCH: Partial update*
   3.2 -> PUT: Full update*
4. REST: A way of designing URLs in an API to create a "resource" or concept where the different methods of the communication protocol are executed.

4.1 - Resource identification: refers to a noun: "users", "products", "cars".
4.2 - Associating the protocol's communication method with the noun.

- Retrieve all elements of the resource: "GET /users"

```
response: 200

[
  {
      uuid: "absd2-123tr-quwquqw4",
      name: "Andres",
      lastName: "Meza",
      dateOfBirth: "01/12/1985",
      email: "student@4geeks.com"
  },
    {
      uuid: "absd2-123tr-quwquqw4",
      name: "Andres",
      lastName: "Meza",
      dateOfBirth: "01/12/1985",
      email: "student@4geeks.com"
  }
]

```

- Retrieve a single element of the resource: "GET /users/:userId" (detail view -> specific element)

```
GET /users/absd2-123tr-quwquqw4

{
  uuid: "absd2-123tr-quwquqw4",
  name: "Andres",
  lastName: "Meza",
  dateOfBirth: "01/12/1985",
  email: "student@4geeks.com"
}

```

- Partially update the resource with PATCH:

```

PATCH /users/:userId

request (body): JSON

{
  dateOfBirth: "12/12/1985" -> I send only one field (partial update)
}

```

- Fully update the resource with PUT:

Incorrect example:

```

PUT /users/:userId

request (body): JSON

{
  dateOfBirth: "12/12/1985" -> I send only one field (partial update) -> server responds with a 4XX
}

fetch("https://dominio.com/users/:userId", {
  METHOD: "PUT",
  BODY: {
    dateOfBirth: "12/12/1985"
  }
}).then((res) => res.status)
.then(()=> )
.catch(()=> {

})

```

The complete example is when you send all the information (every field):

```
PUT /users/:userId

{
  name: "Andres",
  lastName: "Meza",
  dateOfBirth: "12/12/1985",
  email: "student_senior@4geeks.com"
}
```

- Delete: remove a resource:

```
DELETE /users/:userId
```

## Nesting

```
METHOD /resources/:resourceId/nestedResources/
```

```
GET /products

body:
[
  {
    uuid: "123iqweqw-12312niadsa",
    name: "perfume-abc",
    brand: "morning",
    model: "winter"
  }
]

GET /products/123iqweqw-12312niadsa

  {
    name: "perfume-abc",
    brand: "morning",
    model: "winter"
  }

GET /users/:userId/products

GET /users/absd2-123tr-quwquqw4
```
