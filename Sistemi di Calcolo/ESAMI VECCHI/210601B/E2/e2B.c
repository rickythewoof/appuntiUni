#include "e2B.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

off_t searchfile(char* filename, char c){
    int fd = open(filename, 'r');
    if (fd == -1){
        perror("open");
        exit(EXIT_FAILURE);
    }
    char buf[2] = { 0 };
    off_t res = -1;
    while(1){
        int readChar = read(fd, buf, 1);
        if(readChar == 0)
            break;
        if(buf[0] == c){
            res = lseek(fd, 0, SEEK_CUR) - 1;
            break;
        }
    }
    fd = close(fd);
    if (fd == -1){
        perror("close");
        exit(EXIT_FAILURE);
    }
    return res;

}