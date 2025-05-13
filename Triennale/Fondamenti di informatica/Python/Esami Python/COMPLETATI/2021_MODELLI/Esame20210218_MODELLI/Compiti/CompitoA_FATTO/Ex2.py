def Ex2(l):
    sol = set()
    maxPerf = -10000
    for tupla in l:
        localPerf = 0
        for i in range(1, len(tupla)):
            localPerf += tupla[i]
        if localPerf > maxPerf:
            maxPerf = localPerf
            sol.clear()
            sol.add(tupla[0])
        elif localPerf == maxPerf:
            sol.add(tupla[0])
    return sol
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [[('marco',-3,0,1),('aldo',2,3),('maria',-1,1,2,1,2)]],{'aldo','maria'})
    counter_test_positivi += tester_fun(Ex2, [[('sergio',11,2,13)]],{'sergio'})
    counter_test_positivi += tester_fun(Ex2, [[('monica',-3,-2,0),('marcello',-2,-3),('alessandra',-5,-5)]],{'monica','marcello'})
    counter_test_positivi += tester_fun(Ex2, [[('sandro',1,2,3),('sonia',25),('giorgia',-5,-5,-5,-5),('fabio',5,5,5,5,5)]],{'sonia','fabio'})
    counter_test_positivi += tester_fun(Ex2, [[('andrea',2,3,-2,-3),('giorgia',-2,-2,-3),('maria',-5)]],{'andrea'})

    counter_test_positivi += tester_fun(Ex2, [[('giusy',-5,1,2),('serena',3,4),('mario',-1,2,2,2,2)]],{'serena','mario'})
    counter_test_positivi += tester_fun(Ex2, [[('teresa',10,5,10)]],{'teresa'})
    counter_test_positivi += tester_fun(Ex2, [[('massimo',-5,-3,0),('marcella',-8),('alessandra',-5,-3)]],{'massimo','marcella','alessandra'})
    counter_test_positivi += tester_fun(Ex2, [[('john',-1,-2),('sonia',12),('giovanna',-5,5,5,-3),('fabiola',3,3,3,3)]],{'sonia','fabiola'})
    counter_test_positivi += tester_fun(Ex2, [[]],set())
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
