#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/sem.h>
#include <sys/ipc.h>
#include <sys/mman.h>


int sem;

void f1(void * arg){
    struct sembuf sembf ={.sem_num = 0, .sem_op=-1, .sem_flg = 0};
    int ret = semop(sem, &sembf, 1);
    if(ret <0){
        perror("Error semop child");
        exit(1);
    }
        //Critical Section
        printf("[CHILD] Accessed CS\n");
        sleep(2);

    sembf.sem_op = 1;
    ret = semop(sem, &sembf, 1);
    if(ret <0){
        perror("Error semop child");
        exit(1);
    }
    return;
}

void f2(){
    struct sembuf sembf ={.sem_num = 0, .sem_op=-1, .sem_flg = 0};
    int ret = semop(sem, &sembf, 1);
    if(ret <0){
        perror("Error semop");
        exit(1);
    }
        //Critical Section
        printf("[PARENT] Accessed CS\n");
        sleep(2);
        
    sembf.sem_op = 1;
    ret = semop(sem, &sembf, 1);
    if(ret <0){
        perror("Error semop");
        exit(1);
    }
    return;
}

void* map_mem(int fd, int len_size){
    void* res = mmap(NULL, len_size, PROT_NONE, MAP_SHARED, fd, 0);
    if(res == MAP_FAILED){
        perror("Error with mmap");
        exit(1);
    }
    return res;
}

int map_sync(void* map, int len, int fd){
    int ret = msync(map, len, MS_ASYNC);
    if(ret < 0){
        perrof("Error msync");
        exit(1);
    }
    return 0;
}

int unmap_mem(void* map, int len, int fd){
    int ret = munmap(map, len);
    if(ret < 0){
        perror("Error munmap");
        exit(1);
    }
    close(fd);
    return 0;
}

int main(int argc, char** argv){

    sem = semget(IPC_PRIVATE, 1, IPC_CREAT|IPC_EXCL| 0600);
    if(sem < 0){
        perror("Error creating semaphore");
        exit(1);
    }
    union semun{
        int val;
        struct semid_ds* buf;
        unsigned short *array;
        struct seminfo *__buf;
    } sem_un;

    sem_un.val = 1;

    semctl(sem, 0, SETVAL, sem_un);
    pid_t pid;
    pid = fork();
    switch(pid){
        case(-1):
            perror("Error forking");
            exit(1);
            break;
        case(0):
            f1(NULL);
            break;
        default:
            f2();
            break;
    }

    return 0;
}