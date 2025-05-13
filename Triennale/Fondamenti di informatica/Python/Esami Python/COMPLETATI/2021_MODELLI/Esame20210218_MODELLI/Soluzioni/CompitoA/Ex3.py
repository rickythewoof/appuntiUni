def Ex3(file1,file2):
    listino = {}
    diz = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        riga = riga.strip().split(',')
        portatile = riga[0]
        disp = int(riga[1])
        costo = int(riga[2])
        caratt = riga[3:]
        listino[portatile] = [disp,costo,caratt]
    f1.close()
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        riga = riga.strip().split(',')
        cliente = riga[0]
        prezzoMax = int(riga[1])
        carattR = riga[2:]
        costomin = prezzoMax
        portmin = None
        for port in listino:
            if listino[port][0] > 0 and listino[port][1] <= costomin:
                ok = True
                for c in carattR:
                    if c not in listino[port][2]:
                        ok = False
                if ok:
                    costomin = listino[port][1]
                    portmin = port
        if portmin != None:
            diz[cliente] = (portmin,listino[portmin][1])
            listino[portmin][0] -= 1
    return diz

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini1.csv'],{'Giorgio': ('Samsung', 399), 'Paola': ('Acer', 349),'Francesca':('Acer',349)})
    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini2.csv'],{'Giorgio': ('Samsung', 399), 'Paola': ('Acer', 349)})
    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini3.csv'],{'Paola': ('Acer', 349), 'Francesca': ('Samsung', 399)})
    counter_test_positivi += tester_fun(Ex3, ['listino2.csv','ordini2.csv'],{'Giorgio': ('Huawei', 250), 'Paola': ('Acer', 349), 'Francesca': ('Huawei', 250)})
    counter_test_positivi += tester_fun(Ex3, ['listino2.csv','ordini3.csv'],{'Paola': ('Acer', 349), 'Francesca': ('Huawei', 250)})
    
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['listino3.csv','ordini4.csv'],{'Aldo': ('Mac', 529), 'Paolo': ('Dell', 329), 'Francesco': ('Dell', 329)})
    counter_test_positivi += tester_fun(Ex3, ['listino3.csv','ordini5.csv'],{'Giorgia': ('Lenovo', 349), 'Paolo': ('Dell', 329)})
    counter_test_positivi += tester_fun(Ex3, ['listino3.csv','ordini6.csv'],{'Francesco': ('Dell', 329), 'Aldo': ('Dell', 329)})
    counter_test_positivi += tester_fun(Ex3, ['listino4.csv','ordini5.csv'],{'Giorgia': ('Mac', 449), 'Paolo': ('Dell', 249), 'Francesco': ('Lenovo', 150)})
    counter_test_positivi += tester_fun(Ex3, ['listino4.csv','ordini6.csv'],{'Giorgia': ('Mac', 449), 'Paolo': ('Dell', 249), 'Francesco': ('Lenovo', 150), 'Aldo': ('Lenovo', 150)})
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
