from tester import tester_fun

def B_Ex4(file):
    f = open(file,encoding = 'UTF-8')
    nomi = f.readline().strip().split(',') #Legge e salva la riga con i nomi
    d = {}
    for nome in nomi:
        d[nome] = [0,0,0,0]
    for riga in f:
        lista = riga.strip().split(',')
        for i in range(len(lista)):
            lista[i] = int(lista[i])
            if lista[i] > 0:
                d[nomi[i]][0] += 1
                d[nomi[i]][1] += lista[i]
                if d[nomi[i]][2] == 0 or lista[i] < d[nomi[i]][2]:
                    d[nomi[i]][2] = lista[i]
                if lista[i] > d[nomi[i]][3]:
                    d[nomi[i]][3] = lista[i]
    return d
            

###############################################################################


"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['maratone1.csv'],{'Mario': [3, 415, 130, 150], 'Paolo': [2, 273, 132, 141], 'Gianna': [1, 130, 130, 130], 'Giulia': [2, 281, 121, 160]})
counter_test_positivi += tester_fun(B_Ex4, ['maratone2.csv'],{'Mario': [3, 396, 111, 150], 'Paolo': [3, 385, 112, 141], 'Gianna': [2, 243, 113, 130], 'Giulia': [3, 395, 114, 160], 'Riccardo': [2, 247, 115, 132]})
counter_test_positivi += tester_fun(B_Ex4, ['maratone3.csv'],{'Mario': [2, 285, 135, 150], 'Paolo': [2, 273, 132, 141], 'Gianna': [1, 130, 130, 130], 'Giulia': [2, 281, 121, 160], 'Riccardo': [1, 132, 132, 132]})
counter_test_positivi += tester_fun(B_Ex4, ['maratone4.csv'],{'Mario': [4, 539, 121, 150], 'Paolo': [3, 407, 132, 141], 'Gianna': [2, 252, 122, 130], 'Giulia': [3, 404, 121, 160], 'Riccardo': [1, 132, 132, 132], 'Melania': [3, 396, 124, 140]})
counter_test_positivi += tester_fun(B_Ex4, ['maratone5.csv'],{'Mario': [4, 539, 121, 150], 'Paolo': [3, 407, 132, 141], 'Gianna': [2, 252, 122, 130], 'Giulia': [3, 404, 121, 160], 'Riccardo': [1, 132, 132, 132]})

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
