def Ex3(file1,file2):
    mag = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        dati = riga.strip().split(',')
        oggetto = dati[0]
        disp = int(dati[1])
        mindisp = int(dati[2])
        prezzo = int(dati[3])
        mag[oggetto] = [disp,mindisp,prezzo]
    f1.close()
    ris = {}
    for elem in mag:
        ris[elem] = [mag[elem][0],0,mag[elem][2]]
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        dati = riga.strip().split(',')
        oggetto = dati[0]
        quant = int(dati[1])
        olddisp = ris[oggetto][0]
        minimo = mag[oggetto][1]
        if ris[oggetto][0] + quant >= 0: # c'è disponibilità
            ris[oggetto][0] += quant
        else:
            ris[oggetto][1] += abs(ris[oggetto][0] + quant)
            ris[oggetto][0] = 0
        if olddisp < minimo and ris[oggetto][0] >= minimo:
            ris[oggetto][2] -= 5
        elif olddisp >= minimo and ris[oggetto][0] < minimo:
            ris[oggetto][2] += 5
    f2.close()
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv'],{'Iphone': [16, 0, 500], 'Ipad': [0, 2, 705], 'Ps5': [5, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti2.csv'],{'Iphone': [16, 0, 500], 'Ipad': [3, 2, 700], 'Ps5': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti3.csv'],{'Iphone': [4, 0, 505], 'Ipad': [10, 2, 700], 'Ps5': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti1.csv'],{'Iphone': [11, 0, 500], 'Ipad': [0, 2, 705], 'Ps5': [3, 0, 400]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti2.csv'],{'Iphone': [11, 0, 500], 'Ipad': [3, 2, 700], 'Ps5': [5, 0, 400]})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti4.csv'],{'Xbox': [16, 0, 500], 'Galaxy': [0, 2, 705], 'Ps4': [5, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti5.csv'],{'Xbox': [16, 0, 500], 'Galaxy': [3, 2, 700], 'Ps4': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti6.csv'],{'Xbox': [4, 0, 505], 'Galaxy': [10, 2, 700], 'Ps4': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti4.csv'],{'Xbox': [11, 0, 500], 'Galaxy': [0, 2, 705], 'Ps4': [3, 0, 400]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti5.csv'],{'Xbox': [11, 0, 500], 'Galaxy': [3, 2, 700], 'Ps4': [5, 0, 400]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
