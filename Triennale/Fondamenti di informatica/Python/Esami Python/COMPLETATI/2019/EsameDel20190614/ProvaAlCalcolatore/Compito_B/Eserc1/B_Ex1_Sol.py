from tester import tester_fun

def B_Ex1(s1,s2):
    if len(s1) != len(s2):
        return False
    different_chars = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if different_chars==0:
                different_chars = 1
            else:
                return False
    if different_chars == 0:
        return False
    return True

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["amata","arata"],True)
counter_test_positivi += tester_fun(B_Ex1, ["blu","blue"],False)
counter_test_positivi += tester_fun(B_Ex1, ["osso","osso"],False)
counter_test_positivi += tester_fun(B_Ex1, ["antico","antica"],True)
counter_test_positivi += tester_fun(B_Ex1, ["",""],False)


print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
