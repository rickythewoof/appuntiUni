from tester import tester_fun

def A_Ex1(s):
    maxLen = 0
    maxChar = ""
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            localLen = s.rfind(s[i]) - s.find(s[i]) + 1
        else:
            localLen = 1
        maxLen = max(maxLen, localLen)
    return maxLen
            
                
            

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

