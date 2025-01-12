#include "e1B.h"

int crc32b(char *bytes, int n) {
    int magic = 0; 
    magic = ~magic;
    int crc = magic;
L1: 
    if (n <= 0) goto E1;
    int value;
    int byte = *bytes++; // attenzione!
    int index = crc ^ byte;
    index = index & 0xFF;
    get_constant(&value, index);
    crc = crc >> 8;
    crc = value ^ crc;
    n--;
    goto L1;
E1:
    crc = crc ^ magic;
    return crc;
}