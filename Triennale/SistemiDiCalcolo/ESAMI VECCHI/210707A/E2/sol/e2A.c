#include "e2A.h"
#include<string.h>
#include<stdlib.h>
#include<stdio.h>

int wordWithMaxCount(const char* text, const char c, char ** word){
	if (strlen(text)==0) return 0;
	char * string = (char *) malloc(strlen(text)+1);
	strcpy(string,text);
	
	int count=0;
	int max_count=0;
	char * max_word = NULL;

	char * token = strtok(string, " ");    
	while (token != NULL) {
		count=0;
		for (int i=0; i<strlen(token); i++)
			if (token[i]==c) count++;
		if (count>0 && count>max_count) {
			if (max_word!=NULL) free(max_word); 
			max_word = (char *) malloc(strlen(token)+1);
			strcpy(max_word, token);
			max_count=count;
		}
		token = strtok(NULL, " ");
	}
	free(string);
	if (max_count > 0) *word = max_word;
	return max_count;
}