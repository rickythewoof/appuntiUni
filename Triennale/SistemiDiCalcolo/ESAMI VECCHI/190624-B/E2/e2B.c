#include "e2B.h"
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void check_ret(int i, char* msg){
    if(i == -1){
        perror(msg);
        exit(EXIT_FAILURE);

    }
}

void make_files(int n, void (*f)(int i, char name[64], char buf[256])){
    for(int i = 0; i < n; i++){
        pid_t pid = fork();
        check_ret(pid, "fork");
        if(pid == 0){
            char name[64];
            char buf[256];
            f(i, name, buf);
            int fp = open(name, O_CREAT | O_WRONLY | O_TRUNC, 00664);
            check_ret(fp, "File");
            int copy = write(fp, buf, 256);
            while(copy < strlen(buf+copy)+1)
                copy = write(fp, buf+copy, 256);
            check_ret(close(fp), "close");
            _exit(0);
        }
    }
    for(int i = 0; i<n; i++){
        wait(NULL);
    }
    return;
}

