from tester import tester_fun

def A_Ex2(m):
    righe=len(m)
    colonne=len(m[0])
    lista=[]
    somma_colonne = [0]*colonne
    for i in range(righe):
        for j in range(colonne):
            lista.append(m[i][j])
            somma_colonne[j] += m[i][j]
    lista.sort()
    for i in range(len(lista)-1):
        if lista[i]==lista[i+1]:
            return []
    return somma_colonne


###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,5,1],[4,10,11]]],[15, 22, 18])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6],[9,7,1]]],[])
counter_test_positivi += tester_fun(A_Ex2, [[[2,7,6]]],[2, 7, 6] )
counter_test_positivi += tester_fun(A_Ex2, [[[15,5,6,18],[9,7,1,2],[4,3,8,15]]],[] )
counter_test_positivi += tester_fun(A_Ex2, [[[15,18,6,5],[9,0,1,2],[4,3,8,25]]],[28,21,15,32])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
