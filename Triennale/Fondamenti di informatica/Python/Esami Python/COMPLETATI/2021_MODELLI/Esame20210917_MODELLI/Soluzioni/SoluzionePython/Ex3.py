from tester import tester_fun

def Ex3(p,a,file):
    f = open(file)
    partenze = {} #dizionario delle destinazioni partendo da p. Valore = tempo
    arrivi = {} #dizionario delle partenze che arrivano in a. Valore = tempo
    for volo in f:
        dati = volo.strip().split(',')
        partenza = dati[0]
        arrivo = dati[1]
        tempo = int(dati[2])
        if partenza == p:
            if (arrivo in partenze and tempo<partenze[arrivo]) or arrivo not in partenze:
                partenze[arrivo] = tempo
        if arrivo == a:
            if (partenza in arrivo and tempo<arrivi[partenze]) or partenza not in arrivi:
                arrivi[partenza] = tempo
    f.close()
    if a in partenze:
        tempo = partenze[a]
    else:
        tempo = 2000
    for scali in partenze:
        if scali in arrivi and tempo > (partenze[scali] + arrivi[scali]):
            tempo = (partenze[scali] + arrivi[scali])
    if tempo < 2000:
        return tempo
    else:
        return 'Impossibile'
      
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ['Roma','Parigi','voli1.csv'] ,180)
counter_test_positivi += tester_fun(Ex3, ['Roma','Parigi','voli2.csv'] ,170)
counter_test_positivi += tester_fun(Ex3, ['Londra','Madrid','voli2.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Londra','Roma','voli2.csv'] ,80)
counter_test_positivi += tester_fun(Ex3, ['Roma','Madrid','voli2.csv'] ,90)

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

counter_test_positivi += tester_fun(Ex3, ['Mosca','Roma','voli1.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Milano','Parigi','voli3.csv'] ,170)
counter_test_positivi += tester_fun(Ex3, ['Mosca','Amsterdam','voli3.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Amsterdam','Milano','voli3.csv'] ,80)
counter_test_positivi += tester_fun(Ex3, ['Milano','Madrid','voli3.csv'] ,90)
            
    

