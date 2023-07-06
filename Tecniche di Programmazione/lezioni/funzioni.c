#include <stdio.h>
/*
    FUNZIONI:
    Modi di ripetere un pezzo di codice in continuazione, senza riscriverlo. Ogni funzione dichiarata ritorna un tipo diverso
    Devono essere scritte PRIMA della loro chiamata, o almeno DICHIARATE
*/

float f3(int a, int b);                 //dichiarazione di una funzione, che verrà scritta dopo

void f1() {                  //tipo void che NON ritorna valori
    printf("Help\n");
    return;                     //return vuoto
    printf("Non eseguita!\n");   //Non viene eseguita, il return è già uscito dalla funzione
}
char f2(){                  //funzione di tipo char!
    return 'c';             //viene restituito un carattere del tipo corrispondente
}
int main() {                    //la main è stata dichiarata di tipo int
    f1();
    printf("%f\n",f3(2,3));       //chiamo una funzione con VARIABILI
    return 0;                   //ritorna un intero
}

float f3(int a, int b) {        //definita dopo la sua chiamata, grazie alla dichiarazione
    return a+b;
}