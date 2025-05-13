def Ex1(l):
    massimo = 0
    for i in range(len(l)):
        conta = 1
        for j in range(i,len(l)-1):
            if len(l[j]) > len(l[j+1]):
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

    counter_test_positivi += tester_fun(Ex1, [['ora','aldo','gioca','una','carta','e','antonio','prende','tre','danari']],3)
    counter_test_positivi += tester_fun(Ex1, [['tanto','va','la','gatta','al','lardo','che','ci','c','ci']],4)
    counter_test_positivi += tester_fun(Ex1, [['b','aa','ccc','dddd']],1)
    counter_test_positivi += tester_fun(Ex1, [['tanto','va','lardo','zampino','che']],2)
    counter_test_positivi += tester_fun(Ex1, [['nemo','profeta','in','patria','alea','iacta','est','']],3)

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [['aa','a','bbbbb','aaaa','bbb','cc','a']],5)
    counter_test_positivi += tester_fun(Ex1, [['fffaaaa','fffaaaa','aaac','aad','aa','a','']],6)
    counter_test_positivi += tester_fun(Ex1, [['b','c','c','e']],1)
    counter_test_positivi += tester_fun(Ex1, [['ciao','sara','ara','ar','a']],4)
    counter_test_positivi += tester_fun(Ex1, [['gatta','va','lardo','che']],2)


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
