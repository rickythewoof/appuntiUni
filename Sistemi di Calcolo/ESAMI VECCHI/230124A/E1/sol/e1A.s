.globl strings_are_upper 
strings_are_upper:  # int* strings_are_upper(const char** array, int n) {
    pushl %ebp
    pushl %esi
    pushl %edi
    pushl %ebx
    subl $4, %esp

    xorl %eax, %eax
    cmpl $0, 24(%esp)    # if (array == NULL) return NULL;
    je EF
    cmpl $0, 28(%esp)    # if (n <= 0) return NULL;
    jle EF

    movl 24(%esp), %ebx     # const char** ebx = array;
    movl $4, %eax           # int eax = sizeof(int);
    imull 28(%esp), %eax    # eax = n * eax;
    movl %eax, (%esp)
    call malloc             # int* esi = malloc(eax);
    movl %eax, %esi
    xorl %ebp, %ebp         # int ebp = 0;
L:
    cmpl 28(%esp), %ebp     # if (ebp >= n) goto E;
    jge E
    movl (%ebx, %ebp, 4), %edi  # const char* edi = ebx[ebp];
    movl $1, (%esi, %ebp, 4)    # esi[ebp] = 1;
L2:
    cmpb $0, (%edi)             # if (*edi == 0) goto E2;
    je E2
    movsbl (%edi), %eax
    movl %eax, (%esp)
    call isupper                # if (isupper(*edi) != 0) goto C;
    testl %eax, %eax
    jne C
    movl $0, (%esi, %ebp, 4)    # esi[ebp] = 0;
    jmp E2                      # goto E2;
C:
    incl %edi           # edi += 1;
    jmp L2              # goto L2;
E2:
    incl %ebp           # ebp += 1;
    jmp L               # goto L;
E:
    movl %esi, %eax     # int* eax2 = esi;
EF:
    addl $4, %esp
    popl %ebx
    popl %edi
    popl %esi
    popl %ebp
    ret     # return eax2;
