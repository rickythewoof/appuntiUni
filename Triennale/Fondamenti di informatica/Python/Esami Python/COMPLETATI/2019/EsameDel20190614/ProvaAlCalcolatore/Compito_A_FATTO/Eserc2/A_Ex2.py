from tester import tester_fun

def A_Ex2(m,l1,l2):
    ris = []
    for i in range(len(m)):
        l = []
        if i+1 in l1:
            continue
        for j in range(len(m[0])):
            if j+1 in l2:
                continue
            else:
                l.append(m[i][j])
        ris.append(l)
    return ris


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,5,1],[4,10,11],[3,4,4]],[1,3],[2]],[[9,1],[3,4]])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,7,1]],[1],[2]],[[9,1]])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,9,1]],[2],[1,3]],[[7]])
counter_test_positivi += tester_fun(A_Ex2, [[[15,5,6,18],[9,7,1,2],[4,3,8,15]],[],[]],[[15,5,6,18],[9,7,1,2],[4,3,8,15]])
counter_test_positivi += tester_fun(A_Ex2, [[[15,18,6,5],[9,0,1,2],[4,3,8,25],[28,21,15,32]],[],[2,4]],[[15,6],[9,1],[4,8],[28,15]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
