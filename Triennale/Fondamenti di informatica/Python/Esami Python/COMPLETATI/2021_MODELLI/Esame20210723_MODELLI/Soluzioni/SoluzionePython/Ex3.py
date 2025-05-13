from tester import tester_fun

def Ex3(lista,file):
    f = open(file)
    cartelle = {}
    for voto in f:
        dati = voto.strip().split(',')
        nome = dati[0]
        numeri = dati[1:]
        for i in range(len(numeri)):
            numeri[i] = int(numeri[i])
        cartelle[nome] = numeri
    f.close()
    for elem in lista:
        vincitori = []
        for giocatore in cartelle:
            if elem in cartelle[giocatore]:
                cartelle[giocatore].remove(elem)
                if cartelle[giocatore] == []:
                    vincitori.append(giocatore)
        if len(vincitori) > 0:
            vincitori.sort()
            return vincitori[0]
    vincitori = []
    minimo = 90
    for giocatore in cartelle:
        if len(cartelle[giocatore]) < minimo:
            vincitori = [giocatore]
            minimo = len(cartelle[giocatore])
        elif len(cartelle[giocatore]) == minimo:
            vincitori.append(giocatore)
    vincitori.sort()
    return vincitori[0]
      
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, [[5,7,11,3,8],'cartelle1.csv'] ,'Anna')
counter_test_positivi += tester_fun(Ex3, [[8,7,11,3,5],'cartelle1.csv'] ,'Marco')
counter_test_positivi += tester_fun(Ex3, [[8,7,11,3,5],'cartelle2.csv'] ,'Giorgia')
counter_test_positivi += tester_fun(Ex3, [[7,12,3,5,11],'cartelle2.csv'] ,'Anna')
counter_test_positivi += tester_fun(Ex3, [[11,3,5],'cartelle2.csv'] ,'Giorgia')

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

counter_test_positivi += tester_fun(Ex3, [[5,17,44,3,8],'cartelle3.csv'] ,'Alessandra')
counter_test_positivi += tester_fun(Ex3, [[8,17,44,3,5],'cartelle3.csv'] ,'Marco')
counter_test_positivi += tester_fun(Ex3, [[8,17,44,3,5],'cartelle4.csv'] ,'Lucia')
counter_test_positivi += tester_fun(Ex3, [[17,12,3,5,44],'cartelle4.csv'] ,'Alessandra')
counter_test_positivi += tester_fun(Ex3, [[44,3,5],'cartelle4.csv'] ,'Lucia')
            
    

