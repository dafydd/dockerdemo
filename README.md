# Docker demo and discussion of containerisation and virtualisation
2019-07-24


# demo

- clean out previous demos


    docker images
    docker ps

- what does the python docker image look like?
<https://hub.docker.com/_/python>

- what is this "alpine" thing?
<https://www.distrowatch.com/table.php?distribution=alpine>

- make the docker image:


    docker build -t simple-demo .
  
- run the docker image in a new "container":


    docker run -d --rm -p 8080:8080 simple-demo
    
  d  - background (no terminal attached)
  rm - remove stopped containers automatically
  
- getting "inside" the container to poke around:


     docker exec -it <container-id> /bin/sh

- now run it using port 80 instead of 8080:


    docker run -d --rm -p 80:8080 simple-demo

    docker ps
    docker container inspect <container-id>

# stuff to mention
##AWS Lambda 
-- what?
-- dangers!

## AWS Fargate
-- why?

## AWS Firecracker 
-- what it is?
-- why?

## microservices
-- circleci.com
-- quay.io
-- zipkin.io
-- EE book: Continuous Delivery in Java <https://www.amazon.co.uk/Continuous-Delivery-Java-Daniel-Bryant/dp/1491986026/ref=sr_1_1?keywords=microservices+abraham&qid=1563964514&s=gateway&sr=8-1>






