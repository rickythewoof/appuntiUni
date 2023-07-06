#include "e2A.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int countOccurrences(const char* s, char c){
    int occ = 0;
    for(int i = 0; s[i] != '\0'; i++){
        if (s[i] == c) occ++;
    }

    return occ;
}

void checkRes(int i, char* msg){
    if(i != -1) return;
    perror(msg);
    exit(EXIT_FAILURE);
}

int multicount(const char** s, char c, int n){
    if(n == 0 || c == 0)
        return -1;
    int maxOcc = 0;
    for(int i = 0; i<n; i++){
        pid_t pid = fork();
        checkRes(pid, "fork");
        if(pid == 0){
            _exit(countOccurrences(s[i],c));
        }
    }
    for(int i = 0; i<n; i++){
        int occ;
        pid_t pid = wait(&occ);
        if(WEXITSTATUS(occ)>maxOcc) maxOcc = WEXITSTATUS(occ);
    }
    printf("max oxccurrences = %d\n", maxOcc);
    return maxOcc;    
}