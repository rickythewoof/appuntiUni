#include "../e2A.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getLargeTables(struct booking ** list, const char * filename, int num){
	FILE* fp;
	* list = NULL;
	struct booking * last = NULL;
	struct booking * elem;

	//Apro il file
	fp = fopen(filename, "r");
	if (fp==NULL) {
		perror("Error accessing the file: ");
		return;
	}

	//Leggo fio a quando riesco a trovare ulteriori prenotazioni
	while(1) {

		//Leggo la prossima prenotazione dal file
		char buf[38];
		int ret = fread(&buf, 37, 1, fp);
		//Se fread legge meno di 37bytes il file è terminato
		if (ret==0) break;

		//Estraggo dalla prenotazione il numero di posti prenotati
		char seats_tmp [3];
		seats_tmp[0] = buf[30];
		seats_tmp[1] = buf[31];
		seats_tmp[2] = '\0';

		//Se il numero di posti prenotati è maggiore o uguale a num
		if (atoi(seats_tmp)>= num) {
			//Alloco memoria per un nuovo elemento della lista
			elem = malloc(sizeof(struct booking));

			//Aggiungo all'elemento il numero di posti prenotati
			elem->places = atoi(seats_tmp);

			//Estraggo ed aggiungo all'elemento il cognome di chi ha prenotato
			int i=0;
			char surname_tmp [31];
			while (i<30 && buf[i]!='_') {
				surname_tmp[i] = buf[i];
				i++;
			}
			surname_tmp[i]='\0';
			elem->surname = malloc(strlen(surname_tmp) * sizeof(char));
			strcpy(elem->surname, surname_tmp);

			//Estraggo ed aggiungo all'elemento l'ora di prenotazione
			i=32;
			char time_tmp [6];
			while (i<37) {
				time_tmp[i-32] = buf[i];
				i++;
			}
			time_tmp[i-32]='\0';
			elem->time = malloc(strlen(time_tmp) * sizeof(char));
			strcpy(elem->time, time_tmp);

			//Aggiungo l'elemento in coda alla lista
			elem->next=NULL;
			if (*list == NULL)
				*list = elem;
			else
				last->next = elem;
			last = elem;
		}
	}
	//Chiudo il file
	fclose(fp);
	return;
}



