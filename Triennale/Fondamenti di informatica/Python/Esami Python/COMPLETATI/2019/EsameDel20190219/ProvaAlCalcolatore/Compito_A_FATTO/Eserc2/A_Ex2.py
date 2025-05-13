from tester import tester_fun

def A_Ex2(m):
    sol = []
    for colonna in range(len(m[0])):
        sum = 0
        sumColonne = []
        for riga in range (len(m)):
            if m[riga][colonna] not in sumColonne:
                sumColonne.append(m[riga][colonna])
                sum += m[riga][colonna]
            else:
                return []
        if sum not in sol:
            sol.append(sum)
        else:
            return []
    return sol      

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
