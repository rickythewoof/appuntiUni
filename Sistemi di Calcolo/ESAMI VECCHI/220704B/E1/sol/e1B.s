.globl count_matching_vars

count_matching_vars: # int count_matching_vars(char** vars, char* pattern) {
    pushl %ebx
    pushl %esi
    pushl %edi
    subl $8, %esp
    movl $-1, %ebx              # int count = -1;
    movl 24(%esp), %esi
    testl %esi, %esi            # if (vars == NULL) goto E;
    je E
    movl 28(%esp), %edi
    testl %edi, %edi            # if (pattern == NULL) goto E;
    je E
    xorl %ebx, %ebx             # count = 0;
L:
    movl (%esi), %ecx           # char* v = *vars;
    testl %ecx, %ecx            # if(*vars == NULL) goto E;
    je E
    movl %ecx, (%esp)
    call getenv                 # char* value = getenv(v);
    testl %eax, %eax            # if (value == NULL) goto F;
    je F
    movl %eax, (%esp)
    movl %edi, 4(%esp)
    call strstr                 # value = strstr(value, pattern);
    testl %eax, %eax            # if (value == NULL) goto F;
    je F
    incl %ebx                   # count += 1;
F:
    addl $4, %esi               # vars++;
    jmp L                       # goto L;
E:
    movl %ebx, %eax
    addl $8, %esp
    popl %edi
    popl %esi
    popl %ebx
    ret         # return count;
    