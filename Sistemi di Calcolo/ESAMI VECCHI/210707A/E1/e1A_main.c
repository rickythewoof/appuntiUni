#include "e1A.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int score, trials;

void test(char* a, char* b, int ok) {
    trials++;
    int res = suffix(a, b);
    printf("Test %d: %d [corretto=%d]\n", trials, res, ok);
    score += ok == res;
}

int main() {

    test("burger", "hamburger", 0);
    test("hamburger", "burger", 1);
    test("burger", "burger", 1);
    test("uniroma1.it", ".it",1);
    test("uniroma1.it", "",1);
    test("uniroma1.it", ".com",0);

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
