from tester import tester_fun

def Ex3(lista,file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    for ln in f:
        ln = ln.strip().split(",")
        nome = ln[0]
        d[nome] = []
        for i in range(1, len(ln)):
            num = int(ln[i])
            d[nome].append(num)
    vittorie = set()
    puntiMin = 10000
    finito = False
    f.close()
    for num in lista:
        for key in d:
            if num in d[key]:
                d[key].remove(num)
            if len(d[key]) < puntiMin:
                puntiMin = len(d[key])
                vittorie.clear()
                vittorie.add(key)
            elif len(d[key]) == puntiMin:
                vittorie.add(key)
            print(num,key,d[key], len(d[key]))
            if len(d[key]) == 0:
                return min(vittorie)
    return min(vittorie)

            
            
            

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
counter_test_positivi += tester_fun(Ex3, [[5,17,44,3,8],'cartelle3.csv'] ,'Alessandra')
counter_test_positivi += tester_fun(Ex3, [[8,17,44,3,5],'cartelle3.csv'] ,'Marco')
counter_test_positivi += tester_fun(Ex3, [[8,17,44,3,5],'cartelle4.csv'] ,'Lucia')
counter_test_positivi += tester_fun(Ex3, [[17,12,3,5,44],'cartelle4.csv'] ,'Alessandra')
counter_test_positivi += tester_fun(Ex3, [[44,3,5],'cartelle4.csv'] ,'Lucia')
 
print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
