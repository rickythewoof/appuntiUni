def Ex3(file1,file2):
    d = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    for ln in f1:
        dati = ln.strip().split(",")
        nome = dati[0]   
        disp = int(dati[1])
        costo = int(dati[2])     
        d[nome] = [disp, costo]
        for i in range(3, len(dati)):
            d[nome].append(dati[i])
    f1.close()
    print(d)
    sol = {}
    f2 = open(file2, "r", encoding = "UTF-8")
    for ln in f2:
        spec = set()
        dati = ln.strip().split(",") 
        print(dati)     
        utente = dati[0]
        maxCosto = int(dati[1])
        for i in range(2, len(dati)):
            spec.add(dati[i])
        for key in d:
            if d[key][0] > 0 and maxCosto >= d[key][1]:
                tutto = True
                for dato in spec:
                    if dato not in d[key]:
                        tutto = False
                if tutto:
                     sol[utente] = sol.get(utente, ("nulla", 0))
                     if sol[utente][1] <= 0 or sol[utente][1] > d[key][1]:
                        sol[utente] = (key, d[key][1])
                        d[key][0] -= 1
    return sol
        
    
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini1.csv'],{'Giorgio': ('Samsung', 399), 'Paola': ('Acer', 349),'Francesca':('Acer',349)})
    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini2.csv'],{'Giorgio': ('Samsung', 399), 'Paola': ('Acer', 349)})
    counter_test_positivi += tester_fun(Ex3, ['listino1.csv','ordini3.csv'],{'Paola': ('Acer', 349), 'Francesca': ('Samsung', 399)})
    counter_test_positivi += tester_fun(Ex3, ['listino2.csv','ordini2.csv'],{'Giorgio': ('Huawei', 250), 'Paola': ('Acer', 349), 'Francesca': ('Huawei', 250)})
    counter_test_positivi += tester_fun(Ex3, ['listino2.csv','ordini3.csv'],{'Paola': ('Acer', 349), 'Francesca': ('Huawei', 250)})

    counter_test_positivi += tester_fun(Ex3, ['listino3.csv','ordini4.csv'],{'Aldo': ('Mac', 529), 'Paolo': ('Dell', 329), 'Francesco': ('Dell', 329)})
    counter_test_positivi += tester_fun(Ex3, ['listino3.csv','ordini5.csv'],{'Giorgia': ('Lenovo', 349), 'Paolo': ('Dell', 329)})
    counter_test_positivi += tester_fun(Ex3, ['listino3.csv','ordini6.csv'],{'Francesco': ('Dell', 329), 'Aldo': ('Dell', 329)})
    counter_test_positivi += tester_fun(Ex3, ['listino4.csv','ordini5.csv'],{'Giorgia': ('Mac', 449), 'Paolo': ('Dell', 249), 'Francesco': ('Lenovo', 150)})
    counter_test_positivi += tester_fun(Ex3, ['listino4.csv','ordini6.csv'],{'Giorgia': ('Mac', 449), 'Paolo': ('Dell', 249), 'Francesco': ('Lenovo', 150), 'Aldo': ('Lenovo', 150)})
    

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
