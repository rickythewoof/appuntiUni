#include "e2A.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

void check_res(int i, char* msg){
    if(i != -1) return;
    perror(msg);
    exit(EXIT_FAILURE);
}

int contains(char* s, char c, int n){
    int m = strlen(s)/n;
    if(m*n < strlen(s)){
        for(int j = n*m; j < strlen(s); j++)
            if(s[j] == c) return 1;
    }
    for(int i = 0; i <n; i++){
        pid_t pid = fork();
        check_res(pid, "fork");
        if(pid == 0){
            int res = 0;
            for(int k = i*m; k < (i+1)*m; k++)
                if(s[k] == c) res = 1;
            _exit(res);
        }

    }
    int return_res = 0;
    for(int i = 0; i<n; i++){
        int status;
        pid_t pid = wait(&status);
        check_res(pid, "wait");
        if(WIFEXITED(status) && WEXITSTATUS(status) == 1)
            return_res = 1;
    }
    return return_res;
}
