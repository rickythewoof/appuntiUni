.globl crc32

crc32: # unsigned int crc32(unsigned char *bytes, int n) {
    pushl %esi
    pushl %edi
    # int j;
    movl $0xFFFFFFFF, %eax  # int crc = 0xFFFFFFFF; // valore iniziale
    xorl %ecx, %ecx         # int i = 0;
    movl 12(%esp), %edx      
L1:
    cmpl 16(%esp), %ecx      # if (i >= n) goto E1;
    jge E1
    movzbl (%edx, %ecx), %esi
    xorl %esi, %eax         # crc = crc ^ bytes[i];
    xorl %esi, %esi         # j = 0;
L2:
    cmpl $8, %esi           # if (j >= 8) goto E2;
    jge E2
    movl %eax, %edi         # int mask = crc;
    andl $1, %edi           # mask = mask & 1;
    negl %edi               # mask = -mask;
    sarl $1, %eax           # crc = crc >> 1;
    andl $0xEDB88320, %edi  # mask = 0xEDB88320 & mask;
    xorl %edi, %eax         # crc = crc ^ mask;
    incl %esi               # j += 1;
    jmp L2;
E2:
    incl %ecx               # i += 1;
    jmp L1;
E1:
    notl %eax               #  crc = ~crc;
    popl %edi
    popl %esi
    ret                     # return crc;
