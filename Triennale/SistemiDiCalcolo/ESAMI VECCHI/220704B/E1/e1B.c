#include "e1B.h"

int count_matching_vars(char** vars, char* pattern) {
    if (vars == NULL || pattern == NULL) return -1;
    int count = 0;
    while(*vars) {
        char* value = getenv(*vars);
        if (value && strstr(value, pattern))
            count += 1;
        vars++;
    }
    return count;
}
