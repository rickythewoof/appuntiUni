.globl check_quiz
check_quiz: # int* check_quiz(char** answers, char* solution, int n) {
    pushl %ebp
    pushl %ebx
    pushl %edi
    pushl %esi
    subl $4, %esp
    xorl %eax, %eax         # int* eax = NULL;
    cmpl $0, 24(%esp)       # if (answers == NULL) 
    je E                    # goto E;
    cmpl $0, 28(%esp)       # if (solution == NULL)
    je E                    # goto E;
    cmpl $0, 32(%esp)       # if (n <= 0)
    jle E                   # goto E;
    movl 32(%esp), %ecx     # int edx = sizeof(int) * n;
    imull $4, %ecx
    movl %ecx, (%esp)
    call malloc             # eax = malloc(edx);
    xorl %esi, %esi         # int esi = 0;
    movl 24(%esp), %ebp     # char** ebp = answers;
    movl 28(%esp), %ebx     # char* ebx = solution;
L1:
    cmpl 32(%esp), %esi     # if (esi >= n) goto E;
    jge E
    movl $0, (%eax, %esi, 4) # eax[esi] = 0;
    xorl %edx, %edx          # edx = 0;
L2:
    cmpl $4, %edx           # if (edx >= 4) goto F;
    jge F
    movl (%ebp, %esi, 4), %edi  # char* edi = ebp[esi];
    movb (%ebx, %edx, 1), %cl   # char cl = ebx[edx];
    cmpb %cl, (%edi, %edx, 1)   # if (edi[edx] != cl) goto F2;
    jne F2
    incl (%eax, %esi, 4)        # eax[esi] += 1;
F2:
    incl %edx                   # edx++;
    jmp L2                      # goto L2;
F:
    incl %esi                   # esi += 1;
    jmp L1                      # goto L1;
E:
    addl $4, %esp
    popl %esi
    popl %edi
    popl %ebx
    popl %ebp
    ret         # return eax;
