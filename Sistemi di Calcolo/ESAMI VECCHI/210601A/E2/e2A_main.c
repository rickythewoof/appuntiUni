#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score, trials;

static void test(const char* filename, char* expected) {
    trials++;
    unsigned size;
    char* returned = load(filename, &size);
    printf("Test %d: \"", trials);
    fwrite(returned, sizeof(char), size, stdout);
    printf("\" [corretto: \"%s\"]\n", expected);
    int ok = size == strlen(expected) &&
             memcmp(expected, returned, strlen(expected)) == 0;
    free(returned);
    score += ok;
}

int main() {

    test("f1.dat", "hello world");
    test("f2.dat", "");

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
