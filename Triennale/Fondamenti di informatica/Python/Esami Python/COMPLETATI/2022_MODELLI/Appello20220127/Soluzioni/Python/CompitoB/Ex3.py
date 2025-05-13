def Ex3(file1,file2,n):
    mag = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        dati = riga.strip().split(',')
        oggetto = dati[0]
        disp = int(dati[1])
        prezzo = int(dati[2])        
        mag[oggetto] = [disp,prezzo]
    f1.close()
    f2 = open(file2,'r',encoding='UTF-8')
    ris={}
    for riga in f2:
        dati = riga.strip().split(',')
        giorno = int(dati[0].strip())
        oggetto = dati[1].strip()
        quant = int(dati[2].strip())
        # print(giorno,oggetto,quant)
        if giorno > n:
            break
        if oggetto not in ris:
            ris[oggetto] = [0,0]
        if quant > 0:
            mag[oggetto][0] += quant
        elif abs(quant) > mag[oggetto][0]:
            ris[oggetto][0] += mag[oggetto][0]*mag[oggetto][1]
            ris[oggetto][1] += (abs(quant) - mag[oggetto][0])*mag[oggetto][1]
            mag[oggetto][0] = 0
        else:
            ris[oggetto][0] -= quant*mag[oggetto][1]
            mag[oggetto][0] += quant
    f2.close()
    return ris


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv',10],{'Ipad': [4200, 1400], 'Iphone': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv',11],{'Ipad': [4200, 1400], 'Iphone': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti2.csv',9],{'Ipad': [5600, 0], 'Iphone': [5000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti1.csv',7],{'Ipad': [1200, 2000], 'Iphone': [4000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti2.csv',17],{'Ipad': [2000, 1200], 'Iphone': [7000, 5000], 'Ps5': [2500, 1000]})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti3.csv',10],{'Galaxy': [4200, 1400], 'Xbox': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti3.csv',11],{'Galaxy': [4200, 1400], 'Xbox': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti4.csv',9],{'Galaxy': [5600, 0], 'Xbox': [5000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti3.csv',7],{'Galaxy': [1200, 2000], 'Xbox': [4000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti4.csv',17],{'Galaxy': [2000, 1200], 'Xbox': [7000, 5000], 'PC': [2500, 1000]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
