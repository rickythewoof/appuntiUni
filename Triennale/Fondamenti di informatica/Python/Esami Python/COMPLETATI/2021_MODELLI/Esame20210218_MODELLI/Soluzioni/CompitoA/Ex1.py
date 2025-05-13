def Ex1(l):
    ris = set()
    massimo = 0
    for s in l:
        invs = s[::-1]
        i = 0
        uguali = True
        while uguali and i < len(s):
            if s[i] == invs[i]:
                i += 1
            else:
                uguali = False
        if i > massimo:
            massimo = i
            ris = {s}
        elif i == massimo:
            ris.add(s)
    return ris
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda']],{'plutoulp', 'ava'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','anna']],{'anna'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','anna','pattamoattap']],{'pattamoattap'})
    counter_test_positivi += tester_fun(Ex1, [['avola','ava','plutoulp','corda','antoitna']],{'ava', 'antoitna', 'plutoulp'})
    counter_test_positivi += tester_fun(Ex1, [['avoli','avo','pluto','corda']],{'corda', 'avoli', 'pluto', 'avo'})
            
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb']],{'plutoulp', 'bzb'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb','bnnb']],{'bnnb'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb','bnnb','pbttbmobttbp']],{'pbttbmobttbp'})
    counter_test_positivi += tester_fun(Ex1, [['bzolb','bzb','plutoulp','cordb','bntoitnb']],{'bzb', 'bntoitnb', 'plutoulp'})
    counter_test_positivi += tester_fun(Ex1, [['bzoli','bzo','pluto','cordb']],{'cordb', 'bzoli', 'pluto', 'bzo'})
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
