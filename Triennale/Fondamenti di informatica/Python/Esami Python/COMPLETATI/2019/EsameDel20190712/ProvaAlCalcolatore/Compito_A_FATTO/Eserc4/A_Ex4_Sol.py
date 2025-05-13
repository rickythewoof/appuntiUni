from tester import tester_fun

def A_Ex4(file):
    f = open(file,encoding = 'UTF-8')
    d = {}
    g = 1 # serve ad indicizzare i giorni della settimana
    listaAgenti=[] # serve a memorizzare i nomi degli agenti incontrati nel file
    for riga in f:
        lista = riga.strip().split(';')
        maxVendite = 0
        maxAgenti = []
        for elem in lista:
            coppia = elem.split('-')
            vendite = int(coppia[1])
            if vendite > maxVendite:
                maxVendite = vendite
                maxAgenti =[coppia[0]]
            elif vendite == maxVendite:
                maxAgenti.append(coppia[0])
            if coppia[0] not in listaAgenti:
                listaAgenti.append(coppia[0])
        for e in maxAgenti:
            if e not in d:
                d[e]=[g]
            else:
                d[e].append(g)
        g=g+1
    f.close()
    for e in listaAgenti:
        if e not in d:
            d[e]=[]
    return d
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['performance1.csv'],{'Mario': [1, 2], 'Marco': [], 'Anna': [3,4], 'Aldo': [2], 'Antonio': [5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance2.csv'],{'Mario': [2], 'Marco': [], 'Anna': [1,3,4], 'Aldo':[], 'Antonio':[5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance3.csv'],{'Mario': [], 'Marco': [], 'Anna': [1,2,3,4,5], 'Antonio':[]})
counter_test_positivi += tester_fun(A_Ex4, ['performance4.csv'],{'Mario': [1,4], 'Anna': [2,3,5]})
counter_test_positivi += tester_fun(A_Ex4, ['performance5.csv'],{'Mario': [1,2,4], 'Marco': [1,4], 'Anna': [1,3,4,5], 'Aldo': [2,3], 'Antonio': [5]})



print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
