from tester import tester_fun

import re

def Ex2(file):
    sol = set()
    f = open(file, "r", encoding = "UTF-8").read()
    pattern = r"\b(\w)\w*\1\b"
    find = re.finditer (pattern, f, flags = re.MULTILINE)
    for match in find:
        string = match.group()
        for i in range(1,len(string)-1):
            if ord(string[i])+1 == ord(string[i+1]):
                sol.add(string)
    return sol

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ['file1.txt'] ,{'ostico', 'astuta', 'abracadabra'})
counter_test_positivi += tester_fun(Ex2, ['file2.txt'] ,{'acaba', 'arsa', 'alma'})
counter_test_positivi += tester_fun(Ex2, ['file3.txt'] ,{'inoltrati', 'aruva'})
counter_test_positivi += tester_fun(Ex2, ['file4.txt'] ,set())
counter_test_positivi += tester_fun(Ex2, ['file5.txt'] ,{'oxyzwo', 'eebcdeee', 'astratta', 'gghhgg'})
counter_test_positivi += tester_fun(Ex2, ['file6.txt'] ,{'nostran', 'peruvp'})
counter_test_positivi += tester_fun(Ex2, ['file7.txt'] ,{'opquanto','rinovar'})
counter_test_positivi += tester_fun(Ex2, ['file8.txt'] ,set())
counter_test_positivi += tester_fun(Ex2, ['file9.txt'] ,{'inughuali', 'aabvoia','ffgfgfgf'})
counter_test_positivi += tester_fun(Ex2, ['file10.txt'] ,{'nellanotten','ostusto'})


print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

           
    
