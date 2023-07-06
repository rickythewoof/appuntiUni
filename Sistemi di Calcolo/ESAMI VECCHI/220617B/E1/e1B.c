#include "e1B.h"

int crc32b(char *bytes, int n) {
    int magic = ~0; // operazione: not
    int crc = magic;
    while (n--) {
        int value;
        int byte = *bytes++; // attenzione!
        int index = crc ^ byte;
        get_constant(&value, index & 0xFF);
        crc = value ^ (crc >> 8);
    }
    return crc ^ magic;
}

