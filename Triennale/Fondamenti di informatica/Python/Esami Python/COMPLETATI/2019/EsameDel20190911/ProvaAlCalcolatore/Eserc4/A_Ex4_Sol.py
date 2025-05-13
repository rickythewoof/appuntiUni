from tester import tester_fun

def A_Ex4(file):
    f = open(file,encoding = 'UTF-8')
    d = {}
    for riga in f:
        dati = riga.strip().split(',')
        codice = int(dati[0])
        scommessa = dati[1]
        cifra = int(dati[2])
        quota = int(dati[3])
        if codice not in d:
            d[codice] = [0,0,0,0]
        d[codice][0] += cifra
        if scommessa == '1':
            d[codice][1] += cifra*quota
        elif scommessa == 'X':
            d[codice][2] += cifra*quota
        else:
            d[codice][3] += cifra*quota
    return d
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{12: [27, 20, 10, 36]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{12: [27, 20, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{12: [37, 50, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{12: [49, 50, 34, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{12: [69, 110, 34, 36], 10: [37, 20, 24, 45]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
