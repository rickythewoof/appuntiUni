#include "../e2A.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

char* load(const char* filename, unsigned* size) {
    int fd = open(filename, O_RDONLY);
    if (*size == -1) {
        perror("Errore in open: ");
        exit(EXIT_FAILURE);
    }

    *size = lseek(fd, 0, SEEK_END);
    if (*size == -1) {
        perror("Errore in lseek: ");
        exit(EXIT_FAILURE);
    }

    int res = lseek(fd, 0, SEEK_SET);
    if (res == -1) {
        perror("Errore in lseek: ");
        exit(EXIT_FAILURE);
    }

    char *buf = malloc(*size*sizeof(char));
    if (buf == NULL) {
        perror("Errore in malloc: ");
        exit(EXIT_FAILURE);
    }

    res = read(fd, buf, *size);
    if (res < *size) {
        perror("Errore in read: ");
        exit(EXIT_FAILURE);
    }

    close(fd);

    return buf;
}
