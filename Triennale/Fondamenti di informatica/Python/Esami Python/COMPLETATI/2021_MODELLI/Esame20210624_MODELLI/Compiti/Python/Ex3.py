from tester import tester_fun

def Ex3(diz,file):
    f = open(file, "r", encoding = "Utf-8")
    for ln in f:
        dati = ln.strip().split(",")
        nome = dati[0]
        casa = dati[1]
        attacco = dati[2]
        if casa in diz[nome] and attacco not in diz[nome]:
            print("attacco da", casa, "a", attacco)
            for nomeAvv in diz:
                if attacco in diz[nomeAvv]:
                    if diz[nome][casa] > diz[nomeAvv][attacco]:
                        print ("attacco di", nome, "riuscito contro", nomeAvv)
                        diff = diz[nome][casa] - diz[nomeAvv][attacco]
                        diz[nome][casa] = 1
                        diz[nomeAvv].pop(attacco)
                        diz[nome][attacco] = diff
                    else:
                        print("attacco di", nome, "fallito contro", nomeAvv)
                        diz[nome][casa] = 1
    return diz
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':5, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa1.csv'] ,{'Paolo': {'Italia': 1, 'Spagna': 3}, 'Anna': {'Germania': 1, 'Francia': 3}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':5, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa2.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 3}, 'Anna': {'Germania': 1, 'Italia': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':3, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa2.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 1}, 'Anna': {'Germania': 1, 'Italia': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':3, 'Francia':3}, 'Anna': {'Germania':6}, 'Giorgio': {'Spagna':2,'Austria': 1}},'mossa3.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 1}, 'Anna': {'Germania': 1, 'Italia': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Paolo': {'Italia':5, 'Francia':3}, 'Anna': {'Germania':4}, 'Giorgio': {'Spagna':3,'Austria': 1}},'mossa3.csv'] ,{'Paolo': {'Francia': 3, 'Spagna': 2}, 'Anna': {'Germania': 1, 'Italia': 3}, 'Giorgio': {'Austria': 1}})

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

            
    

