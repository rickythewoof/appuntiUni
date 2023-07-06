#include "e1A.h"

int* check_quiz(char** answers, char* solution, int n) {
    if (answers == NULL) return NULL;
    if (solution == NULL) return NULL;
    if (n <= 0) return NULL;
    int* res = malloc(sizeof(int) * n);
    int i, j;
    for(i = 0; i < n; i++) {
        res[i] = 0;
        for (j = 0; j < 4; j++) {
            char* answer = answers[i]; // attenzione: e' un puntatore! 
            if (answer[j] == solution[j]) // attenzione: confronto di caratteri!
                res[i] += 1;
        }
    }
    return res;
}
