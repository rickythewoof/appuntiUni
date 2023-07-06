#include "e2A.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>


char* load(const char* filename, unsigned* size){
    char* ret = NULL;
    int fd = open(filename, 'r');
    if(fd == -1){
        perror("open");
        exit(EXIT_FAILURE);
    }
    *size = lseek(fd, 0, SEEK_END);
    lseek(fd, 0, SEEK_SET);
    ret = malloc(*size);
    int readChars = read(fd, ret, *size);
    if(readChars != *size){
        printf("errore lettura!");
        exit(EXIT_FAILURE);
    }

    fd = close(fd);
    if(fd == -1){
        perror("close");
        exit(EXIT_FAILURE);
    }

    return ret;
}

