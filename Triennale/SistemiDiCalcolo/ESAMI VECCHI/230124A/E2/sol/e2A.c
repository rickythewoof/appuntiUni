#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>

//La funzione findkey è utilizzata opzionalmente solo per codificare il testo
int findkey(const char * keymap,char c){
	printf("\t looking for \'%c\'...",c);
	for(int i = 0; i<58; i++) {
		printf("\t keymap[%d] is \'%c\'\n", i, keymap[i]);
		if (keymap[i]==c) return i+65;
	}
	return -1;
}

void decodeTextFile(const char * encoded_file, const char * key, char ** decoded_text){
	int c;
	char * keymap = (char *) malloc(sizeof(char) * 58);

	// Apriamo il file con la chiave
	FILE * fd = fopen(key, "r");
    if (fd == NULL) perror("File con la chiave non esistente");
	// Carichiamo la chiave dal file
	int i;
	for (i=0; i<58; i++){
		keymap[i] = getc(fd);
		if (feof(fd)) perror("Chiave non valida");
	}
	// Chiudiamo il file;
	fclose(fd);

	// Apriamo il file con il testo da decodificare
	fd = fopen(encoded_file, "r");
    if (fd == NULL) perror("File da decodificare non esistente");

	// Calcoliamo la dimensione del testo e creiamo buffer
	fseek(fd, 0, SEEK_END);
	int text_size = ftell(fd);
	fseek(fd, 0, SEEK_SET);
	* decoded_text = (char *) malloc((text_size+1) * sizeof(char));

	//Leggiamo il file e decodifichiamo
	i = 0;
	do {
    	c = fgetc(fd);
    	if(feof(fd)) {
			(* decoded_text)[i] = '\0';
        	break ; 
    	}
		if(isalpha(c))
			(* decoded_text)[i] = keymap[c-65];
			//La linea che segue può essere usate alternativamente per eseguire la codifica
			//(* decoded_text)[i] = findkey(keymap,c);
		else
			(* decoded_text)[i] = c;
		i++;
   	} while(1);
	return;
}
