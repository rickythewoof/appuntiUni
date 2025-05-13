from tester import tester_fun

def A_Ex1(s,n):
    occorrenze = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        if s.lower().count(char) == n:
            occorrenze += 1
    return occorrenze
    


 
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["ossessivo",4],1)
counter_test_positivi += tester_fun(A_Ex1, ["Anna",2],2)
counter_test_positivi += tester_fun(A_Ex1, ["amico",1],5)
counter_test_positivi += tester_fun(A_Ex1, ["allenAtrice",2],3)
counter_test_positivi += tester_fun(A_Ex1, ["pippo",3],1)

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
