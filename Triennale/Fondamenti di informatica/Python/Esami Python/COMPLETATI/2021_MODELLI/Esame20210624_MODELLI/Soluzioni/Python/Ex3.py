from tester import tester_fun

def Ex3(diz,file):
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        dati = riga.strip().split(',')
        giocatore = dati[0].strip()
        territorio1 = dati[1].strip()
        territorio2 = dati[2].strip()
        attaccante = diz[giocatore]
        for key in diz:
            if territorio2 in diz[key]:
                attaccato = diz[key]
        if (territorio1 in attaccante) and (territorio2 not in attaccante):
            if attaccante[territorio1] > attaccato[territorio2]:
                attaccante[territorio2] = attaccante[territorio1] - attaccato[territorio2]
                attaccante[territorio1] = 1
                attaccato.pop(territorio2)
            else:
                attaccante[territorio1] = 1
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

counter_test_positivi += tester_fun(Ex3, [{'Silvia': {'Belgio':5, 'Olanda':3}, 'Piero': {'Germania':6}, 'Giorgio': {'Portogallo':2,'Austria': 1}},'mossa4.csv'] ,{'Silvia': {'Belgio': 1, 'Portogallo': 3}, 'Piero': {'Germania': 1, 'Olanda': 3}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Silvia': {'Belgio':5, 'Olanda':3}, 'Piero': {'Germania':6}, 'Giorgio': {'Portogallo':2,'Austria': 1}},'mossa5.csv'] ,{'Silvia': {'Olanda': 3, 'Portogallo': 3}, 'Piero': {'Germania': 1, 'Belgio': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Silvia': {'Belgio':3, 'Olanda':3}, 'Piero': {'Germania':6}, 'Giorgio': {'Portogallo':2,'Austria': 1}},'mossa5.csv'] ,{'Silvia': {'Olanda': 3, 'Portogallo': 1}, 'Piero': {'Germania': 1, 'Belgio': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Silvia': {'Belgio':3, 'Olanda':3}, 'Piero': {'Germania':6}, 'Giorgio': {'Portogallo':2,'Austria': 1}},'mossa6.csv'] ,{'Silvia': {'Olanda': 3, 'Portogallo': 1}, 'Piero': {'Germania': 1, 'Belgio': 5}, 'Giorgio': {'Austria': 1}})
counter_test_positivi += tester_fun(Ex3, [{'Silvia': {'Belgio':5, 'Olanda':3}, 'Piero': {'Germania':4}, 'Giorgio': {'Portogallo':3,'Austria': 1}},'mossa6.csv'] ,{'Silvia': {'Olanda': 3, 'Portogallo': 2}, 'Piero': {'Germania': 1, 'Belgio': 3}, 'Giorgio': {'Austria': 1}})
            
    

