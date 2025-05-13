
from tester import tester_fun


def A_Ex1(s):
    somma=0
    sepIndex=s.find('@')    
    while sepIndex!=-1:
        if sepIndex>0:
            intero=int(s[:sepIndex])
        else:
            intero=0
        if intero % 2 ==0:
            somma+=intero
        s=s[sepIndex+1:]    
        sepIndex=s.find('@')
    if len(s) != 0:
        intero=int(s)
        if intero % 2 ==0:
            somma+=int(s)
    return somma

### versione con espressioni regolari
##
###import re
##
##def A_Ex1(s):
##    somma=0
##    pattern='\d+'
##    matches=re.finditer(pattern,s)
##    for m in matches:
##        intero=int(m.group())
##        if intero % 2 ==0:
##            somma+=intero
##    return somma
        
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ['123@2@24@755'], 26)
counter_test_positivi += tester_fun(A_Ex1, ['@23@44@244@22'], 310)
counter_test_positivi += tester_fun(A_Ex1, ['22@@@2@'], 24)
counter_test_positivi += tester_fun(A_Ex1, ['12345678'], 12345678)
counter_test_positivi += tester_fun(A_Ex1, ['12@70@9@1@'], 82)

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
