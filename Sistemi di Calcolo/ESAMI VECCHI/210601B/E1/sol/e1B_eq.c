#include "../e1B.h"

unsigned int adler32_simplified(unsigned char* data, int len)
{
    // a <-> ecx, b <-> eax, index <-> edx, data <-> ebx, len <-> edi
    unsigned int   ecx = 1;
    unsigned int   eax = 0;
    int            edx = 0;
    unsigned char* ebx = data;
    int            edi = len;
L:
    if (edx >= edi)
        goto E;
    unsigned int esi = ebx[edx]; // promozione!
    ecx = ecx + esi;
    ecx = ecx & 0xFFFF;
    eax = eax + ecx;
    eax = eax & 0xFFFF;
    edx += 1;
    goto L;
E:
    eax = eax << 16;
    eax = eax | ecx;
    return eax;
}