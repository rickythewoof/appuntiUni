#include "e1.h"
#include <stdlib.h>
#include <string.h>

int compar(const void *x, const void* y){
    person_t p1 = *(person_t*) x;
    person_t p2 = *(person_t*) y;
    return strcmp(p1.name, p2.name);
}

void sort_people(person_t p[], size_t n){
    qsort(p, n, sizeof(person_t), compar );
}

person_t *find_person(char *key, person_t sorted[], size_t n){
    while (n>0){
        if(strcmp(sorted->name, key) == 0) return sorted;
        sorted++;
        n--;
    }
    return NULL;
}