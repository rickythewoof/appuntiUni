#include <stdio.h>
#include <stdlib.h>
/*
    MEMORIA STATICA:
    Se dichiarata in un blocco { } alla chiusura di essa la memoria viene liberata

    MEMORIA DINAMICA:
    La memoria sopravvive ai blocchi di codice { }, almeno finchè non viene usato free(p) su un puntatore
    che punta alla zona di memoria allocata da malloc

*/
int main() {
    int* q;
    if (1){
        int *p = (int*)malloc(4);   //associo 4 byte al puntatore p
        q = p;          //Associo il punt. q al puntatore di memoria p
    }
    *q = 10;            //posso utilizzare q e anche la memoria allocata da malloc e poi associata a q, MA NON q DIRETTAMENTE
    free(q);            //fine tempo di vita di q e della memoria allocata da p è finito.

    int a;
    int* r = (int*)malloc(4);
    scanf("%d",r);      //utilizzo la memoria dinamica per inserire valori su *p 
    scanf("%d",&a);     //analogo si può fare con la memoria statica 
    return 0;
}