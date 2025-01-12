#include <stdio.h>
#include "e1B.h"

int test(char** data, char* pattern, int expected) {
    int res = count_matching_vars(data, pattern);
    printf("Risultato: %d [atteso: %d] => %s\n", res, expected, res == expected ? "corretto!" : "non corretto!");
    return res == expected;
}

int main() {
    char* v1 = "Sheldon";
    char* r1 = "Bazinga!"; 
    char* v2 = "Barney";
    char* r2 = "Challenge accepted!";
    setenv(v1, r1, 0);
    setenv(v2, r2, 0);
    char* data[] = { v1, "Miss Chanandler Bong", v2, "Red Ross", NULL };
    int score = 0;
    score += test(NULL, "Challenge", -1);
    score += test(data, NULL, -1);
    score += test(data + 3, "Challenge", 0);
    score += test(data, "Challenge", 1);
    score += test(data, "!", 2);
    printf("Punteggio: %d/%d\n", score, 5);
    return score;
}