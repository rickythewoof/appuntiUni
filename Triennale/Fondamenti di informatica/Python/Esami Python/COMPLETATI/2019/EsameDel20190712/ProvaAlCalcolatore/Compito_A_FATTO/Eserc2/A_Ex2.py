from tester import tester_fun

def A_Ex2(M,s):
    righe = len(M)
    colonne = len(M[0])
    for i in M:
        stringa=""
        for j in i:
            stringa += j
        if s in stringa:
            return True
    for i in range(colonne):
        stringa = ""
        for j in range(righe):
            stringa += M[j][i]
        if s in stringa:
            return True
    return False


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'amo'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'aria'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'aia'],True)
counter_test_positivi += tester_fun(A_Ex2, [[['a','m','o'],['r','e','a'],['i','d','i'],['a','x','a']],'amore'],False)
counter_test_positivi += tester_fun(A_Ex2, [[['a']],'c'],False)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
