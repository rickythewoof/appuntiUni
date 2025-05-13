from tester import tester_fun

def A_Ex3(file):
    esclusi = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    d = {}
    f = open(file,encoding = 'UTF-8')
    linea = 1
    for riga in f:
        massimo = 0
        for c in riga:
            if c not in esclusi and riga.count(c) > massimo:
                massimo = riga.count(c)
        for c in riga:
            if c not in esclusi and riga.count(c) == massimo:
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

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],{'c': [1], 'z': [1], 'n': [2, 3]}  )
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],{'c': [1, 5], 'z': [1], 'n': [2, 5], 't': [3, 6], 'l': [4], 's': [4], 'r': [5], 'v': [5], 'd': [5]} )
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'], {'n': [1], 'l': [2], 't': [3]})
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6], 't': [3], 'p': [5], 'z': [6]} )
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6, 8, 9], 't': [3, 7], 'p': [5], 'z': [6]})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
