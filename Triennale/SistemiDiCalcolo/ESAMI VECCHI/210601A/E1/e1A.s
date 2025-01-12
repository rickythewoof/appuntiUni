.globl count_tokens

count_tokens:
    pushl %ebx
    pushl %ebp
    pushl %edi
    pushl %esi
    subl $8, %esp

    movl 28(%esp), %ebx
    movl 32(%esp), %ebp
    xorl %edi, %edi

    movl %ebx, (%esp)
    movl %ebp, 4(%esp)
    call strtok
    
L:
    movl %eax, %esi
    cmpl $0, %esi
    je NL
    incl %edi
    movl $0, (%esp)
    movl %ebp, 4(%esp)
    call strtok
    jmp L

NL:
    movl %edi, %eax
    addl $8, %esp
    popl %esi
    popl %edi
    popl %ebp
    popl %ebx
    ret
