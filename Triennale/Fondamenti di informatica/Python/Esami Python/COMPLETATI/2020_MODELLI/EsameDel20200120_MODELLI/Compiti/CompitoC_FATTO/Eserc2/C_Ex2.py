from tester import tester_fun

def C_Ex2(m):
    sum = 0
    for i in range(len(m)):
        sumRighe = 0
        sumColonne = 0
        if i == 0:
            sumDiag1 = 0
        for j in range(len(m)):
            sumRighe += m[i][j]
            sumColonne += m[j][i]
            if i == 0:
                sumDiag1 += m[j][j]
        print(sumRighe, sumColonne, sumDiag1)
        if sumRighe == sumColonne == sumDiag1 and i == 0:
            sum = sumDiag1
        elif sum == sumRighe == sumColonne and i != 0:
            continue
        else:
            return (False, sumDiag1)
    return (True, sum)        
        

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""
"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex2, [[[2,7,6],[9,5,1],[4,3,8]]], (True,15))
counter_test_positivi += tester_fun(C_Ex2, [[[1,0,0],[1,5,0],[0,0,-1]]], (False, 5))
counter_test_positivi += tester_fun(C_Ex2, [[[7,12,1,14],[2,13,8,11],[16,3,10,5],[9,6,1,4]]], (False,34))
counter_test_positivi += tester_fun(C_Ex2, [[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]], (True,34))
counter_test_positivi += tester_fun(C_Ex2, [[[1,14,14,4],[11,7,6,9],[8,10,10,5],[13,2,3,15]]], (True,33))

print('La funzione',C_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)