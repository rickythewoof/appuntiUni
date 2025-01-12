#include "e2A.h"
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>

void run(int* v, int n, int (*f)(int i)){
    for(int i = 0; i<n; i++){
        pid_t pid = fork();
        if(pid == -1){
            perror("fork");
            exit(EXIT_FAILURE);
        }
            
        if(pid == 0){
            int ret = f(i);
            _exit(ret);
        }
    }
    for(int i = 0; i<n; i++){
        int status;
        if(wait(&status) == -1){
            perror("wait");
            exit(EXIT_FAILURE);
        }
            
        if(WIFEXITED(status)){
            v[i] = WEXITSTATUS(status);
        }
    }
}

