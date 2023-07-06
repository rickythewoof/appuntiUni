#include "../e1A.h"
#include <string.h>

int suffix(const char* a, const char* b) {
    const char* ebx = a;
    const char* ebp = b;
    int esi = strlen(ebx);
    int edi = strlen(ebp);
    int eax = 0;
    if (edi > esi)
        goto E;
    int ecx = esi;
    ecx = ecx - edi;
L:  if (ecx >= esi)
        goto M;
    if (ebx[ecx] != *ebp)
        goto E;
    ebp++;
    ecx++;
    goto L;
M:  eax = 1;
E:  return eax;
}
