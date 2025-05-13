from tester import tester_fun

def A_Ex1(s1,s2):
    if s1[::-1] == s2:
        return True
    else:
        return False

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["acetone","enoteca"],True)
counter_test_positivi += tester_fun(A_Ex1, ["aceto","teca"],False)
counter_test_positivi += tester_fun(A_Ex1, ["otto","otto"],True)
counter_test_positivi += tester_fun(A_Ex1, ["",""],True)
counter_test_positivi += tester_fun(A_Ex1, ["erto",""],False)


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
