# flask-rest-api

## Request Parser

1. It is not meant for complex jsons - only simple jsons
2. It supports inputs like formData and query-parameters (passed with the url)


## Models (Marshalling)

1. Meant for complex json structures
2. If you intend to use ```models``` then you cannot use the request parser
3. It is possible however to have a query parameter + complex json
   1. Ex. ```localhost:8000/alex/<age>``` is a url with a query parameter and can be retrieved with  ```age``` passed as an argument in the function. Along with this we can use a marshalled json by inspecting the ```body``` of the response.


#### Note : We can't have form data + json together. Because we cannot have two payloads simultaneously.


## Dockerfile


## Testing the code

1. We use the pytest module
2. To run all the curated test cases, run ```pytest -v -s```  on the command line.
3. ```pytest``` will search for all python files that start with ```test_``` and will execute all functions in that file that start with ```test```.