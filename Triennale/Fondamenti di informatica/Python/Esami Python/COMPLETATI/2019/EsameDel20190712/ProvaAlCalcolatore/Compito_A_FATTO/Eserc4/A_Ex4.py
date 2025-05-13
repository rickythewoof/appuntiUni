from tester import tester_fun

def A_Ex4(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    numLinea = 0
    for ln in f:
        numLinea += 1
        migliorNome = []
        migliorSoldi = 0
        linea = ln.strip().split(";")
        for elem in linea:
            dati = elem.split("-")
            nome = dati[0]
            d[nome] = d.get(nome, [])
            soldi = int(dati[1])
            if soldi > migliorSoldi:
                migliorNome.clear()
                migliorSoldi = soldi
                migliorNome.append(nome)
            elif soldi == migliorSoldi:
                migliorNome.append(nome)
        for nome in migliorNome:
            d[nome] = d.get(nome, [])
            d[nome].append(numLinea)
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
