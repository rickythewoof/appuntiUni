#include "e1A.h"

int* strings_are_upper(const char** array, int n) {
    if (array == NULL) return NULL;
    if (n <= 0) return NULL;
    int* res = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        const char* s = array[i];
        res[i] = 1;
        while (*s) {
            // isupper e' una funzione della libc (vedere: man isupper)
            if (isupper(*s) == 0) {
                res[i] = 0;
                break;
            }
            s += 1;
        }
    }
    return res;
}
