from tester import tester_fun

def B_Ex4(file):
    f = open(file,encoding = 'UTF-8')
    f.readline() #Legge e butta via la riga di intestazione
    d = {} # dizionario che memorizza per ogni città l'orario minimo di arrivo e quello massimo di partenza
    for riga in f:
        lista = riga.strip().split(',')
        partenza = lista[0]
        arrivo = lista[1]
        ora1 = int(lista[2])
        ora2 = int(lista[3])
        if partenza  == "City1":
            if arrivo not in d:
                d[arrivo] = [ora2,-1]
            else:
                d[arrivo][0] = min(d[arrivo][0],ora2)
        else:
            if partenza not in d:
                d[partenza] = [24,ora1]
            else:
                d[partenza][1] = max(d[partenza][1],ora1)
    lista = []
    for key in d:
        if d[key][1] >= 0 and d[key][0] <= 23 and (d[key][1] > d[key][0]):
            lista.append(key)
    lista.sort()
    return lista
            

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['voli1.csv'],['Londra','Parigi'])
counter_test_positivi += tester_fun(B_Ex4, ['voli2.csv'],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(B_Ex4, ['voli3.csv'],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(B_Ex4, ['voli4.csv'],['Parigi'])
counter_test_positivi += tester_fun(B_Ex4, ['voli5.csv'],[])

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
