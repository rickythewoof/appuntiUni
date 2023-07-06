int most_freq_char(const char* s, int* map) {
    int i, max = 0;
    clear(map, 256);
    while (*s != '\0'){
        map[*s]++;
        s++;
    }
        map[*s++]++;
    for (i=0; i<256; ++i)
        if (map[i] > map[max]) max = i;
    return max;
}
