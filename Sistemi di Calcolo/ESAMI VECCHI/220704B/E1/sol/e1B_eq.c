#include "../e1B.h"

int count_matching_vars(char** vars, char* pattern) {
    int count = -1;
    if (vars == NULL) goto E;
    if (pattern == NULL) goto E;
    count = 0;
L:
    if(*vars == NULL) goto E;
    char* v = *vars;
    char* value = getenv(v);
    if (value == NULL) goto F;
    value = strstr(value, pattern);
    if (value == NULL) goto F;
    count += 1;
F:
    vars++;
    goto L;
E:
    return count;
}
