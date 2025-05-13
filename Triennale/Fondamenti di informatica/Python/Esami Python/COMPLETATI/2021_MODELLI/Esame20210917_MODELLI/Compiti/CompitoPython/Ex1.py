from tester import tester_fun
            
def Ex1(l):
    sol = []
    maxCount = 0
    maxElem = ""
    for elem in l:
        if l.count(elem) > maxCount:
            maxCount = l.count(elem)
            maxElem = elem
    print(maxCount, maxElem)
    for elem in l:
        if elem != maxElem:
            sol.append(elem)
    return sol

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, [[1,2,'pippo',1,2,1,'a','a']],[2,'pippo',2,'a','a'])
counter_test_positivi += tester_fun(Ex1, [['a',1,2,'pippo',1,'a',2,1,'a','a']],[1,2,'pippo',1,2,1])
counter_test_positivi += tester_fun(Ex1, [[1,1,1,1,1,1]],[])
counter_test_positivi += tester_fun(Ex1, [['mamma',2,'pippo','mamma','pippo','mamma']],[2,'pippo','pippo'])
counter_test_positivi += tester_fun(Ex1, [[2,1,3,4,1,3,5,1,2]],[2,3,4,3,5,2])

counter_test_positivi += tester_fun(Ex1, [[5,6,'pluto',6,5,'b','b',6]],[5,'pluto',5,'b','b'])
counter_test_positivi += tester_fun(Ex1, [[0,1,'mamma',0,1,0,'a','a']],[1,'mamma',1,'a','a'])
counter_test_positivi += tester_fun(Ex1, [[5,5,5,5,5,5]],[])
counter_test_positivi += tester_fun(Ex1, [[3,'pippo','pippo',4,'a']],[3,4,'a'])
counter_test_positivi += tester_fun(Ex1, [['a','b','c','a','b','b']],['a','c','a'])

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
