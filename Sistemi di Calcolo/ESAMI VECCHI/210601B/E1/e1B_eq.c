#include "e1B.h"

/*
Adler-32 e' un algoritmo di checksum ideato nel 1995 da Mark Adler ed e'
pensato per essere molto efficiente, anche a scapito della sua robustezza.
E' ancora oggi usato in molte applicazioni (non crittografiche!), ad 
esempio in librerie di compressione come ZLIB.

Ve lo proponiamo in una forma leggermente semplificata.
*/

unsigned int adler32_simplified(unsigned char* data, int len)
{
    unsigned int a = 1, b = 0;
    int          index;

    for (index = 0; index < len; ++index) {
        printf("1\n");
        a = (a + data[index]);
        a = a & 0xFFFF;
        b = (b + a);
        b = b & 0xFFFF;
    }

    int eax = b;
    eax = eax << 16;
    eax = eax | a;
    return eax;
}