from tester import tester_fun
            
def Ex1(l):
    ris=list() # lista risultato
    for i in range(len(l)-1):
        l1=l[i+1:len(l)]
        m=max(l1)
        if l[i]<m:
            ris.append(l[i])
    if len(l)>0:
        ris.append(l[-1])
    return ris
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""  


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [[10,3,4,7,5,6]],[3,4,5,6])
counter_test_positivi += tester_fun(Ex1, [[20,10,0,-2,-4]],[-4])
counter_test_positivi += tester_fun(Ex1, [[]],[])
counter_test_positivi += tester_fun(Ex1, [[14,12,11,12,20]],[14,12,11,12,20])
counter_test_positivi += tester_fun(Ex1, [[1,10,-3,1,-4]],[1,-3,-4])
counter_test_positivi += tester_fun(Ex1, [[15,8,6,9,7,6]],[8,6,6])
counter_test_positivi += tester_fun(Ex1, [[10,5,0,-1,-6]],[-6])
counter_test_positivi += tester_fun(Ex1, [[12]],[12])
counter_test_positivi += tester_fun(Ex1, [[8,10,100,120,1300]],[8,10,100,120,1300])
counter_test_positivi += tester_fun(Ex1, [[2,5,-2,-7,-4]],[2,-7,-4])


print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

