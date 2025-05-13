from tester import tester_fun

def B_Ex3(file):
    vocali = ['a','e','i','o','u','A','E','I','O','U']
    d = {}
    f = open(file,encoding = 'UTF-8')
    linea = 1
    for riga in f:
        minimo = len(riga)
        for c in riga:
            if c in vocali and riga.count(c) < minimo:
                minimo = riga.count(c)
        for c in riga:
            if c in vocali and riga.count(c) == minimo:
                if c not in d:
                    d[c] = [linea]
                elif linea not in d[c]:
                    d[c].append(linea)
        linea += 1
    return d


###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt'],{'I': [1], 'A': [1], 'e': [1], 'u': [2, 3]})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt'],{'I': [1], 'A': [1], 'e': [1, 5], 'u': [2, 3, 5, 6], 'o': [4, 5]} )
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt'],{'I': [1], 'A': [1], 'u': [1, 2, 3]})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt'],{'I': [1], 'A': [1, 4], 'u': [1, 2, 3, 4, 6], 'o': [5], 'e': [6]} )
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt'],{'I': [1, 7, 8], 'A': [1, 4], 'u': [1, 2, 3, 4, 6, 8, 9], 'o': [5], 'e': [6]})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

