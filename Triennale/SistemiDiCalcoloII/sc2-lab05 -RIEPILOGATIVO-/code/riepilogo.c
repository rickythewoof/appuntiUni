#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <semaphore.h>
#include <pthread.h>
#include <errno.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>        /* For mode constants */
#include <fcntl.h>           /* For O_* constants */

// macros for error handling
#include "common.h"

#define N 100   // child process count
#define M 10    // thread per child process count
#define T 3     // time to sleep for main process

#define FILENAME	"accesses.log"

sem_t *start, *ready, *semread;
int* stop;
int shd;

/*
 * data structure required by threads
 */
typedef struct thread_args_s {
    unsigned int child_id;
    unsigned int thread_id;
} thread_args_t;
/*
 * parameters can be set also via command-line arguments
 */
int n = N, m = M, t = T;

/* TODO: declare as many semaphores as needed to implement
 * the intended semantics, and choose unique identifiers for
 * them (e.g., "/mysem_critical_section") */

/* TODO: declare a shared memory and the data type to be placed 
 * in the shared memory, and choose a unique identifier for
 * the memory (e.g., "/myshm") 
 * Declare any global variable (file descriptor, memory 
 * pointers, etc.) needed for its management
 */


/*
 * Ensures that an empty file with given name exists.
 */
void init_file(const char *filename) {
    printf("[Main] Initializing file %s...", FILENAME);
    fflush(stdout);
    int fd = open(FILENAME, O_WRONLY | O_CREAT | O_TRUNC, 0600);
    if (fd<0) handle_error("error while initializing file");
    close(fd);
    printf("closed...file correctly initialized!!!\n");
}



void parseOutput() {
    // identify the child that accessed the file most times
    int* access_stats = calloc(n, sizeof(int)); // initialized with zeros
    printf("[Main] Opening file %s in read-only mode...", FILENAME);
	fflush(stdout);
    int fd = open(FILENAME, O_RDONLY);
    if (fd < 0) handle_error("error while opening output file");
    printf("ok, reading it and updating access stats...");
	fflush(stdout);

    size_t read_bytes;
    int index;
    do {
        read_bytes = read(fd, &index, sizeof(int));
        if (read_bytes > 0)
            access_stats[index]++;
    } while(read_bytes > 0);
    printf("ok, closing it...");
	fflush(stdout);

    close(fd);
    printf("closed!!!\n");

    int max_child_id = -1, max_accesses = -1;
    for (int i = 0; i < n; i++) {
        printf("[Main] Child %d accessed file %s %d times\n", i, FILENAME, access_stats[i]);
        if (access_stats[i] > max_accesses) {
            max_accesses = access_stats[i];
            max_child_id = i;
        }
    }
    printf("[Main] ===> The process that accessed the file most often is %d (%d accesses)\n", max_child_id, max_accesses);
    free(access_stats);
}

void* thread_function(void* x) {
    thread_args_t *args = (thread_args_t*)x;

    printf("[Child#%d-Thread#%d] Started thread_function\n", args->child_id, args->thread_id);
    fflush(stdout);
    /* TODO: protect the critical section using semaphore(s) as needed */
    sem_wait(semread);
    // open file, write child identity and close file
    int fd = open(FILENAME, O_WRONLY | O_APPEND);
    if (fd < 0) handle_error("error while opening file");
    //printf("[Child#%d-Thread#%d] File %s opened in append mode!!!\n", args->child_id, args->thread_id, FILENAME);	

    write(fd, &(args->child_id), sizeof(int));
    //printf("[Child#%d-Thread#%d] %d appended to file %s opened in append mode!!!\n", args->child_id, args->thread_id, args->child_id, FILENAME);	

    close(fd);
    //printf("[Child#%d-Thread#%d] File %s closed!!!\n", args->child_id, args->thread_id, FILENAME);
    sem_post(semread);
    free(x);
    pthread_exit(NULL);
}

