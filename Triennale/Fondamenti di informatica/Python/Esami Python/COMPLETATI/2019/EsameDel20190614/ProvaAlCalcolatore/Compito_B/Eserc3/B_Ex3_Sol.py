from tester import tester_fun

def B_Ex3(file):
    d = {}
    f = open(file,encoding = 'UTF-8')
    for riga in f:
        for c in riga:
            if 'a' <= c <= 'z':
                if c in d:
                    d[c][0] += 1
                else:
                    d[c] = [1,0]
                break
        for i in range(len(riga)-1,-1,-1):
            if 'a' <= riga[i] <= 'z':
                if riga[i] in d:
                    d[riga[i]][1] += 1
                else:
                    d[riga[i]] = [0,1]
                break
    f.close()
    return d


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt'],{'n': [1, 0], 'a': [0, 2], 'u': [1, 0], 'o': [0, 1], 's': [1, 0]})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt'],{'n': [1, 0], 'a': [1, 4], 'u': [2, 0], 'o': [0, 1], 's': [1, 0], 'e': [0, 1], 'v': [1, 0]})
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt'],{'n': [1, 0], 'o': [0, 1], 's': [1, 0], 'e': [0, 1], 'u': [1, 0], 'a': [0, 1]})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt'],{'n': [1, 0], 'o': [0, 2], 's': [1, 0], 'e': [0, 1], 'u': [2, 0], 'a': [0, 3], 'l': [1, 0], 'p': [1, 0]})
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt'],{'n': [1, 0], 'o': [0, 3], 's': [1, 0], 'e': [0, 1], 'u': [2, 0], 'a': [1, 4], 'l': [2, 0], 'p': [1, 0], 'i': [0, 1], 'c': [1, 0]})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

