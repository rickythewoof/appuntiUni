.globl is_prefix

is_prefix:
    pushl %ebx
    pushl %ebp
    pushl %esi
    pushl %edi

    movl 20(%esp), %ebx
    movl 24(%esp), %ebp

L:
    movb (%ebx), %cl
    movb (%ebp), %dl
    cmpb $0, %cl
    je NL
    cmpb $0, %dl
    je NL
    cmpb %cl, %dl
    jne NL

    incl %ebx
    incl %ebp

    jmp L
NL:
    movb (%ebx), %cl
    cmpb $0, %cl
    sete %al
    movzbl %al, %eax
    popl %edi
    popl %esi
    popl %ebp
    popl %ebx
    ret

