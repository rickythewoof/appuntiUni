#include "e2B.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int score, trials;

static int check(off_t a, off_t b) {
    return a==b;
}

static void test(char * f, char c, off_t res) {
    trials++;
    off_t o = searchfile(f, c);
    int ok = check(o, res);
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {

    test("file.txt", 'A', 0);
    test("file.txt", 'E', 4);
    test("file.txt", 'Z', 25);
    test("file.txt", 'm', -1);

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
