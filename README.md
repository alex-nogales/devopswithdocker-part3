# Part 3
This part introduces production-ready practices such as container optimization and deployment pipelines. We’ll also familiarize ourselves with other container orchestration solutions. By the end of this part you are able to:
- Critically examine the images that you pull
- Trim the container size and image build time via multiple methods such as multi-stage builds.
- Automatically deploy containers

## Exercises
### 3.1 A deployment pipeline to heroku
Let’s create our first deployment pipeline!
For this exercise you can select which ever web application you already have containerized.
If you don’t have any web applications available you can use any one from this course and modify it. (Such as the course material itself)
Use GitHub, Github Actions, and Heroku to deploy a container to heroku. You can also use other CI/CD tools instead of GitHub Actions.
Submit a link to the repository with the config.

#### Link submited
`https://testingapponetwo.herokuapp.com`

### 3.2 Building images inside of a container
Watchtower uses volume to docker.sock socket to access Docker daemon of the host from the container. By leveraging this ourselves we can create our own simple build service.
Create a project that downloads a repository from github, builds a Dockerfile located in the root and then publishes it into Docker Hub.
You can use any programming language / technology for the project implementation. A simple bash script is viable
Then create a Dockerfile for it so that it can be run inside a container.
Make sure that it can build at least some of the example projects.

### 3.3
**This exercise is mandatory** 
In the previous parts we created Dockerfiles for both example frontend and backend.
Security issues with the user being a root are serious for the example frontend and backend as the containers for web services are supposed to be accessible through the internet.
Make sure the containers start their processes as a non-root user.
> TIP `man chown` may help you if you have access errors

### 3.4
Return back to our frontend & backend Dockerfiles and you should see the some mistakes we now know to fix.
Document both image sizes at this point, as was done in the material. Optimize the Dockerfiles of both programs, frontend and backend, by joining the RUN commands and removing useless parts.
After your improvements document the image sizes again. The size difference may not be very much yet. The frontend should be around 432MB when using `FROM ubuntu:18.04`. The backend should be around 351MB. The sizes may vary.

### 3.5
Document the image size before the changes.
Let’s test what the image sizes are when using FROM golang and FROM node in the backend and frontend projects respectively.
Return back to our frontend & backend Dockerfiles and change the FROM to something more suitable. Both should have at least alpine variants ready in DockerHub. Make sure the application still works after the changes.
Document the size after your changes.

>> My Backend already uses golang:alpine, so no changes there
#### Command used:
```
% docker build -t example-frontend:alpine -f Dockerfile.alpine .
% docker container run -it -p 5000:5000 example-frontend:alpine
```

### 3.6: Multi-stage frontend
Multi-stage builds. Lets do a multi-stage build for the frontend project since we’ve come so far with the application.
Even though multi-stage builds are designed mostly for binaries in mind, we can leverage the benefits with our frontend project as having original source code with the final assets makes little sense. Build it with the instructions in README and the built assets should be in build folder.
You can still use the serve to serve the static files or try out something else.

#### Command used:
```
% docker build -t example-frontend:alpinev2 -f Dockerfile.alpine.v2 .
% docker container run -it -p 5000:5000 example-frontend:alpinev2
```