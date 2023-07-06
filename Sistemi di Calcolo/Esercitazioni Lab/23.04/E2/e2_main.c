#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "e2.h"

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

static void test(const char* data, const char * time, const char * correct, int size) {
    trials++;
    struct booking * list;
    getBookingsAfterTime(&list, data, size, time);
    int ok = strcmp(correct, getOutput(list)) == 0;
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {

    char data[] = "Rossi_________________________0419:50Marrone_______________________0520:00Verdi_________________________1020:30Bianchi_______________________0221:00Viola_________________________0621:00Azzurra_______________________0321:15";

    test(data, "12:00", "RossiMarroneVerdiBianchiViolaAzzurra", sizeof(data));
    test(data, "20:00", "MarroneVerdiBianchiViolaAzzurra", sizeof(data));
    test(data, "20:30", "VerdiBianchiViolaAzzurra", sizeof(data));
    test(data, "21:00", "BianchiViolaAzzurra", sizeof(data));
    test(data, "21:01", "Azzurra", sizeof(data));
    test(data, "22:00", "", sizeof(data));

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}