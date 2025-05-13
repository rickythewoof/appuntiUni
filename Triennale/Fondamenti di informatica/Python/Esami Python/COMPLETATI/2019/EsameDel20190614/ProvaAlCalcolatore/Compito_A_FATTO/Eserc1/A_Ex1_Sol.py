from tester import tester_fun

def A_Ex1(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[len(s2)-i-1]:
            return False
    return True

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["acetone","enoteca"],True)
counter_test_positivi += tester_fun(A_Ex1, ["aceto","teca"],False)
counter_test_positivi += tester_fun(A_Ex1, ["otto","otto"],True)
counter_test_positivi += tester_fun(A_Ex1, ["",""],True)
counter_test_positivi += tester_fun(A_Ex1, ["erto",""],False)


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
