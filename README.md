# Docker

This is repo for docker impletation and understanding
summary of the 3 hours video here: https://www.youtube.com/watch?v=3c-iBn73dDE
what is container?  a way to package an application with all the necessary dependencies and configuration 
container lives in the container repository and and if you go to docker hub websire you could find official and non official container images
with container we do not need to install packages in the operating system and other team member will just use the docker and they do not need to have different packages
container is stack images on each other what is image here?
base image -> linux
on top we have apllication image

docker Image is artifact in running aroung and docker container is when it is running docker ps showing all the running docker 



docker vs virtual machine? size docker image is smaller since it does not have os kernel so it is faster as well since it only have on top

commen docker comments:

docker pull package name to install docker Image e.g. docker pulll redis
and then to check images on the systems s docksr images on terminal if you provide sepecific version you need to identify it if we need redis run it we need to creat container of the images and we could do it by docker run package e.g. docker run redis this pull and start and to check the running container we need to do docker ps to run container in detachmode you need to use -d 

to reset container we could to docker stop docker id and then use the same id to start again docker start docker id

docker ps -a showing all runing or non runing
docker run redis:4.0 indicate version 
to be able to connect the ports to bind the host to our lsptop we need to specify the ports and forward it e.g. docker run -p ourpor:hostport package name 

if you don't want work with container id you can nme them properly add --name to run
we could get   interactive terminal of the docker docker exect -it container id /bin/bash
using this for debauging container

how to use it?

let say you build python code you push the code and then you push jenkinse we have 

docker need to creat newwork to connect to make mango network to mango db once we creat docker network creat name
then we do docker run -p27017: -d -e username and pass word mango --name mangodb --net networkname that we cratedd

we can write write docker compuse to have everything to make everthing organize which is .yaml file it will also take care the network so we donot need to do this independent how to use the docker container if  we have docker compuse, we should use docker-compose -f name.yaml up and if we use down if will shut them down


to build and docker image your own code first develop code then use docker to test it then to commit it you need to use CI jenkinse
In order to build a docker image we need to creat a docker file the first line is FROM node (for java) so we need to use docker that already have node "chat gpt provide python example as well" then ENV to define enviroment variable then RUN to execute linux comment RUN mkdir -p /home/app and then COPY ./homr/app and last one is CMD["node","server.js"]
the difference cmd and run is enry point but run is not

to biuld an docker image docjer build -t tag of the image and then directory to build . means currantdirectory

how build private repo using amazon ECR first creat docker registery elastic container registery  then ve can use two approache to push the push the private repo use docker login which is aws command and once you successfully login you can push your image and then you need to tag your image regiteryDomain/imageName:tag in aws ecr we have to tag the image to include the repo we want to push it means it wiill rename it properly and then docker push and new name : tag

now deploy we need to add our app to yaml fle which is our image "chat gpt prove example here"
and we need to do docker login as well


the last thing is docker volum when we want to save data e.g. database. we could run -v to define where folder mount or -v name:address and then you can use just by name eveen in docker compuse you could put on the yaml file


