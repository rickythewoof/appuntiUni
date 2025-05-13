def Ex3(file1,file2):
    piatti = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        dati = riga.strip().split(',')
        nomePiatto = dati[0]
        costo = int(dati[1])
        ingredienti = dati[2:]
        piatti[nomePiatto] = [costo,set(ingredienti)]
    f1.close()
    allergie = {}
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        dati = riga.strip().split(',')
        nome = dati[0]
        ingr = dati[1:]
        allergie[nome] = set(ingr)
    f2.close()
    ris = {}
    for nome in allergie:
        ris[nome] = 'Nessuno'
        maxcosto = -1
        for piatto in piatti:
            if len(piatti[piatto][1] & allergie[nome]) == 0:
                if (piatti[piatto][0] > maxcosto or (piatti[piatto][0] == maxcosto and piatto < ris[nome])):
                    ris[nome] = piatto
                    maxcosto = piatti[piatto][0]
    return ris
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','allergie1.csv'],{'Carla': 'Matriciana', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie1.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','allergie2.csv'],{'Carla': 'Matriciana', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno', 'Flavia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie2.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno', 'Flavia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','allergie3.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Caprese', 'Flavia': 'Tiramisu', 'Paolo': 'Focaccia'})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','allergie1.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Caprese'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie1.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti4.csv','allergie4.csv'],{'Carla': 'Focaccia', 'Alessia': 'Saltimbocca', 'Marco': 'Saltimbocca', 'Gianni': 'Saltimbocca', 'Flavia': 'Saltimbocca', 'Paolo': 'Focaccia', 'Filippo': 'Saltimbocca'})
    counter_test_positivi += tester_fun(Ex3, ['piatti4.csv','allergie3.csv'],{'Carla': 'Focaccia', 'Alessia': 'Saltimbocca', 'Marco': 'Saltimbocca', 'Gianni': 'Saltimbocca', 'Flavia': 'Saltimbocca', 'Paolo': 'Focaccia'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','allergie4.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Caprese', 'Flavia': 'Tiramisu', 'Paolo': 'Focaccia', 'Filippo': 'Caprese'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
