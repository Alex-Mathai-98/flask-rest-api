# flask-rest-api

## Request Parser

1. It is not meant for complex jsons - only simple jsons
2. It supports inputs like formData and query-parameters (passed with the url)


## Models (Marshalling)

1. Meant for complex json structures
2. If you intend to use a model then you cannot use the request parser
3. It is possible however to have a path parameter + complex json
   1. Ex. localhost:8000/alex/<age> is a url with a path parameter and can be retrieved with  ```age``` passed as an argument in the function. Along with this we can use the marshalled json.


#### Note : We can't have form data + simple json together. Because we cannot have two payloads simultaneously.


## Dockerfile


