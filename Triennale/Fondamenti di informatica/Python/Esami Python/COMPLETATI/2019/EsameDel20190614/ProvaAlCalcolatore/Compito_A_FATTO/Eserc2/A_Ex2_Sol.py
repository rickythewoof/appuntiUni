from tester import tester_fun

def A_Ex2(m,l1,l2):
    for i in range(len(l1)):
        l1[i]=l1[i]-1
    print(l1)
    for i in range(len(l2)):
        l2[i]=l2[i]-1
    print(l2)
    ris=[]
    for k in range(len(m)):
        if k not in l1:
            riga=[]
            for l in range(len(m[0])):
                if l not in l2:
                    riga.append(m[k][l])
            ris.append(riga)
    return ris 


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,5,1],[4,10,11],[3,4,4]],[1,3],[2]],[[9,1],[3,4]])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,7,1]],[1],[2]],[[9,1]])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,9,1]],[2],[1,3]],[[7]])
counter_test_positivi += tester_fun(A_Ex2, [[[15,5,6,18],[9,7,1,2],[4,3,8,15]],[],[]],[[15,5,6,18],[9,7,1,2],[4,3,8,15]])
counter_test_positivi += tester_fun(A_Ex2, [[[15,18,6,5],[9,0,1,2],[4,3,8,25],[28,21,15,32]],[],[2,4]],[[15,6],[9,1],[4,8],[28,15]])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
