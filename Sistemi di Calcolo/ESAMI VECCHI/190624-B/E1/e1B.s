.globl has_duplicates

has_duplicates:
    pushl %ebx
    pushl %edi
    pushl %esi
    pushl %ebp

    movl 20(%esp), %ebx
    movl 24(%esp), %edi
    movl $0, %esi

    movl $0, %eax

L1:
    cmpl %edi, %esi
    jae NL1
    movl %esi, %ebp
L2:
    cmpl %edi, %ebp
    jae NL2

    movl $1, %ecx
    movw (%ebx, %ebp, 2), %dx
    cmpw (%ebx, %esi, 2), %dx
    cmovel %ecx, %eax

    incl %ebp
    jmp L2
NL2:
    incl %esi
    jmp L1
NL1:
return:
    popl %ebp
    popl %esi
    popl %edi
    popl %ebx
    ret

