from tester import tester_fun

def A_Ex4(file):
    f = open(file,encoding = 'UTF-8')
    f.readline()
    d = {}
    for riga in f:
        lista = riga.strip().split(',')
        acquista = lista[0]
        vende = lista[1]
        pittore = lista[2]
        if acquista not in d:
            d[acquista] = []
        if vende == '':
            d[acquista].append(pittore)
        else:
            if vende in d and pittore in d[vende]:
                d[vende].remove(pittore)
                d[acquista].append(pittore)
    f.close()
    ris = []
    massimo = 0
    for acquirente in d:
        if len(d[acquirente]) > massimo:
            massimo = len(d[acquirente])
    for acquirente in d:
        if len(d[acquirente]) == massimo:
            ris.append(acquirente)    
    ris.sort()
    return ris
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['vendite1.csv'] ,['Mario'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite2.csv'] ,['Gianni', 'Mario', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite3.csv'] ,['Gianni', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite4.csv'] ,['Gianni', 'Maria', 'Paolo'] )
counter_test_positivi += tester_fun(A_Ex4, ['vendite5.csv'] ,['Paolo'] )

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
