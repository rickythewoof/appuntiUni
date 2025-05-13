def Ex1(l1,l2):
    sol = set()
    for word1 in l1:
        for word2 in l2:
            if sorted(word1) == sorted(word2):
                sol.add(word1)
                sol.add(word2)
    return sol       


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [['arco', 'pippo', 'pluto', 'corda'],['palla', 'darco', 'ocra', 'casa']],{'corda', 'darco', 'ocra', 'arco'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', 'pluto', 'corda'],['palla', 'caro', 'ocra', 'casa']],{'caro', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', '', 'corda'],['palla', 'codarco', 'ocra', 'casa', '']],{'', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex1, [['arco', 'pala', '', 'corda', 'roccado'],['palla', 'codarco', 'ocra', 'casa']],{'codarco', 'arco', 'ocra', 'roccado'})
    counter_test_positivi += tester_fun(Ex1, [['pala', '', 'corda', 'rocca do'],['palla', 'co darco', 'ocra', 'casa']],{'rocca do', 'co darco'})

    counter_test_positivi += tester_fun(Ex1, [['arco', 'pippo', 'pluto', 'corda'],[]],set()) # una lista vuota
    counter_test_positivi += tester_fun(Ex1, [['arco', 'caro','pluto'],['tuplo', 'acaro']],{'pluto', 'tuplo'}) # anagrammi presenti tra elementi della prima lista da non ritornare
    counter_test_positivi += tester_fun(Ex1, [['arci', 'pala', '', 'corda'],['palla', 'codarco', 'icra', 'casa', '']],{'', 'arci', 'icra'}) # esempio generico
    counter_test_positivi += tester_fun(Ex1, [['arco', 'ocra', 'corda', 'roccado'],['raco', 'orca', 'cord', 'casa']],{'orca', 'ocra', 'raco', 'arco'}) # parole anagrammabili in entrambe le liste
    counter_test_positivi += tester_fun(Ex1, [[],[]],set()) # entrambe le liste vuote

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
