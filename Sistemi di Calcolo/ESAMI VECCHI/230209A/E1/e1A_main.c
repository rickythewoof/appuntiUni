#include <stdio.h>
#include "e1A.h"

void print_array(char** a, int n, int is_int) {
    if (a == NULL) {
        printf("NULL");
        return;
    }
    printf("{");
    for (int i = 0; i < n; i++) {
        if (is_int)
            printf(" %d%s", ((int*)a)[i], i == n - 1 ? " " : ",");
        else
            printf(" %s%s", a[i], i == n - 1 ? " " : ",");
    }
    printf("}");
}

int compare_int_array(int* a, int* b, int n) {
    if (a == NULL) {
        if (b == NULL) return 1;
        else return 0;
    } else {
        if (b == NULL) return 0;
        for (int i = 0; i < n; i++)
            if (a[i] != b[i]) return 0;
        return 1;
    }
}

static int trials = 0;
int test(char** a, char* s, int n, int* expected, int n2) {
    int* res = check_quiz(a, s, n);

    printf("array=");
    print_array(a, n, 0);
    printf(" solution=%s n=%d: atteso=", s ? s : "NULL", n);
    print_array((char**)expected, n2, 1);
    printf(" ottenuto=");
    print_array((char**)res, n2, 1);
    
    int score = compare_int_array(expected, res, n2);

    free(res);

    printf(" => %s\n", score ? "Corretto!" : "Errore!");

    trials += 1;
    return score;
}

int main() {
    int score = 0;
    
    score += test(NULL, "ABCD", 0, NULL, 0);

    char* a2[] = {"ABCD"};
    score += test(a2, NULL, 1, NULL, 0);

    char* a3[] = {"ABCD"};
    int r3[] = { 4 };
    score += test(a2, "ABCD", 1, r3, 1);

    char* a4[] = {"AAAA", "AABB", "BBAA", "BBBB"};
    int r4[] = { 2, 4, 0, 2 };
    score += test(a4, "AABB", 4, r4, 4);
    
    printf("Report: %d/%d\n", score, trials);
    return 0;
}