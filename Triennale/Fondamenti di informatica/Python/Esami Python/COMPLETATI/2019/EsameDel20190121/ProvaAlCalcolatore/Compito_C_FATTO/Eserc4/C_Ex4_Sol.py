from tester import tester_fun

def C_Ex4(file):
    f=open(file,'r',encoding='UTF-8')
    f.readline() # "consuma" la prima riga
    comande={}
    for r in f:
        lista=r.rstrip().split(',')
        tavolo=int(lista[0])
        clienti=int(lista[1])
        portata=lista[2]
        quantita=int(lista[3])
        prezzo=int(lista[4])
        if tavolo not in comande:
            comande[tavolo]=[clienti,0,0,0,0] # I campi sono: Numero clienti, Costo totale, Numero antipasti, Numero Pizze, Numero Bevande
        comande[tavolo][1]+=prezzo*quantita # Aggiorno il costo
        if portata=='antipasto':
            comande[tavolo][2]+=quantita
        elif portata=='pizza':
            comande[tavolo][3]+=quantita
        else: # caso di bevanda
            comande[tavolo][4]+=quantita
    print(comande)
    d = {}
    for elem in comande:
        tavolo = comande[elem]
        conto = tavolo[1]
        if tavolo[2] > tavolo[0]: # Devo fare sconto sugli antipasti
            conto -= tavolo[2]-tavolo[0]
        if tavolo[3] > tavolo[0]: # Devo fare sconto sulle pizze
            conto -= tavolo[3]-tavolo[0]
        if tavolo[4] > tavolo[0]: # Devo fare sconto sulle bibite
            conto -= tavolo[4]-tavolo[0]
        d[elem] = conto
    return d

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
