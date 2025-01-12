#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <sys/select.h>
#include <sys/sem.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>

#define PORT 7379
#define MAX_PROCS 3
#define MAX_BUF 2048

#define NOT_FOUND 0
#define GET_SUCCEEDED 1
#define OK 2

void exit_with_error(const char * msg) {
    perror(msg);
    exit(EXIT_FAILURE);
}

typedef struct slot{
    time_t expiry;  //EXPIRATION DATE
    char* key;
    char* value;
    struct slot* next;
} slot;

typedef struct Request{
    enum Req_type {GET, SET, INFO} request_type;
    char* key; 
    char* value;
    int time_to_live;
} Request;

typedef struct Dictionary{
    slot* first;

} Dictionary;

int client_socket, sem_id;

Request* parse(char* buf);                              
void set(Dictionary* dict, Request* req);           //Function to add key/value to dictionary
slot* get(Dictionary* dict, Request* req);          //Function to get slot* from key. Returns NULL if not found
slot* del(Dictionary* dict, slot* slot);            //Function to remove slot* from dict
void send_tcp(int socket, int default_ok, slot* slot);
void handle_connection(int fd, int id);
void handle_request(Dictionary* dict, Request* req);


void set(Dictionary* dict, Request* req){
    slot* get_req = get(dict, req);
    if(get_req == NULL){
        printf("Not found, adding to head\n");
        slot* new = malloc(sizeof(slot));
        new->key = req->key;
        new->value = req->value;
        new->expiry = req->time_to_live;
        new->next = dict->first;
        dict->first = new;
        return;
    }
    printf("found it, changing\n");
    get_req->value = req->value;
}
slot* get(Dictionary* dict, Request* req){
    slot* current = dict->first;
    
    while(current != NULL){
        fflush(stdout);
        if(strcmp(current->key, req->key) == 0 && (current->expiry == -1 || time(NULL) < current->expiry)){
            return current;
        }

        current = current->next;
    }
    return NULL;
}
slot* del(Dictionary* dict, slot* slot){
    exit_with_error("To implement\n");
}

void handle_connection(int fd, int id){
    int ret;
    fd_set readfd;

    client_socket = fd;
    Dictionary dict = {0};
    
    while(1){
        FD_ZERO(&readfd);
        FD_SET(client_socket, &readfd);

        ret = select(client_socket + 1, &readfd, NULL, NULL, NULL);
        if(ret > 0){
            char buf[MAX_BUF] = {0};
            ret = recv(fd, &buf, MAX_BUF, 0);
            if(ret == -1) exit_with_error("Error receiving");
            else if(ret == 0) exit_with_error("pipe closed");
            Request *req = parse(buf);
            handle_request(&dict, req);
            free(req);
        }
    }
    _exit(0);
}

void removeChars(char *str) {
    char *src, *dst;
    for (src = dst = str; *src != '\0'; src++) {
        *dst = *src;
        if (*dst != '\n') dst++;
    }
    *dst = '\0';
}

Request* parse(char* buf){
    Request* ret = calloc(1, sizeof(Request));
    ret->time_to_live= -1;
    ret->request_type = INFO;
    int index = 0;
    int number_of_elems = 0;
    int size_of_next_elem = 0;
    removeChars(buf);
    char* token = strtok(buf, "\r");
    while(token){
        if(index == 0){
            number_of_elems = atoi(token+1);
        } else{
            if(index%2){
                size_of_next_elem = atoi(token+1);
            } else {
                if(index == 2){
                    if(memcmp(token, "CLIENT", size_of_next_elem) != 0){
                        ret->request_type = (memcmp(token, "GET", size_of_next_elem) == 0) ? GET : SET;
                    }
                } else if(index == 4 ){
                    ret->key = malloc(sizeof(char)* size_of_next_elem+1);
                    memcpy(ret->key, token, size_of_next_elem+1);
                } else if(index == 6){
                    ret->value = malloc(sizeof(char)* size_of_next_elem+1);
                    memcpy(ret->value, token, size_of_next_elem+1);
                } else if(index == 10){
                    ret->time_to_live = time(NULL) + atoi(token);
                }
            }
        }
        index++;
        token = strtok(NULL, "\r");
    }
    return ret;
}

