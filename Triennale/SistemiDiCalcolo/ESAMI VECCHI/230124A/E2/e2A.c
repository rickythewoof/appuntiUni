#include "e2A.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void checkRes(int i, char* msg){
    if(i != -1) return;
    perror(msg);
    exit(EXIT_FAILURE);
}

char* openEntry(const char* filename){
    int fd = open(filename, O_RDONLY);
    checkRes(fd, "open");
    ssize_t size = lseek(fd, 0, SEEK_END);
    lseek(fd, 0, SEEK_SET);
    char buf[size+1];
    buf[size]  = '\0';
    int red = read(fd, buf, size);
    checkRes(red, "read");
    char* res = strdup(buf);
    fd = close(fd);
    checkRes(fd, "close");
    return res;
}

void decodeTextFile(const char * encoded_file, const char * key, char ** decoded_text){
    int fd = open(encoded_file, O_RDONLY);
    checkRes(fd, "open");
    ssize_t size = lseek(fd, 0, SEEK_END);
    lseek(fd, 0, SEEK_SET);
    char buf[size+1];
    buf[size]  = '\0';
    int res = read(fd, buf, size);
    checkRes(res, "read");
    *decoded_text = strdup(buf);
    char* keys = openEntry(key);
    for(int i = 0; i < size; i++){
        char c = buf[i];
        if(c > 64 && c < 123){
            int entry = c - 65;
            (*decoded_text)[i] = keys[entry];
        }
    }
    free(keys);
    fd = close(fd);
    checkRes(fd, "close");
    return;
}

