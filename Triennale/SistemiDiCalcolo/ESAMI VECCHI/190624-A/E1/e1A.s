.globl init_matrix

init_matrix:
    pushl %ebx
    pushl %ebp
    pushl %esi
    pushl %edi
    subl $8, %esp

    movl 28(%esp), %ebx
    movl 32(%esp), %ebp
    movl $0, %esi
    movl $0, %edi

L1:
    cmpl %ebp, %esi
    jge NL1
L2:
    cmpl %ebp, %edi
    jge NL2
    movl %esi, (%esp)
    movl %edi, 4(%esp)
    call value
    movl (%ebx, %esi, 4), %ecx
    movw %ax, (%ecx, %edi, 2)
    incl %edi
    jmp L2

NL2:
    incl %esi
    jmp L1
NL1:
    addl $8, %esp
    popl %edi
    popl %esi
    popl %ebp
    popl %ebx
    ret
