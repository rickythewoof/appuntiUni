#include "e2.h"

void getBookingsAfterTime(struct booking ** list, const char * data, int size, const char * time){
    struct booking* book = *list;
    book = (struct booking*) malloc(sizeof(struct booking));
    i = 0; 
    while (i < size){
        
        const char* buf = &data[i];
        i+=37;
        
        int j = 0;
        while(j < 37){
            
        }
    }
}
