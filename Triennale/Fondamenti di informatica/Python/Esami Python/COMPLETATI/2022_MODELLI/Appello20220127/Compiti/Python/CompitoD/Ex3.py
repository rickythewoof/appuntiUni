def Ex3(file1,file2):
    d1 = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    for ln in f1:
        ln = ln.strip().split(",")
        nome = ln[0]
        ingredienti = ln[1:]
        d1[nome] = ingredienti
    f1.close()
    sol = {}
    f2 = open(file2, "r", encoding = "UTF-8")
    for ln in f2:
        ln = ln.strip().split(",")
        nome = ln[0]
        maxIngr = 0
        maxPiatto = "Nessuno"
        ingr = ln[1:]
        for piatto in d1:
            localMax = 0
            for i in ingr:
                if i in d1[piatto]:
                    localMax += 1
            if localMax > maxIngr:
                maxIngr = localMax
                maxPiatto = piatto
            elif localMax == maxIngr and maxIngr != 0:
                maxPiatto = max(piatto, maxPiatto)
        sol[nome] = maxPiatto
    return sol    
            
                
    
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','golosi1.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Nessuno', 'Silvia': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','golosi1.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Caprese', 'Silvia': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','golosi2.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Nessuno', 'Silvia': 'PizzaMargherita'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','golosi2.csv'],{'Carla': 'Tiramisu', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'Caprese', 'Silvia': 'Carbonara'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','golosi3.csv'],{'Carla': 'Amatriciana', 'Alessia': 'Tiramisu', 'Marco': 'PizzaMargherita', 'Gianni': 'PizzaMargherita', 'Silvia': 'Focaccia', 'Paolo': 'Tiramisu'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
