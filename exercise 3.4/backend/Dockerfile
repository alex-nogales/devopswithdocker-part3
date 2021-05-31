FROM golang:alpine

EXPOSE 8080

WORKDIR /usr/src/app
COPY . .

RUN addgroup -S appuser && adduser -S appuser -G appuser && \
    chown -R appuser:appuser /usr/src/app

USER appuser 

RUN go build
ENV REQUEST_ORIGIN http://localhost
CMD ["./server"]