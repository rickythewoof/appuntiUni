#include <stdio.h>
#include "e1A.h"

int compare(int* a, int* b, int n) {
    if (n <= 0) return a == b;
    if (a == NULL) return a == b;
    if (b == NULL) return 0;
    int i;
    for (i = 0; i < n; i++)
        if (a[i] != b[i]) return 0;
    return 1;
}

void print(int* r, int n) {
    if (r == NULL) {
        printf("NULL");
        return;
    }
    printf("[");
    int i;
    for (i = 0; i < n; i++) printf(" %d", r[i]);
    printf(" ]");
}


int test(char** data, int n, int* expected) {
    int* res = count_vars(data, n);
    // printf("RES: %p\n", res);
    printf("Risultato: ");
    print(res, n);
    printf(" (atteso: ");
    print(expected, n);
    int correct = compare(expected, res, n);
    printf(") => %s\n", correct ? "corretto!" : "non corretto!");
    return correct;
}

int main() {

    char* v1 = "Sheldon";
    char* r1 = "Bazinga!"; 
    char* v2 = "Barney";
    char* r2 = "Challenge accepted!";
    setenv(v1, r1, 0);
    setenv(v2, r2, 0);
    char* data[] = { v1, "Miss Chanandler Bong", v2, "Red Ross"};
    int t3[] = { 1 };
    int t4[] = { 0 };
    int t5[] = { 1, 0, 1, 0 };
    int score = 0;
    score += test(NULL, 1, NULL);
    score += test(data, 0, NULL);
    score += test(data, 1, t3);
    score += test(data + 3, 1, t4);
    score += test(data, 4, t5);
    printf("Punteggio: %d/%d\n", score, 5);
    return score;
}