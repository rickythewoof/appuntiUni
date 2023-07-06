.globl suffix

suffix:                     # int suffix(const char* a, const char* b)
    pushl %edi
    pushl %esi
    pushl %ebx
    pushl %ebp
    subl $4, %esp
    movl 24(%esp), %ebx     # const char* ebx = a;
    movl 28(%esp), %ebp     # const char* ebp = b;
    movl %ebx, (%esp)
    call strlen             # int esi = strlen(ebx);
    movl %eax, %esi
    movl %ebp, (%esp)
    call strlen             # int edi = strlen(ebp);
    movl %eax, %edi
    xorl %eax, %eax         # int eax = 0;
    cmpl %esi, %edi         # if (edi > esi)
    jg E                    #     goto E;
    movl %esi, %ecx         # int ecx = esi;
    subl %edi, %ecx         # ecx = ecx - edi;
L:  cmpl %esi, %ecx         # if (ecx >= esi)
    jge M                   #     goto M;
    movb (%ebp), %dl
    cmpb (%ebx,%ecx), %dl   # if (ebx[ecx] != *ebp)
    jne E                   #     goto E;
    incl %ebp               # ebp++;
    incl %ecx               # ecx++;
    jmp L                   # goto L;
M:  movl $1, %eax           # eax = 1;
E:  addl $4, %esp
    popl %ebp
    popl %ebx
    popl %esi
    popl %edi
    ret                     # return eax
