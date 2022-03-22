# the base image for python
FROM python:3.9-alpine3.14

#################### Build Phase ####################
WORKDIR /flask-rest-api

# copy all the code
COPY app app
COPY requirements.txt requirements.txt 
COPY run.sh run.sh

# install the requirements
RUN pip install -r requirements.txt

# change to root
USER root

# create a group and user
RUN addgroup -g 1000 -S service-user && adduser -g service-user -u 1000 -S service-user 
#RUN groupadd -g 1000 service-user && useradd -r -u 1000 -g service-user service-user

# assign code ownership to the these groups and user with appropriate permissions
RUN chmod -R 775 /flask-rest-api && chown -R service-user:service-user /flask-rest-api

# make run.sh executable
RUN chmod 775  /flask-rest-api/run.sh

# switch to service user 
USER service-user

# set python path
ENV PYTHONPATH "$PYTHONPATH:/flask-rest-api"
ENV PYTHONUNBUFFERED=1

# Expose port 
EXPOSE 1235

#################### Execute/Running Phase ####################
# run the executable
CMD ./run.sh