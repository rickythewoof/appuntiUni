def Ex3(file1,file2):
    piatti = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        dati = riga.strip().split(',')
        nomePiatto = dati[0]
        ingredienti = dati[1:]
        piatti[nomePiatto] = set(ingredienti)
    f1.close()
    golosi = {}
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        dati = riga.strip().split(',')
        nome = dati[0]
        ingr = dati[1:]
        golosi[nome] = set(ingr)
    f2.close()
    ris = {}
    for nome in golosi:
        massimo = 1
        piattoMax = ''
        ris[nome] = 'Nessuno'
        for piatto in piatti:
            ingrComuni = len(piatti[piatto] & golosi[nome])
            if ingrComuni > massimo or (ingrComuni == massimo and piatto > piattoMax):
                ris[nome] = piatto
                massimo = ingrComuni
                piattoMax = piatto
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','golosi1.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Nessuno', 'Silvia': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','golosi1.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Caprese', 'Silvia': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','golosi2.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Nessuno', 'Silvia': 'PizzaMargherita'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','golosi2.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Caprese', 'Silvia': 'Carbonara'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','golosi3.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu'})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','golosi4.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu', 'Giorgia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti4.csv','golosi4.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu', 'Giorgia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti4.csv','golosi5.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu', 'Giorgia': 'Tiramisu', 'Piero': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti5.csv','golosi4.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu', 'Giorgia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti5.csv','golosi5.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu', 'Giorgia': 'Tiramisu', 'Piero': 'Tiramisu'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
