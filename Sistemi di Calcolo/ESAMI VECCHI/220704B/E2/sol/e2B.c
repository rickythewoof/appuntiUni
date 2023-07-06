#include "../e2B.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int timecmp(const char * A, const char * B){
	char Ah[3] = {A[0], A[1], '\0'};
	char Bh[3] = {B[0], B[1], '\0'};
	char Am[3] = {A[3], A[4], '\0'};
	char Bm[3] = {B[3], B[4], '\0'};
	return ((atoi(Ah) - atoi(Bh)) * 60 + (atoi(Am) - atoi(Bm)));
}

void getBookingsAfterTime(struct booking ** list, const char * filename, const char * time){
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

		//Estraggo l'ora di prenotazione
		int i=32;
		char time_tmp [6];
		while (i<37) {
			time_tmp[i-32] = buf[i];
			i++;
		}
		time_tmp[i-32]='\0';


		//Se l'ora di prenotazione è successiva a time
		if (timecmp(time_tmp, time)>= 0) {
			//Alloco memoria per un nuovo elemento della lista
			elem = malloc(sizeof(struct booking));

			//Aggiungo all'elemento l'orario di prenotazione
			elem->time = malloc(strlen(time_tmp) * sizeof(char));
			strcpy(elem->time, time_tmp);

			//Estraggo ed aggiungo all'elemento il numero di posti prenotati
			char seats_tmp [3];
			seats_tmp[0] = buf[30];
			seats_tmp[1] = buf[31];
			seats_tmp[2] = '\0';
			elem->places = atoi(seats_tmp);

			//Estraggo ed aggiungo all'elemento il cognome di chi ha prenotato
			i=0;
			char surname_tmp [31];
			while (i<30 && buf[i]!='_') {
				surname_tmp[i] = buf[i];
				i++;
			}
			surname_tmp[i]='\0';
			elem->surname = malloc(strlen(surname_tmp) * sizeof(char));
			strcpy(elem->surname, surname_tmp);

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