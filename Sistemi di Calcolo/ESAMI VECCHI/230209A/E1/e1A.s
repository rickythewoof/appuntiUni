.globl check_quiz

check_quiz:
    pushl %ebx
    pushl %ebp
    pushl %edi
    pushl %esi
    subl $4, %esp

    xorl %eax, %eax
    cmpl $0, 24(%esp)
    je return
    cmpl $0, 28(%esp)
    je return
    cmpl $0, 32(%esp)
    jle return
    
    movl 32(%esp), %eax
    shll $2, %eax
    movl %eax, (%esp)
    call malloc

    movl %eax, %esi
    xorl %ebx, %ebx
L1:
    cmpl 32(%esp), %ebx
    jge E1
    movl $0, (%esi, %ebx, 4)
    xorl %ebp, %ebp
L2:
    cmpl $4, %ebp
    jge E2
    movl 24(%esp), %ecx
    movl (%ecx, %ebx, 4), %ecx
    movb (%ecx, %ebp, 1), %cl
    movl 28(%esp), %edx
    movb (%edx, %ebp, 1), %dl
    cmpb %cl, %dl
    jne C
    incl (%esi, %ebx, 4)
    C:
    incl %ebp
    jmp L2
E2:
    incl %ebx
    jmp L1
E1:
    movl %esi, %eax
return:
    addl $4, %esp
    popl %esi
    popl %edi
    popl %ebp
    popl %ebx
    ret
