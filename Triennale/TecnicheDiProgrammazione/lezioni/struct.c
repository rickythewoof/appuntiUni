#include <stdio.h>
/* 
    Gli STRUCT:
    si organizza una zona di memoria contigua con elementi NON omogenei, a differenza degli array.
    Esiste il costrutto, che a volte si chiama record, classe, o struct

    In C è definita da insiemi di variabili, chiamati anche campi, ognuna con il suo tipo.
    LA NOMENCLATURA È:
    typedef struct {
        variabile_1
        ...
        variabile_n
    } lista_variabile;
    
    PER ESEMPIO:
    struct {
        char * nome ;
        char * cognome ;
        short int giorno ;
        short int mese ;
        short int anno ;
    } persona_1 , persona_2 ;
    ora persona_1 e persona_2 avranno allocate a se 14byte di memoria
*/

int main(){
    typedef struct {        //variabile di tipo record
        char * nome ;
        char * cognome ;
        short int giorno ;
        short int mese ;
        short int anno ;
    } persona;       //ora il tipo persona esiste! SI possono dichiarare variabili con quel nome
    persona p;
    printf("%d",sizeof(p));
    p.nome = "mario";      //serve per accedere al campo Nome del record di persona
    p.cognome = "rossi";
    persona p1 = {" Siu "," M " ,7 ,4 ,1964}; //altro modo di dichiarare un tipo

    //PUNTATORI A RECORD
    persona* p2;    //viene allocata memoria per il puntatore, non per la struttura
    p2 = (persona*) malloc(sizeof(persona)); //la memoria adesso è allocata dinamicamente e p2 è allocato nello heap
    (*p2).nome;      //per accedere al campo puntato da p2 nome
    p2 -> nome;      //si usa anceh questo
    free(p);
    //e conveniente racchiudere le informazioni di matrice in una struttura nuova!
    typedef struct {
        int rows;
        int cols;
        float **matrix;
    } mat;
    mat a,b,c;
    //mat *f(mat a, mat b);   //funzione di matrice!
    a = b;                  //SIDE EFFECT: matrix è di tipo puntatore, punta alla stessa zona di memoria
    return 0;
}