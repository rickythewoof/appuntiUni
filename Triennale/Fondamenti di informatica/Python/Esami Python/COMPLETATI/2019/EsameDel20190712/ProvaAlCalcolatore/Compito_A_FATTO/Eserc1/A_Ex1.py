from tester import tester_fun

def A_Ex1(s1,s2):
    var = abs(len(s1)-len(s2))
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            var +=1
    return var


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["aceto","aceto"],0)
counter_test_positivi += tester_fun(A_Ex1, ["pippo","pappa"],2)
counter_test_positivi += tester_fun(A_Ex1, ["aceto","ace"],2)
counter_test_positivi += tester_fun(A_Ex1, ["alba","albino"],3)
counter_test_positivi += tester_fun(A_Ex1, ["","pippo"],5)


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
