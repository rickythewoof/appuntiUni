def Ex1(l1,l2):
    ris = set()
    for s1 in l1:
        for s2 in l2:
            if len(s1) == len(s2):
                anagramma = True
                for c in s1:
                    if s1.count(c) != s2.count(c):
                        anagramma = False
                if anagramma:
                    ris.add(s1)
                    ris.add(s2)
    return ris
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['arco', 'pippo', 'pluto', 'corda'],['palla', 'darco', 'ocra', 'casa']],{'corda', 'darco', 'ocra', 'arco'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', 'pluto', 'corda'],['palla', 'codarco', 'ocra', 'casa']],{'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', '', 'corda'],['palla', 'codarco', 'ocra', 'casa', '']],{'', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', '', 'corda', 'roccado'],['palla', 'codarco', 'ocra', 'casa']],{'codarco', 'arco', 'ocra', 'roccado'})
    counter_test_positivi += tester_fun(Ex1, [['pala', '', 'corda', 'rocca do'],['palla', 'co darco', 'ocra', 'casa']],{'rocca do', 'co darco'})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [['arco', 'pippo', 'pluto', 'corda'],[]],set()) # una lista vuota
    counter_test_positivi += tester_fun(Ex1, [['arco', 'caro','pluto'],['tuplo', 'acaro']],{'pluto', 'tuplo'}) # anagrammi presenti tra elementi della prima lista da non ritornare
    counter_test_positivi += tester_fun(Ex1, [['arci', 'pala', '', 'corda'],['palla', 'codarco', 'icra', 'casa', '']],{'', 'arci', 'icra'}) # esempio generico
    counter_test_positivi += tester_fun(Ex1, [['arco', 'ocra', 'corda', 'roccado'],['raco', 'orca', 'cord', 'casa']],{'orca', 'ocra', 'raco', 'arco'}) # parole anagrammabili in entrambe le liste
    counter_test_positivi += tester_fun(Ex1, [[],[]],set()) # entrambe le liste vuote

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
