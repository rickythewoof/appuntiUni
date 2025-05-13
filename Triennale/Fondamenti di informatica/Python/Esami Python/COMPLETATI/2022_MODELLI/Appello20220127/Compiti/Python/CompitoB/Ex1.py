def Ex1(l):
    maxDecr = 0
    localDecr = 1
    for i in range(len(l)-1):
        if len(l[i]) > len(l[i+1]):
            localDecr += 1
        else:
            maxDecr = max(maxDecr, localDecr)
            localDecr = 1
        maxDecr = max(maxDecr, localDecr)
    return maxDecr
    
    
    
    
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['ora','aldo','gioca','una','carta','e','antonio','prende','tre','danari']],3)
    counter_test_positivi += tester_fun(Ex1, [['tanto','va','la','gatta','al','lardo','che','ci','c','ci']],4)
    counter_test_positivi += tester_fun(Ex1, [['b','aa','ccc','dddd']],1)
    counter_test_positivi += tester_fun(Ex1, [['tanto','va','lardo','zampino','che']],2)
    counter_test_positivi += tester_fun(Ex1, [['nemo','profeta','in','patria','alea','iacta','est','']],3)
    counter_test_positivi += tester_fun(Ex1, [['aa','a','bbbbb','aaaa','bbb','cc','a']],5)
    counter_test_positivi += tester_fun(Ex1, [['fffaaaa','fffaaaa','aaac','aad','aa','a','']],6)
    counter_test_positivi += tester_fun(Ex1, [['b','c','c','e']],1)
    counter_test_positivi += tester_fun(Ex1, [['ciao','sara','ara','ar','a']],4)
    counter_test_positivi += tester_fun(Ex1, [['gatta','va','lardo','che']],2)


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
