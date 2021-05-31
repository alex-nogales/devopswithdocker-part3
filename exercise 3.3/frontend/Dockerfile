FROM ubuntu:18.04

EXPOSE 5000
WORKDIR /usr/src/app
COPY . .

RUN useradd -m appuser
RUN chown -R appuser:appuser /usr/src/app

RUN apt update && apt install curl -y
RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt install -y nodejs

RUN npm install 
RUN REACT_APP_BACKEND_URL=http://localhost:8080 npm run build
RUN npm install -g serve

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]
