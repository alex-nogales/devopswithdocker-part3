FROM ubuntu:18.04

EXPOSE 5000
WORKDIR /usr/src/app
COPY . .

RUN useradd -m appuser && \
    chown -R appuser:appuser /usr/src/app && \
    apt update && apt install curl -y && \
    curl -sL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt install -y nodejs && \
    npm install && \
    REACT_APP_BACKEND_URL=http://localhost:8080 npm run build && \
    npm install -g serve
    
USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]
