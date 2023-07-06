#include "../e2A.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

void check_error(int res, char* msg) {
    if (res != -1) return;
    perror(msg);
    exit(EXIT_FAILURE);
}

int multicount(const char** s, char c, int n){
	int count = 0;
	if (c=='\0' || n==0) return -1;
	for (int k=0; k<n; k++){
		pid_t pid = fork();
		check_error(pid, "Error with fork");
		if (pid==0) {
			const char* string = s[k];
			while (*string) {
				if (*string==c)
					count++;
				string++;
			}
			exit(count);
		}
	}
	int status;
	while(wait(&status) > 0)
		if (WIFEXITED(status))
			if (WEXITSTATUS(status) > count) count = WEXITSTATUS(status);

	return count;
}

