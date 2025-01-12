.globl count_digits

count_digits:
    pushl %ebx
    movl $0, %eax
    movl $0, %ecx
    movl 8(%esp), %edx
loop:
    movb (%edx, %ecx, 1), %bl
    testb %bl, %bl
    je ret
    cmpb $48, %bl
    jl e
    cmpb $57, %bl
    jg e
    incl %eax
    e:
        inc %ecx
    
    jmp loop
ret:
    popl %ebx
    ret