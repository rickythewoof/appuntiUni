.globl count_matching_vars

count_matching_vars:
    pushl %ebx
    pushl %ebp
    pushl %edi
    pushl %esi
    subl $8, %esp

    movl 28(%esp), %ebx
    movl 32(%esp), %ebp
    movl $-1, %eax
    cmpl $0, %ebx
    je return
    cmpl $0, %ebp
    je return

    xorl %edi, %edi
L:
    cmpl $0, (%ebx)
    je E1
    movl (%ebx), %ecx
    movl %ecx, (%esp)
    call getenv
    movl %eax, %esi
    cmpl $0, %esi
    je outif

    movl %esi, (%esp)
    movl %ebp, 4(%esp)
    call strstr
    cmpl $0, %eax
    je outif
    incl %edi
    
outif:
    addl $4, %ebx
    jmp L
E1:
    movl %edi, %eax
return:
    addl $8, %esp
    popl %esi
    popl %edi
    popl %ebp
    popl %ebx
    ret
