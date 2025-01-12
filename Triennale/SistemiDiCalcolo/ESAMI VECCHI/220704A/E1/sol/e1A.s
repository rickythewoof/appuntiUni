.globl count_vars

count_vars: # int* count_vars(char** vars, int n) {
    pushl %ebx
    pushl %esi
    pushl %edi
    subl $4, %esp
    xorl %ebx, %ebx             # int i = 0;
    xorl %esi, %esi             # int* out = NULL;
    movl 20(%esp), %edi
    testl %edi, %edi            # if (vars == NULL) 
    jz E                        # goto E;
    cmpl $0, 24(%esp)           # if (n <= 0) 
    jle E                       # goto E;
    movl $4, %eax               # size_t size = sizeof(int);
    imull 24(%esp), %eax        # size = size * n;
    movl %eax, (%esp)
    call malloc                 # int* out = malloc(size);
    movl %eax, %esi
L:
    cmpl 24(%esp), %ebx # if (i >= n) goto E;
    jge E
    movl (%edi, %ebx, 4), %eax
    movl %eax, (%esp)
    call getenv
    testl %eax, %eax            # if (getenv(vars[i]) == NULL) goto F;
    jz F
    movl $1, (%esi, %ebx, 4)    # out[i] = 1;
    jmp A                       # goto A;
F:
    movl $0, (%esi, %ebx, 4)    # out[i] = 0;
A:
    incl %ebx                   # i++;
    jmp L                       # goto L;
E:
    movl %esi, %eax
    addl $4, %esp
    popl %edi
    popl %esi
    popl %ebx
    ret     # return out;
