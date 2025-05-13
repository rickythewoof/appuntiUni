from tester import tester_fun

def B_Ex2(m,l1,l2):
    sol = []
    for i in l1:
        ins = []
        riga =  i-1
        for j in l2:
            colonna = j-1
            ins.append(m[riga][colonna])
        sol.append(ins)
    return sol
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[2,7,6],[9,5,1],[4,10,11],[3,4,4]],[1,3],[2,3]],[[7,6],[10,11]])
counter_test_positivi += tester_fun(B_Ex2, [[[2,7,6],[9,7,1]],[1],[2]],[[7]])
counter_test_positivi += tester_fun(B_Ex2, [[[2,7,6],[9,9,1]],[2],[1,3]],[[9,1]])
counter_test_positivi += tester_fun(B_Ex2, [[[15,5,6,18],[9,7,1,2],[4,3,8,15]],[1,2],[3,4]],[[6,18],[1,2]])
counter_test_positivi += tester_fun(B_Ex2, [[[15,18,6,5],[9,0,1,2],[4,3,8,25],[28,21,15,32]],[3,4],[1]],[[4],[28]])

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
