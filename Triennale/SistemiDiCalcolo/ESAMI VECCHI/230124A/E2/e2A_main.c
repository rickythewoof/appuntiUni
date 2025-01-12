#include "e2A.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int score, trials;

static void test(const char * filename, const char * key, const char * sol) {
    trials++;
    char * out;
    char * decoded_text;
    decodeTextFile(filename, key, &decoded_text);
    int ok = strcmp(sol, decoded_text)==0;
    printf("Test %d: %s\n", trials, ok ? "OK" : "errore");
    score += ok;
}

int main() {
    char * text1 = "I'm tired of weakness - Tired of my feet of clay - I'm tired of days to come - I'm tired of yesterday - And all the worn out things that I ever said - Now it's much too late - The words stay in my head";
    char * text2 = "Gold man bites down on his silver tongue, takes a deep breath and blows the candle out, yeah, he knows the truth, but he keeps it to himself, here it is, you can only save yourself, only yourself, yeah";
    char * text3 = "As the cheerless towns pass my window | I can see a washed out moon through the fog | And then a voice inside my head | Breaks the analogue And says | \"Follow me down to the valley below | You know | Moonlight is bleeding | From out of your soul\"";
    
    test("input1.txt", "key.txt", text1);
    test("input2.txt", "key.txt", text2);
    test("input3.txt", "key.txt", text3);

    printf("Risultato: %d/%d\n", score, trials);

    return EXIT_SUCCESS;
}

