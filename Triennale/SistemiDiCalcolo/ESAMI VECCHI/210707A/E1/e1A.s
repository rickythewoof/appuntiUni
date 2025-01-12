.globl suffix

suffix:
    pushl %ebx
    pushl %ebp
    pushl %esi
    pushl %edi
    subl $4, %esp

    movl 24(%esp), %ebx
    movl 28(%esp), %ebp

    movl %ebx, (%esp)
    call strlen
    movl %eax, %esi

    movl %ebp, (%esp)
    call strlen
    movl %eax, %edi
    
    movl $0, %eax
    cmpl %esi, %edi
    jae return

    movl %esi, %ecx
    subl %edi, %ecx
L:
    cmpl %esi, %ecx
    jge NL
    movb (%ebx, %ecx, 1), %dl
    cmpb %dl, (%ebp)
    jne return
    incl %ebp
    incl %ecx
    jmp L
NL:
    movl $1, %eax

return:
    addl $4, %esp
    popl %edi
    popl %esi
    popl %ebp
    popl %ebx
    ret
