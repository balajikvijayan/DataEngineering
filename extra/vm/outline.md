At the end of this day, the student should be able to ...


Lecture 

- Introduction to Docker: VMs, Containers and differences
- The purpose of Docker: application containers, achieving portability, isolation, 
- Built on Linux kernel features; Docker runs processes in isolated containers.; - Container lifecycle
- workflow: Dockerfile (actual code) -> ('docker build') Docker Image -> runs in Container (= isolated, )
- "container" = stripped-to-basics version of a Linux operating system
//"operator" = person executing "docker run"
- Docker relies on Linux-specific features of the kernel



/* Run through this in lecture: */
Common Docker commands:
# list all *running* containers:
sudo docker ps

#list of both running and non-running containers:
sudo docker ps -l 

# builds a docker *image* from a Dockerfile
docker build MyIageFile

# creates and runs a Docker *container* in 
docker run


=========================
Lab:
in this lab you will learn how to:
- install Docker on your machine
- use Docker Hub to find and download Docker images
- load a Docker image into a Container and run it
- manually write a Docker file that creates an image based on CentOS 7 

Task 1: Installing Docker
/* INSTALLING  DOCKER */
diagrams for Linux, Mac and Windows:
- Mac: Mac -> Boot2Docker (installs a VirtualBox VM, Docker and B2D mgt tool) -> Docker 
- Mac: must run OS X 10.6 Snow Leapard or newer

- finally: run 'docker images' which shows you have no images stored on your local machine
- also run 'docker ps' which shows you have no containers running on your local machine, which couldn't be the case since you have no local images to use to run in containers
/* INSTALLING  DOCKER */

Task 2: Running Hello World
- go to Docker Hub 
- Find hello-world Image
- in cmd line, type 'docker pull hello-world'
---- what happened here: 'pull': docker goes to Hub and downloads the image with this title
- in cmd line, type 'docker run hello-world'
---- what happened here: the 'run' command combines the 'create' and 'start' command, i.e. it both creates and starts the container
- carefully read the output of 'docker run hello-world', it explains what happened after you typed the command
- note that the Container stopped after its contents were executed. 
- type 'docker images' : it shows all the images present on your machine, which should be hello-world and any others you may have downloaded
- type 'docker ps': it shows all containers presently running. Since the hello-world Container shut down after executing, there are no containers running.
- TODO: run container such that it keeps running, so you can use 'docker ps' to see it and then kill it using 'docker kill hello-world'


/* Task 3: Creating your own image step by step. Goal: Have image with PostGres (based on previous lesson) */ 
// TODO / IDEA: students should have keep all Galvanize work in a specific directory, lesson by lesson. maybe they should have separate dir for all Dockerfiles?
- 'touch' new Dockerfile and open it
- type (DO NOT COPY/PASTE) as we go:
(Important notes on Dockercontainers: only 'FROM' and 'MAINTAINER' are mandatory; 
The last line of the Dockerfile traditionally describes the default command to be executed when the container starts.)
FROM centos:7 
-- this tells Docker that your image will be based on the CentOS image, version 7
- leave an empty line and then:
RUN apt-get -y update && apt-get install -y ...
// TODO: add in Richard's sshd etc.

- create new ssh key
- copy public key to tmp/authorized_key under Docker folder

- after you've saved the Dockerfile, run 
'docker build .' in the directory that it is located in. 
- watch how after each step, the changes are committed to the image and it says 
'----> 897a83befc' for example

===== Dockerfile


# add:
RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*


# add2:
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# expose ports
EXPOSE 80 


commands:

docker build -t testimg .
docker stop ...
docker rm ....
docker run -d -p 22 --privileged -h test --name test testimg
docker inspect gtestrun
sudo route -n add 172.17.0.0/16 `boot2docker ip`
ping 172.17.0.99
ssh root@172.17.  0.99

docker exec -it CONTAINER_ID /bin/bash

ansible all -i hosts -a 'whoami'

ansible-playbook playbook-install-jdk8.yml -i hosts 


========
Links / Resources:
http://docs.docker.com/mac/started/
https://github.com/wsargent/docker-cheat-sheet
http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html


==== 

notes:
Elastic Beanstalk has:
- single instance
- load balanced + auto scale


Extra Credit:
- pull log files out of EBS
- 


