from tester import tester_fun

def A_Ex4(file1,file2):
    costi = {}
    f1 = open(file1,encoding='UTF-8')
    f1.readline()
    for riga in f1:
        coppia = riga.strip().split(',')
        costi[coppia[0]] = int(coppia[1])
    f1.close()
    f2 = open(file2,encoding='UTF-8')
    diz={} # dizionario ausiliare: oltre al totale della ricevuta mantiene anche
           # l'insieme dei prodotti acquistati
    f2.readline()
    for riga in f2:
        tripla = riga.strip().split(',')
        ricevuta = tripla[0]
        prodotto = tripla[1]
        quantita = int(tripla[2])
        if ricevuta in diz:
            if prodotto not in diz[ricevuta][1]:
                diz[ricevuta]=[diz[ricevuta][0]+quantita*costi[prodotto],diz[ricevuta][1]|{prodotto}]
        else:
            diz[ricevuta]=[quantita*costi[prodotto],{prodotto}] # memorizzo la lista dei prodotti 
    f2.close()
    result={} # costruisco il dizionario da restituire
    for elem in diz:
        result[elem]=diz[elem][0]
    return result
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute1.csv'],{'R1': 13, 'R2': 12, 'R3': 6})
counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute2.csv'],{'R1': 13, 'R2': 12, 'R3': 6} )
counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute3.csv'] ,{'R4': 6})
counter_test_positivi += tester_fun(A_Ex4, ['costi2.csv','ricevute4.csv'],{'R6': 8, 'R7': 410})
counter_test_positivi += tester_fun(A_Ex4, ['costi2.csv','ricevute1.csv'] ,{'R1': 8, 'R2': 14, 'R3': 12})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
