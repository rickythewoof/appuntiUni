#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score, trials;

static void test(const char* text, const char c, const int expected_num, const char* expected_word) {
    trials++;
    unsigned size;
    char * word = NULL;
    int ret = wordWithMaxCount(text, c, &word);
    printf("Test %d: \"", trials);
    if (ret>0) 
        printf("%d | %s", ret, word);
    else 
        printf("%d | ", ret);
    printf("\" [corretto: \"%d | %s\"]\n", expected_num, expected_word);
    int ok = ret==expected_num
             &&
             (expected_num==0) ? (word==NULL || strlen(word)==0) : strcmp(word, expected_word)==0;
    if (word!=NULL) free(word);
    score += ok;
}

int main() {
    test("", 'x', 0, "");
    test("Hey brother, happy returns, it's been a while now I bet you thought that I was dead. But I'm still here, nothing has changed. Hey brother, I'd love to tell you I've been busy, but that would be a lie. Cos the truth is the years just past like trains, I wave but they don't slow down.", 't', 2, "thought");
    test("Hey brother, happy returns, it's been a while now I bet you thought that I was dead. But I'm still here, nothing has changed. Hey brother, I'd love to tell you I've been busy, but that would be a lie. Cos the truth is the years just past like trains, I wave but they don't slow down.", 'a', 1, "happy");
    test("Some people raise raccoons for their pelts. A raccoon's home is called a nook. The person who cleans and tidies up the raccoonnooks is called the raccoonnookkeeper. Real word!", 'o', 4, "raccoonnooks");
    test("Some people raise raccoons for their pelts. A raccoon's home is called a nook. The person who cleans and tidies up the raccoonnooks is called the raccoonnookkeeper. Real word!", 'j', 0, "");

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}
