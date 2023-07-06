#include "../e2B.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

void check_error(int res, char* msg) {
    if (res != -1) return;
    perror(msg);
    exit(EXIT_FAILURE);
}

int wordcount(const char** s, int n){
	int count = 0;
	if (n==0) return -1;
	for (int k=0; k<n; k++){
		pid_t pid = fork();
		check_error(pid, "Error with fork");
		if (pid==0) {
			int words=0;
			const char* string = s[k];
			if (*string=='\0') exit(0);
			while (*string) {
				if (*string==' ')
					words++;
				string++;
			}
			exit(words+1);
		}
		int status;
		wait(&status);
		if (WIFEXITED(status))
			if (WEXITSTATUS(status) > count) count = WEXITSTATUS(status);
	}
	return count;
}

