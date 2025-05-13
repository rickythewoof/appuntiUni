from tester import tester_fun

def B_Ex2(M):
    minimo = 100000
    massimo = 0
    righe = len(M)
    colonne = len(M[0])
    for i in range(1, righe-1):
        for j in range (1, colonne-1):
            localSum = M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] + M[i][j-1] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1] 
            minimo = min(localSum, minimo)
            massimo = max(localSum, massimo)
    return((minimo, massimo))        

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[-3,5,8,4],[0,7,6,3],[0,5,3,8],[1,2,0,1]]],(19,43))
counter_test_positivi += tester_fun(B_Ex2, [[[0,0,0,0],[0,0,0,0],[0,0,0,0]]], (0,0))
counter_test_positivi += tester_fun(B_Ex2, [[[-1,3,12],[6,8,9],[15,-10,8]]], (42,42))
counter_test_positivi += tester_fun(B_Ex2, [[[-1,3,12],[6,8,9],[15,-10,8],[8,6,7]]], (42,67))
counter_test_positivi += tester_fun(B_Ex2, [[[0,7,6],[0,6,3],[3,5,8],[0,0,0],[-3,-4,-15]]], (-6,32))

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
