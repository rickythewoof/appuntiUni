def Ex1(s):
    massimo = 0
    for i in range(len(s)):
        conta = 1
        for j in range(i,len(s)-1):
            if s[j] <= s[j+1]:
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

    counter_test_positivi += tester_fun(Ex1, ['cavallo'],4)
    counter_test_positivi += tester_fun(Ex1, ['arciere ponte'],2)
    counter_test_positivi += tester_fun(Ex1, ['casa vacanze arco'],3)
    counter_test_positivi += tester_fun(Ex1, ['parte di una casa'],3)
    counter_test_positivi += tester_fun(Ex1, ['ponte bassuz, tunnel lungo'],5)
    
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, ['giraffa giraffo'],4)
    counter_test_positivi += tester_fun(Ex1, ['pegnorto'],6)
    counter_test_positivi += tester_fun(Ex1, ['spola '],1)
    counter_test_positivi += tester_fun(Ex1, ['passaggio obbligato'],5)
    counter_test_positivi += tester_fun(Ex1, ['proviamole tutte'],3)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
