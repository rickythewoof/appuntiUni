.globl crc32b

# void get_constant(int* value, int index);

crc32b: # int crc32b(char *bytes, int n) {
    pushl %esi
    pushl %edi
    pushl %ebx
    pushl %ebp
    subl $12, %esp
    xorl %ebx, %ebx     # int magic = 0; 
    notl %ebx           # magic = ~magic;
    movl %ebx, %ebp     # int crc = magic;
    movl 32(%esp), %esi
    movl 36(%esp), %edi
L1: 
    cmpl $0, %edi       # if (n <= 0) goto E1;
    jle E1
                        # int value;
    movsbl (%esi), %edx # int byte = *bytes++; // attenzione!
    incl %esi
    xorl %ebp, %edx     # int index = crc ^ byte;
    andl $0xFF, %edx    # index = index & 0xFF;
    movl %edx, 4(%esp)
    leal 8(%esp), %edx
    movl %edx, (%esp)
    call get_constant   # get_constant(&value, index);
    sarl $8, %ebp       # crc = crc >> 8;
    xorl 8(%esp), %ebp  # crc = value ^ crc;
    decl %edi           # n--;
    jmp L1              # goto L1;
E1:
    xorl %ebx, %ebp     # crc = crc ^ magic;
    movl %ebp, %eax
    addl $12, %esp
    popl %ebp
    popl %ebx
    popl %edi
    popl %esi
    ret                 # return crc;
