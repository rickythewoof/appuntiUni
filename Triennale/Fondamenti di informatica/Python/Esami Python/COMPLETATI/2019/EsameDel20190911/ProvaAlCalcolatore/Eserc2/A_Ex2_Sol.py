from tester import tester_fun

def A_Ex2(M):
    numRighe = len(M)
    numColonne = len(M[0])
    lista = []
    for i in range(numRighe):
        for j in range(numColonne):
            lista.append(M[i][j])
    lista.sort()
    k = 0
    for i in range(numRighe):
        for j in range(numColonne):
            M[i][j]=lista[k]
            k = k+1
    return M

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[3,4,3],[2,1,2]]],[[1,2,2],[3,3,4]])
counter_test_positivi += tester_fun(A_Ex2, [[[3,4,3],[2,1,2],[0,-2,7]]],[[-2,0,1],[2,2,3],[3,4,7]])
counter_test_positivi += tester_fun(A_Ex2, [[[9,8,7],[6,5,4],[3,2,1],[0,-1,-2]]],[[-2,-1,0],[1,2,3],[4,5,6],[7,8,9]])
counter_test_positivi += tester_fun(A_Ex2, [[[5,5,5],[4,4,4]]],[[4,4,4],[5,5,5]])
counter_test_positivi += tester_fun(A_Ex2, [[[2],[1]]],[[1],[2]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
