def Ex1(n):
    n = str(n)
    maxLen = 0
    localLen = 1
    for i in range(len(n)-1): 
        if int(n[i]) % 2 == 0 and int(n[i+1]) % 2 == 1:
            localLen += 1
        elif int(n[i]) % 2 == 1 and int(n[i+1]) % 2 == 0:
            localLen += 1
        else:
            maxLen = max(maxLen, localLen)
            localLen = 1
    maxLen = max(maxLen, localLen)
    return maxLen

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [76672172322],4)
    counter_test_positivi += tester_fun(Ex1, [32210],3)
    counter_test_positivi += tester_fun(Ex1, [272323],6)
    counter_test_positivi += tester_fun(Ex1, [77777],1)
    counter_test_positivi += tester_fun(Ex1, [223344],2)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
