.globl count_vars

count_vars:
    pushl %ebx
    pushl %ebp
    pushl %edi
    pushl %esi
    subl $4, %esp

    movl 24(%esp), %ebx
    movl 28(%esp), %edi
    movl $0, %eax
    cmpl $0, %ebx
    je return
    cmpl $0, %edi
    jbe return
    movl %edi, %ecx
    imull $4, %ecx
    movl %ecx, (%esp)
    call malloc
    movl %eax, %esi
    xorl %ebp, %ebp
L:
    cmpl %edi, %ebp
    jae NL
    movl (%ebx, %ebp, 4), %ecx
    movl %ecx, (%esp)
    call getenv
    cmpl $0, %eax
    jne IF1
    movl $0, (%esi, %ebp, 4)
    jmp NIF1
IF1:
    movl $1, (%esi, %ebp, 4)
NIF1:
    incl %ebp
    jmp L
NL:
    movl %esi, %eax

return:
    addl $4, %esp
    popl %esi
    popl %edi
    popl %ebp
    popl %ebx
    ret
    