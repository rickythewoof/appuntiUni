from tester import tester_fun

def A_Ex2(m):
    M=[]
    if len(m[0])==0:
        return M
    for j in range(len(m[0])):
        somma=0
        riga=[]
        for i in range(len(m)):
            riga.append(m[i][j])
            somma=somma+m[i][j]
        if somma%2== 0:
            M.append(riga)           
    return M
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[1, 2, 3], [4, 1, 3],[1, 0, 2]]],[[1, 4, 1],[3, 3, 2]])
counter_test_positivi += tester_fun(A_Ex2, [[[4, 5], [8, 7]]],[[4, 8], [5, 7]])
counter_test_positivi += tester_fun(A_Ex2, [[[]]],[])
counter_test_positivi += tester_fun(A_Ex2, [[[2]]] ,[[2]])
counter_test_positivi += tester_fun(A_Ex2, [[[0, 1, 2, 3], [4, 1, 6, 3], [1, 1, 2, 3]]],[[2, 6, 2]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


