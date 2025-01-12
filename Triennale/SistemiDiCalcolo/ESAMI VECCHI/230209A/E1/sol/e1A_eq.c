#include "../e1A.h"

int* check_quiz(char** answers, char* solution, int n) {
    int* eax = NULL;
    if (answers == NULL) 
    goto E;
    if (solution == NULL)
    goto E;
    if (n <= 0)
    goto E;
    int edx = sizeof(int) * n;
    eax = malloc(edx);
    int esi = 0;
    char** ebp = answers;
    char* ebx = solution;
L1:
    if (esi >= n) goto E;
    eax[esi] = 0;
    edx = 0;
L2:
    if (edx >= 4) goto F;
    char* edi = ebp[esi];
    char cl = ebx[edx];
    if (edi[edx] != cl) goto F2;
    eax[esi] += 1;
F2:
    edx++;
    goto L2;
F:
    esi += 1;
    goto L1;
E:
    return eax;
}
