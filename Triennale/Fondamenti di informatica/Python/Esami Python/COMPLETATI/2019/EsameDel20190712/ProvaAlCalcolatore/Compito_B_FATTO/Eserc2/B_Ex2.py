from tester import tester_fun

def B_Ex2(M,s):
    diag1 = ""
    diag2 = ""
    for i in range(len(M)):
        diag1 += M[i][i]
        diag2 += M[len(M)-(1+i)][i]
        print(i)
    print(diag1, diag2)
    if s in diag1 or s in diag2:
        return True
    elif s in diag1[::-1] or s in diag2[::-1]:
        return True
    else:
        return False



###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'rosa'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'aia'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m','o','r'],['r','i','o','y'],['i','s','a','x'],['a','s','t','a']],'rosato'],False)
counter_test_positivi += tester_fun(B_Ex2, [[['a','m'],['a','m']],'ma'],True)
counter_test_positivi += tester_fun(B_Ex2, [[['a']],'b'],False)


print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
