from tester import tester_fun

def D_Ex4(file,ore,minuti):
    f = open(file,encoding = 'UTF-8')
    scadenza = ore*60 + minuti
    d = {}
    for riga in f:
        lista = riga.strip().split(',')
        if len(lista) == 3:
            codice = lista[0]
            ora = int(lista[1])
            minuto = int(lista[2])
            previsto = ora*60+minuto
            d[codice] = previsto
            
        else:
            codice = lista[0]
            ritardo = int(lista[1])
            d[codice] += ritardo
    ris = []
    for elem in d:
        if d[elem] <= scadenza:
            ris.append(elem)
    ris.sort()
    return ris
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',12,20] ,['54200','6310'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',12,20] ,['54200', '6310', '79001'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',10,20] ,[])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',11,40] ,['54200'] )
counter_test_positivi += tester_fun(D_Ex4, ['ritardi3.csv',14,20] ,['54200', '6310', '6550', '79001'])

print('La funzione',D_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
