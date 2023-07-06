#include "e1A.h"

int suffix(const char* a, const char* b) {
    int alen = strlen(a), blen = strlen(b), i;
    if (blen > alen) return 0;
    for (i=alen-blen; i<alen; i++)
        if (a[i] != *b++) return 0;
	return 1;
}
