What I built: you built the Python images (check-app, db-check). You didn’t build the Oracle one. You pulled it from Docker Hub. It’s worth saying that, because “I built” versus “I used” matters in interviews. I also setup connection between mac and docker conatner and connection between two containers as well using docker network.
 Key ideas:
 Image vs container- Image is like a cake recipe which gives you all the ingredients which are required to bake a cake and conatiner is a cake which is made up using recipe. so container is built from the image and its libraries.
 the recipe in your analogy is really the Dockerfile. The image is the finished, packaged result, and the container is the cake being served. Adding that third step makes the analogy complete.
 -p is used to publish port between your laptop and the container as it helps to flow the traffic from your latop to network -p1521:1521 connects the port from you laptop to the container 1521 port. container itself is also a loclhaots and has itws own ports as well.
 name lookup on network- to connect two conatiners we created a newtork which hlep is kind of looking up of container name to connect. It act as a DNS even though no ip is defined for the same

 Commands I used:

 docker build -t checkapp .
 so you have a docker file in a folder with follwoing things:
 FRROM python: slim-3.12--- what oython image to fetch
 workdir /app--- what should the working directory
 COPY requirements.txt .-- to copy file in current working directory i.e. app in container
 RUN pip install -r requirements.txt-- to install python libraries to connect to oracle think client
 COPY db_check.py .-- copy the python file to be run when container got booted
 CMD["python","db_check.py"]
these above things starting from "from" to "cmd" goes in dockerfile and this file is placed in folder so build command needs to be run from that folder thats why there is . in the end i.e. from where docker file needs to be used.
-t is used to give name to the image.

docker run --rm checkapp --- to run and remove teh container after it is completed

docker network create ai-net-- to create a network to conenct two docker container

docker network connect ai-net oracle-free-- conencting oracle-free connecter to ai-net network

docker run --rm --network ai-net -e DB_USER=username -e DB_PASSWORD='password,-e DB_DSN=oraclefree:1521/FREEPDB1 db_check

the above command is used to conenct the db_check container to oracle-free container and then run the oracle comamnds in that conatiner.

So we have an application conatiner db_check which is used to connect to db conatiner and run the commands.