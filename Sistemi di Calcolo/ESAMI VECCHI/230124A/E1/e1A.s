.globl strings_are_upper

strings_are_upper:
    pushl %ebx  #array
    pushl %ebp  #res
    pushl %esi  #s
    pushl %edi  #i
    subl $4, %esp

    xorl %eax, %eax
    cmpl $0, 24(%esp)
    je return
    cmpl $0, 28(%esp)
    jle return

    movl 24(%esp), %ebx
    movl 28(%esp), %esi
    sall $2, %esi 
    movl %esi, (%esp)
    call malloc
    movl %eax, %ebp
    xorl %edi, %edi
L:
    cmpl 28(%esp), %edi
    jge E
    movl (%ebx, %edi, 4), %esi
    movl $1, (%ebp, %edi, 4)
L1:
    cmpb $0, (%esi)
    je E1
    movb (%esi), %cl
    movzbl %cl, %ecx
    movl %ecx, (%esp)
    call isupper
    testl %eax, %eax
    jne nif
    movl $0, (%ebp, %edi, 4)
    jmp E1
nif:
    incl %esi
    jmp L1
E1:
    incl %edi
    jmp L
E:
    movl %ebp, %eax
return:
    addl $4, %esp
    popl %edi
    popl %esi
    popl %ebp
    popl %ebx
    ret

