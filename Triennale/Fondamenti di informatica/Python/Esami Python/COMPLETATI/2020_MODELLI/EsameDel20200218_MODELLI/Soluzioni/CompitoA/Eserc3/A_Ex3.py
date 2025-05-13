from tester import tester_fun

def A_Ex3(file):
    f = open(file,encoding='UTF-8')
    diz = {}
    numRiga = 1
    for riga in f:
        listaParole = riga.strip().split()
        for parola in listaParole:
            if parola[0] == '*' and parola[-1] == '*' and parola.count('*') == 2:
                parolaPulita = parola[1:-1]
                if parolaPulita not in diz:
                    diz[parolaPulita] = set()
                diz[parolaPulita].add(numRiga)
        numRiga += 1
    return diz

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["file1.txt"],{'testo': {1}, 'parole': {1, 2}, 'immagini': {3}, 'importanti': {3}})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt"],{'testo': {1, 4}, 'parole': {1, 2, 4, 5}, 'immagini': {3, 6}, 'importanti': {3, 6}})
counter_test_positivi += tester_fun(A_Ex3, ["file3.txt"],{'testo': {1, 3}, 'parole': {1, 2, 3, 4}, 'immagini': {5}, 'importanti': {5}})
counter_test_positivi += tester_fun(A_Ex3, ["file4.txt"],{'testo': {1, 4, 7}, 'parole': {1, 2, 4, 5, 7}, 'immagini': {3, 6}, 'importanti': {3, 6}})
counter_test_positivi += tester_fun(A_Ex3, ["file5.txt"],{'testo': {1, 4, 7}, 'parole': {1, 2, 4, 5, 7}, 'immagini': {3, 6}, 'importanti': {3, 6}})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

