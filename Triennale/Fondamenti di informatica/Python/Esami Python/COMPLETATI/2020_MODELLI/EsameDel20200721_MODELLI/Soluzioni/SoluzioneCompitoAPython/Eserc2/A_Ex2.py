from tester import tester_fun

def A_Ex2(m1,m2):
    n=len(m1)
    m = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j]=max(m1[j][i],m2[j][i])
    return m
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[1, 2, 3], [7, 1, 3],[1, 0, 2]],[[5, 4, 6],[0, 3, 9],[1, 2, 5]]],[[5, 7, 1], [4, 3, 2],[6, 9, 5]])
counter_test_positivi += tester_fun(A_Ex2, [[[4, 5], [8, 7]],[[0, 0],[0, 0]]],[[4, 8], [5, 7]])
counter_test_positivi += tester_fun(A_Ex2, [[[2]],[[3]]],[[3]])
counter_test_positivi += tester_fun(A_Ex2, [[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [1, 2, 3, 4]],[[0, 0, 0, 0],[5, 6, 7, 8],[1, 2, 1, 2], [1, 2, 3, 4]]] ,[[1, 5, 9, 1], [2, 6, 10, 2], [3, 7, 11, 3], [4, 8, 12, 4]])
counter_test_positivi += tester_fun(A_Ex2, [[[1, 1], [2, 2]],[[1, 1],[2, 2]]],[[1, 2], [1, 2]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


