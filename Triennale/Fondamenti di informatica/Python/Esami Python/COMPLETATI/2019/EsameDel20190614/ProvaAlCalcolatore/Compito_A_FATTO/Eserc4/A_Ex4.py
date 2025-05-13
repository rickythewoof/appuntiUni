from tester import tester_fun

def A_Ex4(file):
    dict = {}
    nomi = []
    f = open(file, "r", encoding = "UTF-8")
    ln = f.readline().strip().split(",")
    for nome in ln:
        dict[nome] = [111110,0,0,0]
        nomi.append(nome)
    ln = f.readline().strip().split(",")
    while ln != [""]:
        print(ln)
        minTime = 1000000000000000564378965497865978397836585679657657698745698654794867894676987439647983467964376343764389743896473
        maxTime = 0
        for timeIndex in range(len(ln)):
            tempo = int(ln[timeIndex])
            if tempo != 0:
                dict[nomi[timeIndex]][0] = min(dict[nomi[timeIndex]][0], tempo)
                dict[nomi[timeIndex]][1] += 1
                minTime = min(minTime, tempo)
                maxTime = max (maxTime, tempo)
        migliorAtleta = nomi[ln.index(str(minTime))]
        peggiorAtleta = nomi[ln.index(str(maxTime))]
        dict[migliorAtleta][2] += 1
        dict[peggiorAtleta][3] += 1
        print(migliorAtleta, minTime, peggiorAtleta, maxTime)
        ln = f.readline().strip().split(",")
    
    return dict

                
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['maratone1.csv'],{'Mario': [130, 3, 0, 1], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone2.csv'],{'Mario': [111, 3, 1, 0], 'Paolo': [112, 3, 1, 1], 'Gianna': [113, 2, 1, 0], 'Giulia': [114, 3, 1, 1], 'Riccardo': [115, 2, 0, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone3.csv'],{'Mario': [135, 2, 0, 0], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1], 'Riccardo': [132, 1, 0, 1]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone4.csv'],{'Mario': [121, 4, 1, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 1], 'Riccardo': [132, 1, 0, 0], 'Melania': [124, 3, 1, 2]})
counter_test_positivi += tester_fun(A_Ex4, ['maratone5.csv'],{'Mario': [121, 4, 2, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 2], 'Riccardo': [132, 1, 0, 1]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
