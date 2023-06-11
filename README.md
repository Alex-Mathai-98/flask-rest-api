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
The dockerfile is in ```Dockerfile```. It specifies all of the needed dependencies for this microservice application. There are two phases in the dockerfile - ```build``` phase and ```run``` phase.

The ```build``` phase - This phase first starts with a base image (in this case ```alpine```). A base image is a very lighweight model of the OS. Remember that the OS of the baremetal machine must match the base image. So alpine should be used only on unix based baremetal machines (and not windows VMs). Then in the buildphase we first create a folder ```flask-rest-api``` using the ```WORKDIR``` command. Post that code is copied from the users machine into the image using the ```COPY``` command. In ```COPY```, the first argument is a path on the user's machine and the second path is the path in the docker within the ```WORKDIR```. So ```COPY app app``` will copy the ```app``` folder of flask-rest-api from the users machine and paste it in ```flask-rest-api/app```.  After that, ```RUN``` commands are used for installing libraries, addings groups and users and attaching permissions of ```flask-rest-api``` to the newly created user and group. After that we switch to the new user using the ```USER``` command. We set some environment variables using the ```ENV``` command and expose a port using the ```expose``` COMMAND.

The ```run``` phase involves using the ```CMD``` command to run the application.

## Testing the code

1. We use the pytest module
2. To run all the curated test cases, run ```pytest -v -s```  on the command line.
3. ```pytest``` will search for all python files that start with ```test_``` and will execute all functions in that file that start with ```test```.
