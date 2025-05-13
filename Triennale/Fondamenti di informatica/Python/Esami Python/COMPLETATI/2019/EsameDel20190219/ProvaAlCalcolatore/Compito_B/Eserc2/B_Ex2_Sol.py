from tester import tester_fun

def B_Ex2(m):
    righe = len(m)
    colonne = len(m[0])
    sumRighe = []
    sumCol = [0]*colonne
    for i in range(righe):
        sumRighe.append(sum(m[i]))
        for j in range(colonne):
            sumCol[j] += m[i][j]
    conta = 0
    for i in range(righe):
        for j in range(colonne):
            if sumRighe[i] == sumCol[j]:
                conta += 1
    return conta
                       

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,3,3]]] ,2)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,3,3],[10,0,0,5]]] ,4)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,5,4,2],[1,7,3,3]]] ,0)
counter_test_positivi += tester_fun(B_Ex2, [[[1,3,4,5],[2,3,4,2],[1,7,5,3],[8,0,0,5]]] ,4)
counter_test_positivi += tester_fun(B_Ex2, [[[1,1,1],[1,1,1],[1,1,1]]] ,9)

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
