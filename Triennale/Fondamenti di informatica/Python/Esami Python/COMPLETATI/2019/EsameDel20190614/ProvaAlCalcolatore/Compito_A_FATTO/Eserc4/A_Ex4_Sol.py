from tester import tester_fun

def A_Ex4(file):
    f = open(file,encoding = 'UTF-8')
    nomi = f.readline().strip().split(',') #Legge e salva la riga con i nomi
    d = {}
    for nome in nomi:
        d[nome] = [0,0,0,0]
    for riga in f:
        lista = riga.strip().split(',')
        citta = lista[0]
        iprimo = -1
        iultimo = -1
        for i in range(len(lista)):
            lista[i] = int(lista[i])
            if lista[i] > 0:
                d[nomi[i]][1] += 1
                if iultimo < 0 or lista[i] > lista[iultimo]:
                    iultimo = i
                if iprimo < 0 or lista[i] < lista[iprimo]:
                    iprimo = i
                if d[nomi[i]][0] == 0 or lista[i] < d[nomi[i]][0]:
                    d[nomi[i]][0] = lista[i]
        d[nomi[iprimo]][2] += 1
        d[nomi[iultimo]][3] += 1
    f.close()
    return d
            

                
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['maratone1.csv'],{'Mario': [130, 3, 0, 1], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone2.csv'],{'Mario': [111, 3, 1, 0], 'Paolo': [112, 3, 1, 1], 'Gianna': [113, 2, 1, 0], 'Giulia': [114, 3, 1, 1], 'Riccardo': [115, 2, 0, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone3.csv'],{'Mario': [135, 2, 0, 0], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1], 'Riccardo': [132, 1, 0, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone4.csv'],{'Mario': [121, 4, 1, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 1], 'Riccardo': [132, 1, 0, 0], 'Melania': [124, 3, 1, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone5.csv'],{'Mario': [121, 4, 2, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 2], 'Riccardo': [132, 1, 0, 1]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
