def Ex1(l):
    sol = set()
    maxWordInv = 0
    for word in l:
        palindroma = 0
        wordInv = word[::-1]
        for i in  range(len(word)):
            if word[i] == wordInv[i]:
                palindroma += 1
            else:
                break
        if palindroma > maxWordInv:
            maxWordInv = palindroma
            sol.clear()
            sol.add(word)
        elif palindroma == maxWordInv:
            sol.add(word)
        else:
            continue        
    return sol           

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda']],{'plutoulp', 'ava'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','anna']],{'anna'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','anna','pattamoattap']],{'pattamoattap'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','antoitna']],{'ava', 'antoitna', 'plutoulp'})
    counter_test_positivi += tester_fun(Ex1, [['avoli','avo','pluto','corda']],{'corda', 'avoli', 'pluto', 'avo'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb']],{'plutoulp', 'bzb'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb','bnnb']],{'bnnb'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb','bnnb','pbttbmobttbp']],{'pbttbmobttbp'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb','bntoitnb']],{'bzb', 'bntoitnb', 'plutoulp'})
    counter_test_positivi += tester_fun(Ex1, [['bzoli','bzo','pluto','cordb']],{'cordb', 'bzoli', 'pluto', 'bzo'})
        
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
