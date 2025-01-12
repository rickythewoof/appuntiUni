#include "e1A.h"

int crc32(char *bytes, int n) {
    int i, j;
    int crc = 0xFFFFFFFF; // valore iniziale
    for (i = 0; i < n; i++) {
        int byte = bytes[i]; // attenzione!
        crc = crc ^ byte;
        for (j = 0; j < 8; j++) {
            int mask = crc & 1;
            mask = -mask; // operazione: neg
            crc = (crc >> 1) ^ (0xEDB88320 & mask);
        }
    }
    return ~crc; // operazione: not
}
