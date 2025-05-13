from tester import tester_fun

def A_Ex1(squadre,punti):
    l = sorted(punti, reverse=True)
    sol = []
    for p in l:
        sol.append(squadre[punti.index(p)]) 
    return sol
        

	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, [['Roma', 'Lazio', 'Inter', 'Juve', 'Napoli'],[12, 5, 8, 10, 13]], ['Napoli', 'Roma', 'Juve', 'Inter', 'Lazio'])
counter_test_positivi += tester_fun(A_Ex1, [['Atalanta', 'Cagliari', 'Roma'],[30, 28, 40]], ['Roma', 'Atalanta', 'Cagliari'])
counter_test_positivi += tester_fun(A_Ex1, [['Atletico Madrid', 'Real Madrid', 'Siviglia','Barcellona'],[52, 50, 53, 61]], ['Barcellona', 'Siviglia', 'Atletico Madrid', 'Real Madrid'])
counter_test_positivi += tester_fun(A_Ex1, [[],[]], [])
counter_test_positivi += tester_fun(A_Ex1, [['Liverpool', 'Chelsea', 'Manchester City','Manchester United','Tottenham'],[15,0,2,3,10]], ['Liverpool', 'Tottenham', 'Manchester United', 'Manchester City', 'Chelsea'])

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
