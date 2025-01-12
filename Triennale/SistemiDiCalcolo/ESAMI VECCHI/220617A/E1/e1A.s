.globl crc32
crc32:
    pushl %ebx
    pushl %ebp
    pushl %esi
    pushl %edi

    movl 20(%esp), %ebx
    movl $0xFFFFFFFF, %eax

    xorl %ecx, %ecx
L1:
    cmpl 24(%esp), %ecx
    jge NL1
    movzbl (%ebx, %ecx), %ebp
    xorl %ebp, %eax
    xorl %edx, %edx
L2:
    cmpl $8, %edx
    jge NL2
    movl %eax, %ebp
    andl $1, %ebp
    negl %ebp
    andl $0xEDB88320, %ebp

    shrl $1, %eax
    xorl %ebp, %eax
    incl %edx
    jmp L2
NL2:
    incl %ecx
    jmp L1
NL1:
    notl %eax

    popl %edi
    popl %esi
    popl %ebp
    popl %ebx
    ret
