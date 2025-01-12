#include "e2B.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score, trials;

static char * getOutput(struct booking * list) {
    char * out = "";
    while(list!=NULL) {
        int size = strlen(out) + strlen(list->surname);
        char * tmp = malloc((size + 1) * sizeof(char));
        strcat(tmp,out);
        strcat(tmp,list->surname);
        out = tmp;
        list=list->next;
    }
    return out;
}

static void test(const char* filename, const char * time, const char * correct) {
    trials++;
    struct booking * list;
    getBookingsAfterTime(&list, filename, time);
    int ok = strcmp(correct, getOutput(list)) == 0;
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {
    test("booked.txt", "12:00", "RossiMarroneVerdiBianchiViolaAzzurra");
    test("booked.txt", "20:00", "MarroneVerdiBianchiViolaAzzurra");
    test("booked.txt", "20:30", "VerdiBianchiViolaAzzurra");
    test("booked.txt", "21:00", "BianchiViolaAzzurra");
    test("booked.txt", "21:01", "Azzurra");
    test("booked.txt", "22:00", "");

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
