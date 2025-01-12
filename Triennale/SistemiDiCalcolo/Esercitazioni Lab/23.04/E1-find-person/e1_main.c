#include "e1.h"

#include <stdio.h>
#include <string.h>

int is_sorted_by_name(person_t p[], int nel) {
    int i;
    for (i=1; i<nel; ++i)
        if (strcmp(p[i-1].name, p[i].name) > 0) return 0;
    return 1;
}

int main() {
    person_t p[] = { 
        {"marco", 22}, 
        {"paola", 20}, 
        {"mario", 21}, 
        {"serena", 19}, 
        {"anna", 18}
    };

    sort_people(p, 5);
    
    int score = 0;

    int res1 = is_sorted_by_name(p, 5);
    printf("Test 1: %d [corretto: 1]\n", res1);
    score += res1 == 1;

    person_t *res2 = find_person("serena", p, 5);
    printf("Test 2: %s [corretto: serena]\n", res2->name);
    score += !strcmp(res2->name, "serena");

    res2 = find_person("luciano", p, 5);
    printf("Test 3: %s [corretto: (null)]\n", res2 == NULL ? "(null)" : ((char*)res2));
    score += res2 == NULL;

    res2 = find_person("marco", p, 5);
    printf("Test 4: %s [corretto: marco]\n", res2->name);
    score += !strcmp(res2->name, "marco");

    printf("Risultato: %d/4\n", score);
}
