from tester import tester_fun

def A_Ex3(file):
    f = open(file, "r", encoding="UTF-8")
    parole = {}
    ln = 0
    for riga in f:
        riga = riga.strip().split(" ")
        ln += 1
        for parola in riga:
            parole[parola] = parole.get(parola, set())
            parole[parola].add(ln)
    print(parole)
    maxLenWord = []
    for word in parole:
        lenWord = len(word)
        count = len(parole[word])
        if count >= 3:
            maxLenWord.append(word)
    print (maxLenWord)
    maxLen = 0
    if maxLenWord == []:
        return ""
    parolaSol=maxLenWord[0]
    for parola in maxLenWord:
        if len(parola) > maxLen:
            parolaSol = parola
            maxLen = len(parola)
        elif len(parola) == maxLen:
            parolaSol = min(parolaSol, parola)
    return parolaSol
        
        
        
          
                          
###############################################################################


"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],'albero')
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'],'casolare')
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],'')

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
