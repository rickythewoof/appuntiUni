from tester import tester_fun

def A_Ex2(file1,file2):
    riserva = {}
    venduti = {}
    f1 = open(file1,encoding='UTF-8')
    f1.readline()
    for riga in f1:
        coppia = riga.strip().split(',')
        riserva[coppia[0]] = int(coppia[1])
    f1.close()
    f2 = open(file2,encoding='UTF-8')
    f2.readline()
    for riga in f2:
        tripla = riga.strip().split(',')
        acquirente = tripla[0]
        oggetto = tripla[1]
        prezzo = int(tripla[2])
        if prezzo >= riserva[oggetto]:
            if oggetto not in venduti:
                venduti[oggetto] = [acquirente,prezzo]
            elif prezzo > venduti[oggetto][1]:
                venduti[oggetto] = [acquirente,prezzo]          
    f1.close()
    return venduti
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['oggetti1.csv','offerte1.csv'] ,{'Vaso': ['Giorgio', 120], 'Sedia': ['Mario', 100]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti2.csv','offerte2.csv'] ,{'Vaso': ['Giorgio', 120], 'Sedia': ['Mario', 100]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti3.csv','offerte3.csv'] ,{'Vaso': ['Giorgio', 120], 'Iphone': ['Giulia', 500]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti4.csv','offerte4.csv'] ,{'Sedia': ['Mario', 100], 'Iphone': ['Giulia', 500]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti5.csv','offerte5.csv'] ,{'Sedia': ['Mario', 100], 'Iphone': ['Giulia', 500], 'Tavolo': ['Mario', 210]})

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
