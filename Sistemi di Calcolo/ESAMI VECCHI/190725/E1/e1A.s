.globl most_freq_char

most_freq_char:
    pushl %ebx
    pushl %esi
    pushl %edi
    pushl %ebp
    subl $8, %esp

    movl 28(%esp), %ebx
    movl 32(%esp), %esi

    movl $0, %edi
    movl $0, %ebp

    movl %esi, (%esp)
    movl $256, 4(%esp)
    call clear
L:
    movb (%ebx), %cl
    cmpb $0, %cl
    je NL
    movzbl %cl, %ecx
    incl (%esi, %ecx, 4)
    incl %ebx
    jmp L
NL:
for:
    cmpl $256, %edi
    jae nfor

    movl (%esi, %edi, 4), %ecx
    movl (%esi, %ebp, 4), %edx
    cmpl %ecx, %edx
    cmovbl %edi, %ebp

    incl %edi
    jmp for
nfor:
    movl %ebp, %eax
    addl $8, %esp
    popl %ebp
    popl %edi
    popl %esi
    popl %ebx
    ret
