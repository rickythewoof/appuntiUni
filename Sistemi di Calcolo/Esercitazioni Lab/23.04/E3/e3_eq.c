int count_digits(const char *s) {
    int a = 0;      //counter
    int c = 0;      //char number
    char* d = s;
loop:;
    int b = (int) d[c]; 
    if ( b == 0) goto ret;
    if (b < 48 ) goto e;
    if (b > 57) goto e;
        a++;
    e:
        c++;
    goto loop;
    ret:
        return a;
}
