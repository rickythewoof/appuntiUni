#include <stdio.h>

int count_digits(const char *s);

int score = 0, trials = 0;

void doTest(const char* s, int ok) {
    trials++;
    int cnt = count_digits(s);
    printf("Test %d: \"%s\" -> %d [corretto: %d]\n", trials, s, cnt, ok);
    if (cnt == ok) score++;
}

int main() {

    doTest("h3ll0", 2);
    doTest("hello world", 0);
    doTest("", 0);
    doTest("1_2_3_0", 4);
    
    printf("Risultato: %d/%d\n", score, trials);
    
    return 0;
}