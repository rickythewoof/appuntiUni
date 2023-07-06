.globl count_tokens

count_tokens: # int count_tokens(char* str, const char* sep) {
    pushl %ebx
    pushl %esi
    pushl %ebp
    subl $8, %esp
    movl 24(%esp), %ecx     # char *ecx = str;
    movl 28(%esp), %esi     # const char *esi = sep;
    xorl %ebx, %ebx         # int ebx = 0;
    movl %ecx, (%esp)       #
    movl %esi, 4(%esp)      #
    call strtok             # char* ebp = strtok(ecx, esi);
    movl %eax, %ebp         #
L:  cmpl $0, %ebp           # if (ebp == NULL)
    je E                    #    goto E;
    incl %ebx               # ebx++;
    movl $0, (%esp)         #
    movl %esi, 4(%esp)      #
    call strtok             # ebp = strtok(NULL, esi);
    movl %eax, %ebp         #
    jmp L                   # goto L;
E:  movl %ebx, %eax         # int eax = ebx;
    addl $8, %esp
    popl %ebp
    popl %esi
    popl %ebx
    ret                     # return eax;
