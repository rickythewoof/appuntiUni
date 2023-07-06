#include "e1A.h"

int count_tokens(char* str, const char* sep) {
    int cnt = 0;
    char* token = strtok(str, sep);
    while (token != NULL) {
        cnt++;
        token = strtok(NULL, sep);
    }
	return cnt;
}
