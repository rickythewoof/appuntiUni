from tester import tester_fun
            
def Ex1(I):
    X=set()
    for t in I:
        X.add(t[0])
        X.add(t[1])
    card=len(X)
    for t1 in I:
        for t2 in I:
            if t1[1]==t2[0] and (t1[0],t2[1]) not in I:
                return (False,card)
    return (True,card)


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,3),(1,3),(3,5),(1,5),(2,5)}],(True,4))
counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,6),(1,6),(2,1)}],(False,3))
counter_test_positivi += tester_fun(Ex1, [{(2,2),(5,5)}],(True,2))
counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,3),(3,4),(1,3),(2,4),(1,4),(4,5),(1,5),(2,5),(3,5),(1,5)}],(True,5))
counter_test_positivi += tester_fun(Ex1, [{(2,6),(6,2)}],(False,2))

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

counter_test_positivi += tester_fun(Ex1, [{(8,10),(10,12),(8,12),(12,17),(8,17),(10,17),(18,18)}],(True,5))
counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,1)}],(False,2))
counter_test_positivi += tester_fun(Ex1, [{(1,1),(3,3),(4,4)}],(True,3))
counter_test_positivi += tester_fun(Ex1, [{(1,2),(2,3),(3,4),(1,3),(2,4),(1,4)}],(True,4))
counter_test_positivi += tester_fun(Ex1, [{(2,6),(6,2),(7,1)}],(False,4))
