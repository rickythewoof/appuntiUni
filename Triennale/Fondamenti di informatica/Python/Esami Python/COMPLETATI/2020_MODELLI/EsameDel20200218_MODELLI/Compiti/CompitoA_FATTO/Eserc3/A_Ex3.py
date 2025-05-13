from tester import tester_fun

def A_Ex3(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    ln = 1
    for linea in f:
        parole = linea.strip().split()
        for word in parole:
            if word[0] == "*" and word[-1] == "*" and word.count("*") == 2:
                for char in word:
                    if not char.isalpha:
                        break
                wordClean = word[1:-1]
                print(word, ln, wordClean)
                d[wordClean] = d.get(wordClean, set())
                d[wordClean].add(ln)
                print(d)
        ln += 1
    return d


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

