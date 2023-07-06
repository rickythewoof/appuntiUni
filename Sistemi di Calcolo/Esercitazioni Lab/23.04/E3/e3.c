int count_digits(const char *s) {
    int cnt = 0;
    while (*s) {
        if (*s >= '0' && *s <= '9') cnt++;
        s++;
    }
    return cnt;
}