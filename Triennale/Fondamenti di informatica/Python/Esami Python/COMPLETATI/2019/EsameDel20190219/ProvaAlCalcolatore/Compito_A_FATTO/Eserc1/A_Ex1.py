from tester import tester_fun

def A_Ex1(l):
    sol = []
    for i in range(len(l)):
        if i % 2 == 0:
            for j in range(0,len(l[i]),2):
                if l[i][j] not in sol:
                    sol.append(l[i][j])
        if i % 2 == 1:
            for j in range(1,len(l[i]),2):
                if l[i][j] not in sol:
                    sol.append(l[i][j])
    return sorted(sol)        

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, [["mamma","sola","casa"]],["a", "c", "m", "o", "s"])
counter_test_positivi += tester_fun(A_Ex1, [["mamma","sole","casa","sacco"]],["a", "c", "e", "m", "o", "s"])
counter_test_positivi += tester_fun(A_Ex1, [["pippo","castello","se"]],["a","l","o","p","s","t"])
counter_test_positivi += tester_fun(A_Ex1, [[]],[])
counter_test_positivi += tester_fun(A_Ex1, [["assolo",""]],["a","l","s"])


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
