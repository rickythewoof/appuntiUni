def Ex3(file):
    f = open(file, "r", encoding = "UTF-8")
    conti = {}
    numRosso = {}
    for ln in f:
        ln = ln.strip().split(",")
        nome = ln[0]
        movimento = int(ln[1])
        conti[nome] = conti.get(nome, 0)
        if movimento > 0:
            conti[nome] += movimento
        else:
            if abs(movimento) <= conti[nome]:
                conti[nome] += movimento
            else:
                numRosso[nome] = numRosso.get(nome, 0) + 1
                conti[nome] += movimento
    if numRosso == {}:
        return 'nessun prelievo in rosso'
    print(numRosso)
    rossi = []
    maxRossi = 0
    for key in numRosso:
        if numRosso[key] > maxRossi:
            maxRossi = numRosso[key]
            rossi.clear()
            rossi.append(key)
        elif numRosso[key] == maxRossi:
            rossi.append(key)
    return (min(rossi), conti[min(rossi)])


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5
    
    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi1.csv'],('Antonio',-150))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi2.csv'],('Marco', 0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi3.csv'],'nessun prelievo in rosso')
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi4.csv'],('Gianni',0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi5.csv'],('Debora',20))
    
    # test aggiuntivi
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi6.csv'],('Luca',-100))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi7.csv'],('Franco', 0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi8.csv'],'nessun prelievo in rosso')
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi9.csv'],('Giorgio',0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi10.csv'],('Gianni',-400))


    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
