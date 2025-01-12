.globl adler32_simplified

adler32_simplified:
    pushl %ebx
    pushl %ebp
    pushl %edi
    pushl %esi

    movl 20(%esp), %ebx
    movl 24(%esp), %ebp

    movl $1, %edi
    movl $0, %esi

    xorl %ecx, %ecx

L:
    cmpl %ecx, %ebp
    jbe NL
    movzbl (%ebx, %ecx, 1), %edx
    addl %edx, %edi
    andl $0xFFFF, %edi

    addl %edi, %esi
    andl $0xFFFF, %esi
    incl %ecx
    jmp L
NL:
    movl %esi, %eax
    shll $16, %eax
    orl %edi, %eax

return:
    popl %esi
    popl %edi
    popl %ebp
    popl %ebx
    ret
