//funzioni SCL

#include <stdio.h>

/*
    TipoSCL scl = NULL;

    Le strutture collegate che introduciamo in questa unità sono definite
    quindi appositamente per consentire di allocare e deallocare memoria
    in maniera dinamica, a seconda delle esigenze del programma nella
    memorizzazione dei dati di interesse per l’applicazione.

*/
typedef TipoInfoSCL;

struct ElemSCL {
TipoInfoSCL info ;
struct ElemSCL * next ;
};
typedef struct ElemSCL TipoNodoSCL;
typedef TipoNodoSCL *TipoSCL;

int main(){

    return 0;
}
