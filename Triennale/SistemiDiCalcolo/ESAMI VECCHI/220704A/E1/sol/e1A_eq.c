#include "../e1A.h"

int* count_vars(char** vars, int n) {
    int i = 0;
    int* out = NULL;
    if (vars == NULL) goto E;
    if (n <= 0) goto E;
    size_t size = sizeof(int);
    size = size * n;
    out = malloc(size);
L:
    if (i >= n) goto E;
    if (getenv(vars[i]) == NULL) goto F;
    out[i] = 1;
    goto A;
F:
    out[i] = 0;
A:
    i++;
    goto L;
E:
    return out;
}