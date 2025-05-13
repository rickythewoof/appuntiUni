def Ex3(file1,file2):
    d1 = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    for ln in f1:
        ln = ln.strip().split(",")
        piatto = ln[0]
        costo = int(ln[1])
        d1[piatto] = [costo]
        for i in range(2, len(ln)):
            d1[piatto].append(ln[i])
    f1.close()
    d2 = {}
    f2 = open(file2, "r", encoding = "UTF-8")
    for ln in f2:
        ln = ln.strip().split(",")
        nome = ln[0]
        d2[nome] = list(d1.keys())
        for i in range(1, len(ln)):
            allergeno = ln[i]
            for key in d1:
                if allergeno in d1[key] and key in d2[nome]:
                    d2[nome].remove(key)
    for key in  d2:
        costoMax = 0
        piattoMax = "Nessuno"
        for piatto in d2[key]:
            costoLocale = d1[piatto][0]
            if costoLocale > costoMax:
                costoMax = costoLocale
                piattoMax = piatto
        d2[key] = piattoMax
    return d2

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','allergie1.csv'],{'Carla': 'Matriciana', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie1.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno'})
    counter_test_positivi += tester_fun(Ex3, ['piatti1.csv','allergie2.csv'],{'Carla': 'Matriciana', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno', 'Flavia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti2.csv','allergie2.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Nessuno', 'Flavia': 'Tiramisu'})
    counter_test_positivi += tester_fun(Ex3, ['piatti3.csv','allergie3.csv'],{'Carla': 'Focaccia', 'Alessia': 'Tiramisu', 'Marco': 'Matriciana', 'Gianni': 'Caprese', 'Flavia': 'Tiramisu', 'Paolo': 'Focaccia'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
