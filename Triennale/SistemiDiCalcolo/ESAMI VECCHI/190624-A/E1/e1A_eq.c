
#include "e1A.h"

void init_matrix(short** m, unsigned n) {
    unsigned i,j;
    for (i=0; i<n; ++i)
        for (j=0; j<n; ++j){
            short val = value(i, j);
            short* arr = m[i];
            arr[j] = val;
        }
}