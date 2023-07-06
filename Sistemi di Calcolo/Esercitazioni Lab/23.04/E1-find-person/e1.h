#ifndef __SORT_PEOPLE__
#define __SORT_PEOPLE__

#include <stdlib.h>
#include <string.h>

typedef struct person_t person_t;

struct person_t {
	char *name;
	int age;
};

void sort_people(person_t p[], size_t nel);

person_t *find_person(char *key, person_t sorted[], size_t nel);

#endif
