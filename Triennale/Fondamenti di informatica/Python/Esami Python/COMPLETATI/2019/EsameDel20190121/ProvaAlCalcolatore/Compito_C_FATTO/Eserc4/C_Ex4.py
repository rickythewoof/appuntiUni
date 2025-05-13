from tester import tester_fun

def C_Ex4(file):
    tavoli = {}
    f = open(file, "r", encoding= "UTF-8")
    ln = f.readline().strip().split(",")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        tavolo = int(ln[0])
        n_clienti = int(ln[1])
        portata = ln[2]
        quantità = int(ln[3])
        prezzo = int(ln[4])
        tavoli[tavolo] = tavoli.get(tavolo, [n_clienti,0,0,0,0])
        if portata == "antipasto":
            tavoli[tavolo][2] += quantità
        if portata == "bevanda":
            tavoli[tavolo][3] += quantità
        if portata == "pizza":
            tavoli[tavolo][4] += quantità
        tavoli[tavolo][1] += (prezzo*quantità)
        ln = f.readline().strip().split(",")
    print (tavoli)
    ris = {}
    for key in tavoli:
        totale = tavoli[key][1]
        for listIndex in range (2,5):
            if tavoli[key][listIndex] > tavoli[key][0]:
                totale -= (tavoli[key][listIndex] - tavoli[key][0]) 
        ris[key] = totale
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex4, ['comande1.csv'],{1:9, 2:6})
counter_test_positivi += tester_fun(C_Ex4, ['comande2.csv'],{1:23, 2:6})
counter_test_positivi += tester_fun(C_Ex4, ['comande3.csv'],{1:23, 2:6, 3:2})
counter_test_positivi += tester_fun(C_Ex4, ['comande4.csv'],{1: 23, 2: 11, 3: 14})
counter_test_positivi += tester_fun(C_Ex4, ['comande5.csv'],{1: 23, 2: 11, 3: 14, 4: 17})

print('La funzione',C_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
