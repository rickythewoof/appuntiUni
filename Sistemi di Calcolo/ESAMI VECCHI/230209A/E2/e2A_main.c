#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score, trials;

char * readFileContent(const char * file){
    FILE * fp = fopen(file, "r");
    fseek(fp, 0L, SEEK_END);
    int size = ftell(fp);
    fseek(fp, 0L, SEEK_SET);
    char * buffer = malloc(size * sizeof(char) + 1);
    int read_size = fread(buffer, sizeof(char), size, fp);
    buffer[size] = '\0';
    fclose(fp);
    if (size != read_size){
        free(buffer);
        return NULL;
       }
    return buffer;
}

static void test(const char * input, const char * output, const char * sol) {
    trials++;
    char * out;
    reverseTextFile(input, output);
    out = readFileContent(output);
    int ok = strcmp(sol, out)==0;
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {
    char * text1 = "5\n4\n3\n2\n1\n";
    char * text2 = "and for you more sorrow\nWell I got gifts for them,\nDo the kids remember me?\nAnd I got trouble with the bills\nHey brother, I feel I'm living in parentheses\n";
    char * text3 = "Of where we would be when the future comes\n\nThe person you see when you're young\nStrange how you never become\n";
    
    test("input1.txt", "output1.txt", text1);
    test("input2.txt", "output2.txt", text2);
    test("input3.txt", "output3.txt", text3);

    printf("Report: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}

