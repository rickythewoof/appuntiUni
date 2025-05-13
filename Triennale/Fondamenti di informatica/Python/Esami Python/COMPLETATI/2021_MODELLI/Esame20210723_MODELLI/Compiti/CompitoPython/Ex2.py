from threading import local
from tester import tester_fun

def Ex2(s):
    maxL = 0
    localL = 0
    for i in range(len(s)):
        if s[i] == "a":
            print("local!")
            localL += 1
        elif s[i] != "a":
            maxL = max(maxL, localL)
            localL = 0
    maxL = max(maxL, localL)
    return maxL
            
                
                

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ['dfgaadfaaaffgeaf'] ,3)
counter_test_positivi += tester_fun(Ex2, ['serftghno'] ,0)
counter_test_positivi += tester_fun(Ex2, ['portaala'] ,2)
counter_test_positivi += tester_fun(Ex2, ['aaaaaaaaaa'] ,10)
counter_test_positivi += tester_fun(Ex2, ['aaaabbaaaabba'] ,4)
counter_test_positivi += tester_fun(Ex2, ['gaaaadfaffaageaaf'] ,4)
counter_test_positivi += tester_fun(Ex2, ['serfaatghno'] ,2)
counter_test_positivi += tester_fun(Ex2, ['poraallaaala'] ,3)
counter_test_positivi += tester_fun(Ex2, ['aaaaabaaaaa'] ,5)
counter_test_positivi += tester_fun(Ex2, ['a'] ,1)
           
    
print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

           
    
