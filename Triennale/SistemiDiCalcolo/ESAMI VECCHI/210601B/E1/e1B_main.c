#include "e1B.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int score, trials;

void test(char* a, int len, int expected) {
    trials++;
    int res = adler32_simplified(a, len);
    printf("Test %d: %x [corretto=%x] -> %s\n", trials, res, expected, expected == res ? "OK" : "KO" );
    score += expected == res;
}

int main() {

	char a1[] = {};
	char a2[] = {0x00};
	char a3[] = {0xCA, 0xFE};
    char a4[] = {0xDE, 0xAD, 0xC0, 0xDE, 0xDE, 0xAD, 0xC0, 0xDE};

    test(a1, sizeof(a1), 0x1);
    test(a2, sizeof(a2), 0x10001);
    test(a3, sizeof(a3), 0x29401c9);
    test(a4, sizeof(a4), 0x1c660653);

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}