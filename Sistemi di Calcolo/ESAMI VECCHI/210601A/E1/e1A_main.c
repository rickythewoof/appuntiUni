#include "e1A.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int score, trials;

void test(char* s, int ok) {
    trials++;
    int res = count_tokens(s, " ");
    printf("Test %d: %d [corretto=%d]\n", trials, res, ok);
    score += ok == res;
}

int main() {

	char s1[] = "uno due tre";
	char s2[] = "prova";
	char s3[] = " uno  due tre quattro  ";
	char s4[] = "";

    test(s1, 3);
    test(s2, 1);
    test(s3, 4);
    test(s4, 0);

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
