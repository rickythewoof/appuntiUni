#include "../e2B.h"
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
// inserisci la soluzione qui...

void check_error(long res, char* msg) {
    if (res != -1) return;
    perror(msg);
    exit(EXIT_FAILURE);
}

off_t searchfile(char* filename, char c){
	off_t off=-1;
	int i, fd;
	ssize_t res;
	char cinf;

	fd = open(filename, O_RDONLY);
	check_error(fd, "open");

	for (;;) {
		res = read(fd, &cinf, 1);
        check_error(res, "read");
        if (res == 0) break;
		if (cinf==c) {
			off = lseek(fd, 0, SEEK_CUR) - 1;
			check_error(off, "lseek");
			break;
		}
    }

	res = close(fd);
	check_error(res, "close");

	return off;
}

