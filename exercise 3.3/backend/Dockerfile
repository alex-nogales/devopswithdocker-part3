FROM golang:1.16

EXPOSE 8080

WORKDIR /usr/src/app
RUN apt update 

COPY . .

RUN useradd -m appuser
RUN chown  -R appuser:appuser /usr/src/app
USER appuser 

RUN go build
ENV REQUEST_ORIGIN http://localhost
CMD ["./server"]