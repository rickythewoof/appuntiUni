#include <stdio.h>
#include "e1A.h"

void print_array(const char** a, int n, int is_int) {
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

int compare_int_array(const int* a, const int* b, int n) {
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

int test(const char** a, const int n, const int* expected, int n2) {
    int* res = strings_are_upper(a, n);

    printf("array=");
    print_array(a, n2, 0);
    printf(" n=%d: atteso=", n);
    print_array((const char**)expected, n2, 1);
    printf(" ottenuto=");
    print_array((const char**)res, n2, 1);
    
    int score = compare_int_array(expected, res, n2);

    printf(" => %s\n", score ? "Corretto!" : "Errore!");

    return score;
}

int main() {
    int score = 0;
    
    score += test(NULL, 1, NULL, 0);
    
    const char* t1[] = {"a"};
    score += test(t1, 0, NULL, 1);
    
    const char* t2[] = {"a"};
    const int e2[] = { 0 };
    score += test(t2, 1, e2, 1);

    const char* t3[] = {"A"};
    const int e3[] = { 1 };
    score += test(t3, 1, e3, 1);

    const char* t4[] = {"a", "B"};
    const int e4[] = { 0, 1 };
    score += test(t4, 2, e4, 2);

    const char* t5[] = {"A", "b", "C"};
    const int e5[] = { 1, 0, 1 };
    score += test(t5, 3, e5, 3);
    
    printf("Punteggio: %d/%d\n", score, 6);
    return 0;
}