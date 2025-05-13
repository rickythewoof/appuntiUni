def Ex1(n):
    massimo = 0
    s = str(n)
    for i in range(len(s)):
        conta = 1
        for j in range(i,len(s)-1):
            if int(s[j])%2 != int(s[j+1])%2:
                conta += 1
            else: break
        if conta > massimo:
            massimo = conta
    return massimo
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [76672172322],4)
    counter_test_positivi += tester_fun(Ex1, [32210],3)
    counter_test_positivi += tester_fun(Ex1, [272323],6)
    counter_test_positivi += tester_fun(Ex1, [77777],1)
    counter_test_positivi += tester_fun(Ex1, [223344],2)

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [22],1)
    counter_test_positivi += tester_fun(Ex1, [1],1)
    counter_test_positivi += tester_fun(Ex1, [767676767676],12)
    counter_test_positivi += tester_fun(Ex1, [101010101],9)
    counter_test_positivi += tester_fun(Ex1, [111222333],2)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
