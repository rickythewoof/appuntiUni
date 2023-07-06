#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score, trials;

static char * getOutput(struct booking * list) {
    char * out = "";
    while(list!=NULL) {
        int size = strlen(out) + strlen(list->surname);
        char * tmp = malloc((size + 1) * sizeof(char));
        strcpy(tmp,out);
        strcat(tmp,list->surname);
        out = tmp;
        list=list->next;
    }
    return out;
}

static void test(const char* filename, int num, const char * correct) {
    trials++;
    struct booking * list;
    getLargeTables(&list, filename, num);
    int ok = strcmp(correct, getOutput(list)) == 0;
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {
    test("booked.txt", 0, "RossiMarroneVerdiBianchiViolaAzzurra");
    test("booked.txt", 3, "RossiMarroneVerdiViolaAzzurra");
    test("booked.txt", 4, "RossiMarroneVerdiViola");
    test("booked.txt", 6, "VerdiViola");
    test("booked.txt", 10, "Verdi");
    test("booked.txt", 99, "");

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