void handle_request(Dictionary* dict, Request* req){
    printf("Handling request ... \n");
    struct sembuf sem_op = {0, -1, 0};
    int ret = semop(sem_id, &sem_op, 1);
    if(ret == -1){
        perror("Error waiting on semaphore!");
        exit(-1);
    }
    switch(req->request_type){
        case(INFO):
            printf("DETECTED useless garbaj\n");
            send_tcp(client_socket, OK, NULL);
            break;
        case(GET):
            printf("DETECTED GET\n");
            slot* ret = get(dict, req);
            if(ret == NULL){
                send_tcp(client_socket, NOT_FOUND, NULL);
            }else{
                send_tcp(client_socket, GET_SUCCEEDED, ret);
            }
            break;
        case(SET):
            printf("DETECTED SET\n");
            set(dict, req);
            send_tcp(client_socket, OK, NULL);
            break;
        default:
            printf("Sum Tin Wong\n");
    }
    sem_op.sem_op = 1;
    ret = semop(sem_id, &sem_op, 1);
    if(ret == -1){
        perror("Error freeing semaphore!");
        exit(-1);
    }
 }


void send_tcp(int socket, int request, slot* slot){
    char buf[MAX_BUF];
    if(request == GET_SUCCEEDED){
        snprintf(buf, MAX_BUF, "$%ld\r\n%s\r\n", strlen(slot->value), slot->value);
        printf("Sending GET response! %s\n", buf);
        int ret = send(socket, buf, strlen(buf), 0);
        if(ret == -1) exit_with_error("error sending GET response");
    } if(request == OK){
        printf("Sending OK!\n");
        snprintf(buf, MAX_BUF, "+0K\r\n");
        int ret = send(socket, buf, strlen(buf), 0);
        if (ret == -1) exit_with_error("Error sending OK");
    } if(request == NOT_FOUND){
        printf("Sending NOT FOUND!\n");
        snprintf(buf, MAX_BUF, "$-1\r\n");
        int ret = send(socket, buf, strlen(buf), 0);
        if(ret == -1) exit_with_error("error sending NOT FOUND response");
    } 

}

int main(int argc, const char * argv[]) {

    int ret, pid, child_id = 0, opt = 1;
    sem_id = semget(IPC_PRIVATE, 1, IPC_CREAT | 0666);
    union semun {
        int val;
        struct semid_ds *buf;
        unsigned short *array;
        struct seminfo *__buf;
    };
    
    union semun sem_val = {.val = 1};
    ret = semctl(sem_id, 0, SETVAL, sem_val);

    if(ret ==-1){
        perror("Error creating semaphore!");
        exit(1);
    }

    // Open Socket and receive connections
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if(server_fd < 0) exit_with_error("Error creating socket");


    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) exit_with_error("Error with setting opt");

    struct sockaddr_in server_addr = {0};
    socklen_t addr_len = sizeof(struct sockaddr_in);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    ret = bind(server_fd, (struct sockaddr*) &server_addr, addr_len);
    if(ret < 0) exit_with_error("Error Binding");

    ret = listen(server_fd, MAX_PROCS);
    printf("Listening\n");
    while(1){
        int client_fd = accept(server_fd, (struct sockaddr*) &server_addr, &addr_len);
        if(ret < 0) exit_with_error("Error accepting");

        pid = fork();
        switch(pid){
            case(-1):
                exit_with_error("Error connecting");
                break;
            case(0):
                printf("Accepted connection number %d\n", child_id);
                handle_connection(client_fd, child_id++);
                break;
        }
    }
    
    for(;child_id>0; child_id--){
        pid = wait(NULL);
    }

    return 0;

}
