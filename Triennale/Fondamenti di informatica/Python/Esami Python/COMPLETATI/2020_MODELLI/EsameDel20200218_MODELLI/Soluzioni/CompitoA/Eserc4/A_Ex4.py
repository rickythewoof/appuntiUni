from tester import tester_fun

def A_Ex4(file1,file2):
    diz = {}
    f1 = open(file1,encoding='UTF-8')
    f1.readline()
    for riga in f1:
        coppia = riga.strip().split(',')
        diz[coppia[0]] = [int(coppia[1]),0,0]
    f1.close()
    f2 = open(file2,encoding='UTF-8')
    f2.readline()
    for riga in f2:
        tripla = riga.strip().split(',')
        versante = tripla[0]
        ricevente = tripla[1]
        somma = int(tripla[2])
        if somma <= diz[versante][0]:
            if somma > diz[versante][1]:
                diz[versante][1] = somma
            if somma > diz[ricevente][2]:
                diz[ricevente][2] = somma
            diz[ricevente][0] += somma
            diz[versante][0] -= somma
    f2.close()
    return diz
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['utenti1.csv','trasferimenti1.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1400, 0, 500], 'Federica': [1800, 700, 0]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti2.csv','trasferimenti2.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1400, 0, 500], 'Federica': [1700, 700, 0], 'Paolo': [200, 0, 100]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti3.csv','trasferimenti3.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1900, 0, 500], 'Federica': [700, 700, 0], 'Paolo': [600, 500, 100]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti4.csv','trasferimenti4.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1700, 200, 500], 'Federica': [700, 700, 0], 'Paolo': [600, 500, 100], 'Sandra': [200, 0, 200]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti5.csv','trasferimenti5.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1900, 0, 500], 'Federica': [500, 700, 0], 'Paolo': [600, 500, 100], 'Sandra': [200, 0, 200], 'Irene': [0, 0, 0]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
