#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>

int score, trials;

static void test(const char** s, char c, int n, int correct) {
    trials++;
    int res = multicount(s, c, n);
    int ok = res == correct;
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {
    const char* s1[] = {};
    const char* s2[] = {"I'm tired of weakness"};
    const char* s3[] = {"I'm tired of weakness", "tired of my feet of clay", "tired of days to come", "tired of yesterday"};
    test(s1, 'o', 0, -1);
    test(s2, '\0', 1, -1);
    test(s2, 'm', 1, 1);
    test(s2, 'e', 1, 3);
    test(s3, 's', 4, 2);
    test(s3, 'o', 4, 3);
    test(s3, 'x', 4, 0);

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
