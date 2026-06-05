[🇪🇸 Español](example.md) | 🇬🇧 **English**

# REST API

1. HTTP allows transferring information between computers
2. HTTP uses an interface (API) to know what information to send.
3. HTTP uses a keyword (special word) to indicate what action to perform:

- get information: GET (I don't send information)
- create information: POST
- Update information completely: PUT
- Update information partially: PATCH
- Delete information: DELETE

4. What format does the information have?

GET Plural example
REST: Representational State Transfer -> JSON (JavaScript Object Notation)

resource: `cars`, `people`, `animals`, `laptos`

Get multiple cars

base: http://my-super-api.com/v1/

end-point: /<resource>

HTTP: GET

```
{
  "data": [
    {
      "uuid": "123423",
      "brand": "ford",
      "model": "cachilupi-ford-fiesta"
    },
    {
      "uuid": "123427",
      "brand": "citroen",
      "model": "cachilupi-citroen-fiesta"
    },
    ....
  ]
}

```

- Singular GET of a resource

base: http://my-super-api.com/v1/
end-point: /<resource>/:id

example: http://my-super-api.com/v1/cars/123427

```
{
  "data":  {
      "uuid": "123427",
      "brand": "citroen",
      "model": "cachilupi-citroen-fiesta"
    }
}
```
