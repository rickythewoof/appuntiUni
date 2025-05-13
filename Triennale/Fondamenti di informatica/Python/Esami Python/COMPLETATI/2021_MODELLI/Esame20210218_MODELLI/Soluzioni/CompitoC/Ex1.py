def Ex1(l1,l2,n):
    ris = 0
    for s1 in l1:
        for s2 in l2:
            trovato = False
            for i in range(len(s1)-n+1):
                if s1[i:i+n] in s2:
                    trovato = True
            if trovato:
                ris += 1
    return ris
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['arciere', 'pippo', 'accordare'],['arco', 'pappa', 'corda'],3],2)
    counter_test_positivi += tester_fun(Ex1, [['arciere', 'pippo', 'accordare'],['corda', 'arco', 'pappa', 'ippopotamo'],3],3)
    counter_test_positivi += tester_fun(Ex1, [['lanciere', 'ceppo', 'accordarsi'],['corda', 'arco', 'pappa', 'ippopotamo'],4],1)
    counter_test_positivi += tester_fun(Ex1, [['lanciatore', 'ceppo', 'accordarsi'],['corda', 'arco', 'pappa', 'ippopotamo','sciatore'],4],2)
    counter_test_positivi += tester_fun(Ex1, [['lanciere', 'ceppo', 'accordarsi'],['corda', 'arco', 'pappa', 'ippopotamo'],1],12)

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [['aquila', 'torta', 'parli','pippo'] ,['merlo', 'contorta', 'parlargli','impiccio'],3],2)
    counter_test_positivi += tester_fun(Ex1, [['aquila', 'torta', 'parli','pippo'] ,['merlo', 'contorta', 'parlargli','impiccio'],4],2)
    counter_test_positivi += tester_fun(Ex1, [['aquila', 'parli','pippo'] ,['merlo', 'contorta', 'parlargli','impiccio'],3],1)
    counter_test_positivi += tester_fun(Ex1, [['aquila', 'torta', 'parli','pippo'] ,['merlo', 'contorta', 'parlargli','impiccio'],5],1)
    counter_test_positivi += tester_fun(Ex1, [['aquila', 'torta', 'parli','pippo'] ,['merlo', 'contorta', 'parlargli','impiccio'],1],16)
                
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
