from tester import tester_fun

def D_Ex2(m):
    ris = 0
    righe = len(m)
    colonne = len(m[0])
    for i in range(righe):
        for j in range(colonne):
            if i != j and m[i][j] == m[j][i] and m[i][j] > 0:
                ris += m[i][j]
            if i != j and m[i][j] != m[j][i]:
                return -1
    return ris
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3],[-1,5,5],[3,5,0]]] , 16)
counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3],[-1,5,5],[3,-5,0]]] , -1)
counter_test_positivi += tester_fun(D_Ex2, [[[0,-1,3,3],[-1,5,5,2],[3,5,0,1],[3,5,0,1]]] , -1)
counter_test_positivi += tester_fun(D_Ex2, [[[1,1],[1,1]]] , 2)
counter_test_positivi += tester_fun(D_Ex2, [[[1]]] , 0)

print('La funzione',D_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
