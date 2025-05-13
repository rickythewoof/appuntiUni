from tester import tester_fun

def B_Ex1(s1,s2):
    caratteriUguali = 0
    if len(s1) != len(s2):
        return False
    else:
        for charIndex in range(len(s1)):
            if s1[charIndex] == s2[charIndex]:
                caratteriUguali += 1
    if caratteriUguali == len(s1) - 1:
        return True
    else:
        return False
    
    
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["amata","arata"],True)
counter_test_positivi += tester_fun(B_Ex1, ["blu","blue"],False)
counter_test_positivi += tester_fun(B_Ex1, ["osso","osso"],False)
counter_test_positivi += tester_fun(B_Ex1, ["antico","antica"],True)
counter_test_positivi += tester_fun(B_Ex1, ["",""],False)


print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
