#include "e2A.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int count_occurrence(const char* text, const char c){
    int cnt = 0;
    while(*text){
        if(*(text++) == c) cnt++;
    }
    return cnt;
}

int wordWithMaxCount(const char* text, const char c, char ** word){
    if(*text == 0) return 0;
    char buf[strlen(text) + 1];
    int maxCount = 0;
    strcpy(buf, text);
    char* token = strtok(buf, " ");
    while(token != NULL){
        int cnt = count_occurrence(token, c);
        if (cnt > maxCount){
            if((*word) != NULL) free(*word);
            *word = malloc(strlen(token)+1);
            strcpy(*word, token);
            maxCount = cnt;
        }
        token = strtok(NULL, " ");
    }


    return maxCount;
}
