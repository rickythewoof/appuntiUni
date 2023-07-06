#include "e2B.h"
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

int isAfterTime(const char* control, const char* ref){
    for(int i = 0; i < 5; i++){
        if(control[i] < ref[i])
            return 0;
        else if(control[i] > ref[i])
            return 1;
    }
    return 1;
}

void getBookingsAfterTime(struct booking ** list, const char * filename,  const char * time){
    int fd = open(filename, O_RDONLY);
    checkRes(fd, "open");
    struct booking* last = NULL;
    *list = last;

    char buf[38];
    buf[37] = '\0';
    while(1){
        int charRead = read(fd, buf, 37);
        checkRes(charRead, "read");
        if(charRead < 1)
            break;
        char name[31];
        char size[3];
        char hour[6];
        int i;
        for(i = 0; i < 31; i++){
            if(buf[i] == '_'){
                name[i] = '\0';
                break;
            }
            name[i] = buf[i];

        }
        for(i = 30; i < 32; i++){
            size[i-30] = buf[i];
        } size[2] = '\0';

        for(i = 32; i < 37; i++){
            hour[i-32] = buf[i];
        } hour[5] = '\0';



        if(!isAfterTime(hour, time)){
            printf("%s < %s\n", hour, time);
            continue;
        }
        
        printf("name = %s\tsize = %d\thour = %s\n", name, atoi(size), hour);

        struct booking* curr = malloc(sizeof(struct booking));
        curr->surname = malloc(31);
        curr->places = atoi(size);
        curr->time = malloc(6);
        strncpy(curr->surname, name, 31);
        strncpy(curr->time, hour, 6);
        curr->next = NULL;
        
        if(last == NULL)
           *list = curr;
        else
            last->next = curr;
        last = curr;
    }
    
    fd = close(fd);
    checkRes(fd, "close");
    return;
}
