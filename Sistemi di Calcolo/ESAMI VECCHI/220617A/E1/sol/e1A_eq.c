#include "e1A.h"

int crc32(char *bytes, int n) {
    int j;
    int crc = 0xFFFFFFFF; // valore iniziale
    int i = 0;
L1:
    if (i >= n) goto E1;
    int byte = bytes[i];
    crc = crc ^ byte;
    j = 0;
L2:
    if (j >= 8) goto E2;
    int mask = crc;
    mask = mask & 1;
    mask = -mask;
    crc = crc >> 1;
    mask = 0xEDB88320 & mask;
    crc = crc ^ mask;
    j += 1;
    goto L2;
E2:
    i += 1;
    goto L1;
E1:
    crc = ~crc;
    return crc;
}