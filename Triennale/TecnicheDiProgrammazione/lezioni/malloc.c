#include <stdio.h>
#include <stdlib.h>
/*
    MEMORIA DINAMICA (void malloc(n))
    malloc(n) restituisce un puntatore void* di dimensione n

    DEALLOCAZIONE DI MEMORIA (void free(void* p))
    la zona di memoria associata da malloc può essere rilasciata per l'uso di un altro programma

*/
int main() {
    void *p = malloc(12);                                   //alloco n numeri di byte nella variabile void*
    int *p1 = (int *)p;                                     //primi 4 byte della zona di memoria *p si usa per l'int p1
    *p1 = 256;                                              //assegno al valore puntato da p1 l'intero 256
    int *p2 = p1 + 1;                                       //utilizzo l'aritmetica dei puntatori per trovare il prossimo spazio
    int *p3 = p2 + 1;                                       //il puntatore int* p3 è ad un sizeof(int) da p2 (p2 + 1*sizeof(int))
    *p3 = 0x11223344;                                       //assegno alla memoria puntata da p3 il valore esadecimale 0x11223344 (LSB)
    int *q = (int *)malloc(3*sizeof(int));                  //Si può usare anche così! (allocazione a puntatori diretta, con cast del void * di malloc)
    int *s = (int *)malloc(3*sizeof(int)+2*sizeof(double)); //si possono unire anche più tipi contemporaneamente

    free(p);                        //dealloco la memoria che malloc ha associato con void p (d'ora in poi le variabili p1, p2.. non sono deterministiche)
    printf("%d", *p1);              //il sistema operativo potrebbe avere già allocato la memoria ad altri processi!    
    int a;
    int* t1 = &a;
    int* t2 = (int*)malloc(sizeof(int));
    int* t3 = t2;
    free (t1);                      //ERRORE: non si può rilasciare memoria allocata staticamente!!!
    free (t2); t2 = NULL;           //dealloco t2, buona prassi far puntare t2 a una zona nulla così usarlo darebbe errore
    free (t3);                      //ERRORE: non si può deallocare un puntatore che puntava a puntatore già deallocato!           
    return 0;
}