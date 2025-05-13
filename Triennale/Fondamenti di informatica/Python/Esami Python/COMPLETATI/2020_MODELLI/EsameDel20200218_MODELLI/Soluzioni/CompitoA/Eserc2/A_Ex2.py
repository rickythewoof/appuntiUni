from tester import tester_fun

def A_Ex2(l):
    ris = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            simil = 0
            for k in range(min(len(l[i]),len(l[j]))):
                if l[i][k] == l[j][k]:
                    simil += 1
            if simil > ris:
                ris = simil
    return ris
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [['casa','palla','freno','cosa']] ,3)
counter_test_positivi += tester_fun(A_Ex2, [['casale','pallae','freno','treno']] ,4)
counter_test_positivi += tester_fun(A_Ex2, [['cascata','pallone','caserma','freno','qualcuno', 'qualcosa']] ,5)
counter_test_positivi += tester_fun(A_Ex2, [['cascata','pallone','caserma','freno','qualcuno', 'qualcosa','palloni']] ,6)
counter_test_positivi += tester_fun(A_Ex2, [['cascata','pilone','frase']] ,0)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
