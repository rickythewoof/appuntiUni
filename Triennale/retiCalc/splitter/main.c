#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <fcntl.h>
#include <arpa/inet.h>

#define CHUNK_SIZE 10

struct Header{
    int cnk_index;
    int len;
};

struct Message{
    char* buf;
};

enum Destination{
    SOCKET,
    PIPE
};

int create_open_fifo(char* fifo_path){
    unlink(fifo_path);
    int fifo = mkfifo(fifo_path, 0666);

    if(fifo == -1){
        perror("Error creating pipe");
        exit(1);
    }
    int fifo_fd = open(fifo_path, O_RDONLY);
    if(fifo_fd == -1){
        perror("Error opening fifo");
        exit(1);
    }
    return fifo_fd;
}

int create_open_socket(int port){
    struct sockaddr_in srv_addr  = {0};
    int opt = 1;
    int ret;
    int addr_size = sizeof(srv_addr);
    srv_addr.sin_family = AF_INET;
    srv_addr.sin_port = htons(port);
    srv_addr.sin_addr.s_addr = INADDR_ANY;

    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if(sock_fd == -1){
        perror("Error opening socket");
        exit(1);
    }
    if (setsockopt(sock_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    ret = bind(sock_fd, (struct sockaddr*) &srv_addr, (socklen_t) addr_size);
    if(ret == -1){
        perror("Error binding socket!");
    }
    ret = listen(sock_fd, 1);
    if(ret == -1){
        perror("Error listening to srv_socket");
        exit(1);
    }
    int client_sock_fd = accept(sock_fd, (struct sockaddr*) &srv_addr, (socklen_t) addr_size);
    if(client_sock_fd == -1){
        perror("Error accepting connection from client");
        exit(1);
    }
    return client_sock_fd;
}

int main(int argc, char** argv){
    if(argc != 4){
        prinf("Too few arguments!\n");
        exit(1);
    }
    int sock_fd = create_open_socket(atoi(argv[4]));    //Socket client File Descriptor
    int pipe_fd = create_open_fifo(argv[3]);            //Fifo client File Descriptor

    fd_set readfd;
    while(1){
        FD_ZERO(&readfd);
        FD_SET(pipe_fd, &readfd);
        FD_SET(sock_fd, &readfd);

        int ret = select((sock_fd > pipe_fd ? sock_fd : pipe_fd) + 1, &readfd, NULL, NULL 0);
        if(FD_ISSET(pipe_fd, &readfd)){
            //TODO
            ret = recv(sock_fd, )
        }
        if(FD_ISSET(sock_fd, &readfd)){
            //TODO
        }
    }
    




};