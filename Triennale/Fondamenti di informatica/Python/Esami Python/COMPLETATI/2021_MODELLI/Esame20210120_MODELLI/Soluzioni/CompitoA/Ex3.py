def Ex3(file):
    diz = {}
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        dati = riga.strip().split(',')
        nome = dati[0]
        prop = dati[1]
        valore = int(dati[2])
        if nome not in diz:
            diz[nome] = {prop:valore}
        elif prop not in diz[nome]:
            diz[nome][prop] = valore
        else:
            diz[nome][prop] += valore
    print(diz)
    f.close()
    # inizializziamo il massimo ad un valore qualsiasi del dizionario
    nomeMax = nome
    massimo = diz[nome][prop] 
    propMax = prop
    for nome in diz:
        for prop in diz[nome]:
            if diz[nome][prop] >= massimo:
                massimo = diz[nome][prop]
                nomeMax = nome
                propMax = prop
    return nomeMax,propMax

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['file1.csv'],('Marco', 'soldi'))
    counter_test_positivi += tester_fun(Ex3, ['file2.csv'],('Paolo', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file3.csv'],('Marco', 'soldi'))
    counter_test_positivi += tester_fun(Ex3, ['file4.csv'],('Anna', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file5.csv'],('Paolo', 'punti'))

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['file6.csv'],('Anna', 'soldi')) # vi è una sola caratteristica
    counter_test_positivi += tester_fun(Ex3, ['file7.csv'],('Anna', 'punti')) # vi sono due caratteristiche
    counter_test_positivi += tester_fun(Ex3, ['file8.csv'],('Marco', 'soldi')) # valori tutti negativi
    counter_test_positivi += tester_fun(Ex3, ['file9.csv'],('Marco', 'soldi')) # risultato finale = 0
    counter_test_positivi += tester_fun(Ex3, ['file10.csv'],('Anna', 'bonus')) # valori tutti positivi

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
