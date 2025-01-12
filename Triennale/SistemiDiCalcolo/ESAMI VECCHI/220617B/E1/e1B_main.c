#include <stdio.h>
#include "e1B.h"

int test(unsigned char* data, int n, int expected) {
    int res = crc32b(data, n);
    printf("Risultato: %x [atteso: %x] => %s\n", res, expected, res == expected ? "corretto!" : "non corretto!");
    return res == expected;
}

int main() {
    char data[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int score = 0;
    score += test(data, 0, 0);
    score += test(data, 1, 0x2d02ef8d);
    score += test(data + 9, 1, 0x54de5729);
    score += test(data, sizeof(data) / sizeof(char), 0xb9707299);
    printf("Punteggio: %d/%d\n", score, 4);
    return score;
}