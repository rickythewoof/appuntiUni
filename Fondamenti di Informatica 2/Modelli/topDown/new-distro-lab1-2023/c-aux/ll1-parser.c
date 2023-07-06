#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#define ERRMSG1 "A posizione %d, trovato %c, ma atteso %c\n"
#define ERRMSGKO "Parsing fallito; processo terminato\n"
#define ERRMSGKO2 "Parsing terminato prima che l'input sia terminato; processo terminato\n"
#define OKFINALMSG "Parsing correttamente terminato; processo terminato\n"
#define ERRMSGOVF "Tentativo di leggere oltre la fine dell'input\n"
#define OKMSG "A posizione %d, trovato ed accettato %c\n"




int ll1_acceptChar(char *input, char c, int position);
// potrebbero essere utili funz associate alle produz
/*
static int ll1_prod1(char * input, int position);
static int ll1_prod2(char * input, int position);
static int ll1_prod3(char * input, int position);
*/
static int ll1_S(char * input, int position);
static int ll1_T(char * input, int position);
void ll1_goParse(char *input);


/*
 * acceptChar verifica se nella posizione corrente (position) della 
 * stringa in input (input)
 * vi sia il carattere atteso (c); se sì, stampa messaggio di conferma
 * e termina restituendo la posizione del prossimo simbolo da
 * analizzare; se no, stampa diagnostica e ritorna la posizione 
 * inizialmente
 * ricevuta in input, ma cambiata di segno per segnalare errore
 */
int ll1_acceptChar(char *input, char c, int position) {
    // TO IMPLEMENT
    return 0; // solo ai fini della compilazione
}

// potrebbero essere utili funzioni associate alle produz.
/*
static int ll1_prod1(char * input, int position) {
    // TO IMPLEMENT
    return 0; // solo ai fini della compilazione
}

static int ll1_prod2(char * input, int position) {
    // TO IMPLEMENT
    return 0; // solo ai fini della compilazione
}

static int ll1_prod3(char * input, int position) {
    // TO IMPLEMENT
    return 0; // solo ai fini della compilazione
}
*/

/*
 * non-terminale S
 * 
 * usare la produzione selezionata da SELECT e dal simbolo corrente
 * input[position]
 */
static int ll1_S(char * input, int position) {
    // TO IMPLEMENT
    return 0; // solo ai fini della compilazione
}

/*
 * non-terminale T
 * 
 * usare la produzione selezionata da SELECT e dal simbolo corrente
 * input[position]
 */
static int ll1_T(char * input, int position) {
    // TO IMPLEMENT
    return 0; // solo ai fini della compilazione
}

/*
 * avvia il parsing chiamando la produz. sull'assioma e quindi prende
 * atto dell'esito del parsing, stampando a schermo info finali
 */
void ll1_goParse(char *input) {
    // TO IMPLEMENT
    return; // solo ai fini della compilazione
}

static char look_ahead(char *input, int where) {
    int len = strlen(input);
    assert((where >= 0) && (where < n));
    return input[where];
}

/* tabella di parsing - tipo dipende da come vogliamo rappresentare 
   le produzioni
   Assumiamo un semplice intero per rappresentare le produzioni
   La tabella è bidimensionale e presenta una riga per ciascun non terminale
   e una colonna per ciascun terminale (incluso '$')
   e può essere dichiarata come una matrice bidimensionale di int inizializzata
   a 0 (valore che denota la produzione assente)
   Poi la tabella va "riempita" con gli interi: es. 5 produzioni, 5 celle con un
   intero (denotando le produzioni con gli interi da 1 a 5)
   più eventualmente la gestione del termine input ('$')
   La matrice bidimensionale può essere dichiarata in maniera statica (al
   momento della scrittura del codice si conosce il numero di simboli)
   utilizzando int parsing_table[<num_nonterminali>][<num_simboli_alfabeto + 1>]
   Il + 1 è per il '$'
*/

/* la tabella di parsing può essere variabile globale rispetto al file in cui è
   dichiarata
   per non renderla esportabile altrove può essere usato static:
   static int parsing_table[<num_nonterminali>][<num_simboli_alfabeto + 1>]
*/
