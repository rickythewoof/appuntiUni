#include "../e1A.h"

int* strings_are_upper(const char** array, int n) {
    int* eax2 = NULL;
    if (array == NULL) goto EF;
    if (n <= 0) goto EF;

    const char** ebx = array;
    int eax = sizeof(int);
    eax = n * eax;
    int* esi = malloc(eax);
    int ebp = 0;
L:
    if (ebp >= n) goto E;
    const char* edi = ebx[ebp];
    esi[ebp] = 1;
L2:
    if (*edi == 0) goto E2;
    int eax3 = isupper(*edi);
    if (eax3 != 0) goto C;
    esi[ebp] = 0;
    goto E2;
C:
    edi += 1;
    goto L2;
E2:
    ebp += 1;
    goto L;
E:
    eax2 = esi;
EF:
    return eax2;
}
