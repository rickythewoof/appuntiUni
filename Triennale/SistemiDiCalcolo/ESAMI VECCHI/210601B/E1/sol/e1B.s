.globl adler32_simplified

adler32_simplified: # unsigned int adler32_simplified(unsigned char* data, int len)
    pushl %ebx
    pushl %edi
    pushl %esi

    movl $1, %ecx               # unsigned int   ecx = 1;
    xorl %eax, %eax             # unsigned int   eax = 0;
    xorl %edx, %edx             # int            edx = 0;
    movl 16(%esp), %ebx         # unsigned char* ebx = data;
    movl 20(%esp), %edi         # int            edi = len;
L:
    cmpl %edi, %edx             # if (edx >= edi)
    jge E                       #    goto E;
    movzbl (%ebx, %edx), %esi   # unsigned int esi = ebx[edx];
    addl %esi, %ecx             # ecx = ecx + esi;
    andl $0xFFFF, %ecx          # ecx = ecx & 0xFFFF;
    addl %ecx, %eax             # eax = eax + ecx;
    andl $0xFFFF, %eax          # eax = eax & 0xFFFF;
    incl %edx                   # edx += 1;
    jmp L                       # goto L;
E:
    shll $16, %eax              # eax = eax << 16;
    orl %ecx, %eax              # eax = eax | ecx;

    popl %esi
    popl %edi
    popl %ebx
    ret                     # return eax;
