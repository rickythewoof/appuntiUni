#include "../e1A.h"

int count_tokens(char* str, const char* sep) {
    char *ecx = str;
    const char *esi = sep;
    int ebx = 0;
    char* ebp = strtok(ecx, esi);
L:  if (ebp == NULL) goto E;
    ebx++;
    ebp = strtok(NULL, esi);
    goto L;
E:; int eax = ebx;
	return eax;
}
