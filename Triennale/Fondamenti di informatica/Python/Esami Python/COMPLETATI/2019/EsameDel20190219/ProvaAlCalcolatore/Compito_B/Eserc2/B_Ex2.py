from tester import tester_fun

def B_Ex2(m):
    sol = 0
    righe = len(m)
    colonne = len(m[0])
    sommaRighe = []
    sommaColonne = []
    for i in range(righe):
        somma = 0
        for j in  range(colonne):
            somma += m[i][j]
        sommaRighe.append(somma)
    print(sommaRighe)  
    for j in range(colonne):
        somma = 0
        for i in range(righe):
            somma += m[i][j]  
        sommaColonne.append(somma)
    print(sommaColonne)     
    for num in sommaRighe:
        if num in sommaColonne:
            sol += sommaColonne.count(num) 
    return sol

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
