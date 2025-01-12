FROM gcc:latest as builder
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN gcc -o main -static main.c

FROM alpine:latest as runtime
COPY --from=builder /usr/src/myapp/main /main
ENTRYPOINT ["./main"]
