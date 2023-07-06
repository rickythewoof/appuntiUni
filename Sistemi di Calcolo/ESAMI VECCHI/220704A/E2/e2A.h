#ifndef __E2__
#define __E2__

struct booking {
	char * surname;  //stringa
	int places;		 //intero
	char * time;     //stringa
	struct booking * next;
};

void getLargeTables(struct booking ** list, const char * filename, int num);

#endif
