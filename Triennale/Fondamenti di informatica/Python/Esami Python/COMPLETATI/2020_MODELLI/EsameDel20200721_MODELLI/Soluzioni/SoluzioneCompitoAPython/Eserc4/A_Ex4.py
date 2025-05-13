from tester import tester_fun

def A_Ex4(file1,file2):
    f1 = open(file1,encoding='UTF-8')
    prezzi={}
    oggetti ={}
    for line in f1:
        v=line.split(',')
        prezzi[v[1]]=int(v[2])
        oggetti[v[1]]=v[0]
    f1.close()
    f2 = open(file2,encoding='UTF-8')
    result={}
    for line in f2:
        v=line.split(',')
        acquirente=v[0]
        oggetto=v[1]
        prezzo=int(v[2])
        venditore=oggetti[oggetto]
        if prezzo >= prezzi[oggetto]:
            prezzi[oggetto]=prezzo+1
            oggetti[oggetto]=acquirente
            if acquirente not in result:
                result[acquirente]=[1,-prezzo]
            else:
                result[acquirente]=[result[acquirente][0]+1,result[acquirente][1]-prezzo]
            if venditore not in result:
                result[venditore]=[-1,prezzo]
            else:
                result[venditore]=[result[venditore][0]-1,result[venditore][1]+prezzo]
    f2.close()
    return result
                       

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['oggetti1.csv','offerte1.csv'],{'Paolo': [-1, 21], 'Francesco': [0, 4], 'Gianni': [1, -25]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti1.csv','offerte2.csv'],{'Paolo': [-2, 51], 'Francesco': [0, 4], 'Gianni': [2, -55]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti2.csv','offerte3.csv'],{'Paolo': [-2, 50], 'Francesco': [0, 4], 'Gianni': [2, -54]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti2.csv','offerte4.csv'],{'Paolo': [-3, 102], 'Francesco': [0, 4], 'Gianni': [2, -55], 'Piero': [1, -51]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti3.csv','offerte5.csv'],{'Paolo': [-3, 102], 'Francesco': [0, 4], 'Gianni': [2, -55], 'Piero': [0, 1], 'Giovanna': [1, -52]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
