from tester import tester_fun

def A_Ex1(s):
    lung = 0
    for i in range(len(s)):
        last = s.rfind(s[i])
        if last - i + 1 > lung:
            lung = last-i+1
    return lung

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["annabella"],9)
counter_test_positivi += tester_fun(A_Ex1, ["pallone"],2)
counter_test_positivi += tester_fun(A_Ex1, ["aratro"],4)
counter_test_positivi += tester_fun(A_Ex1, ["ancore"],1)
counter_test_positivi += tester_fun(A_Ex1, [""],0)

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

