def Ex1(s,l):
    ris=set()
    for elem in l:
        if len(s)==len(elem) and s!=elem:
            for i in range(len(elem)):
                s1=elem[:i]+s[i]+elem[i+1:]
                if s1==s:
                    ris.add(elem)
                    break
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, ['malta',['marea','malia','alta','molta']],{'malia','molta'})
    counter_test_positivi += tester_fun(Ex1, ['morto',['giorno','notte','botte']],set())
    counter_test_positivi += tester_fun(Ex1, ['morto',['molto','mosto','porto']],{'molto','mosto','porto'})
    counter_test_positivi += tester_fun(Ex1, ['a',['a','b','c','d']],{'b','c','d'})
    counter_test_positivi += tester_fun(Ex1, ['asse',['atte','basse','asso','asta']],{'asso'})
    
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, ['salta',['arcobaleno','salto','alta','salla']],{'salto','salla'})
    counter_test_positivi += tester_fun(Ex1, ['vivo',['visto','notte','botte']],set())
    counter_test_positivi += tester_fun(Ex1, ['vivo',['viva','vino','viro']],{'viva','vino','viro'})
    counter_test_positivi += tester_fun(Ex1, ['o',['s','t','q','b']],{'s','t','q','b'})
    counter_test_positivi += tester_fun(Ex1, ['barre',['barra','porta','basse','parte']],{'barra'})

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
