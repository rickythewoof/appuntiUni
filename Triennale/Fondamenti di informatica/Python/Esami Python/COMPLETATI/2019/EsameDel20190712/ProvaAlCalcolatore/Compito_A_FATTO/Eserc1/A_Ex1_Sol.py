from tester import tester_fun

def A_Ex1(s1,s2):
    distance=abs(len(s1)-len(s2))
    if len(s1) > len(s2):
        m=len(s2)
    else:
        m=len(s1)
    for i in range(m):
        if s1[i]!=s2[i]:
            distance=distance+1
    return distance

 
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["aceto","aceto"],0)
counter_test_positivi += tester_fun(A_Ex1, ["pippo","pappa"],2)
counter_test_positivi += tester_fun(A_Ex1, ["aceto","ace"],2)
counter_test_positivi += tester_fun(A_Ex1, ["alba","albino"],3)
counter_test_positivi += tester_fun(A_Ex1, ["","pippo"],5)



print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