void mainProcess() {
    /* TODO: the main process waits for all the children to be ready,
     * it notifies them to start their activities, and sleeps
     * for some time t. Once it wakes up, it notifies the children
     * to end their activities, and waits for their termination.
     * Finally, it calls the parseOutput() method and releases
     * any shared resources. */

    //ATTENDE READY
    for(int i = 0; i < N; i++){
        sem_wait(ready);
    }
    printf("EVERY CHILD IS READY, start \n");
    //TUTTI READY, DAI START
    for(int i = 0; i < N; i++){
        sem_post(start);
    }
    sleep(T); //dopo dai lo stop
    printf("[Main] Sending stop signal\n");
    *stop = 1;

    for(int i = 0; i < N; i++){
        wait(NULL);
    }

    parseOutput();
    
    //STOP AND DESTROY
    sem_close(start);
    sem_close(ready);
    sem_close(semread);
    sem_destroy(start);
    sem_destroy(ready);
    sem_destroy(semread);

    munmap(stop, sizeof(int));
    shm_unlink("/stopsig");
    close(shd);

}

void childProcess(int child_id) {
    /* TODO: each child process notifies the main process that it
     * is ready, then waits to be notified from the main in order
     * to start. As long as the main process does not notify a
     * termination event [hint: use sem_getvalue() here], the child
     * process repeatedly creates m threads that execute function
     * thread_function() and waits for their completion. When a
     * notification has arrived, the child process notifies the main
     * process that it is about to terminate, and releases any
     * shared resources before exiting. */

    start = sem_open("/semstart", 0);
    if(start == SEM_FAILED) handle_error("errore creazione semaforo start");
    ready = sem_open("/semready", 0);
    if(ready == SEM_FAILED) handle_error("errore creazione semaforo ready");
    semread = sem_open("/semread", 0);
    if(semread == SEM_FAILED) handle_error("errore creazione semaforo semread");
    int shd = shm_open("/stopsig", O_RDONLY, 0666);
    stop = mmap(0, sizeof(int), PROT_READ, MAP_SHARED, shd, 0);
    
    sem_post(ready); //Daje, sono ready
    sem_wait(start);
    while(!*stop){
        pthread_t child[M];
        int started = 0;
        for(int j = 0; j < M; j++){
            if(*stop) break;
            started++;
            thread_args_t* arg = malloc(sizeof(thread_args_t));
            arg->child_id = child_id;
            arg->thread_id = j;
            if(pthread_create(&child[j], NULL, thread_function, arg)!=0)
                handle_error("Errore pthread");
        }
        for(int j = 0; j < started; j++)
            if(pthread_join(child[j], NULL)!=0)
                handle_error("Errore join pthread");
    }

    
    //CHIUDI TUTTO
    sem_close(start);
    sem_close(ready);
    sem_close(semread);
    munmap(stop, sizeof(int));
    close(shd);
}

int main(int argc, char **argv) {
    // arguments
    if (argc > 1) n = atoi(argv[1]);
    if (argc > 2) m = atoi(argv[2]);
    if (argc > 3) t = atoi(argv[3]);

    // initialize the file
    init_file(FILENAME);

    /* TODO: initialize any semaphore needed in the implementation, and
     * create N children where the i-th child calls childProcess(i); 
     * initialize the shared memory (create it, set its size and map it in the 
     * memory), then the main process executes function mainProcess() once 
     * all the children have been created */
    
    //INIZIALIZZO SEMAFORI NAMED PER START E LETTURA
    sem_unlink("/semstart");
    sem_unlink("/semread");
    sem_unlink("/semready");
    start = sem_open("/semstart", O_CREAT | O_EXCL, 0666,0);
    if(start == SEM_FAILED) handle_error("errore creazione semaforo start");
    ready = sem_open("/semready", O_CREAT | O_EXCL, 0666,0);
    if(ready == SEM_FAILED) handle_error("errore creazione semaforo ready");
    semread = sem_open("/semread", O_CREAT | O_EXCL, 0666,1);
    if(semread == SEM_FAILED) handle_error("errore creazione semaforo semread");

    //INIZIALIZZO MEMORIA PER STOP SIG
    shm_unlink("/stopsig");
    shd = shm_open("/stopsig", O_CREAT | O_EXCL | O_RDWR, 0666);
    if (shd == -1) handle_error("Errore shm open");
    if(ftruncate(shd, sizeof(int))==-1) handle_error("Errore ftrunc");
    stop = mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, shd, 0);
    *stop = 0;

    
    for (int i = 0; i < N; i++){
        pid_t pid = fork();
        if(pid == -1) handle_error("Errore Creazione processo");
        if(pid == 0){
            childProcess(i);
            _exit(EXIT_SUCCESS);
        }
    }
    mainProcess();

    exit(EXIT_SUCCESS);
}