from tester import tester_fun

def A_Ex4(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    for riga in f:
        riga = riga.strip().split(",")
        print(riga)
        codice = int(riga[0])
        scommessa = riga[1]
        cifra = int(riga[2])
        quota = int(riga[3])
        d[codice] = d.get(codice, [0,0,0,0])
        d[codice][0] += cifra
        if scommessa == "1":
            d[codice][1] += cifra*quota
        elif scommessa == "X":
            d[codice][2] += cifra*quota
        elif scommessa == "2":
            d[codice][3] += cifra*quota
    return d

###############################################################################


counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{12: [27, 20, 10, 36]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{12: [27, 20, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{12: [37, 50, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{12: [49, 50, 34, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{12: [69, 110, 34, 36], 10: [37, 20, 24, 45]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
