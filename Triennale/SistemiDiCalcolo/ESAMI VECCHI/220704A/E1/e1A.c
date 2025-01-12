#include "e1A.h"

int* count_vars(char** vars, int n) {
    int i;
    if (vars == NULL || n <= 0) return NULL;
    int* out = malloc(sizeof(int) * n);
    for (i = 0; i < n; i++) {
        if (getenv(vars[i]) != NULL)
            out[i] = 1;
        else
            out[i] = 0;
    }
    return out;
}
