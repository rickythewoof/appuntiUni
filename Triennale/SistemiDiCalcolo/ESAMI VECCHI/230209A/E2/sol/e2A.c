#include <stdio.h>
#include <string.h>

void reverseTextFile(const char * input_file, const char * output_file){
	char line[1000];
	int input_size;

	//Per prima cosa apriamo i file
    FILE * in_fp = fopen(input_file, "r");
    FILE * out_fp = fopen(output_file, "w");

	if (in_fp==NULL || out_fp==NULL) return; //Qualcosa è andato storto...

	//Calcoliamo la lunghezza complessiva che avrà il file in output
    fseek(in_fp, 0L, SEEK_END);
    input_size = ftell(in_fp);
    fseek(in_fp, 0L, SEEK_SET);

	//Prepariamo il file di ouput per la lunghezza corretta
	for(int i=0; i<input_size; i++) fputc('0', out_fp);

	//A questo punto il puntatore di scrittura è alla fine del file e possiamo iniziare a scrivere in ordine inverso le stringhe lette
	//Leggiamo una riga alla volta
	while(fgets(line, sizeof(line), in_fp)) {
		//Spostiamo indietro il puntatore del numero di caratteri da scrivere
	    fseek(out_fp, -strlen(line), SEEK_CUR);
		//Scriviamo la linea
		fputs(line, out_fp);
		//Riportiamo il puntatore all'inizio della linea appena scritta
	    fseek(out_fp, -strlen(line), SEEK_CUR);
	}

	//Possiamo ora chiudere i file
	fclose(in_fp);
	fclose(out_fp);
	return;
}