from tester import tester_fun

def A_Ex2(M,s):
    for i in range(len(M)):
        riga=''
        for j in range(len(M[0])):
            riga=riga+M[i][j]
        if riga.find(s) != -1:
            return True
    for j in range(len(M[0])):
        colonna=''
        for i in range(len(M)):
            colonna=colonna+M[i][j]
        if colonna.find(s) != -1:
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
