#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void multi_get_env(const char** names, char*** values, int num) {
    *values = (char**) malloc(num*sizeof(char*));
    for (int i = 0; i<num; i++){
        printf("ENVNAME %d = %s\n", i, getenv(names[i]));
        char* envname = getenv(names[i]);
        if(envname != NULL){
            (*values)[i] = malloc(strlen(envname)+1);
            strcpy((*values)[i], envname);
        }
        else (*values)[i] = NULL;
    }
}
